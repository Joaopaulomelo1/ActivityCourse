import random  
def lancar_dados():
   
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    
    total = dado1 + dado2
    
    return total

resultado = lancar_dados()
print(f"O resultado do lançamento dos dois dados foi: {resultado}")
