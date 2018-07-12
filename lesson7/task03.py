# self print
with open(__file__, 'r', encoding="utf-8-sig") as file:
    for number, line in enumerate(file):
        print("{0}\t{1}".format(number+1, line), end="")
print()