# Bài tập CTF - Reverse Engineering

Bài tập thực hành cơ bản về Reverse Engineering, sử dụng C++ để kiểm tra flag và Python để giải ngược chuỗi.

## Các file chính

- `check_pass.cpp`: Chương trình C++ dùng để kiểm tra flag.
- `solve.py`: Chương trình Python dùng để giải ngược chuỗi và tìm flag.

## Cách hoạt động

```text
C++:
Flag nhập vào
     ↓
Mỗi ký tự +1
     ↓
So sánh với chuỗi bí mật
     ↓
Đúng / Sai


Python:
Chuỗi bí mật
     ↓
Mỗi ký tự -1
     ↓
Flag ban đầu
