import streamlit as st
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os


#loading frontend modules
from frontend import frontend
from backend import chatmodel
from backend import codemodel
modelType = frontend.SideBar()
frontend.chatbotfrontend()

userInput = st.text_input("Type here...")

button = st.button("Ask Now")

if button:
    if modelType == "Code Model":
        with st.spinner("Loading Model.."):
            dataRecived = codemodel.getResponse(userInput)
        frontend.displayData(userInput,dataRecived)
    elif modelType == "Chat Model":
        with st.spinner("Loading Model..."):
            dataRecived = chatmodel.getResponse(userInput)
        frontend.displayData(userInput,dataRecived)

