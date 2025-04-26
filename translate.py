## Install googletrans first using one of the methods below:
# pip install googletrans==4.0.0-rc1
# pip install googletrans==3.1.0a0
# pip install google_trans_new

import googletrans
from googletrans import Translator
import pandas as pd
import time
import json

# Init
translator = Translator()


test_set = []
with open("./wikidata12500-2.jsonl", "r") as f:
  for line in f:
    test_set.append(json.loads(line))

print(test_set)
print(test_set[0]['s'])



all_lang = ['zh-tw']

length = len(test_set)

# append 100 values from 1 to 100
# with 1 as key to list

# display list
print(l)

lines = []

for line in range(length):
    #temp = translator.translate(text[line],src='eng',dest='hin')
    print(line)
    time.sleep(1)
    new_prompt = translator.translate(test_set[line]['prompt'],src='en',dest='zh-tw').text
    time.sleep(1)
    new_ss = translator.translate(test_set[line]['ss'],src='en',dest='zh-tw').text
    time.sleep(1)
    new_os = translator.translate(test_set[line]['os'],src='en',dest='zh-tw').text
    new_s  = test_set[line]['s']
    new_p  = test_set[line]['p']
    new_o = test_set[line]['o']
    lines.append([new_prompt,new_ss,new_os,new_s,new_p,new_o])

print(lines)
columns = ['prompt','ss','os','s','p','o']
df = pd.DataFrame(data = lines,columns=columns)
with open("metadata.jsonl", "w", encoding='utf-8') as outfile:
    for prompt, ss , os , s , p , o in zip(df['prompt'], df['ss'] , df['os'],df['s'] , df['p'] , df['o']):
        entry = {"prompt": prompt, "ss": ss , "os" :os , "s":s , "p":p , "o":o}
        print(json.dumps(entry), file=outfile)


