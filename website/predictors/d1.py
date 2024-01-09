from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
def preProcess(text):
    text = text.lower()
    text = re.sub('[^a-z]',' ',text)
    text = re.sub(' +',' ',text)
    text = text.split()
    text = [ps.stem(word) for word in text if word not in stopwords.words('english') and len(word)>=2 and word!='said' and word!='one']
    return ' '.join(text)

model = load_model('lstm')

with open('tokenizerD1.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def predict(title,text,maxlen):
    print('gg')
    final_text = title+' '+text
    final_text = preProcess(final_text)
    x = [final_text.split()]
    x = tokenizer.texts_to_sequences(x)
    x = pad_sequences(x,maxlen = maxlen)
    print(model.predict(x))
    return (model.predict(x)>=0.5).astype(int)