from download import text_file_convert
import speech_recognition as sr
from pytube import YouTube
import os
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.silence import split_on_silence
import librosa
import soundfile as sf
from huggingsound import SpeechRecognitionModel
import torch
import pickle
import os
from dotenv import load_dotenv

load_dotenv('config.env')
file_path = os.getenv('FILE_PATH')
output_path = os.getenv('OUTPUT_PATH')

# python3 -m pip install git+https://github.com/pytube/pytube
# python -m pip install --upgrade pytube

def Download(v_link,output_path):
    youtubeObject = YouTube(v_link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(f"{output_path}")
    except:
        print("\nAn Error Has Occurred")
    print("\nVideo Downloaded Successfully")


def video_audio(output_path):
  for file in os.listdir(f"{output_path}"):
      if file.endswith(".mp4"):
          path=os.path.join(f"{output_path}",file)
  
          clip = mp.VideoFileClip(path)
          clip.audio.write_audiofile(f"{output_path}/audio_converted.wav")

  print("\nVideo Conversion to Audio is Successful")


def audio_chuck(output_path):
  input_file = f"{output_path}/audio_converted.wav"
  stream = librosa.stream(input_file,block_length=30,frame_length=16000,hop_length=16000)
  # print(librosa.get_samplerate(input_file))
  for i,speech in enumerate(stream):
    sf.write(f'{output_path}/{i}.wav', speech,16000)
  
  return i


#asr
def asr(file_path,output_path):
#   device = "cuda" if torch.cuda.is_available() else "cpu"
#   model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english", device = device)

  model = pickle.load(open(f"{file_path}/models/SpeechRecognitionModel.pkl","rb"))

#   with open('SpeechRecognitionModel.pkl', 'wb') as sp:
#     pickle.dump(model, sp)


  i = audio_chuck(output_path)
  audio_path =[]
  for a in range(i+1):
    audio_path.append(f'{output_path}/{a}.wav') 
  print(audio_path)

  transcriptions = model.transcribe(audio_path)
  full_transcript = ' '
  for item in transcriptions:
    full_transcript += ''.join(item['transcription'])

  len(full_transcript)
  return full_transcript


def extract_data_ncc(v_link,output_path):
    # print("This video doesn't contains subtitles")

    # DOWNLOAD VIDEO
    Download(v_link,output_path)

    # VIDEO TO AUDIO
    video_audio(output_path)

    print("\nSpeech to Text Extraction Processing...")

    # SPEECH TO TEXT
    # text = transcribe_large_audio(file_path)
    # text = speech_text(file_path)
    text = asr(file_path,output_path)

    print("\nText Extracted from the Video")

    text_file_convert(text, "extract_text", output_path)

    return text

# file_path = f"E:/1.SEM 8/nlp lab/nlp project-colab/output"
# Download("https://www.youtube.com/watch?v=pJ9ffd8C1JU",file_path)