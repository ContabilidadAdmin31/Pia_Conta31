from os import system, name

def borrar():
  if name == "nt":
    system("cls")
  else:
    system("clear")


respuestaMenu = 0


while respuestaMenu != 13:
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
    
    respuestaMenu = int(input('Seleccione una opcion del MENU: '))
    print(' ')
    if respuestaMenu == 1:
        print('Selecccionó Presupuesto de Ventas')
         #ProductoD
        unidades_d=int(input('Ingresa las unidades a vender del producto D en el primer semestre: '))
        preciov_d=int(input("Ingresa el precio venta de las unidades del primer semestre: "))
        importe1sem_d= unidades_d*preciov_d
        print(f"\nEl importe de venta del primer semestre es de: {importe1sem_d}")
        unidades_d2=int(input('Ingresa las unidades a vender del producto D en el segundo semestre: '))
        preciov_d2=int(input("Ingresa el precio venta de las unidades del segundo semestre: "))
        importe2sem_d= unidades_d2*preciov_d2
        print(f"\nEl importe de venta del segundo semestre es de: {importe2sem_d}")
        total_prod_d = (importe1sem_d + importe2sem_d)
        print(f"\nEl importe total del 2009 del producto D es de {total_prod_d}")

        #Producto Di
        unidades_di=int(input('Ingresa las unidades a vender del producto Di en el primer semestre: '))
        preciov_di=int(input("Ingresa el precio venta de las unidades del primer semestre: "))
        importe1sem_di= unidades_di*preciov_di
        print(f"\nEl importe de venta del primer semestre es de: {importe1sem_di}")
        unidades_di2=int(input('Ingresa las unidades a vender del producto Di en el segundo semestre: '))
        preciov_di2=int(input("Ingresa el precio venta de las unidades del segundo semestre: "))
        importe2sem_di= unidades_di2*preciov_di2
        print(f"\nEl importe de venta del segundo semestre es de: {importe2sem_di}")
        total_prod_di = (importe1sem_di + importe2sem_di)
        print(f"\nEl importe total del 2009 del producto Di es de {total_prod_di}")

        #Producto Z
        unidades_z=int(input('Ingresa las unidades a vender del producto Z en el primer semestre: '))
        preciov_z=int(input("Ingresa el precio venta de las unidades del primer semestre: "))
        importe1sem_z= unidades_z*preciov_z
        print(f"\nEl importe de venta del primer semestre es de: {importe1sem_z}")
        unidades_z2=int(input('Ingresa las unidades a vender del producto Z en el segundo semestre: '))
        preciov_z2=int(input("Ingresa el precio venta de las unidades del segundo semestre: "))
        importe2sem_z= unidades_z2*preciov_z2
        print(f"\nEl importe de venta del segundo semestre es de: {importe2sem_z}")
        total_prod_z = (importe1sem_z + importe2sem_z)
        print(f"\nEl importe total del 2009 del producto Z es de {total_prod_z}")

        #Total 2009 3 productos
        ventas_2009 = (total_prod_d + total_prod_di + total_prod_z)
        print(f"\nEl total del 2009 por los 3 productos es de {ventas_2009}")

        input("Presione enter para continuar...")
        borrar()

    elif respuestaMenu == 2:
        print('Selecccionó la Determinación del saldo de Clientes y Flujo de Entradas ')
        print(' ')
        saldo_clientes_2008 = int(input("\nIngrese el saldo de clientes al 31 de Diciembre de 2008: "))
        total_clientes_2009 = (saldo_clientes_2008 + ventas_2009)
        print(f"\nTotal de clientes 2009: {total_clientes_2009}")

        print("\n Entradas de efectivo")
        por_cobranza_2008 = int(input("\nIngrese cobranza del 2008: "))
        por_cobranza_2009 = (ventas_2009 * 0.9)
        total_entradas_2009 = (por_cobranza_2008 + por_cobranza_2009)

        saldo_clientes_2009 = (total_clientes_2009 - total_entradas_2009)
        print(f"\nEl saldo de clientes del 2009 es: {saldo_clientes_2009}")

        input("Presione enter para continuar...")
        borrar()


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
    
print('Adiós ')
