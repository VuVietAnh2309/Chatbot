import gradio as gr
from model_setup import load_model
from response_generator import generate_response
import time

model, tokenizer = load_model()

def generate_response_stream(user_input, chat_history):
    try:
        prompt = user_input
        text = generate_response(prompt, model, tokenizer)
        
        # Thêm câu hỏi của người dùng vào lịch sử chat
        chat_history.append((prompt, ""))
        
        formatted_text = text.replace('\n', '<br>')


        words = formatted_text.split()  # Chia văn bản thành từng từ
        for i, word in enumerate(words):
            # Cập nhật văn bản dần dần với từ mới
            chat_history[-1] = (prompt, " ".join(words[:i + 1]))
            time.sleep(0.05)  # Điều chỉnh thời gian chờ giữa các từ
            yield gr.update(value=chat_history)  # Cập nhật dần dần với từng từ mới

    except Exception as e:
        chat_history.append(("Error", f"Error: {str(e)}"))
        yield gr.Chatbot.update(value=chat_history)

custom_css = """
#title {
    font-size: 3em;
    text-align: center;
    font-weight: bold;
    margin-bottom: 20px;
    margin-top: 20px;
    color: #333;
}

#interface {
    background-color: #f5f5f5;
    padding: 30px;
    border-radius: 5px;
    width: 80%;
    max-width: 1200px;
    margin: auto;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

#chatbot {
    width: 90%; /* Đảm bảo khung chatbot chiếm 90% chiều rộng của vùng chứa */
    height: 700px; /* Tăng chiều cao của chatbot */
    overflow-y: auto; /* Cho phép cuộn theo chiều dọc nếu nội dung dài */
    word-wrap: break-word; /* Xuống dòng khi văn bản quá dài */
    padding: 15px; /* Đảm bảo không gian nội dung thoáng */
    background-color: #ffffff;
    border-radius: 10px;
    font-size: 2.0em;
    line-height: 1.5;
    white-space: normal; /* Đảm bảo văn bản xuống dòng tự nhiên */
}

#chatbot p {
    margin: 0;
}
"""

with gr.Blocks() as iface:
    with gr.Column():  # Sắp xếp các thành phần theo chiều dọc
        gr.Markdown("<h1 id='title'>Hệ Thống Hỏi Đáp Y Tế VSS AI</h1>")
        gr.Markdown("Nhập câu hỏi của bạn vào ô bên dưới và nhận phản hồi lại từ hệ thống của chúng tôi.")
        chatbot = gr.Chatbot(elem_id="chatbot", label="Trò chuyện")
        user_input = gr.Textbox(label="Nhập câu hỏi của bạn tại đây", placeholder="Ví dụ: Các vấn đề bạn cần hỗ trợ là gì?")
        submit_button = gr.Button("Gửi câu hỏi")

    # Định nghĩa hành vi khi gửi câu hỏi
    user_input.submit(generate_response_stream, inputs=[user_input, gr.State([])], outputs=[chatbot])
    submit_button.click(generate_response_stream, inputs=[user_input, gr.State([])], outputs=[chatbot])
    
iface.launch(share=True)
