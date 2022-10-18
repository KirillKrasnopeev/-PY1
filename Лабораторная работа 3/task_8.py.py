money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
balance = money_capital
delta = 0
while balance + delta > 0:
    delta = salary - spend
    balance = balance + delta
    spend *= 1.05
    month += 1
print(month)
