import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

df=pd.read_csv('./cleandata.csv')

#favicon = Image.open('favicon.ico')
st.set_page_config(page_title='My App',initial_sidebar_state='auto')


#reading the user input
age = st.selectbox('Enter your age:',list(df['age'].unique()))
sex = st.selectbox('Enter your sex:',list(df['sex'].unique()))
dfr=df[df['age']==age][['sex','highest_qualification']]
highest_qualification = st.selectbox('Enter your highest qualification',list(dfr[dfr['sex']==sex]['highest_qualification'].unique()))
dfr=df[df['age']==age][['sex','highest_qualification','rural']]
dfr=dfr[dfr['sex']==sex][['highest_qualification','rural']]
rural = st.selectbox('Enter rural status:',list(dfr[dfr['highest_qualification']==highest_qualification]['rural'].unique()))
dfr=df[df['age']==age][['sex','highest_qualification','rural','disability_status']]
dfr=dfr[dfr['sex']==sex][['highest_qualification','rural','disability_status']]
dfr=dfr[dfr['highest_qualification']==highest_qualification][['rural','disability_status']]
disability_status = st.selectbox('Enter disability status:',list(dfr[dfr['rural']==rural]['disability_status'].unique()))
dfr=df[df['age']==age][['sex','highest_qualification','rural','disability_status','is_water_filter']]
dfr=dfr[dfr['sex']==sex][['highest_qualification','rural','disability_status','is_water_filter']]
dfr=dfr[dfr['highest_qualification']==highest_qualification][['rural','disability_status','is_water_filter']]
dfr=dfr[dfr['rural']==rural][['disability_status','is_water_filter']]
is_water_filter = st.selectbox('Enter water filter status:',list(dfr[dfr['disability_status']==disability_status]['is_water_filter'].unique()))
dfr=df[df['age']==age][['sex','highest_qualification','rural','disability_status','is_water_filter','chew']]
dfr=dfr[dfr['sex']==sex][['highest_qualification','rural','disability_status','is_water_filter','chew']]
dfr=dfr[dfr['highest_qualification']==highest_qualification][['rural','disability_status','is_water_filter','chew']]
dfr=dfr[dfr['rural']==rural][['disability_status','is_water_filter','chew']]
dfr=dfr[dfr['disability_status']==disability_status][['is_water_filter','chew']]
chew = st.selectbox('Enter chew status:',list(dfr[dfr['is_water_filter']==is_water_filter]['chew'].unique()))
dfr=df[df['age']==age][['sex','highest_qualification','rural','disability_status','is_water_filter','chew','smoke']]
dfr=dfr[dfr['sex']==sex][['highest_qualification','rural','disability_status','is_water_filter','chew','smoke']]
dfr=dfr[dfr['highest_qualification']==highest_qualification][['rural','disability_status','is_water_filter','chew','smoke']]
dfr=dfr[dfr['rural']==rural][['disability_status','is_water_filter','chew','smoke']]
dfr=dfr[dfr['disability_status']==disability_status][['is_water_filter','chew','smoke']]
dfr=dfr[dfr['is_water_filter']==is_water_filter][['chew','smoke']]
smoke = st.selectbox('Enter smoke status:',list(dfr[dfr['chew']==chew]['smoke'].unique()))
dfr=df[df['age']==age][['sex','highest_qualification','rural','disability_status','is_water_filter','chew','smoke','alcohol']]
dfr=dfr[dfr['sex']==sex][['highest_qualification','rural','disability_status','is_water_filter','chew','smoke','alcohol']]
dfr=dfr[dfr['highest_qualification']==highest_qualification][['rural','disability_status','is_water_filter','chew','smoke','alcohol']]
dfr=dfr[dfr['rural']==rural][['disability_status','is_water_filter','chew','smoke','alcohol']]
dfr=dfr[dfr['disability_status']==disability_status][['is_water_filter','chew','smoke','alcohol']]
dfr=dfr[dfr['is_water_filter']==is_water_filter][['chew','smoke','alcohol']]
dfr=dfr[dfr['chew']==chew][['chew','smoke','alcohol']]
alcohol = st.selectbox('Enter alcohol status:',list(dfr[dfr['smoke']==smoke]['alcohol'].unique()))
dfr=df[df['age']==age][['sex','highest_qualification','rural','disability_status','is_water_filter','chew','smoke','alcohol','treatment_source']]
dfr=dfr[dfr['sex']==sex][['highest_qualification','rural','disability_status','is_water_filter','chew','smoke','alcohol','treatment_source']]
dfr=dfr[dfr['highest_qualification']==highest_qualification][['rural','disability_status','is_water_filter','chew','smoke','alcohol','treatment_source']]
dfr=dfr[dfr['rural']==rural][['disability_status','is_water_filter','chew','smoke','alcohol','treatment_source']]
dfr=dfr[dfr['disability_status']==disability_status][['is_water_filter','chew','smoke','alcohol','treatment_source']]
dfr=dfr[dfr['is_water_filter']==is_water_filter][['chew','smoke','alcohol','treatment_source']]
dfr=dfr[dfr['chew']==chew][['chew','smoke','alcohol','treatment_source']]
treatment_source = st.selectbox('Enter treatment source:',list(dfr[dfr['alcohol']==alcohol]['treatment_source'].unique()))

Y=[sex,highest_qualification,rural,disability_status,is_water_filter,chew,smoke,alcohol,treatment_source]
Y=np.array(Y).reshape(1,-1)

from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=10,random_state=0)
regressor.fit(df[['sex','highest_qualification','rural','disability_status','is_water_filter','chew','smoke','alcohol','treatment_source']],df['age'])

rf_model_predictions = regressor.predict(Y)
# Calculate the mean absolute error of your Random Forest model on the validation data
#rf_val_mae = mean_absolute_error(y_test,rf_model_predictions)
data = rf_model_predictions

def calculate():
    st.text_area(label='Results: ',placeholder='You will die at '+str(data))

if st.button(label='Calculate',type='primary',disabled=False,use_container_width=True):
    calculate()
