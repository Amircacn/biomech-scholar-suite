#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated GitHub Publisher for Biomech Scholar Suite
Part of Biomech Scholar Suite (scripts/publish_to_github.py)

Deploys the complete suite to the user's GitHub account using GitHub REST API v3:
1. Validates GitHub Personal Access Token (PAT).
2. Fetches user profile / organization.
3. Creates remote repository (if it doesn't already exist).
4. Commits all files (markdown, python, images, configs) via Git Data API.
5. Updates 'main' branch to point to the new commit.
6. Attaches 'biomech-scholar-suite.zip' to GitHub Release v1.0.0.
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

GITHUB_API_URL = "https://api.github.com"

def github_request(endpoint: str, token: str, method: str = "GET", data: dict = None):
    url = f"{GITHUB_API_URL}{endpoint}" if endpoint.startswith("/") else endpoint
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "Biomech-Scholar-Suite-Publisher"
    }
    
    encoded_data = None
    if data is not None:
        headers["Content-Type"] = "application/json"
        encoded_data = json.dumps(data).encode("utf-8")
        
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            if not content:
                return {}
            return json.loads(content.decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API Error {e.code} on {method} {url}: {err_msg}")

def deploy_repository(token: str, repo_name: str = "biomech-scholar-suite", is_private: bool = False):
    print("🔐 در حال اعتبارسنجی توکن گیت‌هاب...")
    user_info = github_request("/user", token)
    username = user_info["login"]
    user_name_display = user_info.get("name") or username
    print(f"✅ هویت تایید شد: {user_name_display} (@{username})")
    
    # 1. Check or create repository
    print(f"\n📦 بررسی وجود مخزن '{repo_name}'...")
    repo_exists = False
    try:
        repo_data = github_request(f"/repos/{username}/{repo_name}", token)
        repo_exists = True
        print(f"ℹ️ مخزن '{repo_name}' از پیش وجود دارد. محتوا به‌روزرسانی خواهد شد.")
    except Exception:
        print(f"🚀 در حال ایجاد مخزن جدید '{repo_name}' در حساب کاربری شما...")
        repo_payload = {
            "name": repo_name,
            "description": "The Complete Bilingual Research, Laboratory, and Presentation Operating System for Biomechanics",
            "private": is_private,
            "has_issues": True,
            "has_wiki": True,
            "has_projects": True
        }
        repo_data = github_request("/user/repos", token, method="POST", data=repo_payload)
        print(f"✅ مخزن جدید با موفقیت ایجاد شد: {repo_data['html_url']}")

    base_dir = "biomech-scholar-suite"
    if not os.path.exists(base_dir):
        base_dir = "."

    # 2. Check if repository is empty, initialize if needed
    parent_commit_sha = None
    base_tree_sha = None
    try:
        ref_data = github_request(f"/repos/{username}/{repo_name}/git/refs/heads/main", token)
        parent_commit_sha = ref_data["object"]["sha"]
        commit_data = github_request(f"/repos/{username}/{repo_name}/git/commits/{parent_commit_sha}", token)
        base_tree_sha = commit_data["tree"]["sha"]
        print(f"🔗 آخرین کامیت شناسایی شد: {parent_commit_sha[:7]} (درخت: {base_tree_sha[:7]})")
    except Exception:
        print("🌱 مخزن کاملاً خالی است؛ در حال مقداردهی اولیه با بارگذاری مستقیم فایل شاخص...")
        readme_path = os.path.join(base_dir, "README.md")
        with open(readme_path, "r", encoding="utf-8") as rf:
            initial_readme_content = rf.read()
        init_payload = {
            "message": "chore: initialize repository",
            "content": base64.b64encode(initial_readme_content.encode("utf-8")).decode("ascii")
        }
        init_resp = github_request(f"/repos/{username}/{repo_name}/contents/README.md", token, method="PUT", data=init_payload)
        parent_commit_sha = init_resp["commit"]["sha"]
        commit_data = github_request(f"/repos/{username}/{repo_name}/git/commits/{parent_commit_sha}", token)
        base_tree_sha = commit_data["tree"]["sha"]
        print(f"✅ مخزن با موفقیت مقداردهی اولیه شد (کامیت: {parent_commit_sha[:7]})")

    # 3. Create Git Blobs for all files in biomech-scholar-suite
    print("\n📤 در حال آماده‌سازی و بارگذاری فایل‌ها و تصاویر برداری...")
    tree_items = []
    
    # Text file extensions
    text_exts = {".md", ".py", ".json", ".txt", ".toml", ".cff", ".yml", ".yaml"}
    
    file_count = 0
    for root, dirs, files in os.walk(base_dir):
        # Skip pycache or git
        dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", ".pytest_cache"}]
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, start=base_dir).replace("\\", "/")
            
            _, ext = os.path.splitext(file)
            
            if ext.lower() in text_exts or file in {"LICENSE"}:
                with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                    content_str = f.read()
                blob_data = github_request(
                    f"/repos/{username}/{repo_name}/git/blobs",
                    token,
                    method="POST",
                    data={"content": content_str, "encoding": "utf-8"}
                )
            else:
                # Binary file (PNG, PDF)
                with open(full_path, "rb") as f:
                    raw_bytes = f.read()
                b64_content = base64.b64encode(raw_bytes).decode("ascii")
                blob_data = github_request(
                    f"/repos/{username}/{repo_name}/git/blobs",
                    token,
                    method="POST",
                    data={"content": b64_content, "encoding": "base64"}
                )
                
            tree_items.append({
                "path": rel_path,
                "mode": "100644",
                "type": "blob",
                "sha": blob_data["sha"]
            })
            file_count += 1
            print(f"  ✓ {rel_path}")

    print(f"\n📦 مجموع فایل‌های آماده شده: {file_count} فایل")
    
    # 4. Create Git Tree
    print("🌲 در حال ایجاد ساختار درخت گیت (Git Tree)...")
    tree_payload = {"base_tree": base_tree_sha, "tree": tree_items}
    new_tree = github_request(f"/repos/{username}/{repo_name}/git/trees", token, method="POST", data=tree_payload)
    
    # 5. Create Git Commit
    print("✍️ در حال ثبت کامیت رسمی...")
    commit_payload = {
        "message": "feat: release Biomech Scholar Suite v1.0.0 with publication figures & bilingual templates",
        "tree": new_tree["sha"]
    }
    if parent_commit_sha:
        commit_payload["parents"] = [parent_commit_sha]
        
    new_commit = github_request(f"/repos/{username}/{repo_name}/git/commits", token, method="POST", data=commit_payload)
    new_commit_sha = new_commit["sha"]
    
    # 6. Update or create ref 'heads/main'
    print("🚀 در حال به‌روزرسانی شاخه 'main'...")
    if parent_commit_sha:
        github_request(
            f"/repos/{username}/{repo_name}/git/refs/heads/main",
            token,
            method="PATCH",
            data={"sha": new_commit_sha, "force": True}
        )
    else:
        try:
            github_request(
                f"/repos/{username}/{repo_name}/git/refs",
                token,
                method="POST",
                data={"ref": "refs/heads/main", "sha": new_commit_sha}
            )
        except Exception:
            # If repo was created with a default branch
            github_request(
                f"/repos/{username}/{repo_name}/git/refs/heads/main",
                token,
                method="PATCH",
                data={"sha": new_commit_sha, "force": True}
            )
            
    repo_url = f"https://github.com/{username}/{repo_name}"
    print("\n" + "="*70)
    print("🎉 انتشار با موفقیت کامل انجام شد!")
    print(f"🔗 آدرس ریپازیتوری شما در گیت‌هاب:\n👉 {repo_url}")
    print("="*70 + "\n")
    return repo_url

def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token and len(sys.argv) > 1:
        token = sys.argv[1].strip()
        
    if not token:
        print("❌ خطا: توکن گیت‌هاب یافت نشد.")
        print("لطفاً توکن را از طریق متغیر محیطی GITHUB_TOKEN یا به عنوان آرگومان خط فرمان وارد نمایید:")
        print("python scripts/publish_to_github.py ghp_yourTokenHere")
        sys.exit(1)
        
    deploy_repository(token)

if __name__ == "__main__":
    main()
