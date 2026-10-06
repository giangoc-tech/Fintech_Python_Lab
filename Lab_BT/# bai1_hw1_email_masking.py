# bai1_hw1_email_masking.py
# Nhập email từ bàn phím
email = input("Nhập địa chỉ email: ")

# Tách tên đăng nhập và tên miền bằng ký tự @
username, domain = email.split("@")

# Lấy 3 ký tự đầu của tên đăng nhập
first_3 = username[0:3]

# Ghép lại thành email đã che
masked_email = first_3 + "***@" + domain

# In kết quả
print("Email sau khi che:", masked_email)