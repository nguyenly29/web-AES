![Screenshot 2025-05-22 111248](https://github.com/user-attachments/assets/b6110a57-0992-4f77-a13a-d2a580f2e0a1)
1. Chức Năng Chính
Mã Hóa Tệp:
Người dùng có thể tải lên một tệp tin và nhập khóa mã hóa (16 byte).
Ứng dụng sẽ mã hóa tệp tin bằng thuật toán AES và trả về tệp đã mã hóa.

Giải Mã Tệp:
Người dùng có thể tải lên tệp đã mã hóa và nhập khóa giải mã.
Ứng dụng sẽ giải mã tệp và trả về tệp gốc.

2. Kỹ thuật công nghệ.
Flask: Là một framework web nhẹ cho Python, giúp dễ dàng xây dựng ứng dụng web.
Cryptography: Thư viện cung cấp các công cụ mã hóa mạnh mẽ, bao gồm AES.
AES: Thuật toán mã hóa khối tiêu chuẩn, sử dụng khóa 128-bit (16 bytes) để bảo mật dữ liệu.
PKCS7 Padding: Kỹ thuật thêm dữ liệu để đảm bảo độ dài của các khối dữ liệu phù hợp với yêu cầu của thuật toán AES.

3. Cách Thức Hoạt Động
Tải Lên Tệp:
Người dùng chọn tệp thông qua giao diện web hoặc kéo và thả vào khu vực đã chỉ định.
Nhập Khóa:
Người dùng nhập khóa mã hóa (16 byte) vào ô nhập liệu.
Chọn Hành Động:
Người dùng nhấn nút "Encrypt" để mã hóa hoặc "Decrypt" để giải mã.
Xử Lý Tệp:
Ứng dụng sử dụng thuật toán AES để mã hóa hoặc giải mã tệp và lưu kết quả.
Tải Xuống Tệp:
Sau khi quá trình hoàn tất, ứng dụng cung cấp tệp đã mã hóa hoặc giải mã cho người dùng để tải xuống.
Giao Diện Web
Thiết Kế Hiện Đại: Giao diện đơn giản, dễ sử dụng với bố cục rõ ràng.
Hướng Dẫn Rõ Ràng: Có phần hướng dẫn để người dùng biết cách sử dụng ứng dụng.
Hiệu Ứng Tương Tác: Các nút và khu vực có hiệu ứng hover và active để tạo cảm giác tương tác tốt.
