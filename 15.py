from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    StudentNumber: int
    name: str
    date: str
    serial: str
    State: str
    county: str
    Adress: str
    PostCode: int
    PhoneNumber: str
    Landline_phone: int
    College: str
    Subject: str
    marital_status: str
    nation_code: int




@app.post("/")
async def All_item(item: Item):
    count_student_number = 0
    StudentNumber_copy = item.StudentNumber
    while StudentNumber_copy > 0:
        L = StudentNumber_copy % 10
        count_student_number += 1
        StudentNumber_copy //= 10
    if count_student_number != 11:
        return "شماره دانشجویی باید 11 رقم باشد. تعداد ارقام شماره دانشجویی وارد شده نادرست است."
    elif count_student_number == 11:
        if 400 <= item.StudentNumber // 100000000 <= 402:
            if ((item.StudentNumber % 100000000) // 100) == 114150:
                if 1 <= item.StudentNumber % 100 <= 99:
                    i_name = 0
                    name_count = 0
                    while i_name < len(item.name):
                        if len(item.name) <= 10:
                            if 1568 <= ord(item.name[i_name]) <= 1610 or item.name[i_name] == "ی" or item.name[i_name] == "چ" or \
                                    item.name[i_name] == "پ" or \
                                    item.name[i_name] == "ک" or item.name[i_name] == "گ" or item.name[i_name] == "ژ":
                                name_count += 1
                            else:
                                return "لطفا از حروف فارسی استفاده کنید!"
                        else:
                            return "طول اسم بیشتر از 10 کاراکتر است"
                        i_name += 1
                    if name_count == len(item.name):
                        date_copy = item.date.split("/")
                        if 1 <= int(date_copy[0]) <= 1402:
                            if 1 <= int(date_copy[1]) <= 12:
                                if 1 <= int(date_copy[2]) <= 31:
                                    count_num = 0
                                    count_letters = 0
                                    count_digits = 0
                                    if len(item.serial) == 9:
                                        for j_serial in range(0, 6):
                                            if 48 <= ord(item.serial[j_serial]) <= 57:
                                                count_num += 1
                                                if count_num == 6:
                                                    if 1570 <= ord(item.serial[6]) <= 1610 or item.serial[6] == "ی" or \
                                                            item.serial[6] == "ژ" or item.serial[6] == "ک" \
                                                            or item.serial[6] == "پ" or item.serial[6] == "گ" or \
                                                            item.serial[6] == "چ":
                                                        count_letters += 1
                                                        if count_letters != 1:
                                                            return "سریال شناسنامه صحیح نیست"
                                    if len(item.serial) == 9 and count_num == 6 and count_letters == 1:
                                        for k_serial in range(7, 9):
                                            if 48 <= ord(item.serial[k_serial]) <= 57:
                                                count_digits += 1
                                    if len(item.serial) == 9 and count_num == 6 and count_letters == 1 and count_digits == 2:
                                        state = [
                                            "تهران",
                                            "بوشهر",
                                            "خوزستان",
                                            "اصفهان",
                                            "خراسان رضوی",
                                            "فارس",
                                            "آذربایجان شرقی",
                                            "مازندران",
                                            "کرمان",
                                            "البرز",
                                            "گیلان",
                                            "کهگیلویه و بویراحمد",
                                            "آذربایجان غربی",
                                            "هرمزگان",
                                            "اراک",
                                            "یزد",
                                            "	فرامنطقه ای",
                                            "کرمانشاه",
                                            "قزوین",
                                            "سیستان و بلوچستان",
                                            "همدان",
                                            "ایلام",
                                            "گلستان",
                                            "لرستان",
                                            "زنجان",
                                            "اردبیل",
                                            "قم",
                                            "کردستان",
                                            "سمنان",
                                            "چهارمحال و بختیاری",
                                            "خراسان شمالی",
                                            "خراسان جنوبی",
                                        ]
                                        if state[0] == item.State or state[1] == item.State or state[
                                            2] == item.State or state[3] == item.State \
                                                or state[4] == item.State or state[5] == item.State or state[
                                            6] == item.State \
                                                or state[7] == item.State or state[8] == item.State or state[
                                            9] == item.State \
                                                or state[10] == item.State or state[11] == item.State or state[
                                            12] == item.State \
                                                or state[13] == item.State or state[14] == item.State or state[
                                            15] == item.State \
                                                or state[16] == item.State or state[17] == item.State or state[
                                            18] == item.State \
                                                or state[19] == item.State or state[20] == item.State or state[
                                            21] == item.State \
                                                or state[22] == item.State or state[23] == item.State or state[
                                            24] == item.State \
                                                or state[25] == item.State or state[26] == item.State or state[
                                            27] == item.State \
                                                or state[28] == item.State or state[29] == item.State or state[
                                            30] == item.State \
                                                or state[31] == item.State:
                                            counties = [
                                                "اسلامشهر", "پاکدشت", "تهران", "دماوند", "رباط کریم", "رودهن", "ری",
                                                "شمیرانات", "شهریار", "فیروزکوه",
                                                "ورامین""آباد", "انارستان", "اهرم", "برازجان", "بردخون", "بردستان",
                                                "بندر گناوه", "بندر دیر", "بندر ریگ", "بندردیلم", "دشتستان",
                                                "دشتی", "دنا", "دیر", "دیلم", "شبانکاره", "شنبه", "کنگان", "گناوه",
                                                "لیان", "وحدتیه",
                                                "آبادان", "آغاجاری", "الوان", "اندیمشک", "اهواز", "ایذه", "باغ‌ملک",
                                                "بستان", "بندرامام خمینی", "بندرماهشهر", "بهبهان", "حمیدیه",
                                                "خرمشهر", "دزفول", "دشت آزادگان", "رامشیر", "رامهرمز", "سوسنگرد",
                                                "شادگان", "شوش", "شوشتر", "گتوند", "لالی", "مسجدسلیمان", "هندیجان",
                                                "هویزه",
                                                "اردستان", "اصفهان", "برخوار", "تیران و کرون", "چادگان", "خمینی شهر",
                                                "خوانسار", "سمیرم", "شاهین شهر و میمه", "شهرضا", "فریدن", "فریدونشهر",
                                                "فلاورجان",
                                                "کاشان", "گلپایگان", "لنجان", "مبارکه", "نائین", "نجف آباد", "نطنز",
                                                "اردکان", "بردسکن", "بجستان", "تایباد", "تربت جام", "تربت حیدریه",
                                                "چناران", "خواف", "درگز", "رشتخوار", "سبزوار",
                                                "سرخس", "فریمان", "قوچان", "کاشمر", "کلات", "گناباد", "مشهد", "نیشابور",
                                                "فولاد شهر",
                                                "آباده", "ارسنجان", "استهبان", "اقلید", "بوانات", "بوشهر", "داراب",
                                                "زرین دشت", "سپیدان", "شیراز", "فسا", "فیروزآباد", "کازرون", "لارستان",
                                                "لامرد",
                                                "مرودشت", "ممسنی", "مهر", "نی ریز", "قیروکارزین" "اسکو", "اهر",
                                                "بستان آباد", "بناب", "تبریز", "ترکمانچای", "جلفا", "چاراویماق",
                                                "خدا آفرین",
                                                "سراب", "شبستر", "صوفیان", "عجب شیر", "کلیبر", "مراغه", "ورزقان",
                                                "هریس" "آمل", "بابل", "بابلسر", "بهشهر", "تنکابن", "جویبار", "ازنا",
                                                "چالوس", "رامسر", "ساری", "سوادکوه", "قائم‌شهر", "گلوگاه", "محمودآباد",
                                                "نکاء", "نور", "نوشهر", "قم", "نورآباد ",
                                                "بافت", "بردسیر", "بم", "جیرفت", "رابر", "راور", "راین", "رفسنجان",
                                                "زرند", "سیرجان", "شهداد", "شهربابک", "عنبرآباد", "کرمان",
                                                "کوهبنان", "کهنوج", "منوجان" "کرج", "نظرآباد", "طالقان", "فردیس",
                                                "اشتهارد", "ساوجبلاغ", "چهارباغ", "مهرشهر", "تاکستان",
                                                "رشت", "لاهیجان", "انزلی", "فومن", "آستارا", "صومعه سرا", "رودسر",
                                                "تالش", "لنگرود", "خمام", "شفت", "ماسال", "خرم‌آباد",
                                                "یاسوج", "دهدشت", "گچساران", "چرام", "بویراحمد", "دوگنبدان", "لنده",
                                                "سی سخت", "مارگون", "سوق", "باشت", "دیشموک", "الشتر",
                                                "ارومیه", "خوی", "مهاباد", "سلماس", "پلدشت", "میاندوآب", "نقده",
                                                "چالدران", "شاهین دژ", "پیرانشهر", "بوکان", "سردشت", "فولادشهر",
                                                "بندرعباس", "بندرلنگه", "قشم", "میناب", "جاسک", "بندرخمیر", "حاجی آباد",
                                                "بندرجاسک", "رودان", "پارسیان", "کیش", "ابوموسی", "سیریک",
                                                "مرکزی", "اشتیان", "دلیجان", "خمین", "خنداب", "کمیجان", "محلات", "ساوه",
                                                "شازند", "یزد", "ابرکوه", "اردکان", "بافق", "تفت",
                                                "خضرآباد", "مهریز", "میبد", "کرمانشاه", "اسلام‌آباد", "پاوه",
                                                "ثلاث باباجانی", "جوانرود", "رباط", "روانسر", "سرپل ذهاب", "سنقر",
                                                "صحنه",
                                                "قصرشیرین", "قزوین", "آبیک", "البرز", "بوئین زهرا", "تاکستان", "خاکعلی",
                                                "محمودآباد نمونه", "خرم اباد",
                                                "آبیک", "البرز", "بوئین زهرا", "تاکستان", "خاکعلی", "خرمدشت",
                                                "دانسفهان", "رازمیان", "رازیان",
                                                "سیردان", "شال", "ضیاءآباد", "طارم", "غرق آباد", "قزوین",
                                                "محمودآباد نمونه", "محمودآباد",
                                                "معلم کلایه", "نرجه", "نوبندگان", "نیار", "خرم‌آباد", "آوج", "اقبالیه",
                                                "آبگرم", "خرم آباد", "آوج", "پیراج",
                                                "زابل", "زاهدان", "زهک", "سراوان", "سرباز", "ایرانشهر", "چابهار", "خاش",
                                                "نیکشهر", "میرجاوه", "دلگان", "سیب و سوران", "فنوج", "هیرمند", "کنارک",
                                                "قصرقند", "بنت", "محمدآباد", "گلمورتی", "راسک", "پیشین" "همدان",
                                                "تویسرکان", "نهاوند", "ملایر", "اسدآباد", "بهار", "رزن", "فامنین",
                                                "قروه",
                                                "کبودرآهنگ" "ایلام", "آبدانان", "ایوان", "دره شهر", "دهلران",
                                                "مهران" "گرگان", "گنبد کاووس", "آق قلا", "علی آباد", "کردکوی", "کلاله",
                                                "گالیکش", "مراوه تپه",
                                                "بندر گز" "خرم آباد", "بروجرد", "الیگودرز", "دورود", "دلفان", "نورآباد",
                                                "سلسله", "کوهدشت", "ازنا" "ابهر", "ایجرود", "خدابنده", "خرمدره",
                                                "زنجان",
                                                "طارم", "ماهنشان" "اردبیل", "بیله سوار", "پارس آباد", "خلخال", "کوثر",
                                                "گِرمی", "مِشگین شهر", "نَمین" "قم", "جعفریه", "دستجرد", "سلفچگان"
                                                                                                         "بانه",
                                                "بیجار", "دیواندره", "سقز", "سنندج", "قروه", "مریوان" "شاهرود", "سمنان",
                                                "دامغان", "گرمسار", "مهدیشهر", "آرادان", "میامی" "شهرکرد",
                                                "اردل", "بروجن", "فارسان", "لردگان", "کوهرنگ", "بن" "بجنورد", "اسفراین",
                                                "شیروان", "گرمه", "راز و جرگلان", "فاروج", "بیرجند", "درمیان",
                                                "نهبندان", "اسدآباد", "سرایان", "فردوس", "قائن", "خوسف", "زیرکوه"
                                            ]
                                            count_counties = 0
                                            i_counties = 0
                                            while i_counties < len(counties):
                                                if item.county == counties[i_counties]:
                                                    count_counties += 1
                                                i_counties += 1
                                            if count_counties == 1:
                                                i_adress = 0
                                                count_adress = 0
                                                while i_adress < len(item.Adress):
                                                    if 48 <= ord(item.Adress[i_adress]) <= 57:
                                                        count_adress += 1
                                                        if count_adress == len(item.Adress):
                                                            return "آدرس وارد شده صحیح نیست"
                                                    i_adress += 1
                                                if count_adress != len(item.Adress):
                                                    if len(item.Adress) <= 100:
                                                        count_digit = 0
                                                        while item.PostCode > 0:
                                                            L = item.PostCode // 10
                                                            count_digit += 1
                                                            item.PostCode //= 10
                                                        if count_digit == 10:
                                                            count_phone = 0
                                                            if len(item.PhoneNumber) == 11:
                                                                if str(item.PhoneNumber[0]) == "0":
                                                                    if str(item.PhoneNumber[1]) == "9":
                                                                        i_phone = 2
                                                                        while i_phone < 11:
                                                                            if 48 <= ord(item.PhoneNumber[i_phone]) <= 57:
                                                                                count_phone += 1
                                                                            i_phone += 1
                                                                    else:
                                                                        return "شماره موبایل صحیح نیست"
                                                                else:
                                                                    return "شماره موبایل صحیح نیست"
                                                            else:
                                                                return "شماره موبایل صحیح نیست"
                                                            if len(item.PhoneNumber) == 11:
                                                                if count_phone == 9:
                                                                    count_land_line = 0
                                                                    land_line_copy = str(item.Landline_phone)
                                                                    i_land_line = 0
                                                                    while i_land_line < len(land_line_copy):
                                                                        if 48 <= ord(land_line_copy[i_land_line]) <= 57:
                                                                            count_land_line += 1
                                                                        i_land_line += 1
                                                                    if count_land_line == 8:
                                                                        colleges = [
                                                                            "فنی و مهندسی",
                                                                            "علوم پایه",
                                                                            "علوم انسانی",
                                                                            "دامپزشکی",
                                                                            "اقتصاد",
                                                                            "کشاورزی",
                                                                            "منابع طبیعی"
                                                                        ]
                                                                        i_college = 0
                                                                        count_word = 0
                                                                        while i_college < 7:
                                                                            if item.College == colleges[i_college]:
                                                                                count_word += 1
                                                                            i_college += 1
                                                                        if count_word == 1:
                                                                            subjects = [
                                                                                "مهندسی برق-الکترونیک",
                                                                                " مهندسی شهرسازی",
                                                                                "مهندسی کامپیوتر",
                                                                                "مهندسی عمران",
                                                                                "مهندسی برق-قدرت",
                                                                                "مهندسی مکانیک و پلیمر",
                                                                                "مهندسی معدن"
                                                                            ]
                                                                            i_subject = 0
                                                                            count_subject = 0
                                                                            while i_subject < 7:
                                                                                if item.Subject == subjects[i_subject]:
                                                                                    count_subject += 1
                                                                                i_subject += 1
                                                                            if count_subject == 1:
                                                                                nation_code_ccpy = str(item.nation_code)
                                                                                l_nation = len(nation_code_ccpy)
                                                                                sum_nation = 0
                                                                                for i_nation in range(0, l_nation - 1):
                                                                                    c_nation = ord(
                                                                                        nation_code_ccpy[i_nation])
                                                                                    c_nation -= 48
                                                                                    sum_nation = sum_nation + c_nation * (
                                                                                                l_nation - i_nation)
                                                                                    r_nation = sum_nation % 11
                                                                                    c_nation = ord(
                                                                                        nation_code_ccpy[l_nation - 1])
                                                                                    c_nation -= 48
                                                                                    if r_nation >= 2:
                                                                                        r_nation = 11 - r_nation
                                                                                if r_nation == c_nation:
                                                                                    if item.marital_status == "مجرد" or item.marital_status == "متاهل":
                                                                                        if item.marital_status == "مجرد":
                                                                                            return "اطلاعات وارد شده صحیح می باشد"
                                                                                        else:
                                                                                            return "اطلاعات وارد شده صحیح می باشد"
                                                                                    else:
                                                                                        return "وضعیت تاهل نادرست است"
                                                                                else:
                                                                                    return "کد ملی صحیح نمی باشد"
                                                                            else:
                                                                                return "رشته تحصیلی نادرست است"
                                                                        else:
                                                                            return "دانشکده اشتباه است"
                                                                    else:
                                                                        return "شماره تلفن ثابت نادرست است"
                                                                else:
                                                                    return "شماره موبایل صحیح نیست"
                                                        else:
                                                            return "کد پستی صحیح نیست "
                                                    else:
                                                        return "آدرس وارد شده صحیح نیست"
                                            else:
                                                return "شهرستان نادرست است"
                                        else:
                                            return "استان وارد شده نادرست است"
                                    else:
                                        return " سریال شناسنامه صحیح نیست"
                                else:
                                    return "روز تاریخ تولد اشتباه است!"
                            else:
                                return "ماه تاریخ تولد اشتباه است!"
                        else:
                            return "سال تاریخ تولد اشتباه است!"
                else:
                    return "قسمت اندیس شماره دانشجویی نادرست است"
            else:
                return "قسمت ثابت شماره دانشجویی نادرست است. "
        else:
            return "قسمت سال شماره دانشجویی نادرست است."
