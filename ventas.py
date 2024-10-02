from abc import ABC, abstractmethod


class IProducto(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass


class ICalculadoraDeImpuestos(ABC):
    @abstractmethod
    def calcular(self, monto: float) -> float:
        pass


class IDescuento(ABC):
    @abstractmethod
    def aplicar(self, monto: float) -> float:
        pass


class Producto(IProducto):
    def __init__(self, nombre: str, costo: float):
        self.nombre = nombre
        self.costo = costo

    def obtener_precio(self):
        return self.costo

    def obtener_descripcion(self):
        return self.nombre


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: IProducto):
        self.productos.append(producto)
        print(f"{producto.obtener_descripcion()} ha sido agregado correctamente...")

    def eliminar_producto(self, producto: IProducto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"{producto.obtener_descripcion()} ha sido eliminado...")
        else:
            print(f"{producto.obtener_descripcion()} no está en el carrito")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos para mostrar")
        else:
            print("Productos del Carrito:")
            for producto in self.productos:
                print(f"{producto.obtener_descripcion()} - ${producto.obtener_precio():.2f}")

    def calcular_total(self) -> float:
        return sum(producto.obtener_precio() for producto in self.productos)


class DescuentoPorcentaje(IDescuento):
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje

    def aplicar(self, monto: float) -> float:
        return monto * (1 - self.porcentaje / 100)


class CalculadoraImpuestoEstandar(ICalculadoraDeImpuestos):
    def calcular(self, monto: float) -> float:
        return monto * 0.15  # 15% de impuesto


class Usuario:
    def __init__(self, nombre: str, carrito: Carrito):
        self.nombre = nombre
        self.carrito = carrito

    def realizar_compra(
        self, descuento: IDescuento, calculadora_impuestos: ICalculadoraDeImpuestos
    ):
        if not self.carrito.productos:
            print(f"{self.nombre}, tu carrito está vacío.")
        else:
            total = self.carrito.calcular_total()
            print(f"Total antes de descuento e impuestos: ${total:.2f}")

            # Aplicar descuento
            total_con_descuento = descuento.aplicar(total)
            print(f"Total con descuento: ${total_con_descuento:.2f}")

            # Aplicar impuestos
            total_final = total_con_descuento + calculadora_impuestos.calcular(
                total_con_descuento
            )
            print(f"Total con impuestos: ${total_final:.2f}")

            # Completar compra
            self.carrito.productos.clear()
            print("Gracias por tu compra!")


# Crear productos
producto1 = Producto("Laptop", 1000)
producto2 = Producto("Mouse", 50)
producto3 = Producto("Monitor", 75)
producto4 = Producto("CPU", 700)
producto5 = Producto("Memoria", 500)
producto6 = Producto("Procesador", 200)
producto7 = Producto("Disco duro", 150)
producto8 = Producto("Impresora", 500)
producto9 = Producto("Escáner", 200)
producto10 = Producto("Cables", 100)

# Crear carrito y agregar productos
carrito = Carrito()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)
carrito.agregar_producto(producto4)
carrito.agregar_producto(producto5)
carrito.agregar_producto(producto6)
carrito.agregar_producto(producto7)
carrito.agregar_producto(producto8)
carrito.agregar_producto(producto9)
carrito.agregar_producto(producto10)

# Mostrar productos en el carrito
carrito.mostrar_productos()

# Crear usuario y realizar compra
usuario = Usuario("Carlos", carrito)
descuento = DescuentoPorcentaje(10)  # Descuento del 10%
calculadora_impuestos = CalculadoraImpuestoEstandar()
usuario.realizar_compra(descuento, calculadora_impuestos)
