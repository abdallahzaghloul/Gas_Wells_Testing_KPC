from PIL import Image
import numpy as np
import pandas as pd #2
import streamlit as st
from streamlit_gsheets import GSheetsConnection


import datetime
im = Image.open("KPC.png")
image= np.array(im)
st.image(image)
st.markdown(" <center>  <h1> Well Testing Follow UP </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
Well_Name = st.selectbox('The Well Name for current Testing',('BARAKAT-D01X','BARAKAT-D02X','BARAKAT-D06X','FUSTAT-N01X','IO-01X','BAT-10X','NUT-01X','SHAI-01X','ATOUN-N01X','APRIES-E01X','APRIES-E03X','ANTI-01X'))

from datetime import time

col1, col2, col3 = st.columns(3)
Date=datetime.date.today()
Date=Date.strftime('%d-%m-%Y')

Well_ID= Well_Name+"_"+Date

ii=""
with col1:
 if st.button('Show Results'):
  conn = st.experimental_connection("gsheets", type=GSheetsConnection)                      
  for i in range (1,48):
   ii=str(i)           
   try:
    st.write(conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1Z0clIbSazOxcYwngdQGK557s-ltIQ-Al_Ja5ypl2fgw",worksheet=Well_ID+"_"+ii) )
   except:
    pass            
                 
              
            
  
  
   
 
 
 
 
 
