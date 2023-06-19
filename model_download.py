
# import os
# from transformers import TFBartModel, BartTokenizerFast
# from pathlib import Path
# import torch
# from  transformers import BartTokenizer, BartForConditionalGeneration
# import pickle
# from transformers import pipeline

# pretrained_dir = Path('models_cnn_bart2_download')
# pretrained_dir.mkdir(exist_ok=True)

# def load_tokenizer():
#     if not os.path.exists(pretrained_dir / 'tokenizer.json'):
#         print('downloading the pretrained tokenizer')
#         tokenizer = BartTokenizerFast.from_pretrained("facebook/bart-large-cnn")
#         tokenizer.save_pretrained(pretrained_dir)

#     return tokenizer

# def load_bart():
#     if not os.path.exists(pretrained_dir / 'tf_model.h5'):
#         print('downloading the pretrained model')
#         model = TFBartModel.from_pretrained("facebook/bart-large-cnn")
#         model.save_pretrained(pretrained_dir)
#     return model



# model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
# with open('bart_tf_model.pkl', 'wb') as m:
#     pickle.dump(model, m)


# tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
# with open('bart_tokenizer.pkl', 'wb') as t:
#     pickle.dump(tokenizer, t)


# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# with open('bart_model.pkl', 'wb') as p:
#     pickle.dump(summarizer, p)

# import pickle
# data = pickle.load(open('bart_model.pkl', 'rb'))


# # from transformers import pipeline
# # # Allocate a pipeline for sentiment-analysis
# # classifier = pipeline('sentiment-analysis')
# # classifier('We are very happy to introduce pipeline to the transformers repository.')
# # [{'label': 'POSITIVE', 'score': 0.9996980428695679}]