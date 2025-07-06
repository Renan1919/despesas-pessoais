# importando SQLite
import sqlite3 as lite
import pandas as pd

# Criando conexao
con = lite.connect('dados.db')


# funções de Inserção ----------------------------------

# Inserir categorias
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Categoria (nome) VALUES (?)'
        cur.execute(query, i)

# Inserir Receita
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Receitas (categoria, adicionado_em,valor) VALUES (?,?,?)'
        cur.execute(query, i)

# Inserir Gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)'
        cur.execute(query, i)

# funções pra deletar ----------------------------------

# deletar Receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Receitas WHERE id=?'
        cur.execute(query, i)

# deletar Gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Gastos WHERE id=?'
        cur.execute(query, i)

# funções pra ver dados ----------------------------------

# Ver categoria
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Categoria')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    
    return lista_itens


# Ver Receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Receitas')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    
    return lista_itens


# Ver Gastos
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Gastos')
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    
    return lista_itens

# funçao para dados da tabela
def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista


# funçao para dados do grafico de barras
def bar_valores():
    # receita total
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gasto_total = sum(gastos_lista)

    # Saldo Total
    saldo_total = receita_total - gasto_total

    return[receita_total,gasto_total,saldo_total]

# funçao grafico pie
def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista, columns = ['id', 'categoria', 'Data', 'valor'])
    dataframe = dataframe.groupby('categoria',)['valor'].sum()

    lista_valor = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return([lista_categorias, lista_valor])

# funçao percentagem
def percentagem_valor():
    # receita total
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gasto_total = sum(gastos_lista)

    # Percentagem Total
    total = ((receita_total - gasto_total) / receita_total) * 100

    return[total]
