import pandas as pd
import numpy as np
from PIL import Image
import cv2
import gc
#get_ipython().run_line_magic('matplotlib', 'inline')
import os
from os import getcwd
import glob

fer_data = pd.read_csv('../fer2013.csv')
fer_data.columns
fer_data.shape
fer_data.index
fer_data.info()
fer_data.tail(3)
fer_data.head(3)
fer_data.sample(n=8)
fer_data['Usage'].unique()
fer_data.Usage.value_counts()
fer_data.dtypes
fer_data.pixels.dtype
fer_data.describe()
fer_data.isna().any()
fer_data[['emotion', 'Usage']].groupby('Usage').mean()
fer_data.loc[:5,['emotion', 'Usage']]

fer2021_data = pd.read_csv('../fer2021-affectnet-valid.csv')
fer2021_data.columns
fer2021_data.shape
fer2021_data.index
fer2021_data.info()
fer2021_data.tail(3)
fer2021_data.head(3)
fer2021_data.sample(n=8)
fer2021_data['Usage'].unique()
fer2021_data.Usage.value_counts()
fer2021_data.dtypes
fer2021_data.pixels.dtype
fer2021_data.describe()
fer2021_data.isna().any()
fer2021_data[['emotion', 'Usage']].groupby('Usage').median()
fer2021_data.loc[:5,['emotion', 'Usage']]
