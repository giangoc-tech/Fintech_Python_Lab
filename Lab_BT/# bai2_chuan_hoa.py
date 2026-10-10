# bai2_chuan_hoa.py

print("---- CHUAN HOA DU LIEU KHACH HANG ----")

# 1. Khai báo dữ liệu
ten_khach_hang = " nGuYen VAn A "

# 2. Xử lý chuỗi
# Loại bỏ khoảng trắng ở hai đầu
ten_khach_hang = ten_khach_hang.strip()

# Chuyển tất cả thành chữ thường
ten_khach_hang = ten_khach_hang.lower()

# Viết hoa chữ cái đầu mỗi từ
ten_khach_hang = ten_khach_hang.title()

# 3. In kết quả
print("Tên khách hàng sau chuẩn hóa:", ten_khach_hang)