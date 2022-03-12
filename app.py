# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np


import streamlit.components.v1 as components

import pickle
Encoder = open('Country_encoder.pkl','rb')
enc = pickle.load(Encoder)

model=open('LR_VIF.pkl','rb')
lr=pickle.load(model)

global weights

weights=pd.read_csv('Article_weight-2.csv')
 
components.html(
<marquee>
This is a sample scrolling text that has scrolls texts to down.
</marquee>    

)

st.header('Fill the Detail to know the Foreign Exchange Rate')

st.markdown("#### Select a year")
year = st.selectbox('Select Location',(2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
       2017, 2018, 2019))

st.markdown("#### Enter the Country")
Country = st.radio("Is the property New? ", ('USA', 'CHINA', 'INDIA', 'JAPAN', 'SWITZERLAND', 'CANADA',
       'AUSTRALIA', 'BRAZIL', 'UK'))


st.markdown("#### GDP")
gdp=st.number_input('Enter in the GDP',format="%.3f")

st.markdown("#### Enter PPP ")
ppp=st.number_input('Enter PPP',format="%.3f")

st.markdown("#### Enter Export ")
Export=st.number_input('Enter Export',format="%.3f")

st.markdown("#### INVL")
invl=st.number_input('Enter in the INVL',format="%.3f")



st.markdown("#### Enter Invest ")
invest=st.number_input('Enter Invest',format="%.3f")

st.markdown("#### Enter Import ")
Import=st.number_input('Enter Import',format="%.3f")

for i in range(len(weights)):
    if weights['Years'][i]==year:
        Topic_1=round(weights['Topic-1'][i],3)
        Topic_2=round(weights['Topic-2'][i],3)
        Topic_3=round(weights['Topic-3'][i],3)


gdp=round(np.sqrt(gdp),3)
ppp=round(np.sqrt(ppp),3)
Export=round(np.sqrt(Export),3)
invl=round(np.sqrt(invl),3)
Import=round(np.sqrt(Import),3)
invest=round(np.sqrt(invest),3)

Country_ecn=enc.transform([Country])[0]


button=st.button('Predict')




if button:
        
    predict_1={'PPP':[],'GDP':[],'Export':[],'INVL':[],'Invest':[],'Import':[],'Topic-1':[],'Topic-2':[],'Topic-3':[],'Country':[]}
    Pred_data=pd.DataFrame(predict_1)
    Pred_data=Pred_data.append({'PPP':ppp,'GDP':gdp,'Export':Export,'INVL':invl,'Invest':invest,'Import':Import,'Topic-1':Topic_1,'Topic-2':Topic_2,'Topic-3':Topic_3,'Country':Country_ecn},ignore_index=True)
    fer=lr.predict(Pred_data)
    string='The Foreign Exchange is '
    a=str(fer[0])
    st.write(string+ a[1:6])        
    
    
    
    
    
    
    
    
    
