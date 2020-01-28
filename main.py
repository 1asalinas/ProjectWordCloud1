from os import path
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv(r"pandp1.text", header = None) 

comment_words = ' '
stopwords = set(STOPWORDS) 

for word in df.CONTENT:   
    word = str(word) 
    tokens = word.split()    
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower()       
    for words in tokens: 
     comment_words = comment_words + words + ' '
  
wordcloud = WordCloud(width = 100, height = 100, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 
