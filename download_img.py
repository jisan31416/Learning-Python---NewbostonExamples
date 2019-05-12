import random
import urllib.request

def download_url_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + '.jpg'

    urllib.request.urlretrieve(url, full_name)

download_url_image("https://scontent.fdac18-1.fna.fbcdn.net/v/t1.0-9/50487688_2166421803575567_1041637171095666688_n.jpg?_nc_cat=108&_nc_ht=scontent.fdac18-1.fna&oh=e1d731e6f897efe98a7bac065317f37a&oe=5D04F9B2")