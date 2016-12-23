#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:44:17 2016

@author: Jack
"""

import numpy as np
import pandas as pd

with pd.HDFStore('/Users/Jack/Documents/gitTesting/data/train.h5') as train:
    df = train.get('train')
    
#Sampling for testing
sampleAssetIDs = df['id'].drop_duplicates().sample(frac=0.05)
df = df.loc[df['id'].isin(sampleAssetIDs)]
            
#Create average variable
df = df.sort_values(['id','timestamp'])
dfYOnly = df.loc[:,['id','timestamp','y']]

pivoted_df = pd.pivot_table(dfYOnly, index = 'y', columns='timestamp', values='y')
average_fruits = pivoted_df.rolling(window=3).mean().stack() 