from requests import get
from datetime import datetime as dt
import os
import sys

def download_data(url, filename):
    with open(filename, "wb") as f:
        response = get(url)
        f.write(response.content)


def get_bom_data():
    now = dt.strftime(dt.now(), '%Y%m%d')
    m = dt.now().month
    m = '%02d' % m

    urlname_cbr = "http://www.bom.gov.au/fwo/IDN60903/IDN60903.94926.axf"
    download_data(urlname_cbr,path + 'CBR_' + now + '.axf')

    #urlname_cbr_sum = 'http://www.bom.gov.au/climate/dwo/201406/text/IDCJDW2801.201406.csv'
    #download_data(urlname_cbr_sum,path + 'CBR_' + m + '.csv')

    urlname_bne = "http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.axf"
    download_data(urlname_bne, path + 'BNE_' + now + '.axf')


if __name__ == "__main__":

    if len(sys.argv) == 2:
        path = os.path(str(sys.argv[1]), "bom_data/")
    else:
        path = os.path.join("", "bom_data/")
    
    get_bom_data()
