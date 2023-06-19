from deep_translator import GoogleTranslator
from download import text_file_convert

def translation(text,to_lang, output_path):
  translator = GoogleTranslator(source='auto', target=to_lang)
  text_file_convert(translator.translate(text), to_lang, output_path)
  return translator.translate(text)


def trans_switch(output_path):

    print("===============================================================================")
  
    y_n = input("\nDo you like to convert the text into another language ? (y/n) : ")
    if y_n == 'y':
        
        ch = input("Enter 0 to start: ")
        
        while(ch >= '0'):
            print("\n\nList of Languages:\n1.Hindi\n2.Tamil\n3.Arabic\n4.French\n5.Translate any other language using lang_code\n-1.Exit")
            with open(f"{output_path}/final_text_summary.txt","r", encoding="utf-8") as f:
                contents = f.read()

            ch = input("\nEnter your choice: ")
            if (ch == '1'):
                trans_text = translation(contents,'hi', f'{output_path}')
                text_file_convert(trans_text, "hi", f'{output_path}')
                print("\nTranslated Summary Ready!!\n")

            elif (ch == '2'):
                trans_text = translation(contents,'ta', f'{output_path}')
                text_file_convert(trans_text, "ta",f'{output_path}')
                print("\nTranslated Summary Ready!!\n")

            elif ch == '3':
                trans_text = translation(contents,'ar', f'{output_path}')
                text_file_convert(trans_text, "ar",f'{output_path}')
                print("\nTranslated Summary Ready!!\n")

            elif ch == '4':
                trans_text = translation(contents,'fr', f'{output_path}')
                text_file_convert(trans_text, "fr", f'{output_path}')
                print("\nTranslated Summary Ready!!\n")
            
            elif ch == '5':
                print("""\nYou can select one of the supported languages:\n
                {'afrikaans': 'af', \t'albanian': 'sq', \t'amharic': 'am', \t'arabic': 'ar', \t'armenian': 'hy', 
                \n'assamese': 'as', \t'aymara': 'ay', \t'azerbaijani': 'az', \t'bambara': 'bm', \t'basque': 'eu', 
                \n'belarusian': 'be', \t'bengali': 'bn', \t'bhojpuri': 'bho', \t'bosnian': 'bs', \t'bulgarian': 'bg', 
                \n'catalan': 'ca', \t'cebuano': 'ceb', \t'chichewa': 'ny', \t'chinese (simplified)': 'zh-CN', \t'chinese (traditional)': 'zh-TW', 
                \n'corsican': 'co', \t'croatian': 'hr', \t'czech': 'cs', \t'danish': 'da', \t'dhivehi': 'dv', 
                \n'dogri': 'doi', \t'dutch': 'nl', \t'english': 'en', \t'esperanto': 'eo', \t'estonian': 'et', 
                \n'ewe': 'ee', \t'filipino': 'tl', \t'finnish': 'fi', \t'french': 'fr', \t'frisian': 'fy', 
                \n'galician': 'gl', \t'georgian': 'ka', \t'german': 'de', \t'greek': 'el', \t'guarani': 'gn', 
                \n'gujarati': 'gu', \t'haitian creole': 'ht', \t'hausa': 'ha', \t'hawaiian': 'haw', \t'hebrew': 'iw', 
                \n'hindi': 'hi', \t'hmong': 'hmn', \t'hungarian': 'hu', \t'icelandic': 'is', \t'igbo': 'ig', 
                \n'ilocano': 'ilo', \t'indonesian': 'id', \t'irish': 'ga', \t'italian': 'it', \t'japanese': 'ja', 
                \n'javanese': 'jw', \t'kannada': 'kn', \t'kazakh': 'kk', \t'khmer': 'km', \t'kinyarwanda': 'rw', 
                \n'konkani': 'gom', \t'korean': 'ko', \t'krio': 'kri', \t'kurdish (kurmanji)': 'ku', \t'kurdish (sorani)': 'ckb', 
                \n'kyrgyz': 'ky', \t'lao': 'lo', \t'latin': 'la', \t'latvian': 'lv', \t'lingala': 'ln', 
                \n'lithuanian': 'lt', \t'luganda': 'lg', \t'luxembourgish': 'lb', \t'macedonian': 'mk', \t'maithili': 'mai', 
                \n'malagasy': 'mg', \t'malay': 'ms', \t'malayalam': 'ml', \t'maltese': 'mt', \t'maori': 'mi', \t'marathi': 'mr', 
                \n'meiteilon (manipuri)': 'mni-Mtei', \t'mizo': 'lus', \t'mongolian': 'mn', \t'myanmar': 'my', \t'nepali': 'ne', 
                \n'norwegian': 'no', \t'odia (oriya)': 'or', \t'oromo': 'om', \t'pashto': 'ps', \t'persian': 'fa', 
                \n'polish': 'pl', \t'portuguese': 'pt', \t'punjabi': 'pa', \t'quechua': 'qu', \t'romanian': 'ro', 
                \n'russian': 'ru', \t'samoan': 'sm', \t'sanskrit': 'sa', \t'scots gaelic': 'gd', \t'sepedi': 'nso', 
                \n'serbian': 'sr', \t'sesotho': 'st', \t'shona': 'sn', \t'sindhi': 'sd', \t'sinhala': 'si', 
                \n'slovak': 'sk', \t'slovenian': 'sl', \t'somali': 'so', \t'spanish': 'es', \t'sundanese': 'su', 
                \n'swahili': 'sw', \t'swedish': 'sv', \t'tajik': 'tg', \t'tamil': 'ta', \t'tatar': 'tt', 
                \n'telugu': 'te', \t'thai': 'th', \t'tigrinya': 'ti', \t'tsonga': 'ts', \t'turkish': 'tr', 
                \n'turkmen': 'tk', \t'twi': 'ak', \t'ukrainian': 'uk', \t'urdu': 'ur', \t'uyghur': 'ug', 
                \n'uzbek': 'uz', \t'vietnamese': 'vi', \t'welsh': 'cy', \t'xhosa': 'xh', \t'yiddish': 'yi', 
                \n'yoruba': 'yo', \t'zulu': 'zu'}""")
                print()
                dest = input("\nEnter the to_lang code : ")

                try:
                  trans_text = translation(contents,dest, f'{output_path}')
                  text_file_convert(trans_text, dest, f'{output_path}')
                  print("\nTranslated Summary Ready!!\n")

                except:
                  print("\nSorry, there is no such language code")
                  continue

            elif ch == '0':
                continue

            elif ch =='-1':
                exit()

            else:
                print("\nInvalid Choice")

        print("\nKindly download your file...")

    else:
        print("\n\nHAVE A NICE DAY!!")