import pandas as pd 
import numpy as np
import re

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import multidict as multidict
from wordcloud import WordCloud
from PIL import Image

img_path = '/home/matt/portfolio/personal_portfolio/spotify/img'

def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(","):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict

def masked_wordcloud(data, mask, name, min_font = 3, colormap_choice='tab20c'):
    '''
    input: cleaned artist dataframe, mask file path, image name, minimum font, color pallete
    returns: saved wordcloud image, prints used genre text
    '''
    genres_list = data['genres'].tolist()
    genres_text = ",".join(genre for genre in genres_list).replace("'", "").replace('"', '')

    text = getFrequencyDictForText(genres_text)

    note_mask = np.array(Image.open(mask))
    note_mask = note_mask[:,:,2]

    wc = WordCloud(background_color = 'white',mask=note_mask, min_font_size = min_font, colormap=colormap_choice)
    wc.generate_from_frequencies(text)
    
    plt.figure(figsize=[5,5])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    plt.title('Genre Word Cloud')
    plt.savefig(f'{img_path}/{name}.jpg')
