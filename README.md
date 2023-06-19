# VIDEO TO MULTI-LANGUAGE TEXT SUMMARIZER
To automatically generate a concise and accurate summary that captures the essence of the content of a given video by analyzing the audio and video content , pick out the key topics and produce a summary that precisely sums up the content. To make the summary available to a wider people, the system also translate it into various types of languages.

# DATASET :
● Video processing : to process the video and extract the audio component as .wav files

● Audio to text transcription : to transcribe the audio file into text that is to convert the spoken words to text

● Dataset creation : after the transcription is done, can create a dataset by collecting the video links and their corresponding transcriptions.

# IDEOLOGY :
The ability that a video can be automatically transcribed and summarized into multiple languages, making it accessible to a wider people without the need for human translation.

# OUICK START
1. Create a new python environment and download the packages using the command -> pip install -r requirements.txt
2. Change the path according to your system in config.env file
3. Download the trained models using the following link -> https://drive.google.com/drive/folders/1ILkjBk_gzSJVHeYlrIJ8aW8Pv84bg7Ny?usp=drive_link
4. And give the models folder path as FILE_PATH in config.env
5. Create a empty folder to store the results, make sure you give this folder path as OUTPUT_PATH in config.env
6. Run the main.py
7. If StreamData error occur rectify using the commands from error_rectify.txt
