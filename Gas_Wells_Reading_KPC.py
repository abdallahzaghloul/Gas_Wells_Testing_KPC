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
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
L=conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1Z0clIbSazOxcYwngdQGK557s-ltIQ-Al_Ja5ypl2fgw",worksheet=Well_ID+"_1",ttl="1")

dfn=conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1Z0clIbSazOxcYwngdQGK557s-ltIQ-Al_Ja5ypl2fgw",worksheet="Sheet1")
n=dfn['Reading_No'].loc[0]  
n=int(n)
H="R_"
L=[]
st.write(n)
CK=[]
Reading_No=[]
Registeration_Time=[]
Date=[]
WHP=[]
SEP_Pressure=[]
SEP_Temperature=[]
FLP=[]
FLT=[]
Gas_Rate=[]
Water=[]
Condensate=[]
GOR=[]
API=[]
BSW=[]
CO2=[]
H2S=[]
SAL=[]
if st.button('Show Results'):
  conn = st.experimental_connection("gsheets", type=GSheetsConnection)  
  for i in range(1,n+1):           
   L=H+str(i)
   ii=str(i)           
   L=conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1Z0clIbSazOxcYwngdQGK557s-ltIQ-Al_Ja5ypl2fgw",worksheet=Well_ID+"_"+ii,ttl="1")
   CK.append(L['C.K%'].loc[0])
   Reading_No.append(L['Reading_No'].loc[0])
   Registeration_Time.append(L['Registeration_Time'].loc[0])
   Date.append(L['Date'].loc[0])
   WHP.append(L['WHP'].loc[0])
   SEP_Pressure.append(L['SEP_Pressure'].loc[0])
   SEP_Temperature.append(L['SEP_Temperature'].loc[0]) 
   FLP.append(L['FLP'].loc[0])
   FLT.append(L['FLT'].loc[0])
   Gas_Rate.append(L['Gas_Rate'].loc[0])
   Condensate.append(L['Condensate'].loc[0])           
   Water.append(L['Water'].loc[0])           
   GOR.append(L['GOR'].loc[0])           
   BSW.append(L['BS&W'].loc[0])
   CO2.append(L['CO2 %'].loc[0])
   H2S.append(L['H2S'].loc[0])
   SAL.append(L['SAL'].loc[0])
              
   R=pd.DataFrame(Registeration_Time,columns= ["Date"])
   R1=pd.DataFrame(CK,columns= ["C.K %"])           
   R2=pd.DataFrame(Registeration_Time,columns= ["Registeration_Time"])
   R3=pd.DataFrame(WHP,columns= ["WHP"])
   R4=pd.DataFrame(SEP_Pressure,columns= ["SEP_Pressure"])
   R5=pd.DataFrame(SEP_Temperature,columns= ["SEP_Temperature"])
   R6=pd.DataFrame(FLP,columns= ["FLP"])
   R7=pd.DataFrame(FLT,columns= ["FLT"])
   R8=pd.DataFrame(Gas_Rate,columns= ["Gas_Rate"])
   R9=pd.DataFrame(Water,columns= ["Water"])
   R10=pd.DataFrame(Condensate,columns= ["Condensate"])
   R11=pd.DataFrame(GOR,columns= ["GOR"])
   R12=pd.DataFrame(API,columns= ["API"])
   R13=pd.DataFrame(BSW,columns= ["BS&W"])
              
   IMP=pd.DataFrame(H2S,columns= ["H2S"])
   IMP1=pd.DataFrame(SAL,columns= ["SAL"])
   IMP2=pd.DataFrame(CO@,columns= ["CO2 %"])          
   IMP["SAL KPPM"]=IMP1
   IMP["CO2 %"]=IMP2
              
   R["C.K %"]=R1           
   R["Registeration_Time"]=R2           
   R["WHP"]=R3           
   R["SEP_Pressure"]=R4           
   R["SEP_Temperature"]=R5           
   R["FLP"]=R6           
   R["FLT"]=R7           
   R["Gas_Rate"]=R8           
   R["Water"]=R9           
   R["Condensate"]=R10           
   R["GOR"]=R11           
   R["API"]=R12           
   R["BS&W"]=R13
   R["BS&W"]=R["BS&W"].astype('float')*100           
   R["C.K %"]=R["C.K %"].astype('float')*100            
   R["BS&W"]=R["BS&W"].astype('str')+" %"           
   R["C.K %"]=R["C.K %"].astype('str')+" %"            
  st.write(R)     
  st.write(IMP)     
  
 
