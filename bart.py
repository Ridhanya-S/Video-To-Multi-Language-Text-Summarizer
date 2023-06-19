from download import text_file_convert
import pickle
import os
from dotenv import load_dotenv

load_dotenv('config.env')
file_path = os.getenv('FILE_PATH')
output_path = os.getenv('OUTPUT_PATH')

def summary_bart_v1(text,file_path,output_path):
    print("\nText Summarizing...")

    tokenizer = pickle.load(open(f"{file_path}/models/bart_tokenizer.pkl","rb"))
    model = pickle.load(open(f"{file_path}/models/bart_tf_model.pkl","rb"))

    input_tensor = tokenizer.encode(text, return_tensors="pt", max_length=512,truncation=True)
    outputs_tensor = model.generate(input_tensor, max_length=160, min_length=120, length_penalty=2.0, num_beams=4, early_stopping=True)

    summary_v1 = tokenizer.decode(outputs_tensor.squeeze(), skip_special_tokens = True)

    # print(textwrap.fill(summary_v1,100))

    text_file_convert(summary_v1, "summary_bart_v1", output_path)
    print("\nBart Model Text Summarization Executed!!")
    return summary_v1


# def summary_bart_v2(text,output_path):
#     print("\nText Summarizing...")
    
#     summarization = pipeline('summarization',model="facebook/bart-large-cnn")
#     summarized_text = summarization(text)

#     summary_v2 = (summarized_text[0]['summary_text'])
#     print(eval_scores(text,summary_v2,output_path))
#     # text_file_convert(summary_v2, "summary_bart_v2", output_path)

#     return summary_v2
