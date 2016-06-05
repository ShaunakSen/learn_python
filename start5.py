from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=4&e=29&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'


def download_stock_data(csv_url):
    # connect
    response = request.urlopen(csv_url)

    # read data from the url
    csv = response.read()

    # now we have that data stored in var csv
    # i dont kno what kind of data that is

    csv_str = str(csv)

    # this data is now in a single long long string
    lines = csv_str.split(r"\n")
    dest_url = r'goog.csv'
    # r means raw it will accept paths like 'C:\shaunak\....'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)