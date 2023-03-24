class Libro:
    def __init__(self, titulo, autor, editorial, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editor = editorial
        self.paginas = paginas
    
    def describir_libro(self):
        print("Título:",self.titulo)
        print("Autor:", self.autor)
        print("editorial:", self.editorial)
        print("Páginas:", self.paginas)
        