#Questão 4

def nob(num_a, num_b):
	unid_a = num_a%10
	dec_a = (num_a - unid_a)/10
	soma_a = unid_a + dec_a
	unid_b = num_b%10
	dec_b = (num_b - unid_b)/10
	soma_b = unid_b + dec_b
	resposta = soma_a + soma_b
	return resposta

def Q4 ():
        print(nob(36, 21))

Q4()
