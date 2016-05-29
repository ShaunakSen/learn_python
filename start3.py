# lets try to download an image from the web!

import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    # download image
    urllib.request.urlretrieve(url, full_name)

download_web_image('http://www.nitdgp.ac.in/strokes/img/thumb22.jpg')