#Comparativas  ==, !=, >, >=, <, <=

mi_bool = 10 == 25
mi_bool2 = "blanco" == "Blanco"
mi_bool3 = "blanco" == "Blanco".lower()

mi_bool4 = 10 != 25
mi_bool6 = "blanco" != "Blanco"
mi_bool5 = "blanco" != "Blanco".lower()

#test
num1 = 36
num2 = 17
mi_bool = num1 >= num2

# Lógicas AND, OR Y NOT
my_bool = 4 < 5 < 6
my_bool2 = 4 < 5 and 5 > 6
my_bool3 = (4 < 5) and 5 == 2 + 6

print(my_bool)
print(my_bool2)
print(my_bool3)

my_bool4 = 1 == 10 or 3 == 3

texto = "esta frase es breve"
my_bool5 = "esta frase" in texto and "breve" in texto
my_bool6 = "esta frase" in texto or "birra" in texto

print(my_bool4)
print(my_bool5)
print(my_bool6)

my_bool7 = not('a' == 'a')
my_bool8 = not('a' != 'a')

print(my_bool7)
print(my_bool8)