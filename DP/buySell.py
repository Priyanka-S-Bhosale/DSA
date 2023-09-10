#https://www.codingninjas.com/studio/problems/stocks-are-profitable_893405?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1

from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    profit = 0
    mini = prices[0]
    n = len(prices)

    for i in range(1,n):
        cost = prices[i] - mini
        profit = max(profit,cost)
        mini = min(mini, prices[i])
    return profit
