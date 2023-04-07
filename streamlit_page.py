import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#favicon = Image.open('favicon.ico')
st.set_page_config(page_title='My App',initial_sidebar_state='auto')


#reading the user input
age = st.selectbox('Enter your age:',list(death['age']))
sex = st.selectbox('Enter your sex:',list(death['sex']))
highest_qualification = st.selectbox('Enter your highest qualification',list(death['highest_qualification']))
rural = st.selectbox('Enter rural status:',list(death['rural']))
disability_status = st.selectbox('Enter disability status:',list(death['disability_status']))
is_water_filter = st.selectbox('Enter water filter status:',list(death['is_water_filter']))
chew = st.selectbox('Enter chew status:',list(death['chew']))
smoke = st.selectbox('Enter smoke status:',list(death['smoke']))
alcohol = st.selectbox('Enter alcohol status:',list(death['alcohol']))
treatment_source = st.selectbox('Enter treatment source:',list(death['treatment_source']))

def calculate():
    st.text_area(label='Results: ',placeholder='Results will be displayed here')

if st.button(label='Calculate',type='primary',disabled=False,use_container_width=True):
    calculate()

