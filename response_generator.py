import re
from transformers import pipeline

def remove_duplicates(text):
    # Chia văn bản thành các dòng, bao gồm cả các dòng trống
    lines = text.splitlines(keepends=True)
    
    # Set để theo dõi các dòng đã thấy
    seen = set()
    
    # Danh sách để lưu các dòng đã được xử lý
    cleaned_lines = []
    
    for line in lines:
        stripped_line = line.strip()
        
        # Kiểm tra dòng chưa có trong set hoặc dòng trống
        if stripped_line not in seen or stripped_line == "":
            # Thêm vào set nếu không phải dòng trống
            if stripped_line != "":
                seen.add(stripped_line)
            # Giữ lại dòng gốc, bao gồm cả ký tự xuống dòng
            cleaned_lines.append(line)
    
    # Loại bỏ các dòng trống liên tiếp và giữ lại một dòng trống giữa các đoạn
    final_lines = []
    previous_line_was_blank = False
    
    for line in cleaned_lines:
        if line.strip() == "":
            if not previous_line_was_blank:
                final_lines.append(line)
            previous_line_was_blank = True
        else:
            final_lines.append(line)
            previous_line_was_blank = False
    
    # Kết hợp lại thành văn bản hoàn chỉnh
    return ''.join(final_lines)

def clean_output_new(generated_text):
    # Tìm phần bắt đầu từ "assistant:"
    match = re.search(r"assistant:(.*)", generated_text, re.DOTALL)
    if match:
        # Cắt toàn bộ thông tin trước "assistant:"
        cleaned_text = match.group(1).strip()
        
        # Loại bỏ các thẻ không cần thiết và khoảng trắng thừa
        cleaned_text = re.sub(r'<\|im_end\|>|<\|im_start\|>', '', cleaned_text).strip()

            
        # Xóa chữ "Trả lời:" đầu tiên nếu có
        first_answer_match = re.search(r"Trả lời:", cleaned_text)
        if first_answer_match:
            # Xóa chữ "Trả lời:" đầu tiên
            second_answer_match = re.search(r"Trả lời:", cleaned_text[first_answer_match.end():])
            if second_answer_match:
                # Nếu có lần thứ hai, cắt bỏ nội dung từ lần thứ hai trở đi
                cleaned_text = cleaned_text[:first_answer_match.start() + second_answer_match.start()].strip()
        
        user_match = re.search(r"### Hướng dẫn:", cleaned_text) 
        if user_match:
            cleaned_text = cleaned_text[:user_match.start()].strip()
        
        user1_match = re.search(r"### Trả lời:", cleaned_text)
        if user1_match:
            cleaned_text = cleaned_text[:user1_match.start()].strip()
            
        user2_match = re.search(r"A:", cleaned_text)
        if user2_match:
            cleaned_text = cleaned_text[:user2_match.start()].strip()
        
        user3_match = re.search(r"Ý tưởng:", cleaned_text)
        if user3_match:
            cleaned_text = cleaned_text[:user3_match.start()].strip()
            
        question_match = re.search(r"Câu hỏi", cleaned_text)
        if question_match:
            # Nếu có chữ "Câu hỏi", cắt bỏ nội dung từ đó trở đi
            cleaned_text = cleaned_text[:question_match.start()].strip()
            
        # Loại bỏ các dòng trùng lặp
        cleaned_text = remove_duplicates(cleaned_text)
        
        # Kiểm tra nếu output chỉ có dấu chấm hoặc rỗng
        if cleaned_text.strip() == "" or cleaned_text.strip() == ".":
            return "Không có thông tin phù hợp để hiển thị."

        return cleaned_text
    
    return "Rất tiếc, tôi không thể trả lời câu hỏi của bạn. Bạn có thể cung cấp thêm thông tin để tôi có thể giúp đỡ."  

def process_output(text):
    # Tìm câu cuối cùng chưa hoàn chỉnh
    sentences = re.split(r'(?<=[.!?]) +', text.strip())

    # Kiểm tra nếu câu cuối không kết thúc bằng dấu câu
    if not re.match(r'[.!?]$', sentences[-1]):
        # Xóa câu cuối cùng nếu nó không hoàn chỉnh
        sentences = sentences[:-1]

    # Ghép các câu lại thành chuỗi hoàn chỉnh
    return ' '.join(sentences)

def generate_response(user_input, model, tokenizer):

    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer,
                    max_length=350,
                    num_beams=2,
                    repetition_penalty=1.2,
                    top_p=0.85,
                    top_k=35,
                    truncation=True,
                    eos_token_id=tokenizer.eos_token_id)

    result = pipe(f"""<|im_start|>system: Bạn là một trợ lí AI hữu ích. Hãy trả lời người dùng một cách ngắn gọn và chính xác. Không lặp lại thông tin và không thêm thông tin không cần thiết<|im_end|>
                      <|im_start|>user: {user_input}<|im_end|>
                      <|im_start|>assistant:""")[0]['generated_text']

    final_output = clean_output_new(result)
    final_output = process_output(final_output)

    return final_output
