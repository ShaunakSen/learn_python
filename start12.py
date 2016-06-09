stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'APPL': 99.76
}

stocks_list = zip(stocks.values(), stocks.keys())
minimumValue = min(stocks_list)
print(minimumValue)

print(sorted(zip(stocks.values(), stocks.keys())))
