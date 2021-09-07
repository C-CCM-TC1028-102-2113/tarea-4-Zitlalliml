def main():
    #escribe tu código abajo de esta línea
    avg =0
    t=0
    i=0
    n=1
    while  n > 0 :
        n = float(input())
        if n < 0:
            t = (avg / i)
            print (t)

        avg = avg + n
        i = i+1
    pass
if __name__=='__main__':
    main()
