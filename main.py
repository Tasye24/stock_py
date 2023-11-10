import math
from random import random

"""
definitions
    stocks[]
        the list of stocks
            "name" -- name
            "value" -- for this example is not calculated (random)
            "amount" -- same thing random
            "capital" -- value * amount
            "percentage_over_all" -- capital / sum of stocks[] capitals
    stockIndex
        sum of "captial" * "percentage_over_all"  
"""

stocks = [
    {
        "name": "MyEnterprise",
        "value": random()*10,
        "amount": 5e4
    },
    {
        "name": "AnotherOneEntreprise",
        "value": random()*10,
        "amount": 3e3
    }
]
l=0
while l < len(stocks):
    curr = stocks[l]
    capital = curr["value"] * curr["amount"]
    curr["capital"] = capital
    l = l + 1

print(stocks)

def SumAmount(table):
    sum = 0
    i = 0
    while(i<len(table)):
        curr = table[i]
        sum += curr["capital"]
        i = i+1
    return sum


def stockCalc(table):
    stockIndex = 0
    SumCapitals = SumAmount(table)
    for i in range(0, len(table)):
        curr = table[i]
        curr["percentage_over_all"] = 100*curr["capital"]/SumCapitals
        stockIndex += curr["percentage_over_all"]*curr["capital"]
    return stockIndex

print(stocks)
print(f"Value of your index: {stockCalc(stocks)}")
