class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f"El estado de tu cuenta actualmente es este:"
                f"\nNombre: {self.nombre}\nApellido: {self.apellido}"
                f"\nNúmero de Cuenta: {self.numero_cuenta}\nBalance: {self.balance}")

    def depositar(self):
        dinero_agregado = int(input("Dinero que desea ingresar: "))
        self.balance += dinero_agregado
        print(self)

    def retirar(self):
        dinero_retirado = int(input("Dinero que desea retirar: "))
        retirable = self.es_retirable(self.balance, dinero_retirado)
        if retirable:
            self.balance -= dinero_retirado
            print(self)
        else:
            print(f"No puedes retirar {dinero_retirado} euros. Tu saldo actual es de {self.balance} euros.")

    @staticmethod
    def es_retirable(balance, dinero):
        return balance > dinero


def crear_cliente():
    nombre = input(f"Cual es su nombre: ")
    apellido = input(f"Cual es su apellido: ")
    cuenta_bancaria = input(f"Cual es su cuenta bancaria: ")
    balance = int(input(f"Cual es su balance: "))
    return Cliente(nombre, apellido, cuenta_bancaria, balance)


def inicio():
    nuevo_cliente = crear_cliente()

    while True:
        decision = int(input("Que desea hacer ahora:\n1-Depositar\n2-Retirar\n3-Salir\n"))
        match decision:
            case 1:
                nuevo_cliente.depositar()
            case 2:
                nuevo_cliente.retirar()
            case 3:
                break

    print("Vuelva pronto!")


inicio()
