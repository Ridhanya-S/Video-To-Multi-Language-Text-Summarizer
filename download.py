def text_file_convert(file_data, file_name, file_path):
  text_file = open(f"{file_path}/{file_name}.txt", "w", encoding="utf-8")
  text_file.write(file_data)
  text_file.close()

# text_file_convert("file_data", "file_name", "/nlp")