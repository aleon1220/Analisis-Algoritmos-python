# programa para calcular BMI IMC Indice masa corporal
temp = raw_input('''Ingrese su altura en sistema ingles separada por com ej (6'2'') ''')
weight = float(raw_input("Peso en libras: "))

pieces = temp.split("'")
feet   = int(pieces[0])
inches = float(pieces[1][:-1])

feet   = feet * 12
height = feet + inches
bmi = 703 * weight / pow(height, 2)

print 'Segun los calculos el indice es:', bmi, '.'
print 'Su IMC es %.4f.'%(bmi)

raw_input()