from urllib import request

goog_url = "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2017-financial-year-provisional/Download-data/annual-enterprise-survey-2017-financial-year-provisional-csv.csv"

def download_stock_data(csv_url) :
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'goog.csv'
    fx = open('dest_url','w')
    for line in lines :
        fx.write(line + '\n')
    fx.close()

download_stock_data(goog_url)