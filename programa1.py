# calcular unidades

    si unidad_origen = "kilogramos" y unidad_destino = "gramos" entonces
        resultado = cantidad * 1000
    sino si unidad_origen = "gramos" y unidad_destino = "kilogramos" entonces
        resultado = cantidad / 1000
    sino si unidad_origen = "metros" y unidad_destino = "centimetros" entonces
        resultado = cantidad * 100
    sino si unidad_origen = "centimetros" y unidad_destino = "metros" entonces
        resultado = cantidad / 100
    sino
        mostrar "No se puede realizar la conversión"
    
