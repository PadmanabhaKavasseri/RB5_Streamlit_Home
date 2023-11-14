import streamlit as st
from PIL import Image
import av
import requests
import pdb
import urllib.parse
import os



qc_logo = Image.open('Qualcomm-Logo.png')
q_robotics = Image.open('qual_2.jpg')


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

# sends ros msg
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
    return action


def query_llm(query):
    url = 'https://m7zynasrjzhnocfpay2hfhbvwa0ttfpi.lambda-url.us-west-1.on.aws/?query='
    url+=urllib.parse.quote(query)
    response = requests.post(url)
    

    print("Response.content: ", response.content)

    result = response.content.decode("utf-8").strip("\"").lower()
    print("result:", result)
    action = parse_llm(result)
    st.session_state.llm_res = action
    
    # output_string = clean_string[clean_string.find(":") + 1:]
    # print(output_string)

    # ros2 topic pub -1 /llm example_interfaces/msg/String "{data: 'Hello from terminal'}"
    # command = "ros2 topic pub -1 /llm std_msgs/msg/String " + '"{data: \'' + output_string + '\'}"'
    # # print(command)
    # os.system(command)
    #ros executable -> outside of this file ./ros publisher ("txt") 



st.title ('Robotics with LLMs')
st.divider()

col1, col2 = st.columns([3, 1],gap="large")

# col1.divider()
# col2.divider()
# col1.subheader("Examples")
# col2.subheader("Sample Prompts")

sb = st.sidebar

# sb.image(q_robotics)
sb.image(qc_logo)
# sb.subheader("Compute at your fingertips")
# sb.divider()

sb.image(q_robotics)

button1 = col2.button("Get me an Apple")
button2 = col2.button("Get me a cup")
button3 = col2.button("Get me water")
button4 = col2.button("I am thirsty")
button5 = col2.button("I want to make a smoothie")
button6 = col2.button("Get me something to pour my tea")
button7 = col2.button("Get me a fruit")


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



def txtbox_cb():
    query_llm(st.session_state.txtbox)
    st.session_state.txtbox = ''
    

# col1.subheader("Make the arm do work")
col1.text_input("Enter a message for the LLM hosted on the AWS Cloud", key="txtbox", on_change=txtbox_cb)
col1.text_input("LLM Output",key="llm_res", disabled=True, label_visibility="visible")
    
    
    


# col2.image(q_robotics)

rb52 = Image.open('qyalbpt.png')
col2.image(rb52)








