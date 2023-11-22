# Importamos el modulo(suma_y_resta.py) que hay en un paquete (Paquetes)
from Paquetes import suma_y_resta

# Importamos otro paquete del directorio subpaquetes dentro de paquetes
# Accedemos mediante el '.'
from Paquetes.Subpaquetes import saludo

suma_y_resta.suma(15, 2)
suma_y_resta.resta(20,55)

saludo.hola()