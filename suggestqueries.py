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
    keywords = [keyword]
    
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
    response = requests.get(url, verify=False)
    suggestions = json.loads(response.text)
    
    
    for word in suggestions[1]:
        keywords.append(word)
        
    prefixes(keyword)
    suffixes(keyword)
    get_more(keywords)  
    
    
def prefixes(keyword):
    
    prefixes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','x','y','z','how','which','why','where','who','when','are','what']    
    
    for prefix in prefixes:
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + prefix + " " + keyword 
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)
        
        kws = suggestions[1]
        length = len(kws)
        
        for n in range(length):
            print(kws[n])
            keywords.append(kws[n])
            
def suffixes(keyword):
    
    suffixes =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','x','y','z','like','for','without','with','versus','vs','to','near','except','has']
    
    
    for suffix in suffixes:
        print(suffix)
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword + " " + suffix 
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)
        
        kws = suggestions[1]
        length = len(kws)
        
        for n in range(length):
            print(kws[n])
            keywords.append(kws[n])   
'''
get more takes the keywords list and runs the keywords via the
api to get more suggestions. Every new suggestion is stored back in
the keywords list.

I set a limit of 1000 Keywords but this can be increased.
'''
           
def get_more(keywords):
        for i in keywords:
            print(i)
            url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + i
            response = requests.get(url, verify=False)
            suggestions = json.loads(response.text)
            
            keywords2 =  suggestions[1]
            length = len(keywords2)
            
            for n in range(length):
                print(keywords2[n])
                keywords.append(keywords2[n])
                print(len(keywords))
                
                
            if len(keywords) >= 2000: #we can increase this number if we want more keywords
                print('##Finish here####')
                break
            
        keywords = list(dict.fromkeys(keywords))
    
    
        df = pd.DataFrame(keywords,columns=['Keywords'])
        json_hist = df.to_json(orient="table")

        df.to_csv('test.csv')




    
api_call(keyword)




