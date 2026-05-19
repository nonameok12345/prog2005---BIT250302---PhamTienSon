# BÀI 1: Tạo các biến với các kiểu dữ liệu khác nhau
# Khai báo biến
so_nguyen = 42
so_thuc = 3.14
chuoi = "Xin chào!"

# In ra màn hình
print("Số nguyên:", so_nguyen)
print("Số thực:", so_thuc)
print("Chuỗi:", chuoi)

# BÀI 2: Tính chu vi hình tròn
# Đinh nghĩa hằng số PI
PI = 3.14
# Khai báo bán kính hình tròn
r = 5
# Tính chu vi hình tròn
chu_vi = 2 * PI * r
# In ra màn hình
print("\n=== BÀI 2 ===")
print(f"Chu vi hình tròn với bán kính r = {r} là: {chu_vi}")

# BÀI 3: Thực hiện các phép toán cơ bản với hai số
# Nhập 2 số nguyên từ bàn phím
print("\n=== BÀI 3 ===")
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
# Thực hiện các phép toán cơ bản
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else "Không xác định (chia cho 0)"
# In ra màn hình
print(f"Tổng:    {a} + {b} = {tong}")
print(f"Hiệu:    {a} - {b} = {hieu}")
print(f"Tích:    {a} × {b} = {tich}")
print(f"Thương:  {a} ÷ {b} = {thuong}")

# BÀI 4: Hàm tính tổng hai số
# Hàm tính tổng 2 số
def sum_two_numbers(a, b):
    """Trả về tổng của hai số nguyên."""
    return a + b
# In ra màn hình
print("\n=== BÀI 4 ===")
ket_qua = sum_two_numbers(7, 13)
print(f"sum_two_numbers(7, 13) = {ket_qua}")

# BÀI 5: Khai báo, xử lý và hiển thị thông tin cá nhân
# Khai báo biến
name = "Nguyễn Văn An"
age = 20
average_score = 8.5
# Xử lí dữ liệu
age_next_year = age + 1
doubled_score = average_score * 2
# In thông tin
print("\n=== BÀI 5 ===")
print(f"Tên:              {name}  | Kiểu: {type(name)}")
print(f"Tuổi:             {age}   | Kiểu: {type(age)}")
print(f"Điểm trung bình:  {average_score}  | Kiểu: {type(average_score)}")
print(f"Tuổi năm sau:     {age_next_year}   | Kiểu: {type(age_next_year)}")
print(f"Điểm nhân đôi:    {doubled_score}  | Kiểu: {type(doubled_score)}")
