import streamlit as st
import pandas as pd
import numpy as np

from datetime import datetime

today = datetime.today()


from data import calculate_age


## Header

st.header('Time Series Forecasting Tool')


# Input Widgets

# Name widgets

with st.form('my_form1',clear_on_submit=True):
    Name = st.text_area(label='Input your Name',placeholder= 'Please indicate your name e.g Lee Bundi')
    age = st.number_input(label='Insert your age',placeholder='What is your age?')
    date_of_birth = st.date_input(label='Which is your date of birth')
    
    submit = st.form_submit_button('Submit')


if submit is True:
    
    st.write(f'My name is {Name} and my age is {int(age)} ')
    st.write(f'My date of birth is {date_of_birth}')

    results = calculate_age(date_of_birth,age)
    st.warning(results)
    
else:
    
    st.markdown('''
                #### Please fill your details and submit above ☝️ :red[click me]
                
                ''')







