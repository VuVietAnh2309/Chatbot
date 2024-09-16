# VA-VSS: Hệ thống hỏi đáp Y tế VSS

## Giới thiệu

**VA-VSS** là trợ lý ảo thông minh được thiết kế để hỗ trợ người dùng một cách toàn diện trong các hoạt động chăm sóc khách hàng. Với khả năng tương tác, hướng dẫn, và thu thập phản hồi từ người dùng, VA-VSS giúp nâng cao trải nghiệm khách hàng, đồng thời được tích hợp sâu vào hệ thống chăm sóc khách hàng của **Vietsens**. Chatbot này không chỉ giúp giải đáp thắc mắc mà còn đóng vai trò là cầu nối giúp khách hàng sử dụng các sản phẩm và dịch vụ một cách hiệu quả hơn.

## Mô hình sử dụng

VA-VSS được xây dựng trên nền tảng **Vinallama2-7B**, đã được tinh chỉnh (finetuned) với tập dữ liệu bao gồm các văn bản, tài liệu hướng dẫn từ công ty, nhằm hỗ trợ sử dụng phần mềm **V+** và các ứng dụng khác của Vietsens.

## Hiệu suất

Mô hình đã được tinh chỉnh với tập dữ liệu **instruction_v2** và đang đạt được hiệu suất cao trên các bài kiểm tra thực tế, đáp ứng tốt nhu cầu sử dụng của khách hàng.

---

## Cách chạy project

### Bước 1: Clone repository

```bash
# Xóa folder nếu tồn tại
!rm -rf vsschatbox

# Lệnh clone mã nguồn từ gitlab.
!git clone https://ForDevelop:P4yVeW5-DzRx3vLQnHAs@gitlab.vietsens.vn/ivt-dev/vsschatbox.git
```

### Bước 2: Di chuyển vào thư mục dự án
``` bash
%cd /content/vsschatbox/GUI
```

### Bước 3: Cài đặt các gói phụ thuộc
``` bash
!pip install -r /content/vsschatbox/GUI/requirments.txt
```

### Bước 4: Chạy ứng dụng
``` bash
!python app.py
```
      
