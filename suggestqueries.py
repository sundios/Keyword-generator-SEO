#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:09:14 2020

@author: kburchardt
"""


import requests
import json
import pandas as pd

keyword=input('Add your keyword')


def api_call(keyword):
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
    response = requests.get(url, verify=False)
    suggestions = json.loads(response.text)
    
    # get_keyword(suggestions)
    keywords =[]
    for word in suggestions[1]:
        k = word
        keywords.append(k)
        print(k)
        
    get_more(keywords)
           
def get_more(keywords):
    
    for i in keywords:
        print(i)
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + i
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)
        for word in suggestions[1]:
            k = word
            keywords.append(k)
            print(word)
            
        df = pd.DataFrame(keywords,columns=['Keywords'])
        json_hist = df.to_json(orient="table")

    
api_call(keyword)



