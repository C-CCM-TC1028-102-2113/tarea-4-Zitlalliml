
def main():
    #Escribe tu código debajo de esta línea
    height = int(input("Enter triangle height: "))

    for i in range(height):
        for j in range(i + 1):
            print("* ", end="")
        print()
    pass


if __name__=='__main__':
    main()
