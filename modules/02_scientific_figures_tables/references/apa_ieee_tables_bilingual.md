# Scientific Tables Standards (APA 7th & IEEE Booktabs Standard)
# شیوه‌نامه تدوین جداول علمی دانشگاهی (دوزبانه فارسی و انگلیسی)

جداول در مقالات علمی، پایان‌نامه‌ها و گزارش‌های آزمایشگاهی باید ساختاری پاک، فشرده و فاقد خطوط تزئینی داشته باشند.

---

## ۱. قانون بنیادین ۳ خطی (The 3-Rule Standard)

مجلات معتبر علمی (مانند *Journal of Biomechanics*، *IEEE TBME*، *Annals of Biomedical Engineering* و *Elsevier*) استفاده از هرگونه خط عمودی را اکیداً ممنوع کرده‌اند. ساختار جدول شامل ۳ خط افقی اصلی است:

1. **خط بالای جدول (Top Rule):** خط افقی ممتد با ضخامت ۱ تا ۱٫۵ پوینت در بالای عناوین ستون‌ها.
2. **خط زیر عنوان ستون‌ها (Mid Rule):** خط افقی باریک با ضخامت ۰٫۵ تا ۰٫۷۵ پوینت بین سرستون‌ها و بدنه داده‌ها.
3. **خط انتهای جدول (Bottom Rule):** خط افقی ممتد با ضخامت ۱ تا ۱٫۵ پوینت در زیر آخرین ردیف داده‌ها.

```
---------------------------------------------------------------------  <-- Top Rule (1.5 pt)
سرستون ۱             سرستون ۲ [واحد]            مقدار p
---------------------------------------------------------------------  <-- Mid Rule (0.75 pt)
داده ۱                  ۲۴٫۵ ± ۱٫۲               ۰٫۰۱۲*
داده ۲                  ۱۸٫۳ ± ۲٫۱               ۰٫۲۴۰
---------------------------------------------------------------------  <-- Bottom Rule (1.5 pt)
زیرنویس: * معناداری آماری در سطح خطای ۰٫۰۵.
```

---

## ۲. مکان‌یابی عنوان و زیرنویس (Caption & Notes Placement)

- **عنوان جدول (Table Caption):** همیشه در **بالای** جدول قرار می‌گیرد:
  - انگلیسی: `Table 1: Anthropometric characteristics and baseline gait parameters.`
  - فارسی: `جدول ۱: مشخصات آنتروپومتریک و پارامترهای پایه راه رفتن آزمودنی‌ها.`
- **زیرنویس و توضیحات اختصارات (Table Notes):** همیشه در **پایین** خط انتهایی جدول درج می‌شود:
  - توضیحات نمادهای معناداری آماری ($* p < 0.05$, $** p < 0.01$, $*** p < 0.001$, $\text{n.s.}=\text{non-significant}$).
  - تعریف تمام اختصارات به کار رفته در جدول (مانند `ROM: Range of Motion`, `GRF: Ground Reaction Force`, `STA: Soft Tissue Artifact`).

---

## ۳. تراز اعداد و تعداد ارقام اعشار (Decimal Consistency)
- تمام اعداد یک ستون باید از نظر تعداد ارقام اعشار کاملاً یکدست باشند (معمولاً ۲ رقم اعشار برای زوایا و نیروها، ۳ رقم اعشار برای مقادیر $p$).
- مقادیر $p$ کمتر از ۰٫۰۰۱ باید به صورت $p < 0.001$ نوشته شوند نه $p = 0.000$.
- در جداول فارسی، ممیز اعشاری فارسی (٫) و ارقام فارسی (۰ تا ۹) به کار می‌روند؛ برای مقادیر نامگذاری‌های انگلیسی یا متغیرهای لاتین، ستون می‌تواند LTR باشد.

---

## ۴. نمونه کدهای آماده

### ۴.۱. کد لاتکس بر اساس پکیج `booktabs`
```latex
\usepackage{booktabs}

\begin{table}[htbp]
  \centering
  \caption{Comparison of lower-extremity joint moments between cohorts.}
  \label{tab:moments}
  \begin{tabular}{lcccc}
    \toprule
    Joint Moment [$N\cdot m/kg$] & Control ($n=12$) & Impairment ($n=12$) & Effect Size ($d$) & $p$-value \\
    \midrule
    Peak Hip Extensor Moment    & $1.42 \pm 0.15$   & $1.10 \pm 0.18$     & 1.93              & $0.002^*$ \\
    Peak Knee Extensor Moment   & $1.28 \pm 0.14$   & $0.94 \pm 0.20$     & 1.97              & $0.001^*$ \\
    Peak Ankle Plantarflexor    & $1.65 \pm 0.19$   & $1.32 \pm 0.24$     & 1.52              & $0.008^*$ \\
    \bottomrule
  \end{tabular}
  \vspace{1ex}
  {\raggedright \footnotesize \textit{Note.} Data presented as Mean $\pm$ SD. * indicates statistically significant difference ($p < 0.05$). \par}
\end{table}
```

### ۴.۲. پیاده‌سازی در پایتون ورد (python-docx)
برای ایجاد جداول ۳ خطی راست‌به‌چپ در Word:
```python
table = doc.add_table(rows=rows_count, cols=cols_count)
# اضافه کردن جهت راست به چپ
table._tbl.tblPr.append(OxmlElement('w:bidiVisual'))

# حذف کادرهای عمودی و اعمال فقط ۳ کادر افقی
# خط اول: Top, خط سرستون: InsideH (برای سطر ۱), خط آخر: Bottom
```
(اسکریپت `scripts/table_formatter.py` این فرآیند را به صورت خودکار اجرا می‌کند).
