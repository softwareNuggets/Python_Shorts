men_100_meter = [9.79, 10.01, 9.70,
                 9.63, 9.81,  9.83,
                 9.98, 10.03, 9.69,
                 9.75, 9.76, 9.76]

gold        = 100
silver      = 100
bronze      = 100

for num in men_100_meter:
    if num < gold:
        bronze = silver
        silver = gold
        gold = num
    elif num < silver and num > gold:
        bronze = silver
        silver = num
    elif num < bronze and num > silver:
        bronze = num

print(gold)
print(silver)
print(bronze)
