#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:05:10 2021

@author: uliw
"""
import pandas as pd

df = pd.read_excel("Yao_2018_pd_series.xlsx")

print(df.head())

x = df.loc[df.Location=='in','Age [Ma]']
y = df.loc[df.Location=='in','d34S']
print(type(x))