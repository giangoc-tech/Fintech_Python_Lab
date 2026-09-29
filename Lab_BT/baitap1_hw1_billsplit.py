# baitap1_hw1_billsplit.py
print("---CHIA TIỀN HÓA ĐƠN---")

# Nhập tổng hoá đơn 
X = float(input("NHập tổng hóa đơn: "))

# Nhập tỷ lệ tiền tip 
Y = float(input("Nhập tỷ lệ tiền tip: (vd: 10 cho 10%): "))

# Nhập số người chia tiền 
Z = float(input("Nhập số người: "))

# Nhập tính toán thành phần 
tip_amount = X * Y / 100
total_amount = X + tip_amount
amount_per_person = total_amount / N

# Làm tròn số tiền mỗi người 
amount_per_person = round(amount_per_person)

# Hiển thị kết quả 
print("\n---HÓA ĐƠN CHIA TIỀN---")
print(f"Tổng tiền hàng : {round(X):,.0f} VND")
print(f"Tiền tip       : {round(tip_amount):,.0f} VND")
print("-" * 25)
print(f"Tổng thanh toán : {round(total_amount):,.0f} VND")
print(f"Mỗi người phải trả : {round(amount_per_person):,.0f}")

