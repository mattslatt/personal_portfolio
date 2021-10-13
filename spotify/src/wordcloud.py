import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from wordcloud import WordCloud
from PIL import Image

img_path = '/home/matt/personal_projects/spotify/img/'

def masked_wordcloud(data, mask, name, min_font = 3, colormap_choice='tab20c'):
    '''
    input: artist_split dataframe, mask file path, image name, minimum font, color pallete
    returns: saved wordcloud image, prints used genre text
    '''
    artist_genres = data[data['genres'] != '[]'].copy()
    artist_genres['genres_clean'] = artist_genres['genres'].str.strip("[]")
    text = " ".join(genre for genre in artist_genres['genres_clean']).replace("'", "").replace('"', '').replace(',', '')

    note_mask = np.array(Image.open(mask))
    note_mask = note_mask[:,:,2]

    wc = WordCloud(mask=note_mask, min_font_size = min_font, colormap=colormap_choice)
    wc.generate(text)
    
    plt.figure(figsize=[15,7])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(f'{img_path}{name}.png')