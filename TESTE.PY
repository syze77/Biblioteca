import tkinter as tk
from tkinter import messagebox

class Biblioteca:
    def __init__(self):
        self.livros = {}

    def adicionar_livro(self, titulo, autor, ano, disponivel=True):
        if titulo in self.livros:
            return False
        else:
            self.livros[titulo] = {
                'autor': autor,
                'ano': ano,
                'disponivel': disponivel
            }
            return True

    def atualizar_livro(self, titulo, autor=None, ano=None, disponivel=None):
        if titulo in self.livros:
            if autor:
                self.livros[titulo]['autor'] = autor
            if ano:
                self.livros[titulo]['ano'] = ano
            if disponivel is not None:
                self.livros[titulo]['disponivel'] = disponivel
            return True
        else:
            return False

    def remover_livro(self, titulo):
        if titulo in self.livros:
            del self.livros[titulo]
            return True
        else:
            return False

    def consultar_disponibilidade(self, titulo):
        if titulo in self.livros:
            return self.livros[titulo]['disponivel']
        else:
            return None

class BibliotecaApp:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.root = root
        self.root.title("Biblioteca de Livros")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.titulo_label = tk.Label(self.frame, text="Título:")
        self.titulo_label.grid(row=0, column=0)
        self.titulo_entry = tk.Entry(self.frame)
        self.titulo_entry.grid(row=0, column=1)

        self.autor_label = tk.Label(self.frame, text="Autor:")
        self.autor_label.grid(row=1, column=0)
        self.autor_entry = tk.Entry(self.frame)
        self.autor_entry.grid(row=1, column=1)

        self.ano_label = tk.Label(self.frame, text="Ano de Publicação:")
        self.ano_label.grid(row=2, column=0)
        self.ano_entry = tk.Entry(self.frame)
        self.ano_entry.grid(row=2, column=1)

        self.disponivel_label = tk.Label(self.frame, text="Disponível:")
        self.disponivel_label.grid(row=3, column=0)
        self.disponivel_var = tk.BooleanVar(value=True)
        self.disponivel_check = tk.Checkbutton(self.frame, variable=self.disponivel_var)
        self.disponivel_check.grid(row=3, column=1)

        self.adicionar_button = tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro)
        self.adicionar_button.grid(row=4, column=0, columnspan=2)

        self.atualizar_button = tk.Button(self.frame, text="Atualizar Livro", command=self.atualizar_livro)
        self.atualizar_button.grid(row=5, column=0, columnspan=2)

        self.remover_button = tk.Button(self.frame, text="Remover Livro", command=self.remover_livro)
        self.remover_button.grid(row=6, column=0, columnspan=2)

        self.consultar_button = tk.Button(self.frame, text="Consultar Disponibilidade", command=self.consultar_disponibilidade)
        self.consultar_button.grid(row=7, column=0, columnspan=2)

    def adicionar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        ano = self.ano_entry.get()
        disponivel = self.disponivel_var.get()

        if self.biblioteca.adicionar_livro(titulo, autor, ano, disponivel):
            messagebox.showinfo("Sucesso", f"Livro '{titulo}' adicionado com sucesso.")
        else:
            messagebox.showerror("Erro", f"O livro '{titulo}' já existe na biblioteca.")

    def atualizar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        ano = self.ano_entry.get()
        disponivel = self.disponivel_var.get()

        if self.biblioteca.atualizar_livro(titulo, autor, ano, disponivel):
            messagebox.showinfo("Sucesso", f"Informações do livro '{titulo}' atualizadas com sucesso.")
        else:
            messagebox.showerror("Erro", f"O livro '{titulo}' não existe na biblioteca.")

    def remover_livro(self):
        titulo = self.titulo_entry.get()

        if self.biblioteca.remover_livro(titulo):
            messagebox.showinfo("Sucesso", f"Livro '{titulo}' removido com sucesso.")
        else:
            messagebox.showerror("Erro", f"O livro '{titulo}' não existe na biblioteca.")

    def consultar_disponibilidade(self):
        titulo = self.titulo_entry.get()

        disponivel = self.biblioteca.consultar_disponibilidade(titulo)
        if disponivel is None:
            messagebox.showerror("Erro", f"O livro '{titulo}' não existe na biblioteca.")
        else:
            status = 'disponível' if disponivel else 'indisponível'
            messagebox.showinfo("Disponibilidade", f"O livro '{titulo}' está {status}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
