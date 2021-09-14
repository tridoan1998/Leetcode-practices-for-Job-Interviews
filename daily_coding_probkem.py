def sell_stock(stocks):
    lowest, highest = stock[0], 0
    for i  in range(1, len(stocks)):
        lowest = min(lowest, stocks[i])
        if stocks[i] - lowest > highest:
            highest = stocks[i] - lowest
    return highest


