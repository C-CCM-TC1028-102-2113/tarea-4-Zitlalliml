
def main():
    #escribe tu código abajo de esta línea
    num = int (input('Enter a number:'))
    a= 0
    b= 1
    for i in range (1,num):
        c = a + b
        a = b
        b = c

    
print (b, end=" ")
    pass

if __name__=='__main__':
    main()
