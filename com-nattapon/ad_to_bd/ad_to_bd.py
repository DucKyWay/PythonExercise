ad_year = int(input())
bd_year = ad_year + 543

str_ad = str(ad_year)
str_bd = str(bd_year)

each_ad_num = []
each_bd_num = []
ad_ans = 0
bd_ans = 0

for i in str_ad:
    each_ad_num.append(int(i))

for i in str_bd:
    each_bd_num.append(int(i))

for i in str_ad:
    for j in str(i):
        ad_ans += int(j)
    each_ad_num.append(ad_ans)
for i in str_bd:
    for j in str(i):
        bd_ans += int(j)
    each_bd_num.append(bd_ans)
    
print(bd_year)
print(ad_ans)
print(bd_ans)