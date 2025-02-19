import streamlit as st 
import pickle 
import nltk # type: ignore
import seaborn as sns # type: ignore
from nltk.corpus import stopwords # type: ignore
from nltk.stem.porter import PorterStemmer # type: ignore
from wordcloud import WordCloud
from collections import Counter

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

ps  = PorterStemmer()
import string 

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y=[]
    for i in text :
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


st.title("Email/SMS spam classifier")

input_sms = st.text_area("Enter the message : ")

if st.button("Predict"):

    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize 
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict 
    result = model.predict(vector_input)[0]
    # 4. Display 
    if result == 1:
        st.header("Spam")
    else: 
        st.header("Not Spam")