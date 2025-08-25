class Persona:
    def __init__(self, nombre:str, documento:str):
        self.nombre = nombre
        self.documento = documento

    def __str__(self) -> str:
        return f"{self.nombre}, se creó esta persona con el documento {self.documento}"
    
class CuentaBancaria:
    def __init__(self, titular:Persona, saldo: int = 0):
        self.titular = titular
        self._saldo = saldo
    def saldo(self) -> int:
        return self.saldo        
    def depositar(self, monto: float) -> None:
        if monto > 0:
            self._saldo += monto
            print(f"Se incrementó un monto de {monto}, el saldo actual es de {self._saldo}")
        else:
            print("El monto debe ser mayor a cero")
    def retirar(self, monto:float) -> None:
        if monto <= self._saldo:
            self._saldo -= monto
            print (f"Se acaba de retirar el monto de {monto}. El nuevo saldo es de {self._saldo}")
        else:
            print(f"No se puede retirar un onto mayor al saldo de la cuenta")
    def __str__(self) -> str:
        return f"{self.titular}, se creó esta persona con el documento {self.documento}"

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo = 0, interes: float = 0.02):
        super().__init__(titular, saldo)
        self.interes = interes

    def calcular_interes(self):
        ganancia = self._saldo * self.interes
        self._saldo += ganancia
        print(f"La ganancia es de {ganancia}. Su nuevo saldo es de {self._saldo}")

    def __str__(self)-> str:
        return f"Cuenta de Ahorros - Titular: {self.titular}"

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo = 0, limite_de_sobregiro: float = 500):
        super().__init__(titular, saldo)
        self.limite_de_sobregiro = limite_de_sobregiro

    def __str__(self)-> str:
        return f"Cuenta Corriente - Titular: {self.titular}"

    def retirar(self, monto: float):
        if monto <= self._saldo + self.limite_de_sobregiro:
            self._saldo -= monto
            print (f"Se retira del saldo {self._saldo} el monto de {monto}")
        else:
            print (f"No se puede retirar un monto mayor al saldo de la cuenta")

class Banco:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cuentas = []
    
    def crear_cuenta(self, titular: Persona, tipo="ahorros") -> object:
        if tipo == "ahorros":
            cuenta = CuentaAhorro(titular)
        else:
            cuenta = CuentaCorriente(titular)
        self.cuentas.append(cuenta)
        print(f"Cuenta bancaria creada con el titular {titular}")
        return cuenta
    
    def mostrar_cuentas(self):
        if not self.cuentas:
            print(f"Sin cuentas registradas")
        else:
            for cuenta in self.cuentas:
                print (f"{cuenta}")

banco =Banco(nombre="Banco ITM") 

while True:
    print("\n--- MENU ---")
    print("1. Crear persona y cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Aplicar interes a una cuenta de ahorros")
    print("5. Mostrar cuentas")
    print("6. Salir")

    opcion = int(input("Elige una opcion: "))

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre de la persona: ")
            documento = input("Ingrese el documento de la persona: ")

            persona = Persona(nombre=nombre,documento=documento)

            print(f"\nQue tipo de cuenta quiere crear")
            tipo = input("Escriba ahorros o corriente: ").lower()
            
            cuenta = banco.crear_cuenta(titular=persona, tipo=tipo)
        case 2:
            if not banco.cuentas:
                print("No hay cuentas creadas aún.")
            else:
                print("\n--- Seleccione la cuenta para depositar ---")
                for i, cuenta in enumerate(banco.cuentas):
                    print(f"{i+1}. {cuenta}")
                seleccion = int(input("Ingrese el número de la cuenta: ")) - 1

                if 0 <= seleccion < len(banco.cuentas):
                    monto = float(input("Ingrese el monto a depositar: "))
                    banco.cuentas[seleccion].depositar(monto)
                else:
                    print("Selección inválida.")
        case 3:
            if not banco.cuentas:
                print("No hay cuentas creadas aún.")
            else:
                print("\n--- Seleccione la cuenta para depositar ---")
                for i, cuenta in enumerate(banco.cuentas):
                    print(f"{i+1}. {cuenta}")
                seleccion = int(input("Ingrese el número de la cuenta: ")) - 1

                if 0 <= seleccion < len(banco.cuentas):
                    monto = float(input("Ingrese el monto a retirar: "))
                    banco.cuentas[seleccion].retirar(monto)
                else:
                    print("Selección inválida.")
        case 4:
            if not banco.cuentas:
                print("No hay cuentas creadas aún")
            else:
                print("\n--- Seleccione la cuenta para depositar ---")
                for i, cuenta in enumerate(banco.cuentas):
                    print(f"{i+1}.{cuenta}")
                seleccion = int(input("Ingrese el numero de la cuenta: "))-1

                if 0 <= seleccion < len(banco.cuentas):
                    if isinstance(banco.cuentas[seleccion], CuentaAhorro):
                        banco.cuentas[seleccion].calcular_interes()
                    elif isinstance(banco.cuentas[seleccion], CuentaCorriente):
                        print("No se puede calcular intereses en una cuenta corriente")                            
        case 5:
            banco.mostrar_cuentas()
        case 6:
            print("Gracias por usar nuestro sistema")
            break
        case _:
            print("Opcion no valida")