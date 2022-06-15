import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

from datetime import datetime

# Load the words.
with open('all_comments.txt', encoding='UTF-8') as f:
    text = f.read()
    

# Load an image as a NumPy array.
mask = np.array(Image.open('Montu.png'))

# Get stop words as a set and add extra words.
stopwords = STOPWORDS
stopwords.update(['PM', "say"])

wc = WordCloud(
    max_words=500,
    relative_scaling=0.5,
    mask=mask,
    background_color='black',
    stopwords=stopwords,
    margin=3,
    random_state=7,
    contour_width=2,
    contour_color='white',
    colormap='Greens_r'   
    ).generate(text)

colors = wc.to_array()

comments_date = f'{datetime.now():%m.%d.%Y}'
print(comments_date)

plt.figure(figsize=(5,5))
plt.title("Comments on 'What is the Future of Stellaris?'")
plt.suptitle(f"Video by Montu Plays\nComments as of {comments_date}", x=0.52, y=0.095)
plt.imshow(colors, interpolation="bilinear")
plt.axis('off')

plt.savefig('COMMENTS_Future_of_Stellaris.png', dpi=300)

plt.show()

