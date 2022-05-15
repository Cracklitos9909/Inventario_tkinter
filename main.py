import tkinter as tk

def registrar_producto():
  ventana_registrar = tk.Tk()
  ventana_registrar.title("Registrar producto")
  ventana_registrar.geometry("600x600")

  etiqueta_nombre = tk.Label(ventana_registrar,text = "Nombre del producto:")
  etiqueta_nombre.pack()
  entrada_nombre = tk.Entry(ventana_registrar)
  entrada_nombre.pack()

  etiqueta_cantidad = tk.Label(ventana_registrar,text = "Cantidad:")
  etiqueta_cantidad.pack()
  entrada_cantidad = tk.Entry(ventana_registrar)
  entrada_cantidad.pack()

  etiqueta_costo = tk.Label(ventana_registrar,text = "Costo del producto:")
  etiqueta_costo.pack()
  entrada_costo = tk.Entry(ventana_registrar)
  entrada_costo.pack()

  etiqueta_codigo = tk.Label(ventana_registrar,text = "Codigo del producto:")
  etiqueta_codigo.pack()
  entrada_codigo = tk.Entry(ventana_registrar)
  entrada_codigo.pack()

  etiqueta_descripcion = tk.Label(ventana_registrar,text = "Descripcion del producto:")
  etiqueta_descripcion.pack()
  entrada_descripcion = tk.Text(ventana_registrar, width=25, height=5)
  entrada_descripcion.pack()

  boton_registrar = tk.Button(ventana_registrar,text = "Registrar producto")
  boton_registrar.pack()
  
  ventana_registrar.mainloop()


def main():
  ventana = tk.Tk()
  ventana.title("Inventario de productos")
  ventana.geometry("600x600")
  barra_menu = tk.Menu(ventana)
  elementos_menu = tk.Menu(barra_menu, tearoff = 0)
  barra_menu.add_cascade(label = "Operaciones", menu = elementos_menu)
  elementos_menu.add_command(label = "Registrar producto", command = registrar_producto)
  elementos_menu.add_command(label = "Listar productos")
  elementos_menu.add_command(label = "Modificar producto")
  elementos_menu.add_command(label = "Eliminar producto")
  elementos_menu.add_separator()
  elementos_menu.add_command(label = "Salir", command = ventana.destroy)

  ventana.config(menu = barra_menu)
  ventana.mainloop()


if __name__ == "__main__":
  main()