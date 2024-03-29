from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt
import csv
from PIL import ImageTk, Image


indice = 0

def reporte_categorias():
  ventana_reporte_categoria = tk.Tk()
  ventana_reporte_categoria.title("Reporte de categorias")
  ventana_reporte_categoria.iconbitmap("./icono.ico")

  tree = ttk.Treeview(ventana_reporte_categoria)
  tree.pack()
  productos = {}
  with open("Inventario.csv", "r", newline="") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    for campo in lector:
      if campo[4] in productos:
        productos[campo[4]].append(campo[0])
      else:
        productos[campo[4]] = [campo[0]]
    for categoria, productos_temp in productos.items():
      categoria_arbol = tree.insert("",tk.END, text= categoria)
      for p in productos_temp:
        tree.insert(categoria_arbol, tk.END,text=p)

  boton_salir = tk.Button(ventana_reporte_categoria, text = "Salir", command=ventana_reporte_categoria.destroy)
  boton_salir.pack()
  # ventana_reporte_categoria.attributes("-fullscreen", True)
  ventana_reporte_categoria.mainloop()

def reporte_inventario_costo():
   with open("Inventario.csv","r", newline="") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    contenido = []
    for val in lector:
      contenido.append(val)
    nombres = []
    cantidades = []
    for linea in contenido:
      nombres.append(linea[0])
      cantidades.append(float(linea[2]))

    fig = plt.figure(figsize = (10, 5))
    plt.bar(nombres, cantidades, color ='blue',
        width = 0.10)
    plt.xlabel("Nombre de los productos")
    plt.ylabel("Costo de los productos")
    plt.title("Costos")
    plt.show()

def reporte_inventario():
  with open("Inventario.csv","r", newline="") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    contenido = []
    for val in lector:
      contenido.append(val)
  nombres = []
  cantidades = []
  for linea in contenido:
    nombres.append(linea[0])
    cantidades.append(float(linea[2]))
  plt.figure(num="Grafica de reportes de inventario")
  plt.title("Reporte de inventario")
  plt.pie(cantidades, labels = nombres)
  plt.show()

def eliminar_producto():
  ventana_eliminar_producto = tk.Tk()
  ventana_eliminar_producto.title("Modificar producto")
  ventana_eliminar_producto.iconbitmap("./icono.ico")

  etiqueta_identificador = tk.Label(ventana_eliminar_producto, text="Ingresa el codigo del producto que quieres eliminar:")
  etiqueta_identificador.pack()
  identificador = tk.Entry(ventana_eliminar_producto)
  identificador.pack()

  etiqueta_nombre = tk.Label(ventana_eliminar_producto,text = "Nombre del producto:")
  etiqueta_nombre.pack()
  entrada_nombre = tk.Entry(ventana_eliminar_producto)
  entrada_nombre.pack()

  etiqueta_cantidad = tk.Label(ventana_eliminar_producto,text = "Cantidad:")
  etiqueta_cantidad.pack()
  entrada_cantidad = tk.Entry(ventana_eliminar_producto)
  entrada_cantidad.pack()

  etiqueta_costo = tk.Label(ventana_eliminar_producto,text = "Costo del producto:")
  etiqueta_costo.pack()
  entrada_costo = tk.Entry(ventana_eliminar_producto)
  entrada_costo.pack()

  etiqueta_codigo = tk.Label(ventana_eliminar_producto,text = "Codigo del producto:")
  etiqueta_codigo.pack()
  entrada_codigo = tk.Entry(ventana_eliminar_producto)
  entrada_codigo.pack()

  etiqueta_descripcion = tk.Label(ventana_eliminar_producto,text = "Descripcion del producto:")
  etiqueta_descripcion.pack()
  entrada_descripcion = tk.Text(ventana_eliminar_producto, width=25, height=5)
  entrada_descripcion.pack()

  def eliminar_registro():
    global indice
    datos = []
    with open("Inventario.csv", "r", newline="") as archivo:
      lector = csv.reader(archivo, delimiter=",")
      for lista in lector:
        datos.append(lista)
      datos.pop(indice)
      indice = 0
    
    with open("Inventario.csv", "w", newline="") as archivo:
      escritor = csv.writer(archivo, delimiter=",")
      for registro in datos:
        escritor.writerow(registro)

  def buscar_producto():
    try:
      id = identificador.get()
      with open("Inventario.csv", 'r', newline = "") as archivo:
        lector = csv.reader(archivo, delimiter = ",")
        bandera = False
        registro_temporal = []
        global indice 
        for registro in lector:
          if registro[3] == id:
            registro_temporal = registro
            bandera = True
            break
          indice += 1
        if bandera:
          entrada_nombre.insert(0, registro_temporal[0])
          entrada_cantidad.insert(0, registro_temporal[1])
          entrada_costo.insert(0, registro_temporal[2])
          entrada_codigo.insert(0, registro_temporal[3])
          entrada_descripcion.insert(1.0, registro_temporal[4])
        else:
          etiqueta_error = tk.Label(ventana_eliminar_producto, text="El producto no fue encontrado:)")
          etiqueta_error.pack()
    except:
      etiqueta_error = tk.Label(ventana_eliminar_producto, text="Lo sentimos algo salio mal, por favor intente de nuevo :)")
      etiqueta_error.pack()

  boton_buscar = tk.Button(ventana_eliminar_producto ,text="Buscar producto", command=buscar_producto)
  boton_buscar.pack()

  boton_modificar_datos = tk.Button(ventana_eliminar_producto, text="Eliminar", command=eliminar_registro)
  boton_modificar_datos.pack()

  boton_salir = tk.Button(ventana_eliminar_producto ,text="Salir", command=ventana_eliminar_producto.destroy)
  boton_salir.pack()

  # ventana_eliminar_producto.attributes("-fullscreen", True)
  ventana_eliminar_producto.config(background="green")
  ventana_eliminar_producto.mainloop()

def modificar_producto():
  ventana_modificar_producto = tk.Tk()
  ventana_modificar_producto.title("Modificar producto")
  ventana_modificar_producto.iconbitmap("./icono.ico")

  etiqueta_identificador = tk.Label(ventana_modificar_producto, text="Ingresa el codigo del producto que quieres modificar:")
  etiqueta_identificador.pack()
  identificador = tk.Entry(ventana_modificar_producto)
  identificador.pack()

  etiqueta_nombre = tk.Label(ventana_modificar_producto,text = "Nombre del producto:")
  etiqueta_nombre.pack()
  entrada_nombre = tk.Entry(ventana_modificar_producto)
  entrada_nombre.pack()

  etiqueta_cantidad = tk.Label(ventana_modificar_producto,text = "Cantidad:")
  etiqueta_cantidad.pack()
  entrada_cantidad = tk.Entry(ventana_modificar_producto)
  entrada_cantidad.pack()

  etiqueta_costo = tk.Label(ventana_modificar_producto,text = "Costo del producto:")
  etiqueta_costo.pack()
  entrada_costo = tk.Entry(ventana_modificar_producto)
  entrada_costo.pack()

  etiqueta_codigo = tk.Label(ventana_modificar_producto,text = "Codigo del producto:")
  etiqueta_codigo.pack()
  entrada_codigo = tk.Entry(ventana_modificar_producto)
  entrada_codigo.pack()

  etiqueta_descripcion = tk.Label(ventana_modificar_producto,text = "Descripcion del producto:")
  etiqueta_descripcion.pack()
  entrada_descripcion = tk.Text(ventana_modificar_producto, width=25, height=5)
  entrada_descripcion.pack()

  def modificar_datos():
    global indice
    datos = []
    with open("Inventario.csv", "r", newline="") as archivo:
      lector = csv.reader(archivo, delimiter=",")
      for lista in lector:
        datos.append(lista)
      nombre = entrada_nombre.get()
      cantidad = entrada_cantidad.get()
      costo = float(entrada_costo.get())
      codigo = entrada_codigo.get()
      descripcion = str(entrada_descripcion.get("1.0", "end-1c"))
      datos[indice][0] = nombre
      datos[indice][1] = cantidad
      datos[indice][2] = costo
      datos[indice][3] = codigo
      datos[indice][4] = descripcion
      indice = 0
    
    with open("Inventario.csv", "w", newline="") as archivo:
      escritor = csv.writer(archivo, delimiter=",")
      for registro in datos:
        escritor.writerow(registro)

  def buscar_producto():
    try:
      id = identificador.get()
      with open("Inventario.csv", 'r', newline = "") as archivo:
        lector = csv.reader(archivo, delimiter = ",")
        bandera = False
        registro_temporal = []
        global indice 
        for registro in lector:
          if registro[3] == id:
            registro_temporal = registro
            bandera = True
            break
          indice += 1
        if bandera:
          entrada_nombre.insert(0, registro_temporal[0])
          entrada_cantidad.insert(0, registro_temporal[1])
          entrada_costo.insert(0, registro_temporal[2])
          entrada_codigo.insert(0, registro_temporal[3])
          entrada_descripcion.insert(1.0, registro_temporal[4])
        else:
          etiqueta_error = tk.Label(ventana_modificar_producto, text="El producto no fue encontrado:)")
          etiqueta_error.pack()
    except:
      etiqueta_error = tk.Label(ventana_modificar_producto, text="Lo sentimos algo salio mal, por favor intente de nuevo :)")
      etiqueta_error.pack()

  boton_buscar = tk.Button(ventana_modificar_producto ,text="Buscar producto", command=buscar_producto)
  boton_buscar.pack()

  boton_modificar_datos = tk.Button(ventana_modificar_producto, text="Modificar datos", command=modificar_datos)
  boton_modificar_datos.pack()

  boton_salir = tk.Button(ventana_modificar_producto ,text="Salir", command=ventana_modificar_producto.destroy)
  boton_salir.pack()

  # ventana_modificar_producto.attributes("-fullscreen", True)
  ventana_modificar_producto.config(background="green")
  ventana_modificar_producto.mainloop()

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
        entrada_nombre.delete(0,"end")
        entrada_cantidad.delete(0,"end")
        entrada_costo.delete(0,"end")
        entrada_codigo.delete(0,"end")
        entrada_descripcion.delete(1.0,"end")
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
  ventana_registrar.iconbitmap("./icono.ico")

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
  
  # ventana_registrar.attributes("-fullscreen", True)
  ventana_registrar.config(background="green")
  ventana_registrar.mainloop()

def listar_productos():
  ventana_listar_productos = tk.Tk()
  ventana_listar_productos.title("Lista de productos")
  ventana_listar_productos.iconbitmap("./icono.ico")

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

  with open("Inventario.csv", 'r', newline = "") as archivo:
    lector = csv.reader(archivo, delimiter = ",")
    for registro in lector:
      arbol.insert("",0,values = (registro[0], registro[1], registro[2], registro[3], registro[4]))

  boton_salir = tk.Button(ventana_listar_productos ,text="Salir", command=ventana_listar_productos.destroy)
  boton_salir.pack()

  # ventana_listar_productos.attributes("-fullscreen", True)
  ventana_listar_productos.config(background="green")
  ventana_listar_productos.mainloop()


def main():
  ventana = tk.Tk()
  ventana.title("Tienda deportiva futbol emotion")
  ventana.geometry("600x600")
  ventana.iconbitmap("./icono.ico")
 
  frame = tk.Frame(ventana, width=600, height=400)
  frame.pack()
  frame.place(anchor='center', relx=0.5, rely=0.5)

  # Create an object of tkinter ImageTk
  img = ImageTk.PhotoImage(Image.open("./background.png"))

  # Create a Label Widget to display the text or Image
  label = tk.Label(frame, image = img)
  label.pack()

  barra_menu = tk.Menu(ventana)
  elementos_menu = tk.Menu(barra_menu, tearoff = 0)
  menu_reportes = tk.Menu(barra_menu, tearoff = 0)
  barra_menu.add_cascade(label = "Operaciones", menu = elementos_menu)
  barra_menu.add_cascade(label="Reportes",menu= menu_reportes)
  elementos_menu.add_command(label = "Registrar producto", command = registrar_producto)
  elementos_menu.add_command(label = "Listar productos", command=listar_productos)
  elementos_menu.add_command(label = "Modificar producto", command=modificar_producto)
  elementos_menu.add_command(label = "Eliminar producto", command=eliminar_producto)
  elementos_menu.add_separator()
  elementos_menu.add_command(label = "Salir", command = ventana.destroy)
  menu_reportes.add_command(label="Reporte de inventario", command=reporte_inventario)
  menu_reportes.add_command(label = "Reporte de costos", command=reporte_inventario_costo)
  menu_reportes.add_command(label = "Reporte por categoria", command = reporte_categorias)

  
  ventana.config(menu = barra_menu)
  ventana.config(background="green")
  ventana.mainloop()


if __name__ == "__main__":
  main()