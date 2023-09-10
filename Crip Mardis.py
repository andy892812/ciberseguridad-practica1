import tkinter as tk
from tkinter import ttk, messagebox

def verificar_contrasena():
    # Obtenemos la contraseña ingresada por el usuario
    contrasena_ingresada = entry_contrasena.get()

    # Contraseña correcta (puedes cambiarla a tu gusto)
    contrasena_correcta = "contrasena123"

    if contrasena_ingresada == contrasena_correcta:
        messagebox.showinfo("Acceso concedido", "Contraseña correcta. Bienvenido.")
        # Destruir ventana de ingreso de contraseña
        ventana_contrasena.destroy()
        # Llamar a la función para mostrar la tabla
        mostrar_tabla()
    else:
        messagebox.showerror("Acceso denegado", "Contraseña incorrecta. Inténtalo de nuevo.")

def mostrar_tabla():
    # Crear ventana para mostrar la tabla
    ventana_tabla = tk.Tk()
    ventana_tabla.title("Tabla de Valores")



    # Crear una tabla (Treeview)
    tabla = ttk.Treeview(ventana_tabla)
    tabla["columns"] = ("Clave", "Nombre", "Edad", "Ciudad")  # Definir las columnas de la tabla
    tabla.heading("#0", text="ID")
    tabla.column("#0", width=50)
    tabla.heading("Clave", text="Clave")
    tabla.column("Clave", anchor=tk.CENTER, width=100)
    tabla.heading("Nombre", text="Nombre")
    tabla.column("Nombre", anchor=tk.CENTER, width=100)
    tabla.heading("Edad", text="Edad")
    tabla.column("Edad", anchor=tk.CENTER, width=100)
    tabla.heading("Ciudad", text="Ciudad")
    tabla.column("Ciudad", anchor=tk.CENTER, width=100)

    # Insertar datos de ejemplo en la tabla
    datos_ejemplo = [
        ("ABC123", "Juan", 25, "Ciudad A"),
        ("XYZ456", "María", 30, "Ciudad B"),
        ("DEF789", "Pedro", 28, "Ciudad C"),
        ("GHI012", "Luisa", 22, "Ciudad D")
    ]

    for i, (clave, nombre, edad, ciudad) in enumerate(datos_ejemplo, start=1):
        tabla.insert(parent='', index='end', iid=i, text=str(i), values=(clave, nombre, edad, ciudad))

    tabla.pack()

    # Función para agregar un nuevo registro en la tabla
    def agregar_registro():
        nombre_nuevo = entry_nombre.get()
        edad_nueva = entry_edad.get()
        ciudad_nueva = entry_ciudad.get()

        # Validar que se ingresen datos en todos los campos
        if nombre_nuevo and edad_nueva and ciudad_nueva:
            # Obtener el último índice de la tabla
            ultimo_indice = int(tabla.get_children()[-1]) if tabla.get_children() else 0
            nuevo_indice = ultimo_indice + 1

            # Insertar el nuevo registro en la tabla
            tabla.insert(parent='', index='end', iid=nuevo_indice, text=str(nuevo_indice), values=(nombre_nuevo, edad_nueva, ciudad_nueva))
            messagebox.showinfo("Registro agregado", "El nuevo registro ha sido agregado correctamente.")
            # Limpiar los campos de entrada
            entry_clave.delete(0, tk.END)
            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
            entry_ciudad.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos incompletos", "Por favor, ingresa valores en todos los campos.")

    # Función para editar un registro existente en la tabla
    def editar_registro():
        seleccionado = tabla.focus()  # Obtener el ID del ítem seleccionado
        if seleccionado:
            datos_actuales = tabla.item(seleccionado, "values")
            entry_clave.delete(0, tk.END)
            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
            entry_ciudad.delete(0, tk.END)
            entry_clave.insert(0, datos_actuales[0])
            entry_nombre.insert(0, datos_actuales[1])
            entry_edad.insert(0, datos_actuales[2])
            entry_ciudad.insert(0, datos_actuales[3])
            messagebox.showinfo("Edición habilitada", "Puedes editar los valores ahora.")
        else:
            messagebox.showwarning("No se seleccionó ningún registro", "Por favor, selecciona un registro para editar.")

    # Función para guardar los cambios en el registro editado
    def guardar_cambios():
        seleccionado = tabla.focus()  # Obtener el ID del ítem seleccionado
        if seleccionado:
            clave_editada = entry_clave.get()
            nombre_editado = entry_nombre.get()
            edad_editada = entry_edad.get()
            ciudad_editada = entry_ciudad.get()

            # Validar que se ingresen datos en todos los campos
            if clave_editada and nombre_editado and edad_editada and ciudad_editada:
                tabla.item(seleccionado, values=(clave_editada, nombre_editado, edad_editada, ciudad_editada))
                messagebox.showinfo("Cambios guardados", "Los cambios en el registro han sido guardados correctamente.")
            else:
                messagebox.showwarning("Campos incompletos", "Por favor, ingresa valores en todos los campos.")
        else:
            messagebox.showwarning("No se seleccionó ningún registro", "Por favor, selecciona un registro para editar.")

    # Función para mostrar el contenido de la columna Clave en un popup
    def mostrar_clave_popup(event):
        item = tabla.selection()[0]
        clave = tabla.item(item, "values")[0]
        popup = tk.Toplevel()
        popup.title("Contenido Clave")
        label = tk.Label(popup, text="Clave: " + clave)
        label.pack(padx=10, pady=10)

    # Etiquetas y campos de entrada para agregar un nuevo registro
    label_clave = tk.Label(ventana_tabla, text="Clave:")
    label_clave.pack()
    entry_clave = tk.Entry(ventana_tabla)
    entry_clave.pack()

    label_nombre = tk.Label(ventana_tabla, text="Nombre:")
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana_tabla)
    entry_nombre.pack()

    label_edad = tk.Label(ventana_tabla, text="Edad:")
    label_edad.pack()
    entry_edad = tk.Entry(ventana_tabla)
    entry_edad.pack()

    label_ciudad = tk.Label(ventana_tabla, text="Ciudad:")
    label_ciudad.pack()
    entry_ciudad = tk.Entry(ventana_tabla)
    entry_ciudad.pack()

    # Botones para agregar, editar y guardar cambios en registros
    boton_agregar = tk.Button(ventana_tabla, text="Agregar Registro", command=agregar_registro)
    boton_agregar.pack()

    boton_editar = tk.Button(ventana_tabla, text="Editar Registro", command=editar_registro)
    boton_editar.pack()

    boton_guardar_cambios = tk.Button(ventana_tabla, text="Guardar Cambios", command=guardar_cambios)
    boton_guardar_cambios.pack()

    # Asociar la función mostrar_clave_popup al clic en la columna Clave
    tabla.bind("<Double-1>", mostrar_clave_popup)

    # Iniciar bucle de la aplicación para mostrar la tabla
    ventana_tabla.mainloop()

# Crear ventana para ingreso de contraseña
ventana_contrasena = tk.Tk()
ventana_contrasena.title("Ingreso de Contraseña")
ventana_contrasena.geometry("400x300")

# Etiqueta
label_contrasena = tk.Label(ventana_contrasena, text="Ingresa tu contraseña:")
label_contrasena.pack()

# Campo de entrada para la contraseña
entry_contrasena = tk.Entry(ventana_contrasena, show="*")  # La opción show="*" muestra los caracteres como asteriscos
entry_contrasena.pack()

# Botón para verificar la contraseña
boton_verificar = tk.Button(ventana_contrasena, text="Verificar", command=verificar_contrasena)
boton_verificar.pack()

# Iniciar bucle de la aplicación para ingreso de contraseña
ventana_contrasena.mainloop()
