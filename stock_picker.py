import datetime, sys
from math import sqrt
from util_functions import *
from stock_data import *


# main function
def main():
    # fetch filepath argument
    mindate, maxdate = extract(sys.argv[1])
    # main loop
    while True:
        # fetch the name of the stock to analyze
        stock_name = raw_input("Welcome Agent! Which stock do you need to process?: ")
        # check for incorrect stock names
        while stock_name not in stock_names:
            # Use edit distance algorithm to predict what the user wanted to type
            corrected_stock_name = find_correction(stock_name)
            ask = raw_input("Oops! Did you mean %s? (y/n): "%(corrected_stock_name))
            if ask.lower() == 'y':
                stock_name = corrected_stock_name
                break
            stock_name = raw_input("Please enter the stock name again!: ")

        date1 = None
        date2 = None
        #Fetch date ranges
        while not date1:
            try:
                date1 = raw_input("From which date do you want to start? (dd-month-yyyy): ")
                date1 = datetime.datetime.strptime(date1, frmt)
            except:
                print "Invalid Format, Try again!"
                date1 = None
        while not date2:
            try:
                date2 = raw_input("Till which date do you want to analyze? (dd-month-yyyy): ")
                date2 = datetime.datetime.strptime(date2, frmt)
            except:
                print "Invalid Format, Try again!"
                date2 = None

        if date1 > date2:
            print "\nThe dates have been swapped as the first one was greater than the second one\n"
            date1, date2 = date2, date1

        if date1 and date1 < mindate:
            date1 = mindate
        if date2 and date2 < mindate:
            date2 = mindate

        cur_date = date1

        vals = []
        dates = []

        # Fetch the stock prices in the given date range
        while cur_date in stocks and cur_date <= date2:
            if stock_name in stocks[cur_date]:
                dates.append(cur_date)
                vals.append(stocks[cur_date][stock_name])
            cur_date += plus_one

        #find mean, stdev and profit
        mean = None
        stdev = None
        d1 = d2 = None
        if vals:
            mean = find_mean(vals)
            stdev = find_stdev(mean, vals)
            d1, d2 = best_time_to_buy_and_sell(vals)

        date_buy = None
        date_sell = None
        profit = None
        if d1 != None and d2 != None:
            date_buy = datetime.datetime.strftime(dates[d1], frmt)
            date_sell = datetime.datetime.strftime(dates[d2], frmt)
            profit = vals[d2]*100-vals[d1]*100

        print "Here's the result: "
        print "-------------------------------------------------"
        print "Mean: ", mean
        print "Standard Deviation: ",  stdev
        print "Best date to buy: ", date_buy
        print "Best date to sell: ", date_sell
        print "Profit: ", profit
        print "-------------------------------------------------"

        ask = raw_input("Do you want to continue? (y/n): ").lower()
        while ask != 'y' and ask != 'n':
            print "INVALID INPUT!"
            ask = raw_input("Do you want to continue? (y/n): ")
        if ask == 'n':
            break

if __name__ == "__main__":
    main()
