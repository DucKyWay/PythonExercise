money_1 = int(input())
money_2 = int(input())

money_1_check = money_1 % 100
money_2_check = money_2 % 100

money_sum = 0

if money_1 <= 20000:
    if money_2 <= 20000:
        money_sum = money_1 + money_2
        if money_sum % 100 == 0:
            if money_sum >= 100:
                moneyCash = money_sum / 1000
                moneyOver = moneyCash-20
                if moneyOver > 0:
                    moneyCash -= moneyOver
                print(int(moneyCash))
                money_sum %= 1000
                if moneyOver > 0:
                    money_sum = money_sum + (moneyOver * 1000)

                moneyCash = money_sum / 500
                moneyOver = moneyCash - 20
                if moneyOver > 0:
                    moneyCash -= moneyOver
                print(int(moneyCash))
                money_sum %= 500
                if moneyOver > 0:
                    money_sum = money_sum + (moneyOver * 500)

                moneyCash = money_sum / 100
                moneyOver = moneyCash - 20
                if moneyOver > 0:
                    moneyCash -= moneyOver
                print(int(moneyCash))
                money_sum %= 100
                if moneyOver > 0:
                    money_sum = money_sum + (moneyOver * 100)
        else:
            print("Input Error")
    else:
        print("Input Error")
else:
    print("Input Error")