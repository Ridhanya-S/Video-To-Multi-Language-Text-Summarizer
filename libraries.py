import re
import nltk
import spacy
import os
import json 
import pickle
import matplotlib.pyplot as plt

from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import extract
import moviepy.editor as mp

from deep_translator import GoogleTranslator

from transformers import pipeline

import speech_recognition as sr

from nltk.corpus import stopwords
from heapq import nlargest
from string import punctuation

from rouge import Rouge
import validators

from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BartTokenizer, BartForConditionalGeneration
import textwrap
import torch

import librosa
import soundfile as sf
import numpy as np
from pydub import AudioSegment
from pydub.silence import split_on_silence

# from flask import Flask, request, jsonify
# from flask_cors import CORS

from dotenv import load_dotenv
import os