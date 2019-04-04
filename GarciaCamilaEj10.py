#!/usr/bin/env python
# coding: utf-8

# In[2]:


import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal


# In[3]:


datos1= pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2008.txt",sep=";",header=None, names= ["A","B","C","D"])
datos2= pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2009.txt",sep=";",header=None, names= ["A","B","C","D"])
datos3= pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2010.txt",sep=";",header=None, names= ["A","B","C","D"])
datos1["A"]= datos1["A"].astype(str).str[:-7]
datos1["B"]=datos1["B"].astype(str).str[11:]
sol1=datos1["A"]
print(datos1)


# In[4]:


datos2["A"]= datos2["A"].astype(str).str[:-7]
datos2["B"]=datos2["B"].astype(str).str[11:]
print(datos2)


# In[5]:


datos3= pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2010.txt",sep=";",header=None, names= ["A","B","C","D"])
datos3["A"]= datos3["A"].astype(str).str[:-7]
datos3["B"]=datos3["B"].astype(str).str[11:]
s3=datos3
print(datos3)


# In[6]:


final=pd.concat([datos1,datos2,datos3])
print(final)


# In[7]:


final.to_csv("DatosFinales.csv")





