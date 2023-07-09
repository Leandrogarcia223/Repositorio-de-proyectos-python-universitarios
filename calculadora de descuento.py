#calculadora para descuentos

precio = int (input("precios: "))
cantidad = int(input("cantidad: "))
especial =int(input("oferta especial: "))
subtotal = precio * cantidad
descuento = subtotal * 50.00
especial = subtotal *1.00
total = subtotal - descuento
print("subtotal: ",subtotal)
print("descuento: ",descuento)
print("especial: ",especial)
