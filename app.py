import streamlit as st

st.title(":red[innomatics] data app")
st.snow()


btn_click = st.button("click me!")

st.write(btn_click)

if btn_click == True: 
    
    
    st.subheader("you clicked me:angry:") 
    st.balloons()
st.header(" data science internship")


st.subheader(":violet[feb 2023]")

CODE='''print("hello world")'''


st.code(CODE,language="python")