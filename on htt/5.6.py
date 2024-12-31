def chuan_hoa_chuoi(s):
    # Loại bỏ khoảng trắng thừa xung quanh chuỗi
    s = s.strip()
    # Thêm dấu cách sau dấu chấm và dấu phẩy nếu cần
    s = s.replace('.', '. ').replace(',', ', ')
    # Loại bỏ các khoảng trắng thừa
    s = ' '.join(s.split())
    # Chuyển chuỗi thành danh sách ký tự để xử lý từng ký tự
    chars = list(s)
    # Viết hoa chữ cái đầu chuỗi
    if chars:
        chars[0] = chars[0].upper()
    # Viết hoa chữ cái sau dấu chấm
    for i in range(1, len(chars) - 1):
        if chars[i] == '.' and chars[i + 1] == ' ':
            chars[i + 2] = chars[i + 2].upper()
    # Kết hợp danh sách ký tự thành chuỗi
    return ''.join(chars)

# Nhập hai chuỗi từ bàn phím
X = input()
Y = input()

# Chuẩn hóa chuỗi
result_X = chuan_hoa_chuoi(X)
result_Y = chuan_hoa_chuoi(Y)

# In kết quả
print(result_X)
print(result_Y)
