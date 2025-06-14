import pyautogui
import time

#pyautogui-> criado para fazer automações com python, ele usa o seu mouse , teclado e tela do computador
#pyautogui.click -> clicar em algum lugar
#pyautogui.press-> apertar 1 uma unica tecla 
#pyautogui.write-> escrever um texto
#pyautogui.hotkey-> apertar uma combinação de teclas, um atalho

pyautogui.PAUSE= 0.5 # define uma configuração de delaypara que seja possivel executar todos os passos sem atropelar nenhum, em maiusculo pois é uma configuração
# essa configuração define essa pausa para cada comando do pyautogui

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# depois do enter eu preciso que le espere 3 segundos
time.sleep(3)

# Passo 2: Fazer Login
# precisamos dizer onde clicar
pyautogui.click(x=745, y=358)
pyautogui.write("alexiarkopke@gmail.com")

# preencher a senha
pyautogui.press("tab")
pyautogui.write("amor1972")

# Botao logar
pyautogui.press("tab")
pyautogui.press("enter")

#espera de 3 segundos
time.sleep(3)


# Passo 3: Importar a base de dados
import pandas

tabela= pandas.read_csv("produtos.csv")
# estamos armazenando as informações na variavel tabela 

# Passo 4: Cadastrar um produto
pyautogui.click(x=756, y=244)
codigo="MOLO000251"
pyautogui.write(codigo)
pyautogui.press("tab")# passar para o proximo campo

marca="Logitech"
pyautogui.write(marca)
pyautogui.press("tab")# passar para o proximo campo

tipo="Mouse"
pyautogui.write(tipo)
pyautogui.press("tab")# passar para o proximo campo

categoria="1"
pyautogui.write(categoria)
pyautogui.press("tab")# passar para o proximo campo

preco_unitario="25.95"
pyautogui.write(preco_unitario)
pyautogui.press("tab")# passar para o proximo campo

custo="6.50"
pyautogui.write(custo)
pyautogui.press("tab")# passar para o proximo campo

obs=" "
pyautogui.write(obs)
pyautogui.press("tab")# passar para o botao enviar
pyautogui.press("enter")

pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos
for linha in tabela.index:# para cada linha da minha tabela pelo índice(começa do zero)
    pyautogui.click(x=756, y=244)

    codigo= tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")# passar para o proximo campo

    marca=tabela.loc[linha, "marca"]

    pyautogui.write(marca)
    pyautogui.press("tab")# passar para o proximo campo

    tipo=tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")# passar para o proximo campo


    categoria=str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")# passar para o proximo campo

    preco_unitario=str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")# passar para o proximo campo

    custo=str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")# passar para o proximo campo

    obs=str(tabela.loc[linha, "obs"])
    if obs!= "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")# passar para o botao enviar
    pyautogui.press("enter")

    pyautogui.scroll(10000)

    #nan-> not a number