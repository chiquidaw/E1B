# ============================================================================
# SISTEMA DE GESTIÓN DE ALMACÉN - Importaciones y Configuración
# ============================================================================
import tkinter as tk
from tkinter import ttk, messagebox
import json, os
from pathlib import Path

# Ruta del archivo JSON que persiste los datos del almacén
ARCHIVO_DATOS = Path(__file__).parent / "almacen_datos.json"

# Paleta de colores centralizada para consistencia visual en toda la interfaz
COLORES = {"fondo": "white", "grisel": "#ecf0f1", "texto": "#2c3e50", "grisT": "#7f8c8d",
           "exito": "#27ae60", "info": "#3498db", "advertencia": "#e67e22", "error": "#e74c3c",
           "trabajo": "#16a085", "especial": "#9b59b6", "fondo_entrada": "#f8f9fa"}

# Estilos de fuentes reutilizables para mantener coherencia visual
FUENTES = {"titulo": ("Arial", 11, "bold"), "etiqueta": ("Arial", 10, "bold"), "normal": ("Arial", 10),
           "ayuda": ("Arial", 9, "italic"), "monoesp": ("Courier", 9)}

# ============================================================================
# CLASE MODELO - Representa un producto en el almacén
# ============================================================================
class Producto:
    """Modelo que encapsula los datos de un producto (ID, nombre, precio, stock)."""
    
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.precio_original = precio  # Se mantiene para restaurar después de descuentos
        self.cantidad = cantidad
    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | ${self.precio} | Stock: {self.cantidad}"
    
    def to_dict(self):
        """Convierte el producto a diccionario para guardar en JSON."""
        return {"id": self.id, "nombre": self.nombre, "precio": self.precio, "cantidad": self.cantidad, "precio_original": self.precio_original}
    
    @staticmethod
    def from_dict(data):
        """Factory method que crea un producto desde datos cargados del JSON."""
        prod = Producto(data["id"], data["nombre"], data["precio"], data["cantidad"])
        prod.precio_original = data.get("precio_original", data["precio"])
        return prod

# ============================================================================
# CLASE DE LÓGICA DE NEGOCIOS - Gestión del almacén
# ============================================================================
class Almacen:
    """Controla la lógica de operaciones del almacén: CRUD, búsquedas, descuentos y persistencia."""
    
    def __init__(self):
        self.productos = []
        self.proximo_id = 1
        self.dinero_vendido = 0  # Acumula dinero total de todas las ventas
        self.cargar_datos()  # Cargar datos existentes al inicializar
    
    def cargar_datos(self):
        """Lee el JSON y carga todos los productos existentes, dinero acumulado y próximo ID."""
        if os.path.exists(str(ARCHIVO_DATOS)):
            try:
                with open(str(ARCHIVO_DATOS), 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    self.productos = [Producto.from_dict(p) for p in datos.get("productos", [])]
                    # Obtener el máximo ID y asignar el siguiente
                    self.proximo_id = max((p.id for p in self.productos), default=0) + 1 if self.productos else 1
                    # Cargar el dinero acumulado de ventas
                    self.dinero_vendido = datos.get("dinero_vendido", 0)
            except Exception as e:
                print(f"Error al cargar datos: {e}")
    
    def guardar_datos(self):
        """Persiste todos los productos, dinero acumulado y próximo ID en el JSON."""
        try:
            with open(str(ARCHIVO_DATOS), 'w', encoding='utf-8') as f:
                json.dump({"productos": [p.to_dict() for p in self.productos], "proximo_id": self.proximo_id, 
                          "dinero_vendido": self.dinero_vendido}, 
                         f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar datos: {e}")
    
    def crear_producto(self, nombre, precio, cantidad):
        """Valida y crea un nuevo producto con ID único. Persiste en JSON."""
        if not nombre or precio <= 0 or cantidad < 0 or any(p.nombre.lower() == nombre.lower() for p in self.productos):
            return (False, "✗ Datos inválidos o producto existente")
        prod = Producto(self.proximo_id, nombre, precio, cantidad)
        self.productos.append(prod)
        self.proximo_id += 1
        self.guardar_datos()
        return (True, f"✓ Producto '{nombre}' creado con ID {prod.id}")
    
    def buscar_por_id(self, id):
        return next((p for p in self.productos if p.id == id), None)
    
    def vender(self, id, cantidad):
        """Reduce el stock de un producto e incrementa dinero acumulado por venta."""
        prod = self.buscar_por_id(id)
        if prod and prod.cantidad >= cantidad and cantidad > 0:
            monto_venta = cantidad * prod.precio
            prod.cantidad -= cantidad
            self.dinero_vendido += monto_venta  # Acumular dinero de la venta
            self.guardar_datos()
            return (True, f"✓ Venta: {cantidad}x {prod.nombre} = ${monto_venta:.2f}", monto_venta)
        return (False, "✗ Stock insuficiente o cantidad inválida", 0)
    
    def listar_productos(self):
        return "El almacén está vacío" if not self.productos else "\n--- INVENTARIO ---\n" + "\n".join(str(p) for p in self.productos)
    
    def valor_total_almacen(self):
        return sum(p.precio * p.cantidad for p in self.productos)
    
    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]
    
    def actualizar_stock(self, id, cantidad):
        prod = self.buscar_por_id(id)
        if prod:
            prod.cantidad += cantidad
            self.guardar_datos()
            return f"✓ Stock: {prod.nombre} -> {prod.cantidad} unidades"
        return "✗ Producto no encontrado"
    
    def aplicar_descuento(self, id, porcentaje):
        """Aplica un descuento porcentual al precio, manteniendo el precio original para restauración."""
        prod = self.buscar_por_id(id)
        if prod and 0 <= porcentaje <= 100:
            prod.precio = prod.precio_original * (1 - porcentaje/100)
            self.guardar_datos()
            return f"✓ Descuento aplicado: {prod.nombre} = ${prod.precio:.2f}"
        return "✗ Producto no encontrado" if not prod else "✗ Porcentaje inválido"
    
    def resetear_descuento(self, id):
        """Restaura el precio original del producto removiendo cualquier descuento."""
        prod = self.buscar_por_id(id)
        if prod:
            if prod.precio != prod.precio_original:
                prod.precio = prod.precio_original
                self.guardar_datos()
                return f"✓ Descuento removido: {prod.nombre} = ${prod.precio:.2f}"
            return f"⚠️ {prod.nombre} sin descuento"
        return "✗ Producto no encontrado"
    
    def eliminar_producto(self, id):
        prod = self.buscar_por_id(id)
        if prod:
            self.productos.remove(prod)
            self.guardar_datos()
            return f"✓ {prod.nombre} eliminado"
        return "✗ Producto no encontrado"

# ============================================================================
# CLASE DE PRESENTACIÓN - Interfaz gráfica del almacén
# ============================================================================
class InterfazAlmacen:
    """Gestiona la interfaz gráfica Tkinter y la interacción del usuario con el almacén."""
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("▦ SISTEMA DE GESTIÓN DE ALMACÉN ▦")
        self.ventana.geometry("1300x900")
        self.almacen = Almacen()  # Instancia del controlador de negocio
        self.crear_interfaz()
    
    def mostrar_resultado(self, text_widget, msg):
        """Actualiza un widget de texto con un mensaje (limpia anterior y inserta nuevo)."""
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, msg)
    
    def crear_interfaz(self):
        """Construye toda la interfaz gráfica con tres secciones principales:
           1. Panel de inventario (lectura)
           2. Panel de información (valor total)
           3. Panel de operaciones (tabs para cada operación)"""
        self.ventana.config(bg=COLORES["fondo"])
        
        # Panel de inventario: muestra lista actualizada de todos los productos
        marco_inv = tk.Frame(self.ventana, bg=COLORES["fondo"], relief="solid", bd=1)
        marco_inv.pack(fill="both", expand=True, padx=12, pady=(12,5))
        tk.Label(marco_inv, text="▬ INVENTARIO ACTUAL", font=FUENTES["etiqueta"],
                bg=COLORES["fondo"], fg=COLORES["texto"]).pack(anchor="w", padx=15, pady=(10,5))
        
        marco_texto = tk.Frame(marco_inv, bg=COLORES["fondo"])
        marco_texto.pack(fill="both", expand=True, padx=15, pady=10)
        scrollbar = ttk.Scrollbar(marco_texto)
        scrollbar.pack(side="right", fill="y")
        self.text_inventario = tk.Text(marco_texto, height=10, width=110, yscrollcommand=scrollbar.set,
                                       font=FUENTES["monoesp"], bg=COLORES["fondo_entrada"],
                                       fg=COLORES["texto"], relief="solid", bd=1)
        self.text_inventario.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.text_inventario.yview)
        
        # Info
        marco_info = tk.Frame(self.ventana, bg=COLORES["grisel"], relief="solid", bd=1)
        marco_info.pack(fill="x", padx=12, pady=5)
        self.label_valor_total = tk.Label(marco_info, text="", font=FUENTES["titulo"],
                                         bg=COLORES["grisel"], fg=COLORES["exito"])
        self.label_valor_total.pack(side="left", padx=20, pady=10)
        self.label_cantidad_productos = tk.Label(marco_info, text="", font=FUENTES["etiqueta"],
                                                bg=COLORES["grisel"], fg=COLORES["info"])
        self.label_cantidad_productos.pack(side="left", padx=30, pady=10)
        self.label_dinero_vendido = tk.Label(marco_info, text="", font=FUENTES["etiqueta"],
                                            bg=COLORES["grisel"], fg=COLORES["especial"])
        self.label_dinero_vendido.pack(side="left", padx=30, pady=10)
        notebook = ttk.Notebook(self.ventana)
        notebook.pack(fill="both", expand=True, padx=12, pady=10)
        
        tabs = [("⊕ CREAR PRODUCTO", "crear"), ("◈ VENDER PRODUCTO", "ventas"),
                ("◻ GESTIONAR STOCK", "stock"), ("▣ DESCUENTOS", "descuentos"),
                ("◉ BUSCAR/ELIMINAR", "busqueda")]
        for texto, tipo in tabs:
            tab = tk.Frame(notebook, bg=COLORES["fondo"])
            notebook.add(tab, text=texto)
            getattr(self, f"crear_seccion_{tipo}")(tab)
        
        # Botones
        marco_botones = tk.Frame(self.ventana, bg=COLORES["grisel"])
        marco_botones.pack(fill="x", padx=12, pady=(10,12))
        tk.Button(marco_botones, text="▦ VER REPORTE", command=self.generar_reporte,
                 bg=COLORES["especial"], fg="white", font=FUENTES["etiqueta"],
                 padx=15, pady=8, relief="flat", cursor="hand2",
                 activebackground=COLORES["especial"]).pack(side="left", padx=5)
        tk.Button(marco_botones, text="◎ REFRESCAR", command=self.actualizar_inventario,
                 bg=COLORES["trabajo"], fg="white", font=FUENTES["etiqueta"],
                 padx=15, pady=8, relief="flat", cursor="hand2",
                 activebackground=COLORES["trabajo"]).pack(side="left", padx=5)
        
        self.actualizar_inventario()
    
    def crear_seccion_crear(self, parent):
        parent.config(bg=COLORES["fondo"])
        tk.Label(parent, text="▶ Crea un nuevo producto", font=FUENTES["titulo"],
                bg=COLORES["fondo"], fg=COLORES["texto"]).pack(pady=(15,15))
        marco = tk.Frame(parent, bg=COLORES["fondo"], relief="solid", bd=1)
        marco.pack(fill="x", padx=20, pady=10)
        tk.Label(marco, text="► Nombre:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=0, column=0, sticky="w", padx=15, pady=10)
        self.entry_nombre_prod = tk.Entry(marco, width=35, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_nombre_prod.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Label(marco, text="◈ Precio ($):", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=1, column=0, sticky="w", padx=15, pady=10)
        self.entry_precio_prod = tk.Entry(marco, width=35, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_precio_prod.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        tk.Label(marco, text="◻ Cantidad:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=2, column=0, sticky="w", padx=15, pady=10)
        self.entry_cantidad_prod = tk.Entry(marco, width=35, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_cantidad_prod.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        marco.columnconfigure(1, weight=1)
        tk.Button(parent, text="✓ CREAR", command=self.crear_producto, bg=COLORES["exito"],
                 fg="white", font=FUENTES["etiqueta"], padx=25, pady=12, relief="flat",
                 cursor="hand2", activebackground=COLORES["exito"]).pack(pady=20)
        tk.Label(parent, text="► Resultado:", font=FUENTES["ayuda"], bg=COLORES["fondo"], fg=COLORES["grisT"]).pack(pady=(20,5))
        self.text_resultado_crear = tk.Text(parent, height=6, width=90, font=FUENTES["monoesp"],
                                            bg=COLORES["fondo_entrada"], fg=COLORES["texto"], relief="solid", bd=1)
        self.text_resultado_crear.pack(fill="both", expand=True, padx=20, pady=5)
    
    def crear_seccion_ventas(self, parent):
        parent.config(bg=COLORES["fondo"])
        tk.Label(parent, text="▶ Vender producto", font=FUENTES["titulo"],
                bg=COLORES["fondo"], fg=COLORES["texto"]).pack(pady=(15,15))
        marco = tk.Frame(parent, bg=COLORES["fondo"], relief="solid", bd=1)
        marco.pack(fill="x", padx=20, pady=10)
        tk.Label(marco, text="⊕ ID:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=0, column=0, sticky="w", padx=15, pady=10)
        self.entry_id_venta = tk.Entry(marco, width=25, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_id_venta.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Label(marco, text="▦ Cantidad:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=1, column=0, sticky="w", padx=15, pady=10)
        self.entry_cantidad_venta = tk.Entry(marco, width=25, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_cantidad_venta.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        marco.columnconfigure(1, weight=1)
        tk.Button(parent, text="✓ VENDER", command=self.realizar_venta, bg=COLORES["info"],
                 fg="white", font=FUENTES["etiqueta"], padx=25, pady=12, relief="flat",
                 cursor="hand2", activebackground=COLORES["info"]).pack(pady=20)
        tk.Label(parent, text="► Resultado:", font=FUENTES["ayuda"], bg=COLORES["fondo"], fg=COLORES["grisT"]).pack(pady=(20,5))
        self.text_resultado_venta = tk.Text(parent, height=6, width=90, font=FUENTES["monoesp"],
                                            bg=COLORES["fondo_entrada"], fg=COLORES["texto"], relief="solid", bd=1)
        self.text_resultado_venta.pack(fill="both", expand=True, padx=20, pady=5)
    
    def crear_seccion_stock(self, parent):
        parent.config(bg=COLORES["fondo"])
        tk.Label(parent, text="▶ Modificar stock", font=FUENTES["titulo"],
                bg=COLORES["fondo"], fg=COLORES["texto"]).pack(pady=(15,15))
        marco = tk.Frame(parent, bg=COLORES["fondo"], relief="solid", bd=1)
        marco.pack(fill="x", padx=20, pady=10)
        tk.Label(marco, text="⊕ ID:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=0, column=0, sticky="w", padx=15, pady=10)
        self.entry_id_stock = tk.Entry(marco, width=25, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_id_stock.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Label(marco, text="◈ Cambio:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=1, column=0, sticky="w", padx=15, pady=10)
        self.entry_cantidad_stock = tk.Entry(marco, width=25, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_cantidad_stock.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        marco.columnconfigure(1, weight=1)
        tk.Button(parent, text="✓ ACTUALIZAR", command=self.actualizar_stock, bg=COLORES["trabajo"],
                 fg="white", font=FUENTES["etiqueta"], padx=25, pady=12, relief="flat",
                 cursor="hand2", activebackground=COLORES["trabajo"]).pack(pady=20)
        tk.Label(parent, text="► Resultado:", font=FUENTES["ayuda"], bg=COLORES["fondo"], fg=COLORES["grisT"]).pack(pady=(20,5))
        self.text_resultado_stock = tk.Text(parent, height=6, width=90, font=FUENTES["monoesp"],
                                            bg=COLORES["fondo_entrada"], fg=COLORES["texto"], relief="solid", bd=1)
        self.text_resultado_stock.pack(fill="both", expand=True, padx=20, pady=5)
    
    def crear_seccion_descuentos(self, parent):
        parent.config(bg=COLORES["fondo"])
        tk.Label(parent, text="▶ Gestionar descuentos", font=FUENTES["titulo"],
                bg=COLORES["fondo"], fg=COLORES["texto"]).pack(pady=(15,15))
        marco = tk.Frame(parent, bg=COLORES["fondo"], relief="solid", bd=1)
        marco.pack(fill="x", padx=20, pady=10)
        tk.Label(marco, text="⊕ ID:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=0, column=0, sticky="w", padx=15, pady=10)
        self.entry_id_desc = tk.Entry(marco, width=25, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_id_desc.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Label(marco, text="▣ %:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=1, column=0, sticky="w", padx=15, pady=10)
        self.entry_porcentaje = tk.Entry(marco, width=25, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_porcentaje.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        marco.columnconfigure(1, weight=1)
        mb = tk.Frame(parent, bg=COLORES["fondo"])
        mb.pack(fill="x", padx=20, pady=15)
        tk.Button(mb, text="✓ APLICAR", command=self.aplicar_descuento, bg=COLORES["advertencia"],
                 fg="white", font=FUENTES["etiqueta"], padx=20, pady=10, relief="flat",
                 cursor="hand2", activebackground=COLORES["advertencia"]).pack(side="left", padx=5)
        tk.Button(mb, text="↩ QUITAR", command=self.quitar_descuento, bg=COLORES["error"],
                 fg="white", font=FUENTES["etiqueta"], padx=20, pady=10, relief="flat",
                 cursor="hand2", activebackground=COLORES["error"]).pack(side="left", padx=5)
        tk.Label(parent, text="► Resultado:", font=FUENTES["ayuda"], bg=COLORES["fondo"], fg=COLORES["grisT"]).pack(pady=(20,5))
        self.text_resultado_desc = tk.Text(parent, height=6, width=90, font=FUENTES["monoesp"],
                                           bg=COLORES["fondo_entrada"], fg=COLORES["texto"], relief="solid", bd=1)
        self.text_resultado_desc.pack(fill="both", expand=True, padx=20, pady=5)
    
    def crear_seccion_busqueda(self, parent):
        parent.config(bg=COLORES["fondo"])
        tk.Label(parent, text="▶ Buscar/Eliminar", font=FUENTES["titulo"],
                bg=COLORES["fondo"], fg=COLORES["texto"]).pack(pady=(15,15))
        mb = tk.Frame(parent, bg=COLORES["fondo"], relief="solid", bd=1)
        mb.pack(fill="x", padx=20, pady=10)
        tk.Label(mb, text="◉ Nombre:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=0, column=0, sticky="w", padx=15, pady=10)
        self.entry_buscar = tk.Entry(mb, width=25, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_buscar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Button(mb, text="🔍 BUSCAR", command=self.buscar_producto, bg=COLORES["info"],
                 fg="white", font=FUENTES["etiqueta"], padx=15, pady=8, relief="flat",
                 cursor="hand2", activebackground=COLORES["info"]).grid(row=0, column=2, padx=10, pady=10)
        mb.columnconfigure(1, weight=1)
        me = tk.Frame(parent, bg=COLORES["fondo"], relief="solid", bd=1)
        me.pack(fill="x", padx=20, pady=10)
        tk.Label(me, text="▼ ID:", font=FUENTES["etiqueta"], bg=COLORES["fondo"], fg=COLORES["texto"]).grid(row=0, column=0, sticky="w", padx=15, pady=10)
        self.entry_id_elim = tk.Entry(me, width=25, font=FUENTES["normal"], relief="solid", bd=1)
        self.entry_id_elim.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Button(me, text="⚠️ ELIMINAR", command=self.eliminar_producto, bg=COLORES["error"],
                 fg="white", font=FUENTES["etiqueta"], padx=15, pady=8, relief="flat",
                 cursor="hand2", activebackground=COLORES["error"]).grid(row=0, column=2, padx=10, pady=10)
        me.columnconfigure(1, weight=1)
        tk.Label(parent, text="► Resultado:", font=FUENTES["ayuda"], bg=COLORES["fondo"], fg=COLORES["grisT"]).pack(pady=(20,5))
        self.text_resultado_busqueda = tk.Text(parent, height=6, width=90, font=FUENTES["monoesp"],
                                              bg=COLORES["fondo_entrada"], fg=COLORES["texto"], relief="solid", bd=1)
        self.text_resultado_busqueda.pack(fill="both", expand=True, padx=20, pady=5)
    
    def actualizar_inventario(self):
        self.text_inventario.delete("1.0", tk.END)
        self.text_inventario.insert(tk.END, self.almacen.listar_productos())
        v = self.almacen.valor_total_almacen()
        c = len(self.almacen.productos)
        d = self.almacen.dinero_vendido
        self.label_valor_total.config(text=f"◈ Valor Total: ${v:,.2f}")
        self.label_cantidad_productos.config(text=f"◻ Total: {c}")
        self.label_dinero_vendido.config(text=f"◉ Dinero Vendido: ${d:,.2f}")
    
    def crear_producto(self):
        try:
            n = self.entry_nombre_prod.get().strip()
            p = float(self.entry_precio_prod.get())
            c = int(self.entry_cantidad_prod.get())
            ok, msg = self.almacen.crear_producto(n, p, c)
            self.mostrar_resultado(self.text_resultado_crear, msg)
            if ok:
                messagebox.showinfo("✅", msg)
                self.entry_nombre_prod.delete(0, tk.END)
                self.entry_precio_prod.delete(0, tk.END)
                self.entry_cantidad_prod.delete(0, tk.END)
            else:
                messagebox.showerror("❌", msg)
            self.actualizar_inventario()
        except ValueError:
            msg = "❌ Valores inválidos"
            self.mostrar_resultado(self.text_resultado_crear, msg)
            messagebox.showerror("❌", msg)
    
    def realizar_venta(self):
        try:
            id_p = int(self.entry_id_venta.get())
            cant = int(self.entry_cantidad_venta.get())
            if cant <= 0:
                raise ValueError("Cantidad > 0")
            ok, msg, tot = self.almacen.vender(id_p, cant)
            self.mostrar_resultado(self.text_resultado_venta, msg)
            if ok:
                messagebox.showinfo("✅", f"Venta: ${tot:.2f}")
                self.entry_id_venta.delete(0, tk.END)
                self.entry_cantidad_venta.delete(0, tk.END)
            else:
                messagebox.showerror("❌", msg)
            self.actualizar_inventario()
        except ValueError:
            msg = "❌ Valores inválidos"
            self.mostrar_resultado(self.text_resultado_venta, msg)
            messagebox.showerror("❌", msg)
    
    def actualizar_stock(self):
        try:
            id_p = int(self.entry_id_stock.get())
            cant = int(self.entry_cantidad_stock.get())
            msg = self.almacen.actualizar_stock(id_p, cant)
            self.mostrar_resultado(self.text_resultado_stock, msg)
            if "✓" in msg:
                messagebox.showinfo("✅", msg)
                self.entry_id_stock.delete(0, tk.END)
                self.entry_cantidad_stock.delete(0, tk.END)
            else:
                messagebox.showerror("❌", msg)
            self.actualizar_inventario()
        except ValueError:
            msg = "❌ Valores inválidos"
            self.mostrar_resultado(self.text_resultado_stock, msg)
            messagebox.showerror("❌", msg)
    
    def aplicar_descuento(self):
        try:
            id_p = int(self.entry_id_desc.get())
            porc = float(self.entry_porcentaje.get())
            if not (0 <= porc <= 100):
                raise ValueError("0-100")
            msg = self.almacen.aplicar_descuento(id_p, porc)
            self.mostrar_resultado(self.text_resultado_desc, msg)
            if "✓" in msg:
                messagebox.showinfo("✅", msg)
                self.entry_id_desc.delete(0, tk.END)
                self.entry_porcentaje.delete(0, tk.END)
            else:
                messagebox.showerror("❌", msg)
            self.actualizar_inventario()
        except ValueError:
            msg = "❌ Valores inválidos"
            self.mostrar_resultado(self.text_resultado_desc, msg)
            messagebox.showerror("❌", msg)
    
    def quitar_descuento(self):
        try:
            id_p = int(self.entry_id_desc.get())
            msg = self.almacen.resetear_descuento(id_p)
            self.mostrar_resultado(self.text_resultado_desc, msg)
            if "✓" in msg:
                messagebox.showinfo("✅", msg)
                self.entry_id_desc.delete(0, tk.END)
                self.entry_porcentaje.delete(0, tk.END)
            else:
                messagebox.showwarning("⚠️", msg)
            self.actualizar_inventario()
        except ValueError:
            msg = "❌ ID inválido"
            self.mostrar_resultado(self.text_resultado_desc, msg)
            messagebox.showerror("❌", msg)
    
    def buscar_producto(self):
        n = self.entry_buscar.get().strip()
        if not n:
            messagebox.showwarning("⚠️", "Ingresa un nombre")
            return
        enc = self.almacen.buscar_por_nombre(n)
        if enc:
            res = f"✅ {len(enc)} encontrado(s):\n\n" + "\n".join(f"ID: {p.id} | {p.nombre} | ${p.precio:.2f} | {p.cantidad}" for p in enc)
            self.mostrar_resultado(self.text_resultado_busqueda, res)
            messagebox.showinfo("✅", f"{len(enc)} hallado(s)")
        else:
            res = "❌ No encontrado"
            self.mostrar_resultado(self.text_resultado_busqueda, res)
            messagebox.showwarning("⚠️", res)
        self.entry_buscar.delete(0, tk.END)
    
    def eliminar_producto(self):
        try:
            id_p = int(self.entry_id_elim.get())
            prod = self.almacen.buscar_por_id(id_p)
            if not prod:
                msg = "❌ No encontrado"
                self.mostrar_resultado(self.text_resultado_busqueda, msg)
                messagebox.showerror("❌", msg)
                return
            if messagebox.askyesno("⚠️", f"¿Eliminar '{prod.nombre}'?"):
                msg = self.almacen.eliminar_producto(id_p)
                self.mostrar_resultado(self.text_resultado_busqueda, msg)
                messagebox.showinfo("✅", msg)
                self.actualizar_inventario()
            self.entry_id_elim.delete(0, tk.END)
        except ValueError:
            msg = "❌ ID inválido"
            self.mostrar_resultado(self.text_resultado_busqueda, msg)
            messagebox.showerror("❌", msg)
    
    def generar_reporte(self):
        r = "╔════════════════════════════════════╗\n║    REPORTE DEL ALMACÉN\n╚════════════════════════════════════╝\n\n"
        r += f"Total: {len(self.almacen.productos)} | Valor: ${self.almacen.valor_total_almacen():,.2f}\n{'='*60}\n"
        if self.almacen.productos:
            r += f"{'ID':<5} {'Nombre':<20} {'Precio':<12} {'Stock':<8} {'Valor':<12}\n{'-'*60}\n"
            for p in self.almacen.productos:
                r += f"{p.id:<5} {p.nombre:<20} ${p.precio:<11.2f} {p.cantidad:<8} ${p.precio * p.cantidad:<11,.2f}\n"
            r += f"{'='*60}\nTOTAL: ${self.almacen.valor_total_almacen():,.2f}\n"
        else:
            r += "Vacío"
        messagebox.showinfo("▣ REPORTE", r)
    
    def mostrar_ayuda(self):
        a = """╔════════════════════════════════════════╗
║ GUÍA DE GESTIÓN DE ALMACÉN
╚════════════════════════════════════════╝

1. CREAR PRODUCTO
   - Nombre, precio, cantidad inicial
   - ID automático

2. VENDER
   - ID del producto y cantidad
   - Verifica stock

3. STOCK
   - Modifica cantidad (+/-)

4. DESCUENTOS
   - ID y porcentaje
   - Quitar descuento

5. BUSCAR/ELIMINAR
   - Por nombre o ID
   - Con confirmación

BOTONES
   - VER REPORTE
   - REFRESCAR
"""
        messagebox.showinfo("❓ AYUDA", a)

# ============================================================================
# PUNTO DE ENTRADA - Inicio de la aplicación
# ============================================================================
if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazAlmacen(ventana)
    ventana.mainloop()