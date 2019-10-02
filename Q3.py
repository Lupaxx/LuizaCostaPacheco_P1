#Questão 3

def Q3( ):
                anterior = 10
                n = 1
                i = 3
                sinal = 1
                while(abs(n*sinal - anterior) > (5*(10**(-8)))):
                        sinal = sinal*(-1)
                        anterior = n
                        n += (1/i)*sinal
                        i += 2
                print(4*n)

Q3()

