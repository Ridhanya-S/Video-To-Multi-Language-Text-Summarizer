from models import model
import validators
from translate import trans_switch
import os
from dotenv import load_dotenv

load_dotenv('config.env')
file_path = os.getenv('FILE_PATH')
output_path = os.getenv('OUTPUT_PATH')

# v_link = "https://www.youtube.com/watch?v=KxvPR0cd3-k" #cc
# v_link = "https://www.youtube.com/watch?v=rrRuBrUrnCw"
v_link = "https://www.youtube.com/watch?v=8Yh2pL38ysM"


def main():
  # v_link = input("\nEnter the video link: ")

  valid=validators.url(v_link)

  if valid==True:
    print("\nUrl is valid")
    model(v_link, file_path,output_path)
    trans_switch(output_path)

  else:
      print("\nInvalid url")


main()
