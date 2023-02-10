n = int(input()) #Station
m = int(input()) #money
moneyCoin = 0
fare = [27, 35, 42]

def CountCoin(m):
    moneyCoin = m/10
    print(int(moneyCoin))
    m %= 10

    moneyCoin = m/5
    print(int(moneyCoin))
    m %= 5
        
    moneyCoin = m/2
    print(int(moneyCoin))
    m %= 2
        
    moneyCoin = m/1
    print(int(moneyCoin))
    m %= 1

if n == 1:
    change = m - fare[0]
    if change >= 0:
        CountCoin(change)
    elif change < 0:
        print("จำนวนเงินไม่เพียงพอ")

if n == 2:
    change = m - fare[1]
    if change >= 0:
        CountCoin(change)
    elif change < 0:
        print("จำนวนเงินไม่เพียงพอ")

if n == 3:
    change = m - fare[2]
    if change >= 0:
        CountCoin(change)
    elif change < 0:
        print("จำนวนเงินไม่เพียงพอ")

