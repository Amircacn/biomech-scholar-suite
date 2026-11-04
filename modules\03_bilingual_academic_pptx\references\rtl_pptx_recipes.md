# Persian PowerPoint Automation Recipes (python-pptx RTL Engine)
# دستورالعمل‌های فنی تولید اسلایدهای راست‌به‌چپ با پایتون

در کتابخانه `python-pptx` هیچ سوئیچ پیش‌فرضی برای زبان فارسی وجود ندارد. برای ساخت اسلایدهای راست‌به‌چپ حرفه‌ای باید مشخصه‌های شیء XML در زیرلایه DrawingML تنظیم شوند.

---

## ۱. ماژول پایه‌ای تنظیمات راست‌به‌چپ (Core Helper Functions)

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

def set_rtl_paragraph(paragraph, align=PP_ALIGN.RIGHT):
    """
    تنظیم جهت راست‌به‌چپ برای پاراگراف در پاورپوینت.
    توجه: در DrawingML برخلاف Word، تراز فیزیکی PP_ALIGN.RIGHT کاملاً درست عمل می‌کند.
    """
    paragraph.alignment = align
    pPr = paragraph._p.get_or_add_pPr()
    pPr.set('rtl', '1')

def format_persian_run(run, text: str, font_name: str = 'Vazirmatn', size_pt: float = 18, bold: bool = False, color_rgb: RGBColor = None):
    """
    اعمال فونت اسکریپت پیچیده (Complex Script) و تنظیمات زبان فارسی روی کاراکترها.
    بدون تگ a:cs، پاورپوینت حروف فارسی را با فونت پیش‌فرض سیستم نمایش می‌دهد.
    """
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    if color_rgb:
        run.font.color.rgb = color_rgb
        
    rPr = run._r.get_or_add_rPr()
    rPr.set('lang', 'fa-IR')
    
    # تنظیم اسکریپت پیچیده (Complex Script Typeface)
    cs = rPr.find(qn('a:cs'))
    if cs is None:
        cs = etree.SubElement(rPr, qn('a:cs'))
    cs.set('typeface', font_name)

def apply_persian_text_frame(text_frame, font_name: str = 'Vazirmatn', size_pt: float = 16):
    """اعمال تنظیمات فارسی روی تمام پاراگراف‌ها و کلمات یک جعبه متن."""
    for p in text_frame.paragraphs:
        set_rtl_paragraph(p)
        for r in p.runs:
            format_persian_run(r, r.text, font_name=font_name, size_pt=size_pt, bold=r.font.bold)
```

---

## ۲. اصلاح لیست‌های نقطه‌ای و شماره‌دار (Bullets & Numbering)

لیست‌های شماره‌دار خودکار در پاورپوینت فقط از ارقام انگلیسی استفاده می‌کنند و جهت سطر را معکوس می‌نمایند. برای لیست‌های فارسی از روش دستی زیر استفاده کنید:

```python
FA_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
to_fa_digits = lambda n: str(n).translate(str.maketrans("0123456789", FA_DIGITS))

items = [
    "ثبت داده‌های سینماتیک با فرکانس ۱۰۰ هرتز توسط دوربین‌های فروسرخ",
    "فیلترگذاری موقعیت مارکرها با فیلتر باترورث پایین‌گذر ۶ هرتز",
    "محاسبه گشتاورهای مفصلی زانو بر اساس مدل دینامیک معکوس"
]

for idx, item in enumerate(items, 1):
    p = text_frame.add_paragraph()
    set_rtl_paragraph(p)
    
    # غیرفعال کردن بولت خودکار
    pPr = p._p.get_or_add_pPr()
    buNone = etree.SubElement(pPr, qn('a:buNone'))
    
    # اضافه کردن شماره فارسی و متن
    r_num = p.add_run()
    format_persian_run(r_num, f"{to_fa_digits(idx)}.  ", font_name='Vazirmatn', size_pt=16, bold=True, color_rgb=RGBColor(0, 114, 178))
    
    r_text = p.add_run()
    format_persian_run(r_text, item, font_name='Vazirmatn', size_pt=16)
```

---

## ۳. ایجاد جداول آیینه‌شده در پاورپوینت (RTL Mirrored Tables)

در جداول پاورپوینت، ستون اول از دیدگاه ناظر همیشه سمت چپ است. برای جدول فارسی باید داده‌های ستون‌ها را خودتان برعکس کنید (ستون داده اول در خانه‌های ستون سمت راست قرار گیرد):

```python
# ایجاد جدول در اسلاید
table_shape = slide.shapes.add_table(rows=4, cols=3, left=Inches(1), top=Inches(2), width=Inches(8), height=Inches(3))
table = table_shape.table

# چیدمان ستون‌ها از راست به چپ:
# سلول 2 = ستون اول فارسی (سمت راست)
# سلول 1 = ستون دوم فارسی (وسط)
# سلول 0 = ستون سوم فارسی (سمت چپ)
headers = ["واحد", "مقدار میانگین", "پارامتر حرکتی"] # از چپ به راست

for col_idx, h_text in enumerate(headers):
    cell = table.cell(0, col_idx)
    cell.text = h_text
    p = cell.text_frame.paragraphs[0]
    set_rtl_paragraph(p, align=PP_ALIGN.CENTER)
    format_persian_run(p.runs[0], h_text, font_name='Vazirmatn', size_pt=14, bold=True)
```
