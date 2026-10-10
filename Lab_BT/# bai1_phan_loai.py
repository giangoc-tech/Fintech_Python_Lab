# bai1_phan_loai.py

print("---- PHAN LOAI RUI RO TIN DUNG ----")

# 1. Nhập dữ liệu và ép kiểu
diem_credit = int(input("Nhập điểm tín dụng (300 - 850): "))

# 2. Phân loại rủi ro
if diem_credit >= 750 and diem_credit <= 850:
    # Điểm từ 750 đến 850
    print("Rủi ro Thấp - Duyệt tự động")

elif diem_credit >= 600 and diem_credit < 750:
    # Điểm từ 600 đến dưới 750
    print("Rủi ro Trung bình - Cần thẩm định")

elif diem_credit >= 300 and diem_credit < 600:
    # Điểm dưới 600
    print("Rủi ro Cao - Từ chối cấp tín dụng")

else:
    # Điểm không nằm trong khoảng hợp lệ
    print("Điểm tín dụng không hợp lệ")