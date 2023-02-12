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
                print("money over: ", moneyOver)
                if moneyOver > 0:
                    moneyCash -= moneyOver
                    money_sum += (moneyOver * 1000)
                    print("sum : ", money_sum)
                    print("money over", moneyOver)
                print(int(moneyCash))
                print("test : ", money_sum)
                money_sum //= 1000

                print("test ", money_sum)

                moneyCash = money_sum / 500
                moneyOver = moneyCash - 20
                if moneyOver > 0:
                    moneyCash -= moneyOver
                    money_sum += (moneyOver * 500)
                print(int(moneyCash))
                money_sum //= 500

                moneyCash = money_sum / 100
                moneyOver = moneyCash - 20
                if moneyOver > 0:
                    moneyCash -= moneyOver
                    money_sum += (moneyOver * 100)
                print(int(moneyCash))
                money_sum //= 100
        else:
            print("Input Error")
    else:
        print("Input Error")
else:
    print("Input Error")