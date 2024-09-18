import cmath
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

class Calculadora:
    def __init__(self):
        pass

    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

    def potencia(self, a, b):
        return a ** b

    def raiz_quadrada(self, a):
        return cmath.sqrt(a)

class CalculadoraComplexa:
    def __init__(self):
        pass

    def adicionar(self, a, b):
        return complex(a) + complex(b)

    def subtrair(self, a, b):
        return complex(a) - complex(b)

    def multiplicar(self, a, b):
        return complex(a) * complex(b)

    def dividir(self, a, b):
        if complex(b) == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return complex(a) / complex(b)

    def potencia(self, a, b):
        return complex(a) ** complex(b)

    def raiz_quadrada(self, a):
        return cmath.sqrt(complex(a))

class ManipulacaoMatriz:
    def __init__(self):
        pass

    def adicionar(self, matriz1, matriz2):
        return np.add(matriz1, matriz2)

    def subtrair(self, matriz1, matriz2):
        return np.subtract(matriz1, matriz2)

    def multiplicar(self, matriz1, matriz2):
        return np.dot(matriz1, matriz2)

    def transpor(self, matriz):
        return np.transpose(matriz)

def menu():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    while True:
        escolha = simpledialog.askstring("Menu", "Selecione o tipo de operação:\n1. Operações básicas\n2. Operações com números complexos\n3. Manipulação de matrizes\n4. Sair")

        if escolha == '1':
            calc = Calculadora()
            a = float(simpledialog.askstring("Operações básicas", "Digite o primeiro número:"))
            b = float(simpledialog.askstring("Operações básicas", "Digite o segundo número:"))
            operacao = simpledialog.askstring("Operações básicas", "Escolha a operação (+, -, *, /, **, sqrt):")
            try:
                if operacao == '+':
                    resultado = calc.adicionar(a, b)
                elif operacao == '-':
                    resultado = calc.subtrair(a, b)
                elif operacao == '*':
                    resultado = calc.multiplicar(a, b)
                elif operacao == '/':
                    resultado = calc.dividir(a, b)
                elif operacao == '**':
                    resultado = calc.potencia(a, b)
                elif operacao == 'sqrt':
                    resultado = calc.raiz_quadrada(a)
                else:
                    raise ValueError("Operação inválida.")
                messagebox.showinfo("Resultado", f"Resultado: {resultado}")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        elif escolha == '2':
            calc_complexa = CalculadoraComplexa()
            a = complex(simpledialog.askstring("Operações com números complexos", "Digite o primeiro número complexo (ex: 1+2j):"))
            b = complex(simpledialog.askstring("Operações com números complexos", "Digite o segundo número complexo (ex: 3+4j):"))
            operacao = simpledialog.askstring("Operações com números complexos", "Escolha a operação (+, -, *, /, **, sqrt):")
            try:
                if operacao == '+':
                    resultado = calc_complexa.adicionar(a, b)
                elif operacao == '-':
                    resultado = calc_complexa.subtrair(a, b)
                elif operacao == '*':
                    resultado = calc_complexa.multiplicar(a, b)
                elif operacao == '/':
                    resultado = calc_complexa.dividir(a, b)
                elif operacao == '**':
                    resultado = calc_complexa.potencia(a, b)
                elif operacao == 'sqrt':
                    resultado = calc_complexa.raiz_quadrada(a)
                else:
                    raise ValueError("Operação inválida.")
                messagebox.showinfo("Resultado", f"Resultado: {resultado}")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        elif escolha == '3':
            manip_matriz = ManipulacaoMatriz()
            linhas1 = int(simpledialog.askstring("Manipulação de matrizes", "Digite o número de linhas da primeira matriz:"))
            colunas1 = int(simpledialog.askstring("Manipulação de matrizes", "Digite o número de colunas da primeira matriz:"))
            matriz1 = []
            for i in range(linhas1):
                linha = list(map(float, simpledialog.askstring("Manipulação de matrizes", f"Digite os elementos da linha {i+1} separados por espaço:").split()))
                matriz1.append(linha)
            matriz1 = np.array(matriz1)

            linhas2 = int(simpledialog.askstring("Manipulação de matrizes", "Digite o número de linhas da segunda matriz:"))
            colunas2 = int(simpledialog.askstring("Manipulação de matrizes", "Digite o número de colunas da segunda matriz:"))
            matriz2 = []
            for i in range(linhas2):
                linha = list(map(float, simpledialog.askstring("Manipulação de matrizes", f"Digite os elementos da linha {i+1} separados por espaço:").split()))
                matriz2.append(linha)
            matriz2 = np.array(matriz2)

            operacao = simpledialog.askstring("Manipulação de matrizes", "Escolha a operação (add, sub, mul, trans):")
            try:
                if operacao == 'add':
                    resultado = manip_matriz.adicionar(matriz1, matriz2)
                elif operacao == 'sub':
                    resultado = manip_matriz.subtrair(matriz1, matriz2)
                elif operacao == 'mul':
                    resultado = manip_matriz.multiplicar(matriz1, matriz2)
                elif operacao == 'trans':
                    resultado = manip_matriz.transpor(matriz1)
                else:
                    raise ValueError("Operação inválida.")
                messagebox.showinfo("Resultado", f"Resultado:\n{resultado}")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        elif escolha == '4':
            messagebox.showinfo("Saindo", "Saindo...")
            break
        else:
            messagebox.showerror("Erro", "Opção inválida.")

if __name__ == "__main__":
    menu()
