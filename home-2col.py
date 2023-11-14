import streamlit as st
from PIL import Image
import av
import requests
import pdb
import urllib.parse
import os



qc_logo = Image.open('Qualcomm-Logo-500x313.png')
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


def parse_llm(resp):
    action = None

    if "water" in resp:
        action = "water"
    elif "apple" in resp:
        action = "apple"
    elif "cup" in resp:
        action = "cup"
    else:
        return
    
    # publish on /llm
    # example publish command : 
    # ros2 topic pub -1 /llm example_interfaces/msg/String "{data: 'Hello from terminal'}"
    command = "ros2 topic pub -1 /robot_action std_msgs/msg/String " + '"{data: \'' + action + '\'}"'
    print("command : ", command)
    os.system(command)


def query_llm(query):
    url = 'https://m7zynasrjzhnocfpay2hfhbvwa0ttfpi.lambda-url.us-west-1.on.aws/?query='
    url+=urllib.parse.quote(query)
    response = requests.post(url)
    

    print("Response.content: ", response.content)

    result = response.content.decode("utf-8").strip("\"").lower()
    print("result:", result)
    col1.text(result)
    parse_llm(result)
    
    # output_string = clean_string[clean_string.find(":") + 1:]
    # print(output_string)

    # ros2 topic pub -1 /llm example_interfaces/msg/String "{data: 'Hello from terminal'}"
    # command = "ros2 topic pub -1 /llm std_msgs/msg/String " + '"{data: \'' + output_string + '\'}"'
    # # print(command)
    # os.system(command)
    #ros executable -> outside of this file ./ros publisher ("txt") 



st.title ('Robotics with LLMs')

col1, col2 = st.columns([3, 1])




sb = st.sidebar

sb.image(qc_logo)
sb.subheader("Sample Prompts")
sb.divider()

button1 = sb.button("Get me an Apple")
button2 = sb.button("Get me a cup")
button3 = sb.button("Get me water")
button4 = sb.button("I am thirsty")
button5 = sb.button("I want to make a smoothie")
button6 = sb.button("Get me something to pour my tea")
button7 = sb.button("Get me a fruit")


if button1:
    query_llm("Get me an Apple")
if button2:
    query_llm("Get me a cup")
if button3:
    query_llm("Get me water")
if button4:
    query_llm("I am thirsty")
if button5:
    query_llm("I want to make a smoothie")
if button6:
    query_llm("Get me something to pour my tea")
if button7:
    query_llm("Get me a fruit")




col1.subheader("Make the arm do work")
llm_message = col1.text_input("Enter a message for the LLM hosted on the AWS Cloud",key="placeholder")

col1.subheader("LLM's response: ")
if llm_message:
    # col1.write("You enetered: ", llm_message)
    query_llm(llm_message)
    
    
col2.subheader("About the RB5")
rb5 = Image.open('qual_2.jpg')
col2.image(rb5)






