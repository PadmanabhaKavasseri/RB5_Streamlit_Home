import streamlit as st
from PIL import Image
import av


image = Image.open('Qualcomm-Logo-500x313.png')


st.title ('Qualcomm Demo')

sb = st.sidebar

sb.image(image)

button1 = sb.button("Apple")
button2 = sb.button("Beer")
button3 = sb.button("Cake")


if button1:
    st.write(":apple:")
if button2:
    st.write(":beer:")
if button3:
    st.write(":cake:")


llm_message = st.text_input("Enter a message for the LLM hosted on the AWS Cloud",key="placeholder")

if llm_message:
    st.write("You enetered: ", llm_message)


