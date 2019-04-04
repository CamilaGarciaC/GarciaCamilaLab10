#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal


# In[4]:


data= pd.read_csv('DatosFinales.csv')

plt.figure(figsize=(20,7))
plt.plot(data["A"],data["D"])
plt.xticks(rotation=70)
plt.show()


# In[ ]:




