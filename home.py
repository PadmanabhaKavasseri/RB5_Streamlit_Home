import streamlit as st
from PIL import Image
import av
import requests
from bs4 import BeautifulSoup
import pdb
import urllib.parse



image = Image.open('Qualcomm-Logo-500x313.png')



def query_llm(query):
    url = 'https://m7zynasrjzhnocfpay2hfhbvwa0ttfpi.lambda-url.us-west-1.on.aws/?query='
    url+=urllib.parse.quote(query)
    response = requests.post(url)
    st.write(response.content)



st.title ('Qualcomm Demo')

sb = st.sidebar

sb.image(image)

button1 = sb.button("Apple")
button2 = sb.button("Beer")
button3 = sb.button("Cake")


if button1:
    st.write(":apple:")
    query_llm("Can i get an apple?")
if button2:
    st.write(":beer:")
    query_llm("Can i get a drink?")
if button3:
    st.write(":cake:")
    query_llm("Can i get something to eat?")


llm_message = st.text_input("Enter a message for the LLM hosted on the AWS Cloud",key="placeholder")

if llm_message:
    st.write("You enetered: ", llm_message)
    query_llm(llm_message)
    
    






