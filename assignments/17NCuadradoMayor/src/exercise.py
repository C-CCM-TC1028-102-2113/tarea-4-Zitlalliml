

def main():
    #Escribe tu código debajo de esta línea
    num = int(input("Escribe un numero : "))
    for j in range(num):
        p = j **2
        if p > num:
            print (j)
            break
    pass

if __name__=='__main__':
    main()
