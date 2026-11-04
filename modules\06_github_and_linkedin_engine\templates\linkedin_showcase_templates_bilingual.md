# LinkedIn Showcase Templates for Biomechanics Researchers (Bilingual FA & EN)
# قالب‌های آماده پست لینکدین برای پژوهشگران بیومکانیک (دوزبانه فارسی و انگلیسی)

این قالب‌ها بر اساس فرمول ۴ مرحله‌ای (قلاب، زمینه فنی، شواهد عددی، فراخوان به عمل) و با نثری اصیل، بدون کلیشه‌های مرسوم شبکه‌های اجتماعی تدوین شده‌اند.

---

## قالب ۱: انتشار مقاله در ژورنال بین‌المللی (Journal Paper Publication)

### نسخه انگلیسی (English Version)
```text
Can we reduce biological knee joint loading during walking without altering natural swing kinematics?

In our latest study published in the Journal of Biomechanics, we investigated this trade-off using an active knee exoskeleton incorporating an adaptive quasi-stiffness control law.

Key findings across 12 human participants:
🔹 Net internal knee extension moment decreased by 19.4% (1.34 vs. 1.08 N·m/kg, p = 0.002, Cohen’s d = 1.62).
🔹 Surface EMG revealed a 21.4% reduction in rectus femoris root-mean-square amplitude during the loading response phase.
🔹 Natural sagittal-plane knee kinematics remained preserved during swing (61.8° vs. 62.4° peak flexion, p = 0.420).

These results indicate that precise timing in assistive torque can offload the biological joint without inducing unnatural kinematic compensation.

📖 Read the full paper (Open Access): [DOI Link]
💻 Processing code & inverse dynamics pipeline: [GitHub Link]

I would like to thank my co-authors and supervisor, Prof. [Name], for their continuous guidance.

#Biomechanics #GaitAnalysis #Exoskeletons #MotionCapture #BiomedicalEngineering
```

### نسخه فارسی (Persian Version)
```text
آیا می‌توان بار مکانیکی تحمیل‌شده بر مفصل زانو در راه رفتن را کاهش داد بدون آنکه الگوی طبیعی حرکت در فاز نوسان مخدوش شود؟

در مقاله جدیدمان که در نشریه Journal of Biomechanics منتشر شد، این چالش را با آزمایش یک اسکلت بیرونی فعال زانو با کنترل سفتی انطباقی روی ۱۲ داوطلب بررسی کردیم.

یافته‌های کلیدی آزمایشگاهی:
🔹 بیشینه گشتاور داخلی اکستنشن زانو ۱۹٫۴ درصد کاهش یافت (از ۱٫۳۴ به ۱٫۰۸ نیوتن‌متر بر کیلوگرم، p = 0.002، اندازه اثر: d = 1.62).
🔹 فعالیت الکترومایوگرافی عضله چهارسر ران در فاز پاسخ بارگیری ۲۱٫۴ درصد افت کرد.
🔹 دامنه طبیعی فلکشن زانو در فاز نوسان در سطح ۶۱٫۸ درجه بدون افت محسوس حفظ شد (p = 0.420).

این داده‌ها نشان می‌دهند که زمان‌بندی دقیق گشتاور کمکی، می‌تواند مفصل زانو را بدون ایجاد سازوکارهای جبرانی نامطلوب سبک کند.

📖 متن کامل مقاله (دسترسی باز): [لینک مقاله]
💻 کدهای متلب و پایتون تحلیل داده‌های C3D در گیت‌هاب: [لینک گیت‌هاب]

از راهنمایی‌های ارزشمند استاد راهنمای محترم، جناب آقای دکتر [نام استاد] صمیمانه سپاسگزارم.

#مهندسی_پزشکی #بیومکانیک #تحلیل_حرکت #اسکلت_بیرونی #پایان_نامه
```

---

## قالب ۲: انتشار جعبه‌ابزار و کد در گیت‌هاب (Open-Source Code & Dataset Release)

### نسخه انگلیسی (English Version)
```text
Processing raw 3D motion capture (.c3d) files, synchronizing force plates, and calculating inverse dynamics shouldn't require hundreds of lines of repetitive boilerplate code.

Today, I am releasing OpenBiomech-Gait — an open-source Python toolkit designed to streamline gait analysis pipelines:

⚡ Automated 4th-order zero-lag Butterworth filtering with residual analysis cutoff selection.
⚡ 3D Euler/Cardan joint angles conforming to International Society of Biomechanics (ISB) recommendations.
⚡ Recursive Newton-Euler inverse dynamics yielding net joint moments and powers.
⚡ Publication-ready vector plots (PDF/SVG) with ±1 SD confidence ribbons.

The repository includes complete unit tests and sample C3D datasets.

⭐️ Check out the repository on GitHub: [GitHub Link]
Feedback, issues, and contributions are warmly welcome!

#Python #OpenScience #Biomechanics #MotionCapture #GaitAnalysis #DataScience
```

### نسخه فارسی (Persian Version)
```text
پردازش داده‌های خام ضبط حرکت (فایل‌های C3D)، همگام‌سازی صفحات نیرو و حل معادلات دینامیک معکوس نباید نیازمند صدها سطر کدنویسی تکراری در متلب یا پایتون باشد.

جعبه‌ابزار متن‌باز OpenBiomech-Gait را در گیت‌هاب منتشر کردم تا فرایند تحلیل داده‌های آزمایشگاه بیومکانیک را خودکار و تکرارپذیر کند:

⚡ فیلتر باترورث دوطرفه بدون تاخیر فاز همراه با تحلیل باقیمانده وینتر برای انتخاب خودکار فرکانس قطع.
⚡ محاسبه زوایای مفصلی مچ پا، زانو و ران منطبق بر استاندارد انجمن بین‌المللی بیومکانیک (ISB).
⚡ استخراج گشتاورها و توان‌های مفصلی از طریق دینامیک معکوس نیوتن-اویلر.
⚡ رسم خودکار نمودارهای باکیفیت علمی همراه با نوارهای انحراف معیار آماده چاپ در مقالات.

پروژه به همراه تست‌های اعتبارسنجی و نمونه داده آزمایشی در دسترس است:
⭐️ لینک مخزن در گیت‌هاب: [لینک گیت‌هاب]

خوشحال می‌شوم اگر از این ابزار استفاده کنید و نظرات یا پیشنهادات اصلاحی‌تان را به اشتراک بگذارید.

#بیومکانیک #پایتون #علم_باز #گیت_هاب #مهندسی_پزشکی #تحلیل_گیت
```

---

## قالب ۳: نقطه عطف آزمایشگاهی و پیشرفت پایان‌نامه (Lab Experiment Milestone)

### نسخه فارسی (Persian Version)
```text
امروز پس از سه هفته کالیبراسیون دشوار، ثبت داده‌های فاز تجربی پایان‌نامه‌ام در آزمایشگاه بیومکانیک به پایان رسید.

ثبت هم‌زمان داده‌های ۱۰ دوربین فروسرخ Vicon، دو صفحه نیروی Kistler و ۸ کانال الکترومایوگرافی سطحی Delsys چالش‌های فنی زیادی داشت؛ به‌ویژه کنترل خطای جابه‌جایی بافت نرم (Soft Tissue Artifact) و حذف نویز ۵۰ هرتز برق شهر.

در گام بعدی، پردازش داده‌های سینماتیک و سینتیک را در نرم‌افزارهای ProCalc و پایتون آغاز خواهم کرد تا اثر پروتز انطباقی بر تقارن گام‌برداری ارزیابی شود.

تجربه کار با سوژه‌های واقعی در آزمایشگاه نشان داد که داده‌های حرکتی چقدر می‌توانند فراتر از شبیه‌سازی‌های تئوری، رفتارهای تطبیقی شگفت‌انگیز بدن انسان را نمایان کنند.

#آزمایشگاه_بیومکانیک #مهندسی_پزشکی #پردازش_سیگنال #حرکت_شناسی
```

---

## قالب ۴: ارائه در کنفرانس علمی (Conference Presentation Recap)

### نسخه فارسی (Persian Version)
```text
در سی‌ویکمین کنفرانس بین‌المللی مهندسی پزشکی (ICBME)، نتایج پژوهشمان پیرامون «مدل‌سازی محاسباتی تخریب غضروف مفصل زانو در شرایط بارگذاری دینامیکی» را ارائه دادم.

یکی از پرسش‌های جذاب داوران و اساتید در بخش پرسش و پاسخ، اثر نرخ کرنش و رفتار ویسکوالاستیک غضروف در سرعت‌های مختلف دویدن بود که بحث مفیدی را پیرامون شرایط مرزی المان محدود ایجاد کرد.

ارائه این یافته‌ها و گفتگو با سایر پژوهشگران بیومکانیک کشور، ایده‌های ارزنده‌ای برای تعمیم مدل در پایان‌نامه فراهم آورد.

فایل اسلایدهای ارائه را برای علاقه‌مندان در لینکدین به اشتراک گذاشتم: [لینک اسلایدها]

#کنفرانس_مهندسی_پزشکی #ارائه_علمی #بیومکانیک_ارتوپدی #پژوهش_دانشگاهی
```
