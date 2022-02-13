# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np



import pickle
Encoder = open('/Users/ishanishah/Documents/Technocolab Software/Project/Web app/Country_encoder.pkl','rb')
enc = pickle.load(Encoder)

model=open('/Users/ishanishah/Documents/Technocolab Software/Project/Web app/LR.pkl','rb')
lr=pickle.load(model)

st.header('Fill the Detail to know the Foreign Exchange Rate')

st.markdown("#### Select a year")
year = st.selectbox('Select Location',(2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
       2017, 2018, 2019))

st.markdown("#### Enter the Country")
Country = st.radio("Is the property New? ", ('USA', 'CHINA', 'INDIA', 'JAPAN', 'SWITZERLAND', 'CANADA',
       'AUSTRALIA', 'BRAZIL', 'UK'))


st.markdown("#### GDP")
gdp=st.number_input('Enter in the GDP',format="%.5f")

st.markdown("#### Enter PPP ")
ppp=st.number_input('Enter PPP',format="%.5f")

st.markdown("#### INVL")
invl=st.number_input('Enter in the INVL',format="%.5f")

st.markdown("#### Enter Invest ")
invest=st.number_input('Enter Invest',format="%.5f")



gdp=np.sqrt(gdp)
ppp=np.sqrt(ppp)
invl=np.sqrt(invl)
invest=np.sqrt(invest)

Country_ecn=enc.transform([Country])[0]


button=st.button('Predict')


if button:
        
    predict_1={'PPP':[],'GDP':[],'INVL':[],'Invest':[],'Country':[]}
    Pred_data=pd.DataFrame(predict_1)
    
    Pred_data=Pred_data.append({'PPP':ppp,'GDP':gdp,'INVL':invl,'Invest':invest,'Country':Country_ecn},ignore_index=True)
    
    
    fer=lr.predict(Pred_data)
    string='The Foreign Exchange is '
    a=str(fer[0])
    st.write(string+ a[:6])        
    
    
    
    
    
    
    
    
    