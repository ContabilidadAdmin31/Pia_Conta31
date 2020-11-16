totald_2009=[]
respuestaMenu = 0

print('Bienvenido al Programa de Presupuesto Maestro')
print('1. Presupuesto de Ventas')
print('2. Determinación del saldo de Clientes y Flujo de Entradas ')
print('3. Prespuesto de Producción')
print('4. Presupuesto de Requerimento de Materiales')
print('5. Presupuesto de Compra de Materiales')
print('6. Determinacion del saldo de Proveedores y Flujo de Salidas')
print('7. Presupuesto de Mano de Obra  Directa')
print('8. Presupuesto de Gastos Indirectos de Fabricación')
print('9. Presupuesto de Gastos de Operación')
print('10. Determinación de Costo Unitario de Productos Terminados')
print('11. Valuación de Inventarios Finales')
print('12. Presupuesto Financiero')
print('13. Salir')
print(' ')
while respuestaMenu != 13:
    respuestaMenu = int(input('Seleccione una opcion del MENU: '))
    print(' ')
    if respuestaMenu == 1:
        print('Seleccciono Presupuesto de Ventas')
         #ProductoD
        unidades_d=int(input('Ingresa las unidades a vender del producto D en el primer semestre: '))
        preciov_d=int(input("Ingresa el precio venta de las unidades del primer semestre: "))
        importe1sem= unidades_d*preciov_d
        print(f"El importe de venta del primer semestre es de: {importe1sem}")
        totald_2009.append(importe1sem)
        unidades_d2=int(input('Ingresa las unidades a vender del producto D en el segundo semestre: '))
        preciov_d2=int(input("Ingresa el precio venta de las unidades del segundo semestre: "))
        importe2sem= unidades_d2*preciov_d2
        print(f"El importe de venta del segundo semestre es de: {importe2sem}")
        totald_2009.append(importe2sem)
        total=sum(totald_2009)
        print(f"El importe total del 2009 es de {total}")

    elif respuestaMenu == 2:
        print('Seleccciono la Determinación del saldo de Clientes y Flujo de Entradas ')
        print(' ')

    elif respuestaMenu == 3:
        print('Seleccciono Prespuesto de Producción ')
        print(' ')

    elif respuestaMenu == 4:
        print('Seleccciono Presupuesto de Requerimento de Materiales ')
        print(' ')


    elif respuestaMenu == 5:
        print('Seleccciono Presupuesto de Compra de Materiales')
        print(' ')


    elif respuestaMenu == 6:
        print('Seleccciono Determinacion del saldo de Proveedores y Flujo de Salidas ')
        print(' ')


    elif respuestaMenu == 7:
        print('Seleccciono Presupuesto de Mano de Obra  Directa')
        print(' ')


    elif respuestaMenu == 8:
        print('Seleccciono Presupuesto de Gastos Indirectos de Fabricación ')
        print(' ')


    elif respuestaMenu == 9:
        print('Seleccciono Presupuesto de Gastos de Operación ')
        print(' ')


    elif respuestaMenu == 10:
        print('Seleccciono Determinación de Costo Unitario de Productos Terminados')
        print(' ')


    elif respuestaMenu == 11:
        print('Seleccciono Valuación de Inventarios Finales')
        print(' ')


    elif respuestaMenu == 12:
        print('Seleccciono Presupuesto Financiero ')
        print(' ')
    
print('Adios ')
