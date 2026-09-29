# hw2_roi.py

print("--- TÍNH TỶ SUẤT SINH LỜI ROI ---")

# Nhập tổng vốn đầu tư ban đầu
initial_investment = float(input("Nhập tổng vốn ban đầu: "))

# Nhập tổng giá trị bán ra
final_value = float(input("Nhập tổng giá trị bán ra: "))


# Tính toán các thành phần
net_profit = final_value - initial_investment
ROI = (net_profit / initial_investment) * 100


# Hiển thị kết quả
print("\n--- KẾT QUẢ ĐẦU TƯ ---")

print(f"Tổng vốn ban đầu : {round(initial_investment):,} VND")
print(f"Tổng giá trị bán : {round(final_value):,} VND")
print(f"Lợi nhuận ròng   : {round(net_profit):,} VND")
print(f"Tỷ lệ ROI        : {ROI:.2f}%")

print("-" * 25)
print(f"LỢI NHUẬN RÒNG: {round(net_profit):,} VND")
print(f"ROI: {ROI:.2f}%")