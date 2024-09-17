# VA-VSS: Hệ thống hỏi đáp Y tế VSS

## Giới thiệu

**VA-VSS** (Virtual Assistant) là trợ lý ảo thông minh được thiết kế để hỗ trợ người dùng một cách toàn diện trong các hoạt động chăm sóc khách hàng. Với khả năng tương tác, hướng dẫn, và thu thập phản hồi từ người dùng, VA-VSS giúp nâng cao trải nghiệm khách hàng, đồng thời được tích hợp sâu vào hệ thống chăm sóc khách hàng của **Vietsens**. Chatbot này không chỉ giúp giải đáp thắc mắc mà còn đóng vai trò là cầu nối giúp khách hàng sử dụng các sản phẩm và dịch vụ một cách hiệu quả hơn.

## Mô hình sử dụng

VA-VSS được xây dựng trên nền tảng **Vinallama2-7B**, đã được tinh chỉnh (finetuned) với tập dữ liệu bao gồm các văn bản, tài liệu hướng dẫn từ Vietsens, nhằm hỗ trợ sử dụng phần mềm **V+** và các ứng dụng khác của Vietsens.

## Hiệu suất

Mô hình đã được tinh chỉnh với kỹ thuật QLora và instruction tunning sử dụng **instruction_v2**, đang đạt được hiệu suất cao trên các bài kiểm tra thực tế, đáp ứng tốt nhu cầu sử dụng của khách hàng.

## Nền tảng và tài nguyên triển khai mô hình

Để phát triển và huấn luyện mô hình cho dự án này, chúng tôi sử dụng nền tảng Google Colab và Kaggle. Đây là hai công cụ hỗ trợ mạnh mẽ trong việc phát triển mô hình học sâu, cho phép người dùng truy cập vào tài nguyên phần cứng cao cấp mà không cần đầu tư quá nhiều về cơ sở hạ tầng.

Cụ thể, mô hình được huấn luyện trên GPU NVIDIA Tesla P100 và GPU NVIDIA T4, đây là những GPU mạnh mẽ với khả năng tính toán vượt trội, giúp tăng tốc độ quá trình huấn luyện mô hình, đặc biệt là các mô hình xử lý khối lượng lớn dữ liệu như mô hình ngôn ngữ tự nhiên (LLMs).

Ngoài ra, Google Colab cung cấp môi trường lập trình Python tích hợp, đi kèm với các thư viện như Tensorflow, Pytorch, và Transformers đã được cài đặt sẵn, giúp dễ dàng thiết lập và triển khai mô hình. Các tài nguyên này mang đến sự tiện lợi tối đa cho việc thử nghiệm và tinh chỉnh mô hình mà không cần cấu hình phức tạp.

Để sử dụng Google Colab với GPU, bạn cần chọn "Runtime" > "Change runtime type" và sau đó chọn "GPU" làm phần cứng tăng tốc. Google Colab sẽ tự động cấp phát tài nguyên GPU (trong đó P100 và T4 là hai lựa chọn phổ biến) để tối ưu hóa quá trình huấn luyện và dự đoán.

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

### Bước 3: Cài đặt file môi trường nếu cần thiết
``` bash
# Tạo file .env với nội dung env_content
with open('.env', 'w') as f:
    f.write(env_content)

# Kiểm tra nội dung file đã tạo
!cat .env
```

### Bước 4: Cài đặt các gói phụ thuộc
``` bash
!pip install -r /content/vsschatbox/GUI/requirments.txt
```

### Bước 5: Chạy ứng dụng
``` bash
!python app.py
```
      
