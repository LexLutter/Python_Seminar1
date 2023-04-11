number = 123321
part1 = int(number / 100000) + int((number / 10000) % 10)  + int((number % 10000) / 1000)
part2 = int((number % 1000) / 100) + int((number % 100) / 10) + int(number % 10)
print(f"Билет {number}")
if(part1 == part2): print("счастливый")
else: print("несчастливый")

