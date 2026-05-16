import pandas as pd #Importamos pandas para poder trabajar con el archivo .csv
import matplotlib.pyplot as plt #Para mostrar y crear graficos

print("Bienvenido, a continuacion se le mostrara el grafico de ventas totales de la semana del 15/05/2026 al 19/05/2026")
print("Debe elejir un dia (del 15 al 19) y se le mostrara la cantidad de materiales que se vendio en ese dia")
while True:
    elegir_dia=input("Opcion 1: 15/05/2026\nOpcion 2: 16/05/2026\nOpcion 3: 17/05/2026\nOpcion 4: 18/05/2026\nOpcion 5: 19/05/2026\n>>> ") #El usuario elije un dia de la semana
    if elegir_dia.isdigit() == True: #Validamos que ingrese un numero
        elegir_dia=int(elegir_dia) #si es un numero lo transformamos en entero
        if elegir_dia in (1,2,3,4,5): #Si el numero esta dentro de la tupla continuamos
            break
        else:
            print("\tERROR. Fuera de rango")
    else:
        print("\tERROR. Ingrese un numero")
#Asignamos el dia elejido para el grafico
if elegir_dia == 1:
    fecha_seleccionada="15/05/2026"
elif elegir_dia == 2:
    fecha_seleccionada="16/05/2026"
elif elegir_dia == 3:
    fecha_seleccionada="17/05/2026"
elif elegir_dia == 4:
    fecha_seleccionada="18/05/2026"
elif elegir_dia == 5:
    fecha_seleccionada="19/05/2026"

df_productos = pd.read_csv("otras_cosas/lista.csv") # Abrimos el archivo .csv

#Elementos del primer grafico
ventas_semanal = df_productos.groupby("fecha_venta")["cantidad"].sum()
"""
se trabaja en el .csv, con groupby se agrupan las filas del mismo valor, que en este caso son las filas de las fechas que son iguales.
["cantidad"] selecciona solo la columna cantidad, y con .sum() se suman los valores de la columna cantidad.
Ejemplo: se selecciona la mismas fechas (15/05/2026) luego selecciona la columna cantidad de la mismas fechas y se suman los valores de esa columna.
Esto se hace en todas las fechas, que en este ejemplo practico son las del 15 al 19.
"""

#Elementos del segundo grafico
dia_venta = df_productos[df_productos["fecha_venta"] == fecha_seleccionada]
ventas_producto = dia_venta.groupby("item")["cantidad"].sum()
"""
En la primera linea, se fltra la fecha seleccionada(fecha_seleccionada) de "fecha_venta"
En la segunda linea, se agrupa por item (herramienta) y luego se le suma las cantidades de cada item.
"""
# Crear ventana con 2 graficos
fig, axs = plt.subplots(1, 2, figsize=(18,9))

#Creacion del primer grafico, con sus interfaces
ventas_semanal.plot(kind="barh", ax=axs[0])
axs[0].set_title("Ventas de la semana")
axs[0].set_xlabel("Cantidad")
axs[0].set_ylabel("Fecha")

#Creacion del segundo grafico con sus interfaces
ventas_producto.plot(kind="barh", ax=axs[1])
axs[1].set_title(f"Ventas del {fecha_seleccionada}")
axs[1].set_xlabel("Cantidad")
axs[1].set_ylabel("Producto")

plt.tight_layout() #Con esto se ajusta la imagen, recomendable ponerlo antes de guardar la imagen y antes de mostrar la imagen

plt.savefig("../resultados/grafico.png") #Guardamos la imagen

plt.show() #Se muestran ambos graficos
