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

from datetime import time

col1, col2, col3 = st.columns(3)

with col1:
 if st.button('Show Results'):
  for i in range (1,48):           
   try:
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)           
    st.write(conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1Z0clIbSazOxcYwngdQGK557s-ltIQ-Al_Ja5ypl2fgw",worksheet=Well_ID+"_"+str(i)) )            
   except:
    pass        
  
            
 
 
  


 


