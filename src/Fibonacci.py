#Se define una funcion que es la abstraccion para la sequencia de fibonacci. Luego se llama la funcion y
#se le pasa el parametro n para mirar la secuencia con un n ingresado. binet's fibonacci formula
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
