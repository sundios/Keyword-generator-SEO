import requests
import json
import pandas as pd


keyword = 'sharks'

def api(keyword):
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
    response = requests.get(url, verify=False)
    suggestions = json.loads(response.text) 
    df1 = suggestions[1]
    
    df1 = pd.DataFrame(df1, columns=['Keywords'])
    
    df2 = []
    for i in df1['Keywords']:
        print(i)
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + i
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text) 
        df2.append(suggestions[1])
        
    new_df = []
    for k in df2:
        for i in range(10):
            new_df.append(k[i])
    print(new_df)
            
    
for i in new_df:
    api(i)    


api(keyword)


