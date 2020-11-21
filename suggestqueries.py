import requests
import json
import pandas as pd
# =============================================================================
# Keyword Suggestor for Keyword Research
# =============================================================================

keyword=input('Add your keyword: ')

'''
api_call makes the first api call to get the initial 10 queries
We only need one parameter which is the initial Keyword we want 
to get ideas from. We create a list called Keywords that we store
all the keywords

End of function we call 3 other functions to build up the keywords list
'''

def api_call(keyword):
    
    keywords = [keyword]
     
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
    response = requests.get(url, verify=False)
    suggestions = json.loads(response.text)
    
    
    for word in suggestions[1]:
        keywords.append(word)
        
    prefixes(keyword,keywords)
    suffixes(keyword,keywords)
    get_more(keyword,keywords) 
    
'''
prefixes adds a value from the prefix list before the keyword we passed 
and get suggestions out of that. Then it appends each of the keyword to 
the keywords lists.

function passes to parameters:
    keyword: value we want to check.
    keywords: list to append values.
'''    
        
def prefixes(keyword,keywords):
    #we can add more suffixes tailored to the company or type of search we are looking. E.g: food delivery, delivery,etc
    prefixes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','x','y','z','how','which','why','where','who','when','are','what']    
    
    for prefix in prefixes:
        print(prefix)
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + prefix + " " + keyword 
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)
        
        kws = suggestions[1]
        length = len(kws)
        
        for n in range(length):
            print(kws[n])
            keywords.append(kws[n])
            
'''
suffixes adds a value from the prefix list after the keyword we passed 
and get suggestions out of that. Then it appends each of the keyword to 
the keywords lists.

function passes to parameters:
    keyword: value we want to check.
    keywords: list to append values.
'''  
            
def suffixes(keyword,keywords):
    #we can add more suffixes tailored to the company or type of search we are looking. E.g: food delivery, delivery,etc
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
Once it hits 1000 keyowrds it stops and we run a deduplicator so we
 only get unique keywords
'''        
def get_more(keyword,keywords):
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
            
                   
            if len(keywords) >= 1000: #we can increase this number if we want more keywords
                print('###Finish here####')
                break
            
        #removing duplicates from the list
        keywords = list(dict.fromkeys(keywords)) 
        
        df = pd.DataFrame(keywords,columns=['Keywords'])
        json_hist = df.to_json(orient="table")

        #Exporting all keywords to CSV
        df.to_csv(keyword+'-keywords.csv')
   
api_call(keyword)




