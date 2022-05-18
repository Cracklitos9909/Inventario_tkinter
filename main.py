from tkinter import ttk
import tkinter as tk
import csv

def registrar_producto():
  def guardar_datos():
    try:
      nombre = entrada_nombre.get()
      cantidad = entrada_cantidad.get()
      costo = float(entrada_costo.get())
      codigo = entrada_codigo.get()
      descripcion = str(entrada_descripcion.get("1.0", "end-1c"))
      with open("Inventario.csv", "a", newline="") as archivo:
        registro = [nombre, cantidad, costo, codigo, descripcion]
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(registro)
        archivo.close()
    except:
      etiqueta_error = tk.Label(ventana_registrar, text="Lo sentimos algo salio mal, por favor intente de nuevo :)")
      etiqueta_error.pack()
  
  def limpiar_campos():
    entrada_nombre.delete(0,"end")
    entrada_cantidad.delete(0,"end")
    entrada_costo.delete(0,"end")
    entrada_codigo.delete(0,"end")
    entrada_descripcion.delete(1.0,"end")

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

  boton_registrar = tk.Button(ventana_registrar,text = "Registrar producto", command=guardar_datos)
  boton_registrar.pack()
  boton_limpiar_campos = tk.Button(ventana_registrar, text="Limpiar campos", command=limpiar_campos)
  boton_limpiar_campos.pack()
  boton_salir = tk.Button(ventana_registrar, text="Salir", command=ventana_registrar.destroy)
  boton_salir.pack()
  
  ventana_registrar.attributes("-fullscreen", True)
  ventana_registrar.mainloop()

def listar_productos():
  ventana_listar_productos = tk.Tk()
  ventana_listar_productos.title("Lista de productos")
  ventana_listar_productos.geometry("600x600")

  arbol = ttk.Treeview(ventana_listar_productos, columns=("nombre", "cantidad", "costo", "codigo", "descripcion"), show="headings")
  arbol.column("nombre", width=150, minwidth=150)
  arbol.heading("nombre", text="Nombre")
  arbol.column("cantidad", width=150, minwidth=150)
  arbol.heading("cantidad", text="Cantidad")
  arbol.column("costo", width=150, minwidth=150)
  arbol.heading("costo", text="Costo")
  arbol.column("codigo", width=150, minwidth=150)
  arbol.heading("codigo", text="Codigo")
  arbol.column("descripcion", width=150, minwidth=150)
  arbol.heading("descripcion", text="Descripcion")
  arbol.pack()

  boton_salir = tk.Button(ventana_listar_productos ,text="Salir", command=ventana_listar_productos.destroy)
  boton_salir.pack()

  ventana_listar_productos.attributes("-fullscreen", True)
  ventana_listar_productos.mainloop()


def main():
  ventana = tk.Tk()
  ventana.title("Inventario de productos")
  ventana.geometry("600x600")
  barra_menu = tk.Menu(ventana)
  elementos_menu = tk.Menu(barra_menu, tearoff = 0)
  barra_menu.add_cascade(label = "Operaciones", menu = elementos_menu)
  elementos_menu.add_command(label = "Registrar producto", command = registrar_producto)
  elementos_menu.add_command(label = "Listar productos", command=listar_productos)
  elementos_menu.add_command(label = "Modificar producto")
  elementos_menu.add_command(label = "Eliminar producto")
  elementos_menu.add_separator()
  elementos_menu.add_command(label = "Salir", command = ventana.destroy)

  ventana.attributes("-fullscreen", True)
  ventana.config(menu = barra_menu)
  ventana.mainloop()


if __name__ == "__main__":
  main()