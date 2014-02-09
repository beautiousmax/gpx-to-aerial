import requests
import sys
from bs4 import BeautifulSoup


def aer(f):
    gps = {x.find('name').text: '{0},{1}'.format(x['lat'], x['lon']) for x in BeautifulSoup(open(f)).find_all('wpt')}
    for i in gps:
        url = "http://maps.googleapis.com/maps/api/staticmap?center={0}&zoom=18&size=800x500&sensor=false&maptype=" \
              "hybrid".format(gps[i])
        with open("AER_"+i+".jpg", 'wb') as pic:
            for data in requests.get(url).iter_content():
                pic.write(data)
                pic.flush()

if __name__ == "__main__":
    aer(sys.argv[1])