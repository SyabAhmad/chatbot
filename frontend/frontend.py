import streamlit as st

def SideBar():
    st.sidebar.title("Chat Application")
    
    st.sidebar.write("This chat bot is currenlty on top of deepseek free API,\n and its just for educational purposes")
    
    st.sidebar.write("Please select your model first")
    
    modelType = st.sidebar.selectbox("Choose model",["Code Model", "Chat Model"])
    
    return modelType
    

def chatbotfrontend():
    st.title("Chat Application")

    
    
def displayData(userInput,dataRecived):
    st.chat_message("👩‍💻")
    st.success(userInput)
    
    
    st.chat_message("👽")
    st.markdown(dataRecived)