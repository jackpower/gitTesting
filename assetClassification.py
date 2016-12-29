#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 17:31:42 2016

@author: Jack
"""

# A script to test if different asset classes respond 
# differently to different predictor variables

# Load data

import pandas as pd
import os

os.chdir('/Users/Jack/Documents/gitTesting')

with pd.HDFStore('data/train.h5') as train:
    df = train.get('train')