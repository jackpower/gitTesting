#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 17:31:42 2016

@author: Jack
"""

# A script to test if different asset classes respond 
# differently to different predictor variables

# Set working directory
import os
os.chdir('/Users/Jack/Documents/gitTesting')

# Load data
import pandas as pd

with pd.HDFStore('data/train.h5') as train:
    df = train.get('train')
    
# Sample dataset for testing the script
sampleAssetIDs = df['id'].drop_duplicates().sample(frac=0.05)
df = df.loc[df['id'].isin(sampleAssetIDs)]
del(sampleAssetIDs)

df.groupby(['id']).corr()["y"]

newDF = pd.DataFrame(index=df['id'].drop_duplicates(), columns=df.columns)