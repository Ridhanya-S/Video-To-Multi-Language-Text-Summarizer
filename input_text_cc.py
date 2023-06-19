from youtube_transcript_api import YouTubeTranscriptApi
from download import text_file_convert
from pytube import extract
from input_text_ncc import asr, Download, video_audio

def generate_transcript(id):
	transcript = YouTubeTranscriptApi.get_transcript(id)
	script = ""

	for text in transcript:
		t = text["text"]
		if t != '[Music]':
			script += t + " "
		
	return script

def extract_data_cc(v_link,output_path):
    id = extract.video_id(v_link)
    
    print("\nText Extraction Processing...")

    transcript = generate_transcript(id)
    
    Download(v_link,output_path)

    # VIDEO TO AUDIO
    video_audio(output_path)

    print("\nSpeech to Text Extraction Processing...")

    # SPEECH TO TEXT
    # transcript2 = asr(file_path,output_path)
    # text_file_convert(transcript2, "transcript2", output_path)

    print("\nText Extracted from the Video")    

    text_file_convert(transcript, "extract_text", output_path)
    
    print("\nText Extracted from the File")

    return transcript