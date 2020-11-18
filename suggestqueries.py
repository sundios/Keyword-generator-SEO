#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:09:14 2020

@author: kburchardt
"""


import requests
import json
import pandas as pd
# =============================================================================
# Keyword Suggestor for Keyword Research
# =============================================================================

keyword=input('Add your keyword')

'''
api_call makes the first api call to get the initial 10 queries
We only need one parameter which is the initial Keyword we want 
to get ideas from. We create a list called Keywords that we store
all the keywords

Inside this function we also have get_more
'''

def api_call(keyword):
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
    response = requests.get(url, verify=False)
    suggestions = json.loads(response.text)
    
    # get_keyword(suggestions)
    keywords =[]
    for word in suggestions[1]:
        keywords.append(word)
        print(word)
        
    get_more(keywords)  
    
'''
get more takes the keywords list and runs the keywords via the
api to get more suggestions. Every new suggestion is stored back in
the keywords list.

I set a limit of 1000 Keywords but this can be increased.
'''
           
def get_more(keywords):
        for i in keywords:
            url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + i
            response = requests.get(url, verify=False)
            suggestions = json.loads(response.text)
            for word in suggestions[1]:
                print(word)
                keywords.append(word)
                print(len(keywords))

            if len(keywords) >= 1000: #we can increase this number if we want more keywords
                print('##Finish here####')
                break
    
    
        df = pd.DataFrame(keywords,columns=['Keywords'])
        json_hist = df.to_json(orient="table")

        df.to_csv('test.csv')
    
api_call(keyword)



