import unicodedata

class NodoIngrediente:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.siguiente = None

class PostreItem:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cabeza_ingredientes = None

class EstructuraPostres:
    def __init__(self):
        self.postres = []
        self.precargar_datos()

    def _normalizar(self, texto):
        if not texto:
            return ""
        nfkd_form = unicodedata.normalize('NFKD', texto)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower().strip()

    def _buscar_indice(self, nombre):
        inicio = 0
        fin = len(self.postres) - 1
        nombre_buscado = self._normalizar(nombre)
        while inicio <= fin:
            medio = (inicio + fin) // 2
            nombre_actual = self._normalizar(self.postres[medio].nombre)
            if nombre_actual == nombre_buscado:
                return medio
            elif nombre_actual < nombre_buscado:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1

    def imprimir_ingredientes(self, nombre):
        idx = self._buscar_indice(nombre)
        if idx == -1:
            print(f"\nEl postre '{nombre}' no se encuentra registrado en el sistema.")
            return
        
        actual = self.postres[idx].cabeza_ingredientes
        print(f"\nIngredientes del postre '{self.postres[idx].nombre}':")
        if not actual:
            print("   (No tiene ingredientes registrados)")
            return
        
        while actual:
            print(f"   - {actual.ingrediente}")
            actual = actual.siguiente

    def insertar_ingrediente(self, nombre, ingrediente):
        idx = self._buscar_indice(nombre)
        if idx == -1:
            print(f"\nError: El postre '{nombre}' no existe. No se puede insertar el ingrediente.")
            return

        actual = self.postres[idx].cabeza_ingredientes
        ingrediente_buscado = self._normalizar(ingrediente)
        while actual:
            if self._normalizar(actual.ingrediente) == ingrediente_buscado:
                print(f"\nEl ingrediente '{ingrediente}' ya se encuentra registrado en este postre.")
                return
            actual = actual.siguiente

        nuevo_nodo = NodoIngrediente(ingrediente)
        if not self.postres[idx].cabeza_ingredientes:
            self.postres[idx].cabeza_ingredientes = nuevo_nodo
        else:
            actual = self.postres[idx].cabeza_ingredientes
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"\nIngrediente '{ingrediente}' agregado exitosamente al postre '{nombre}'.")

    def eliminar_ingrediente(self, nombre, ingrediente):
        idx = self._buscar_indice(nombre)
        if idx == -1:
            print(f"\nError: El postre '{nombre}' no existe en el sistema.")
            return

        actual = self.postres[idx].cabeza_ingredientes
        anterior = None
        ingrediente_buscado = self._normalizar(ingrediente)

        while actual:
            if self._normalizar(actual.ingrediente) == ingrediente_buscado:
                if anterior is None:
                    self.postres[idx].cabeza_ingredientes = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"\nIngrediente '{ingrediente}' eliminado del postre '{nombre}'.")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"\nEl ingrediente '{ingrediente}' no se encuentra en la lista del postre '{nombre}'.")

    def dar_de_alta_postre(self, nombre, lista_ingredientes, silencioso=False):
        # Modificado para permitir postres repetidos
        nuevo_postre = PostreItem(nombre)
        cabeza = None
        cola = None
        
        for ing in lista_ingredientes:
            nuevo_nodo = NodoIngrediente(ing.strip())
            if not cabeza:
                cabeza = nuevo_nodo
                cola = nuevo_nodo
            else:
                cola.siguiente = nuevo_nodo
                cola = nuevo_nodo
        nuevo_postre.cabeza_ingredientes = cabeza

        pos = 0
        nombre_norm = self._normalizar(nombre)
        while pos < len(self.postres) and self._normalizar(self.postres[pos].nombre) < nombre_norm:
            pos += 1
        
        self.postres.insert(pos, nuevo_postre)
        if not silencioso:
            print(f"\nPostre '{nombre}' dado de alta exitosamente.")

    def dar_de_baja_postre(self, nombre):
        idx = self._buscar_indice(nombre)
        if idx == -1:
            print(f"\nError: El postre '{nombre}' no existe, por lo que no se puede dar de baja.")
            return
        
        self.postres.pop(idx)
        print(f"\nPostre '{nombre}' y su lista de ingredientes han sido dados de baja exitosamente.")

    def eliminar_repetidos(self):
        """Subprograma para eliminar de manera automatica los postres repetidos."""
        if len(self.postres) <= 1:
            print("\nEl catalogo tiene 0 o 1 elemento, no hay repetidos posibles.")
            return

        i = 0
        eliminados = 0
        while i < len(self.postres) - 1:
            actual_norm = self._normalizar(self.postres[i].nombre)
            siguiente_norm = self._normalizar(self.postres[i + 1].nombre)
            
            if actual_norm == siguiente_norm:
                # Al eliminar el nodo del arreglo, se pierde la referencia a su lista enlazada de ingredientes asociada
                self.postres.pop(i + 1)
                eliminados += 1
            else:
                i += 1
                
        print(f"\nProceso finalizado. Se eliminaron {eliminados} postres repetidos.")

    def mostrar_catalogo(self):
        if not self.postres:
            print("\nNo hay postres registrados en el sistema.")
            return
        print("\n--- CATALOGO DE POSTRES (Orden alfabetico) ---")
        for i, p in enumerate(self.postres, 1):
            print(f"{i}. {p.nombre}")

    def precargar_datos(self):
        ejemplos = {
            "Flan": ["Leche condensada", "Leche evaporada", "Huevos", "Azucar", "Vainilla"],
            "Brownie": ["Chocolate amargo", "Mantequilla", "Azucar", "Huevos", "Harina de trigo", "Nueces picadas"],
            "Arroz con leche": ["Arroz", "Leche entera", "Canela en rama", "Azucar", "Cascara de limon"],
            "Pay de limon": ["Galletas Maria", "Mantequilla derretida", "Leche condensada", "Jugo de limon"]
        }
        for nombre, ingredientes in ejemplos.items():
            self.dar_de_alta_postre(nombre, ingredientes, silencioso=True)



# Menu por Consola

def menu():
    sistema = EstructuraPostres()
    print("Se han cargado algunos postres de ejemplo automaticamente.")
    
    while True:
        print("\n===============================")
        print("   SISTEMA DE GESTION DE POSTRES")
        print("===============================")
        print("1. Dar de alta un postre")
        print("2. Dar de baja un postre")
        print("3. Agregar ingrediente a un postre")
        print("4. Eliminar ingrediente de un postre")
        print("5. Consultar ingredientes por nombre de postre")
        print("6. Ver catalogo completo de postres")
        print("7. Eliminar postres repetidos automaticamente")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opcion (1-8): ").strip()
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del nuevo postre: ").strip()
            if not nombre:
                print("El nombre no puede estar vacio.")
                continue
            
            print("Ingrese los ingredientes uno por uno (presione [Enter] sin escribir nada para terminar):")
            ingredientes = []
            while True:
                ing = input(" > Ingrediente: ").strip()
                if ing == "":
                    break
                ingredientes.append(ing)
            
            sistema.dar_de_alta_postre(nombre, ingredientes)
            
        elif opcion == "2":
            nombre = input("Ingrese el nombre del postre que desea dar de baja: ").strip()
            sistema.dar_de_baja_postre(nombre)
            
        elif opcion == "3":
            nombre = input("Ingrese el nombre del postre al que desea agregar un ingrediente: ").strip()
            ing = input("Ingrese el nombre del nuevo ingrediente: ").strip()
            if ing:
                sistema.insertar_ingrediente(nombre, ing)
            else:
                print("El ingrediente no puede estar vacio.")
                
        elif opcion == "4":
            nombre = input("Ingrese el nombre del postre: ").strip()
            ing = input("Ingrese el nombre del ingrediente que desea eliminar: ").strip()
            if ing:
                sistema.eliminar_ingrediente(nombre, ing)
            else:
                print("El ingrediente no puede estar vacio.")
                
        elif opcion == "5":
            nombre = input("Ingrese el nombre del postre para ver sus ingredientes: ").strip()
            sistema.imprimir_ingredientes(nombre)
            
        elif opcion == "6":
            sistema.mostrar_catalogo()

        elif opcion == "7":
            sistema.eliminar_repetidos()
            
        elif opcion == "8":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpcion no valida. Por favor, ingrese un numero entre 1 y 8.")

if __name__ == "__main__":
    menu()
