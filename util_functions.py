from math import sqrt
from stock_data import *

# Spell check for stock names
def editDistance(str1, str2): 
    m = len(str1)
    n = len(str2)
    dp = [[0 for y in range(n+1)] for x in range(m+1)] 
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0: 
                dp[i][j] = j    

            elif j == 0: 
                dp[i][j] = i

            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            else: 
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
  
    return dp[m][n]

def find_correction(string):
    mn = float('inf')
    corrected_str = None
    for key in stock_names.keys():
        cur = min(mn, editDistance(string, key))
        if cur < mn:
            mn = cur
            corrected_str = key
    return corrected_str

#FIND MEAN
def find_mean(vals):
    return sum(vals)/len(vals)

#FIND STDDEV
def find_stdev(mean, vals):
    var = 0
    n = len(vals)
    if n == 1:
        return 0
    for x in vals:
        var += (mean-x)**2
    stdev = sqrt(var/(n-1))
    return stdev

#FIND BEST TIME TO BUY AND SELL
def best_time_to_buy_and_sell(vals):
    if not vals:
        return (None, None)
    i = 0
    j = 1
    n = len(vals)
    ans_i = 0
    ans_j = 0
    for j in range(n):
        if vals[j] < vals[i]:
            i = j
        if vals[j]-vals[i] > vals[ans_j] - vals[ans_i]:
            ans_i = i
            ans_j = j
    return (ans_i, ans_j)