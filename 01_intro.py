import matplotlib.pyplot as plt

def generar_pie():
    etiquetas = ['A', 'B', 'C']
    valores = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(valores, labels=etiquetas, autopct='%1.1f%%')

    plt.savefig('grafico_pie.png')
    plt.close()

generar_pie()