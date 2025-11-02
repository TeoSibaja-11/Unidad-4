class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Su nombre{self.nombre}, artista del género {self.genero} con popularidad {self.popularidad}/100, se presenta en este festival musical")

    def actuar(self):
        print(f"{self.nombre} actualemente presentandose en el escenario...")

    def despedirse(self):
        print(f"{self.nombre} agradece al público por su apoyo y se despide con una gran sonrisa\n")


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su éxito '{self.cancion_mas_popular}' con gran energía")


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público")


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra")

def iniciar_festival(lista_artistas):
    print("\n¡Comienza el Festival de Música!\n")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación \n")
    print("El festival ha terminado. ¡Gracias por asistir!")

def main():
    lista_artistas = []
    cantidad = int(input("¿Cuántos artistas se presentarán en el festival? "))

    for i in range(cantidad):
        print(f"\nArtista #{i + 1}")
        tipo = input("Tipo de artista (Cantante / DJ / Banda): ").strip().lower()
        nombre = input("Nombre: ")
        genero = input("Género musical: ")
        popularidad = int(input("Popularidad (1 a 100): "))

        if tipo == "cantante":
            cancion = input("Canción mas popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == "dj":
            estilo = input("Estilo del DJ: ")
            artista = DJ(nombre, genero, popularidad, estilo)
        elif tipo == "banda":
            integrantes = int(input("Numero de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)
        else:
            print("Tipo de artista no válido. Se omitirá.")
            continue

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()
