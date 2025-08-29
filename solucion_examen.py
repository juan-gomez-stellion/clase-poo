class Libro:
    def __init__(self, autor, titulo, fecha, genero):
        self.autor = autor
        self.titulo = titulo
        self.fecha = fecha
        self.genero = genero


lista_libros = []
while True:
    print("Seleccione la opciòn deseada")
    print("1. Registrar libros")

    opcion = int(input())
    if opcion == 1:
        autor = input("Ingresar autor")
        titulo = input("Ingresar título")
        fecha = input("Ingresar fecha")
        genero = input("Ingresar genero")
        libro_nuevo = Libro(autor, titulo, fecha, genero)
        lista_libros.append(libro_nuevo)
        print("Libro agregado exitosamente")
    if opcion == 2:
        # for libro in lista_libros:
        #     print(libro.autor)
        #     print(libro.titulo)
        print(lista_libros)
    elif opcion == 0:
        break
