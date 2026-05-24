
# Bai 1: Kiem tra so chan
# Ham (function) la mot khoi code co ten, co the goi lai nhieu lan
# Cau truc: def ten_ham(tham_so):
#               return ket_qua

def is_even(n):
    if n % 2 == 0:
        return True   # tra ve True neu chan
    else:
        return False  # tra ve False neu le

# Goi ham
so = int(input("Bai 1 - Nhap mot so: "))
if is_even(so):
    print(f"So {so} la so CHAN")
else:
    print(f"So {so} la so LE")


# Bai 2: Tim so lon nhat trong ba so
# Dung if/elif/else de so sanh lan luot

print("\nBai 2 - Tim so lon nhat")
a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))

if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c

print(f"So lon nhat la: {lon_nhat}")


# Bai 3: Ham voi doi so mac dinh
# Doi so mac dinh: neu goi ham ma khong truyen gi
# --> tu dong dung gia tri mac dinh

def greet(name="Student"):   # "Student" la gia tri mac dinh
    print(f"Hello, {name}!")

print("\nBai 3 - Ham voi doi so mac dinh")
greet()              # khong truyen gi --> dung mac dinh "Student"
greet("An")          # truyen "An" --> dung "An"
greet("Binh")        # truyen "Binh" --> dung "Binh"


# Bai 4: Kiem tra dau vao tuoi
# Phai xu ly 2 truong hop:
#   1. Nguoi dung nhap khong phai so (vi du: nhap chu)
#   2. So nhap vao nam ngoai khoang 1-120

print("\nBai 4 - Kiem tra tuoi")
try:
    tuoi = int(input("Nhap tuoi cua ban: "))  # thu chuyen sang int
    if 1 <= tuoi <= 120:                       # kiem tra khoang hop le
        print(f"Tuoi {tuoi} hop le!")
    else:
        print(f"Tuoi {tuoi} khong hop le! Tuoi phai tu 1 den 120.")
except ValueError:
    # Neu nhap chu hoac ki tu la, int() se bao loi --> bat loi o day
    print("Loi: Vui long nhap mot so nguyen!")


# Bai 5: Dem so lan xuat hien chu 'a'
# Chuoi (string) trong Python co the duyet bang vong lap for
# Moi lan gap 'a' thi cong bien dem len 1

print("\nBai 5 - Dem chu 'a'")
chuoi = input("Nhap mot chuoi: ")
dem = 0

for ki_tu in chuoi:         # duyet tung ki tu trong chuoi
    if ki_tu == 'a':        # neu la chu 'a'
        dem = dem + 1       # cong them 1

print(f"Chu 'a' xuat hien {dem} lan")


# Bai 6: Chuyen do C sang do F
# Cong thuc: F = C x 9/5 + 32
# Dung f-string de dinh dang ket qua dep

print("\nBai 6 - Chuyen do C sang do F")
C = float(input("Nhap nhiet do (do C): "))
F = C * 9/5 + 32
print(f"{C}°C = {F:.2f}°F")   # :.2f = lay 2 chu so sau dau phay


# Bai 7: Tinh BMI
# BMI = can nang / (chieu cao * chieu cao)
# Phan loai theo chuan WHO

print("\nBai 7 - Tinh BMI")
weight = float(input("Nhap can nang (kg): "))
height = float(input("Nhap chieu cao (m): "))

BMI = weight / (height * height)
print(f"BMI cua ban = {BMI:.2f}")

# Phan loai BMI
if BMI < 18.5:
    print("Phan loai: Thieu can")
elif 18.5 <= BMI < 25:
    print("Phan loai: Binh thuong")
elif 25 <= BMI < 30:
    print("Phan loai: Thua can")
else:
    print("Phan loai: Beo phi")


# Bai 8: Phep chia - xu ly loi
# try/except giup xu ly loi ma khong lam chuong trinh crash
# ValueError : nguoi dung nhap khong phai so
# ZeroDivisionError : chia cho 0

print("\nBai 8 - Phep chia hai so")
try:
    so1 = int(input("Nhap so thu nhat: "))
    so2 = int(input("Nhap so thu hai: "))
    ket_qua = so1 / so2
    print(f"{so1} / {so2} = {ket_qua:.2f}")
except ZeroDivisionError:
    print("Loi: Khong the chia cho 0!")
except ValueError:
    print("Loi: Vui long chi nhap so nguyen!")


# Bai 9: Can bac hai
# Can bac hai chi tinh duoc voi so >= 0
# Dung thu vien math de tinh sqrt()

import math   # nhap thu vien toan hoc

print("\nBai 9 - Tinh can bac hai")
try:
    so = float(input("Nhap mot so: "))
    if so < 0:
        print("Loi: Khong tinh duoc can bac hai cua so am!")
    else:
        ket_qua = math.sqrt(so)
        print(f"Can bac hai cua {so} = {ket_qua:.4f}")
except ValueError:
    print("Loi: Vui long nhap mot so!")


# Bai 10: Thong tin 3 sinh vien
# Dung list (danh sach) de luu thong tin nhieu sinh vien
# Vong lap for de nhap va in thong tin tung nguoi

print("\nBai 10 - Thong tin sinh vien")

danh_sach = []   # list rong, se them dan vao

# Nhap thong tin 3 sinh vien
for i in range(1, 4):              # i = 1, 2, 3
    print(f"\n-- Sinh vien {i} --")
    ten = input("  Nhap ten: ")
    toan = float(input("  Diem Toan: "))
    ly   = float(input("  Diem Ly:   "))
    hoa  = float(input("  Diem Hoa:  "))

    dtb = (toan + ly + hoa) / 3    # tinh diem trung binh

    # Luu vao list dang dictionary (goi la dict - luu theo cap key:value)
    danh_sach.append({
        "ten": ten,
        "dtb": dtb
    })

# In ket qua
print("\n Ket Qua ")
print(f"{'STT':<5} {'Ho va Ten':<20} {'Diem TB'}")
print("-" * 35)
for i, sv in enumerate(danh_sach, start=1):
    print(f"{i:<5} {sv['ten']:<20} {sv['dtb']:.2f}")
print("=" * 35)