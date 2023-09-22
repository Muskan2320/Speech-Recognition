#!/usr/bin/env python
# coding: utf-8

# IMPORTING NECESSARY FILES

# In[22]:


import numpy as np                     # for dealing arrays
import matplotlib.pyplot as plt        # for plotting
from glob import glob                  # for reading files

import librosa as lr                   # for reading and manipulating audio files


# In[23]:


# Read all files with wav extension/ending

direc = './minor'
audio_files = glob(direc + '/*.WAV')   

len(audio_files)


# READING FIRST AUDIO FILE

# In[9]:


audio, freq_in_sec = lr.load(audio_files[0])   
# load() function returns the time series
# It is one-dimensional floating point array, where array[t] gives the amplitude at t time
# freq_in_sec is the sampling rate


# In[10]:


time = np.arange(0, len(audio))/ freq_in_sec    # time = 1/freq

time


# In[16]:


# Plotting audio file

plt.plot(time, audio)
plt.xlabel('Time(sec)')
plt.ylabel('Sound Amplitude')
plt.show()


# READING ANOTHER AUDIO FILE

# In[21]:


audio, freq_in_sec = lr.load(audio_files[19])
time = np.arange(0, len(audio))/ freq_in_sec
plt.plot(time, audio)
plt.xlabel('Time(sec)')
plt.ylabel('Sound Amplitude')
plt.show()

