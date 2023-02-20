# Python Keyword tool generator SEO

Keyword tool generator SEO is a python script that uses Google suggested queries to get keyword ideas for keyword research. It also uses prefixes and suffixes to get more ideas so you dont miss any important keyword.
You can see this script in action on [https://www.keywordresearchtool.io/](https://www.keywordresearchtool.io/)

## Installation

To use this script we need to install the following libraries.

```bash
pip install requests
pip install json
pip install pandas
```

## Usage

This script is very straight forward. There are two ways you can use it. 

The first way is to run it in the terminal by doing:

```bash
python3 suggestqueries.py
```

This will aks you to `Add your keyword:` and once you add the keyword it will start getting keywords around that initial keyword.

Once is finished it will output a `.csv` file that will be named `<your keyword>-keywords.csv`

Here you will be able to see only unique keywords. 


### Limits

I set up a limit of 1000 keywords so it can stop at some point. But this is not necessary, you can set any limit you want by changing row 118 to any number you want.

```python

if len(keywords) >= 1000: #we can increase this number if we want more keywords
                print('##Finish here####')
                break
```

One thing to note is that at the end of the script, we remove all duplicate values so that the export only has unique values. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

*I'm planning to include other resources like yahoo, bing, youtube and others. There is a `service.py` file with all the endpoints. If you want to contribute that would be a good thing to start.*




