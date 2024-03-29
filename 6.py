from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    county: str

@app.post("/")
async def create_item(item: Item):
    counties = [
        "اسلامشهر", "پاکدشت", "تهران", "دماوند", "رباط کریم", "رودهن", "ری", "شمیرانات", "شهریار", "فیروزکوه",
        "ورامین""آباد", "انارستان", "اهرم", "برازجان", "بردخون", "بردستان", "بندر گناوه", "بندر دیر", "بندر ریگ", "بندردیلم", "دشتستان",
        "دشتی", "دنا", "دیر", "دیلم" ,"شبانکاره", "شنبه", "کنگان", "گناوه", "لیان", "وحدتیه",
        "آبادان", "آغاجاری", "الوان", "اندیمشک", "اهواز", "ایذه", "باغ‌ملک", "بستان", "بندرامام خمینی", "بندرماهشهر", "بهبهان", "حمیدیه",
        "خرمشهر", "دزفول", "دشت آزادگان", "رامشیر", "رامهرمز", "سوسنگرد", "شادگان", "شوش", "شوشتر", "گتوند", "لالی", "مسجدسلیمان", "هندیجان", "هویزه",
        "اردستان", "اصفهان", "برخوار", "تیران و کرون", "چادگان", "خمینی شهر", "خوانسار", "سمیرم", "شاهین شهر و میمه", "شهرضا", "فریدن", "فریدونشهر", "فلاورجان",
        "کاشان",  "گلپایگان",  "لنجان",  "مبارکه",  "نائین",  "نجف آباد",  "نطنز",
        "اردکان", "بردسکن", "بجستان", "تایباد", "تربت جام", "تربت حیدریه", "چناران", "خواف", "درگز", "رشتخوار", "سبزوار",
        "سرخس", "فریمان", "قوچان", "کاشمر", "کلات", "گناباد", "مشهد", "نیشابور", "فولاد شهر" ,
        "آباده", "ارسنجان", "استهبان", "اقلید", "بوانات", "بوشهر", "داراب", "زرین دشت", "سپیدان", "شیراز", "فسا", "فیروزآباد", "کازرون", "لارستان", "لامرد",
        "مرودشت", "ممسنی", "مهر", "نی ریز", "قیروکارزین" "اسکو", "اهر", "بستان آباد", "بناب", "تبریز", "ترکمانچای", "جلفا", "چاراویماق", "خدا آفرین",
        "سراب", "شبستر", "صوفیان", "عجب شیر", "کلیبر", "مراغه", "ورزقان", "هریس" "آمل", "بابل", "بابلسر", "بهشهر", "تنکابن", "جویبار", "ازنا",
        "چالوس", "رامسر", "ساری", "سوادکوه", "قائم‌شهر", "گلوگاه", "محمودآباد", "نکاء", "نور", "نوشهر", "قم","نورآباد ",
        "بافت", "بردسیر", "بم", "جیرفت", "رابر", "راور", "راین", "رفسنجان", "زرند", "سیرجان", "شهداد", "شهربابک", "عنبرآباد", "کرمان",
        "کوهبنان", "کهنوج", "منوجان" "کرج", "نظرآباد", "طالقان", "فردیس", "اشتهارد", "ساوجبلاغ", "چهارباغ", "مهرشهر", "تاکستان",
       "رشت", "لاهیجان", "انزلی", "فومن", "آستارا", "صومعه سرا", "رودسر", "تالش", "لنگرود", "خمام", "شفت", "ماسال", "خرم‌آباد",
        "یاسوج", "دهدشت", "گچساران", "چرام", "بویراحمد", "دوگنبدان", "لنده", "سی سخت", "مارگون", "سوق", "باشت", "دیشموک", "الشتر",
        "ارومیه", "خوی", "مهاباد", "سلماس", "پلدشت", "میاندوآب", "نقده", "چالدران", "شاهین دژ", "پیرانشهر", "بوکان", "سردشت", "فولادشهر",
        "بندرعباس", "بندرلنگه", "قشم", "میناب", "جاسک", "بندرخمیر", "حاجی آباد", "بندرجاسک", "رودان", "پارسیان", "کیش", "ابوموسی", "سیریک",
        "مرکزی", "اشتیان", "دلیجان", "خمین", "خنداب", "کمیجان", "محلات", "ساوه", "شازند", "یزد", "ابرکوه", "اردکان", "بافق", "تفت",
        "خضرآباد", "مهریز", "میبد", "کرمانشاه", "اسلام‌آباد", "پاوه", "ثلاث باباجانی", "جوانرود", "رباط", "روانسر", "سرپل ذهاب", "سنقر", "صحنه",
        "قصرشیرین", "قزوین", "آبیک", "البرز", "بوئین زهرا", "تاکستان", "خاکعلی", "محمودآباد نمونه", "خرم اباد",
        "آبیک", "البرز", "بوئین زهرا", "تاکستان", "خاکعلی", "خرمدشت", "دانسفهان", "رازمیان", "رازیان",
        "سیردان", "شال", "ضیاءآباد", "طارم", "غرق آباد", "قزوین", "محمودآباد نمونه", "محمودآباد",
        "معلم کلایه", "نرجه", "نوبندگان", "نیار", "خرم‌آباد" , "آوج", "اقبالیه", "آبگرم", "خرم آباد", "آوج", "پیراج",
        "زابل", "زاهدان", "زهک", "سراوان", "سرباز", "ایرانشهر", "چابهار", "خاش", "نیکشهر", "میرجاوه", "دلگان", "سیب و سوران", "فنوج", "هیرمند", "کنارک",
        "قصرقند", "بنت", "محمدآباد", "گلمورتی", "راسک", "پیشین" "همدان", "تویسرکان", "نهاوند", "ملایر", "اسدآباد", "بهار", "رزن", "فامنین", "قروه",
        "کبودرآهنگ" "ایلام", "آبدانان", "ایوان", "دره شهر", "دهلران", "مهران" "گرگان", "گنبد کاووس", "آق قلا", "علی آباد", "کردکوی", "کلاله", "گالیکش", "مراوه تپه",
        "بندر گز" "خرم آباد", "بروجرد", "الیگودرز", "دورود", "دلفان", "نورآباد", "سلسله", "کوهدشت", "ازنا" "ابهر", "ایجرود", "خدابنده", "خرمدره", "زنجان",
        "طارم", "ماهنشان" "اردبیل", "بیله سوار", "پارس آباد", "خلخال", "کوثر", "گِرمی", "مِشگین شهر", "نَمین" "قم", "جعفریه", "دستجرد", "سلفچگان"
        "بانه", "بیجار", "دیواندره", "سقز", "سنندج", "قروه", "مریوان" "شاهرود", "سمنان", "دامغان", "گرمسار", "مهدیشهر", "آرادان", "میامی" "شهرکرد",
        "اردل", "بروجن", "فارسان", "لردگان", "کوهرنگ", "بن" "بجنورد", "اسفراین", "شیروان", "گرمه", "راز و جرگلان", "فاروج", "بیرجند", "درمیان",
        "نهبندان", "اسدآباد", "سرایان", "فردوس", "قائن", "خوسف", "زیرکوه"
    ]
    count_counties = 0
    i_counties = 0
    while i_counties < len(counties):
        if item.county == counties[i_counties]:
            count_counties += 1
        i_counties += 1
    if count_counties == 1:
        return "صحیح است"
    else:
        return "شهرستان نادرست است"
