import datetime
import csv

frmt = '%d-%b-%Y'

mindate = None
maxdate = None
stock_names = {}
stocks = {}
plus_one = datetime.timedelta(days=1)

# Extract information from csv file and stor into a dict
def extract(filepath):
    global mindate, maxdate
    with open(filepath, 'rt') as f:
        d = csv.reader(f)
        for row in d:
            if row[0] == 'StockName':
                continue
            stock_names[row[0]] = True
            cur_date = datetime.datetime.strptime(row[1], frmt)
            if cur_date not in stocks:
                stocks[cur_date] = {}
                stocks[cur_date][row[0]] = float(row[2])
            if mindate == None:
                mindate = cur_date
                maxdate = cur_date
            else:
                if cur_date < mindate:
                    mindate = cur_date
                if cur_date > maxdate:
                    maxdate = cur_date

    # Add missing dates to dict to simplify search
    cur_date = mindate
    while cur_date < maxdate:
        if cur_date not in stocks:
            stocks[cur_date] = {}
        cur_date += plus_one