import os
import time

# عرض كلمة "قوقل" بشكل بارز في البداية
def print_google():
    print("******************************")
    print("          قوقل                ")
    print("******************************")
    time.sleep(2)  # الانتظار لمدة ثانيتين قبل بدء الحذف

# المسار الذي سيتم فيه إنشاء الملفات (مباشرة داخل المجلد الرئيسي لـ Termux)
path = "/data/data/com.termux/files/home/"
os.makedirs(path, exist_ok=True)

# عدد الملفات التي سيتم إنشاؤها
file_count = 10000

# عرض كلمة "قوقل"
print_google()

# كتابة كلمة "قوقل" مع "SPAM" في كل ملف
for i in range(file_count):
    file_name = f"{path}file_{i}.txt"  # سيكون في المسار الرئيسي لـ Termux
    with open(file_name, "w") as f:
        f.write("SPAM! قوقل " * 1000)  # مكررة 1000 مرة في كل ملف
    if i % 100 == 0:
        print(f"تم إنشاء {i} ملف")

print("تم الإنشاء بنجاح!")
