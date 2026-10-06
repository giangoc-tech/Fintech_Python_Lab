# bai2_hw2_promo_code.py

# Nhập họ tên
name = input("Nhập Họ Tên: ")

# Nhập năm sinh
year = input("Nhập Năm sinh: ")

# Lấy 3 ký tự đầu tiên của tên
first_3 = name[0:3]

# Chuyển 3 ký tự đầu thành chữ in hoa
first_3 = first_3.upper()

# Tạo mã ưu đãi
promo_code = first_3 + "-" + year + "-VIP"

# In mã ưu đãi
print("Mã ưu đãi:", promo_code)