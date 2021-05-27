#...................taller 8..............#

import matplotib.pylot as plt
mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
ingresos = [100, 200, 300, 400, 500, 600]
plt.bar (mes, ingresos, width = 0.8, color = "r")
plt.title ("Cantidad de ingresos")
plt.xlabel ("mes")
plt.ylabel("ingresos")
plt.savefig("GraficoBarra.png")
plt.show()

