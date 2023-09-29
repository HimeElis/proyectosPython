# Función para convertir de centímetros a pulgadas
import tkinter as tk


def cm_a_pulgadas(cm):
    pulgadas = cm / 2.54
    return pulgadas


# Solicitar al usuario la cantidad en centímetros
cm = float(input("Ingresa la longitud en centímetros: "))

# Realizar la conversión
pulgadas = cm_a_pulgadas(cm)

# Mostrar el resultado
print(f"{cm} centímetros son equivalentes a {pulgadas} pulgadas")


# Función para realizar la conversión

def convertir():
    try:
        cm = float(entrada_cm.get())
        pulgadas = cm / 2.54
        resultado.set(
            f"{cm} centímetros son equivalentes a {pulgadas:.2f} pulgadas")
    except ValueError:
        resultado.set("¡Ingresa un valor válido!")


# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Conversor de Centímetros a Pulgadas")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresa la longitud en centímetros:")
etiqueta.pack(pady=10)

# Entrada de texto
entrada_cm = tk.Entry(ventana)
entrada_cm.pack()

# Botón de conversión
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack(pady=5)

# Resultado
resultado = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado)
resultado_label.pack(pady=10)

ventana.mainloop()
