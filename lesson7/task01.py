-------------------------------------#
inp_stream = open("lesson7/test.txt", mode="r", buffering=-1)

try:
    for line in inp_stream:
        print(line)
except EOFError:
    inp_stream.close()