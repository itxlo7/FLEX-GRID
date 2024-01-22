import matplotlib.pyplot as plt
from matplotlib.patches import Arc

fig, ax = plt.subplots()

x_inicio = 0
y_alt = 1.006
x_fin1 = 0.11
x_fin = 0.02
y = 1
y_g = 1.008

plt.plot([0, 0], [y, y_alt], 'black')
plt.plot([0.035, 0.035], [y, y_alt], 'black')
plt.plot([0.07, 0.07], [y, y_alt], 'black')
plt.plot([0.09, 0.09], [y, y_alt], 'black')
plt.plot([0.11, 0.11], [y, y_alt], 'black')
plt.plot([0.0018, 0.033], [y_g, y_g], 'black')
plt.plot([0.037, 0.068], [y_g, y_g], 'black')
plt.plot([0.072, 0.088], [y_g, y_g], 'black')
plt.plot([0.092, 0.108], [y_g, y_g], 'black')

radio = 0.002
centros = [
    (0.002, 1.006),
    (0.092, 1.006),
    (0.037, 1.006),
    (0.072, 1.006),
    (0.033, 1.006),
    (0.068, 1.006),
    (0.088, 1.006),
    (0.108, 1.006)
]

for i in range(len(centros)):
    arco = Arc(centros[i], 2 * radio, 2 * radio, theta1=90, theta2=180, linewidth=1.5, edgecolor='black')
    if i > 3:
        arco = Arc(centros[i], 2 * radio, 2 * radio, theta1=0, theta2=90, linewidth=1.5, edgecolor='black')
    ax.add_patch(arco)

h=0.995
h1=0.99750
h2=0.99875
h3 = 0.99625
x_inicio1=0.0050
x_inicio2=0.00250
x_inicio3=0.00750
x_inicio4 = 0.01

plt.plot([x_inicio, x_fin1], [y, y], 'black')
aux = 0
for _ in range(6):
    plt.plot([x_inicio + aux, x_inicio + aux], [y, h], 'black')
    plt.plot([x_inicio1 + aux, x_inicio1 + aux], [y, h1], 'black')
    plt.plot([x_inicio2 + aux, x_inicio2 + aux], [y, h2], 'black')
    plt.plot([x_inicio3 + aux, x_inicio3 + aux], [y, h2], 'black')
    plt.plot([x_inicio4 + aux, x_inicio4 + aux], [y, h3], 'black')
    if aux <= 0.08:
        plt.plot([x_inicio1 + 0.01 + aux, x_inicio1 + 0.01 + aux], [y, h1], 'black')
        plt.plot([x_inicio2 + 0.01 + aux, x_inicio2 + 0.01 + aux], [y, h2], 'black')
        plt.plot([x_inicio3 + 0.01 + aux, x_inicio3 + 0.01 + aux], [y, h2], 'black')
    aux += 0.02 

y_texto = 1.003
y_texto1 = 1.012
y_textof=0.994

x_text = [0.0175, 0.0525, 0.08, 0.1005, 0.018, 0.053, 0.08, 0.1005]
texto = ['n=-1, m=7','n=13, m=7','n=24,m=4','n=32,m=4','87.5 GHz','87.5 GHz','50 GHz','50 GHz']
for i in range(len(x_text)):
    if i > 3:
        y_texto = y_texto1
    ax.text(x_text[i], y_texto, texto[i], ha='center', va='center', fontsize=9, color='black')

ubi = [0, 0.017, 0.0345, 0.0525, 0.0695, 0.0795, 0.0895, 0.0995, 0.1095]
frec = [193.05, 193.09375, 193.1375, 193.18125, 193.225, 193.25, 193.275, 193.3, 193.325]
for i, valor_ubi in enumerate(ubi):
    ax.text(valor_ubi, y_textof, frec[i], rotation=-90, ha='center', va='top', fontsize=10, color='black')

y_fle = 1.01
plt.annotate('', xytext=(0, y_fle), xy=(0.035, y_fle), arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xytext=(0.035, y_fle), xy=(0, y_fle), arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xytext=(0.035, y_fle), xy=(0.07, y_fle), arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xytext=(0.07, y_fle), xy=(0.035, y_fle), arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xytext=(0.07, y_fle), xy=(0.09, y_fle), arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xytext=(0.09, y_fle), xy=(0.07, y_fle), arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xytext=(0.09, y_fle), xy=(0.11, y_fle), arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xytext=(0.11, y_fle), xy=(0.09, y_fle), arrowprops=dict(arrowstyle='->', color='black'))

plt.xlim(x_inicio - 0.005, x_fin1 + 0.005)
plt.ylim(y_fle - 0.04, y_fle + 0.02)

plt.axis('off')
plt.show()
