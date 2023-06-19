import re
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

def clean_data(data):
  text = re.sub(r"\[[0-9]*\]"," ",data)
  text = re.sub('[%s]' % re.escape("""!",-.:;?`"""),' ', text)  # remove punctuations
  text = text.lower() # convert to lower case
  text = re.sub(r'\s+'," ",text)  # remove extra whitespace
  # text = re.sub(r'[^\x00-\x7f]',r' ', text) #non ascii values
  # tokens = [w for w in data.split() if not w in stop_words]
  # text = ' '.join(tokens)
  return text

# cleaned_data = clean_data(raw_data)