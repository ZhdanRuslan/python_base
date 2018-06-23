
#Converter from dec to bin
n = int(input('Input decimal number: '))

#common logic of convertation
def to_binary_converter(n):
    k = []
    while (n > 0):
        a=int(float(n % 2))
        k.append(a)
        n=(n-a)/2
    string=""
    for j in k[::-1]:
        string=string+str(j)
    print('The binary num is %s'%(string))

to_binary_converter(n)