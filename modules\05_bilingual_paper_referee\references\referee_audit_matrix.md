# Peer Reviewer Audit Matrix (ماتریس جامع ممیزی داور برای مقالات بیومکانیک)
# Part of Biomech Scholar Suite (modules/05_bilingual_paper_referee)

از این ماتریس برای استخراج ساختارمند ایرادات مقاله در فرآیند داوری استفاده می‌شود.

---

## ۱. جدول ارزیابی ابعاد مقاله (Scoring Rubric 1 to 5)

| بعد ارزیابی | شاخص‌های کلیدی | امتیاز (۱ تا ۵) | نقاط ضعف متداول |
|---|---|:---:|---|
| **۱. نوآوری و اهمیت** | توجیه فرضیه، حل چالش واقعی بالینی یا مهندسی | | تکرار کارهای گذشته بدون ارزش افزوده |
| **۲. روش‌شناسی تجربی** | کالیبراسیون، ابزارها، تعداد آزمودنی‌ها، کنترل متغیرها | | عدم گزارش حجم نمونه، نادیده گرفتن خستگی |
| **۳. پردازش داده‌ها** | فیلتر باترورث، دینامیک معکوس، مدل هیل، نرمال‌سازی | | انحراف فاز فیلتر، نرمال نکردن گشتاور به وزن |
| **۴. تحلیل آماری** | نرمال بودن، توان آزمون، اندازه اثر کوهن، تصحیح مقایسات | | اکتفا به مقدار p بدون گزارش اندازه اثر |
| **۵. بحث و تفسیر** | انطباق ادعا با داده‌ها، مقایسه با وینتر، بررسی محدودیت‌ها | | تعمیم نتایج آزمودنی‌های سالم به بیماران |
| **۶. ارائه بصری و جداول** | نمودارهای بدون کادر، جداول ۳ خطی APA، وضوح برداری | | استفاده از خطوط عمودی، نبود واحد در کروشه |
| **۷. نگارش و اصالت قلم** | عدم استفاده از الگوهای رباتیک، رسم‌الخط بی‌نقص | | ردپای هوش مصنوعی (می‌باشد، delve into) |

---

## ۲. سناریوهای رایج بازخورد داور به نویسندگان (Sample Reviewer Feedback)

### نمونه ۱: ایراد اساسی در فیلترگذاری سینماتیک
> **Major Issue 1 (Filtering Discrepancy):**  
> "The authors report that 3D marker coordinates were low-pass filtered at 12 Hz, whereas ground reaction forces were filtered at 6 Hz. In dynamic inverse dynamics calculations, using a higher cutoff frequency for kinematics than for kinetics introduces severe artificial impact spikes in net joint moments around heel-strike. Please recalculate joint kinetics using consistent or systematically evaluated cutoff frequencies (e.g., Winter residual analysis) and update Figures 3 and 4 accordingly."

### نمونه ۲: ایراد در نرمال‌سازی EMG
> **Major Issue 2 (EMG Normalization):**  
> "Surface EMG linear envelopes are presented in raw millivolts (mV) to compare muscle recruitment between the control cohort and the patient cohort. As inter-electrode impedance, subcutaneous adipose tissue thickness, and muscle geometry vary drastically between individuals, raw EMG amplitudes cannot be directly compared between subjects. The authors must normalize all EMG trajectories to a validated maximal voluntary isometric contraction (% MVC) or a dynamic functional peak before statistical comparison."

### نمونه ۳: تعمیم بیش‌ازحد نتایج
> **Minor Issue 1 (Overgeneralized Claims):**  
> "In lines 245-248 of the Discussion, the authors state that 'the adaptive exoskeleton cures pathological gait deficits'. This is an overstatement unsupported by the empirical data. The study evaluated only 8 healthy male participants during short treadmill bouts. Please tone down the conclusion and explicitly discuss this in the study limitations."
