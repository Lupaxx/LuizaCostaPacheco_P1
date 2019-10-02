#Questão 3

def Q3( ):
                anterior = 1
                n = 1
                i = 3
                sinal = 1


                while((1/anterior) - (1/i) <= 5*(10**(-8))):
                        sinal = sinal*(-1)
                        if(sinal == 1):
                                n += 1/i
                        else:
                                n -= 1/i
                        anterior = i
                        i += 2
                print(4*n)
Q3()

