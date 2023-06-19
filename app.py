import os
from dotenv import load_dotenv

load_dotenv('config.env')
output_path = os.getenv('OUTPUT_PATH')

# file_path = f"E:/1.SEM 8/nlp lab/nlp project-final/output/cat"

file1 = open(f"{output_path}/extract_text.txt", "r")
file2 = open(f"{output_path}/spacy_summary.txt", "r")
file3 = open(f"{output_path}/summary_bart_v1.txt", "r")
file4 = open(f"{output_path}/final_text_summary.txt", "r")


data1 = file1.read()
data2 = file2.read()
data3 = file3.read()
data4 = file4.read()


print('Number of characters in original text :', len(data1))
print('Number of characters in summary text :', len(data4))