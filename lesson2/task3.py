try:
    first_word = str(input("inputh the 1st word: "))
    second_word = str(input("inputh the 2nd word: "))
except Exception:
    print("Something wrong")
else:
    print(first_word + "," + second_word)    