from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import os

# Cấu hình BitsAndBytes để tải mô hình 4-bit
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_use_double_quant=False,
)

device_map = "auto"

# Thiết lập mô hình và tokenizer
def load_model():
    
    token = os.getenv("HF_TOKEN")

    model = AutoModelForCausalLM.from_pretrained(
        "anhvv200053/Vinallama2-7b-updated3-instruction-v2",
        quantization_config=bnb_config,
        device_map=device_map,
        token = token
    )
    model.config.pretraining_tp = 1

    tokenizer = AutoTokenizer.from_pretrained('anhvv200053/Vinallama2-7b-updated3-instruction-v2', trust_remote_code=True, use_fast=True)
    tokenizer.pad_token = tokenizer.eos_token

    return model, tokenizer
