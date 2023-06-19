
# def nlp_model(v_link,reference,file_path):

#     v_id = extract.video_id(v_link)
#     transcript = get_transcript_of_yt_video(v_id)
#     transcript_size = len(transcript)

#     original_text = ' '.join([t['text'] for t in transcript])
#     original_text_length = len(original_text)

#     s_t = []

#     result = ""

#     for txt in range(0, transcript_size):
#         if (txt != 0 and txt % 100 == 0):
#             result += ' ' + transcript[txt]['text']
#             s_t.append(spacy_summarizer(result,file_path))
#             result = ""
#         else:
#             result += ' ' + transcript[txt]['text']

#         if (txt == transcript_size - 1):
#             result += ' ' + transcript[txt]['text']
#             s_t.append(spacy_summarizer(result,file_path))

#     english_summary = ' '.join(s_t) + '.'

#     final_summary_length = len(english_summary)
#     print("\nNLP Model Text Summarization Executed!!\n",english_summary)
#     print(eval_scores(reference,english_summary,f"E:/1.SEM 8/nlp lab/nlp project-colab/models/"))

#     return original_text_length, final_summary_length, english_summary

