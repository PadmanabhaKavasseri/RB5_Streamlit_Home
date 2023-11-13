import streamlit as st
from PIL import Image
import av
import requests
from bs4 import BeautifulSoup
import pdb
import urllib.parse
import os



image = Image.open('Qualcomm-Logo-500x313.png')



def query_llm(query):
    url = 'https://m7zynasrjzhnocfpay2hfhbvwa0ttfpi.lambda-url.us-west-1.on.aws/?query='
    url+=urllib.parse.quote(query)
    response = requests.post(url)
    st.write(response.content)

    result = str(response.content)
    clean_string = result.strip("'")
    clean_string = clean_string.replace('"', '')
    clean_string = clean_string.replace('\'', '')
    output_string = clean_string[clean_string.find(":") + 2:]
    print(output_string)

    # ros2 topic pub -1 /llm example_interfaces/msg/String "{data: 'Hello from terminal'}"
    command = "ros2 topic pub -1 /llm std_msgs/msg/String " + '"{data: \'' + output_string + '\'}"'
    print(command)
    os.system(command)
    #ros executable -> outside of this file ./ros publisher ("txt") 



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
    
    






