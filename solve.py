'''Nhiệm vụ 2: Lập trình Python (Viết công cụ tự động tìm Flag)
Giả sử bạn nhìn thấy mã nguồn C++ ở Nhiệm vụ 1. Thay vì ngồi nhẩm từng chữ cái bằng tay, hãy viết một đoạn script Python ngắn (solve.py) để đảo ngược quá trình trên:

Khai báo biến secret = "GMBH|D0ef_Cb4t1d~"

Dùng vòng lặp duyệt qua từng ký tự trong secret, trừ mã ASCII của mỗi ký tự đi 1 để khôi phục lại ký tự gốc (Gợi ý: Dùng hàm ord() để lấy mã ASCII và hàm chr() để đổi ngược số về ký tự).

In chuỗi Flag gốc ra màn hình, sau đó copy chuỗi đó chạy thử vào chương trình C++ ở Nhiệm vụ 1 để kiểm chứng.
'''
secret = "GMBH|D0ef_Cb4t1d~"
flag = ""
for char in secret:
    flag += chr(ord(char) - 1)
print(flag)
