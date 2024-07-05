import tkinter as tk
from tkinter import messagebox

# Acervo é referente a coleção ou estoque de livros
class ColLivros:
    def __init__(self):
        self.acervo = {}

    def add_livro(self, tit, aut, ano, disp=True):
        # Adicionar um livro a coleção da biblioteca
        if tit in self.acervo:
            return False
        else:
            self.acervo[tit] = {
                'autor': aut,
                'ano': ano,
                'disponivel': disp
            }
            return True

    def atualiz_livro(self, tit, novo_aut=None, novo_ano=None, novo_disp=None):
        # Atualizar dados dos livros existentes na coleção da biblioteca
        if tit in self.acervo:
            if novo_aut:
                self.acervo[tit]['autor'] = novo_aut
            if novo_ano:
                self.acervo[tit]['ano'] = novo_ano
            if novo_disp is not None:
                self.acervo[tit]['disponivel'] = novo_disp
            return True
        else:
            return False

    def rem_livro(self, tit):
        # Remoção do livro da coleção da biblioteca
        if tit in self.acervo:
            del self.acervo[tit]
            return True
        else:
            return False

    def ver_disp(self, tit):
        # Verifica se um livro está disponível na coleção da biblioteca
        if tit in self.acervo:
            return self.acervo[tit]['disponivel']
        else:
            return None

# Interface gráfica da aplicação
class InterfaceBib:
    def __init__(self, janela):
        self.col = ColLivros()
        self.janela = janela
        self.janela.title("Biblioteca de Livros")

        # Frame principal (Campo branco no fundo)
        self.frm_princ = tk.Frame(janela)
        self.frm_princ.pack(padx=10, pady=10)

        # Campo de entrada do título do livro
        self.lbl_tit = tk.Label(self.frm_princ, text="Título:")
        self.lbl_tit.grid(row=0, column=0)
        self.ent_tit = tk.Entry(self.frm_princ)
        self.ent_tit.grid(row=0, column=1)

        # Campo de entrada do autor do livro
        self.lbl_aut = tk.Label(self.frm_princ, text="Autor:")
        self.lbl_aut.grid(row=1, column=0)
        self.ent_aut = tk.Entry(self.frm_princ)
        self.ent_aut.grid(row=1, column=1)

        # Campo de entrada do ano de publicação
        self.lbl_ano = tk.Label(self.frm_princ, text="Ano de Publicação:")
        self.lbl_ano.grid(row=2, column=0)
        self.ent_ano = tk.Entry(self.frm_princ)
        self.ent_ano.grid(row=2, column=1)

        # Checkbox para disponibilidade do livro
        self.lbl_disp = tk.Label(self.frm_princ, text="Disponível:")
        self.lbl_disp.grid(row=3, column=0)
        self.var_disp = tk.BooleanVar(value=True)
        self.chk_disp = tk.Checkbutton(self.frm_princ, variable=self.var_disp)
        self.chk_disp.grid(row=3, column=1)

        # Botão para adicionar um livro
        self.btn_add = tk.Button(self.frm_princ, text="Adicionar Livro", command=self.add_livro)
        self.btn_add.grid(row=4, column=0, columnspan=2)

        # Botão para atualizar as informações de um livro
        self.btn_atualiz = tk.Button(self.frm_princ, text="Atualizar Livro", command=self.atualiz_livro)
        self.btn_atualiz.grid(row=5, column=0, columnspan=2)

        # Botão para remover um livro
        self.btn_rem = tk.Button(self.frm_princ, text="Remover Livro", command=self.rem_livro)
        self.btn_rem.grid(row=6, column=0, columnspan=2)

        # Botão para consultar a disponibilidade de um livro
        self.btn_ver = tk.Button(self.frm_princ, text="Consultar Disponibilidade", command=self.ver_disp)
        self.btn_ver.grid(row=7, column=0, columnspan=2)
        
        # Adicionar o livro na coleção
    def add_livro(self):
        tit = self.ent_tit.get()
        aut = self.ent_aut.get()
        ano = self.ent_ano.get()
        disp = self.var_disp.get()

        if self.col.add_livro(tit, aut, ano, disp):
            messagebox.showinfo("Sucesso", f"Livro '{tit}' adicionado com sucesso.")
        else:
            messagebox.showerror("Erro", f"O livro '{tit}' já existe na biblioteca.")

        #Atualizar o livro na coleção 
    def atualiz_livro(self):
        tit = self.ent_tit.get()
        aut = self.ent_aut.get()
        ano = self.ent_ano.get()
        disp = self.var_disp.get()

        if self.col.atualiz_livro(tit, aut, ano, disp):
            messagebox.showinfo("Sucesso", f"Informações do livro '{tit}' atualizadas com sucesso.")
        else:
            messagebox.showerror("Erro", f"O livro '{tit}' não existe na biblioteca.")

        #Remover o livro da coleção 
    def rem_livro(self):
        tit = self.ent_tit.get()

        if self.col.rem_livro(tit):
            messagebox.showinfo("Sucesso", f"Livro '{tit}' removido com sucesso.")
        else:
            messagebox.showerror("Erro", f"O livro '{tit}' não existe na biblioteca.")

        # Verificar no disponibildade do livro
    def ver_disp(self):
        tit = self.ent_tit.get()

        disp = self.col.ver_disp(tit)
        if disp is None:
            messagebox.showerror("Erro", f"O livro '{tit}' não existe na biblioteca.")
        else:
            status = 'disponível' if disp else 'indisponível'
            messagebox.showinfo("Disponibilidade", f"O livro '{tit}' está {status}.")

# Inicia a aplicação
if __name__ == "__main__":
    janela = tk.Tk()
    app = InterfaceBib(janela)
    janela.mainloop()

