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

        input("Presione enter para continuar...")
        borrar()

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

        input("Presione enter para continuar...")
        borrar()

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

        input("Presione enter para continuar...")
        borrar()

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
        print('Selecccionó Prespuesto de Producción ')
        print(' ')
        #Producto D 1 Semestre
        inventario_final_d_1sem = int(input("Ingresar inventario final del producto D del 1 Semestre: "))
        total_unidades_d_1sem = (unidades_d + inventario_final_d_1sem)
        inventario_inicial_d_1sem = int(input("Ingresar inventario inicial del producto D del 1 Semestre: "))
        unidades_a_producir_d_1sem = (total_unidades_d_1sem - inventario_inicial_d_1sem)
        print(f"Unidades a producir del producto D del 1er. Semestre: {unidades_a_producir_d_1sem}")

        input("Presione enter para continuar...")
        borrar()

        #Producto D 2 Semestre
        inventario_final_d_2sem = int(input("Ingresar inventario final del producto D del 2 Semestre: "))
        total_unidades_d_2sem = (unidades_d2 + inventario_final_d_2sem)
        inventario_inicial_d_2sem = inventario_final_d_1sem
        unidades_a_producir_d_2sem = (total_unidades_d_2sem - inventario_inicial_d_2sem)
        print(f"Unidades a producir del producto D del 2 Semestre: {unidades_a_producir_d_2sem}")

        input("Presione enter para continuar...")
        borrar()

        #Totales 2009 Producto D
        unidades_2009_d = (unidades_d + unidades_d2)
        inventario_final_2009_d = inventario_final_d_2sem
        total_unidades_2009_d = (unidades_2009_d + inventario_final_2009_d)
        inventario_inicial_2009_d = inventario_inicial_d_1sem
        unidades_a_producir_2009_d = (total_unidades_2009_d - inventario_inicial_2009_d)
        print("Totales 2009, Producto D\n")
        print(f"Las unidades a vender son: {unidades_2009_d}\nEl inventario final es: {inventario_final_2009_d}\nEl total de unidades es: {total_unidades_2009_d}\nEl inventario inicial es: {inventario_inicial_2009_d}\nLas unidades a producir son: {unidades_a_producir_2009_d}")

        input("Presione enter para continuar...")
        borrar()


        #Producto Di 1 Semestre
        inventario_final_di_1sem = int(input("Ingresar inventario final del producto Di del 1 Semestre: "))
        total_unidades_di_1sem = (unidades_di + inventario_final_di_1sem)
        inventario_inicial_di_1sem = int(input("Ingresar inventario inicial del producto Di del 1 Semestre: "))
        unidades_a_producir_di_1sem = (total_unidades_di_1sem - inventario_inicial_di_1sem)
        print(f"Unidades a producir del producto Di del 1er. Semestre: {unidades_a_producir_di_1sem}")

        input("Presione enter para continuar...")
        borrar()

        #Producto Di 2 Semestre
        inventario_final_di_2sem = int(input("Ingresar inventario final del producto Di del 2 Semestre: "))
        total_unidades_di_2sem = (unidades_di2 + inventario_final_di_2sem)
        inventario_inicial_di_2sem = inventario_final_di_1sem
        unidades_a_producir_di_2sem = (total_unidades_di_2sem - inventario_inicial_di_2sem)
        print(f"Unidades a producir del producto Di del 2 Semestre: {unidades_a_producir_di_2sem}")

        input("Presione enter para continuar...")
        borrar()

        #Totales 2009 Producto Di
        unidades_2009_di = (unidades_di + unidades_di2)
        inventario_final_2009_di = inventario_final_di_2sem
        total_unidades_2009_di = (unidades_2009_di + inventario_final_2009_di)
        inventario_inicial_2009_di = inventario_inicial_di_1sem
        unidades_a_producir_2009_di = (total_unidades_2009_di - inventario_inicial_2009_di)
        print("Totales 2009, Producto Di\n")
        print(f"Las unidades a vender son: {unidades_2009_di}\nEl inventario final es: {inventario_final_2009_di}\nEl total de unidades es: {total_unidades_2009_di}\nEl inventario inicial es: {inventario_inicial_2009_di}\nLas unidades a producir son: {unidades_a_producir_2009_di}")

        input("Presione enter para continuar...")
        borrar()


        #Producto Z 1 Semestre
        inventario_final_z_1sem = int(input("Ingresar inventario final del producto Z del 1 Semestre: "))
        total_unidades_z_1sem = (unidades_z + inventario_final_z_1sem)
        inventario_inicial_z_1sem = int(input("Ingresar inventario inicial del producto Z del 1 Semestre: "))
        unidades_a_producir_z_1sem = (total_unidades_z_1sem - inventario_inicial_z_1sem)
        print(f"Unidades a producir del producto Z del 1er. Semestre: {unidades_a_producir_z_1sem}")

        input("Presione enter para continuar...")
        borrar()

        #Producto Z 2 Semestre
        inventario_final_z_2sem = int(input("Ingresar inventario final del producto Z del 2 Semestre: "))
        total_unidades_z_2sem = (unidades_z2 + inventario_final_z_2sem)
        inventario_inicial_z_2sem = inventario_final_z_1sem
        unidades_a_producir_z_2sem = (total_unidades_z_2sem - inventario_inicial_z_2sem)
        print(f"Unidades a producir del producto Z del 2 Semestre: {unidades_a_producir_z_2sem}")

        input("Presione enter para continuar...")
        borrar()

        #Totales 2009 Producto Z
        unidades_2009_z = (unidades_z + unidades_z2)
        inventario_final_2009_z = inventario_final_z_2sem
        total_unidades_2009_z = (unidades_2009_z + inventario_final_2009_z)
        inventario_inicial_2009_z = inventario_inicial_z_1sem
        unidades_a_producir_2009_z = (total_unidades_2009_z - inventario_inicial_2009_z)
        print("Totales 2009, Producto Z\n")
        print(f"Las unidades a vender son: {unidades_2009_z}\nEl inventario final es: {inventario_final_2009_z}\nEl total de unidades es: {total_unidades_2009_z}\nEl inventario inicial es: {inventario_inicial_2009_z}\nLas unidades a producir son: {unidades_a_producir_2009_z}")

        input("Presione enter para continuar...")
        borrar()

    elif respuestaMenu == 4:
        print('Selecccionó Presupuesto de Requerimento de Materiales \n')
        unidadesd = unidades_a_producir_d_1sem
        unidadesd2 = unidades_a_producir_d_2sem
        totalunidadesd= unidadesd+unidadesd2
        #Material A Producto D
        print("PRODUCTO D\n")
        mad=int(input("Ingrese el requerimiento de material A del primer semestre: "))
        mad2=int(input("ingrese el requerimiento de material A del segundo semestre: "))
        totalma1=  unidadesd*mad
        print(f"El material A requerido del primer semestre del producto D es de: {totalma1}")
        totalma2= unidadesd2*mad2
        print(f"El material A requerido del segundo semestre del producto D es de: {totalma2}")

        input("Presione enter para continuar...")
        borrar()
        
        #Material B Producto D
        print("PRODUCTO D\n")
        mbd=int(input("Ingrese el requerimiento de material B del primer semestre: "))
        mbd2=int(input("Ingrese el requerimiento de material B del segundo semestre: "))
        totalmb1=  unidadesd*mbd
        print(f"El material B requerido del primer semestre del producto D es de: {totalmb1}")
        totalmb2= unidadesd2*mbd2
        print(f"El material B requerido del segundo semestre del producto D es de: {totalmb2}")

        input("Presione enter para continuar...")
        borrar()
        
        #Material C Producto D
        print("PRODUCTO D\n")
        mcd=int(input("Ingrese el requerimiento de material C del primer semestre: "))
        mcd2=int(input("Ingrese el requerimiento de material C del segundo semestre: "))
        totalmc1=  unidadesd*mcd
        print(f"El material C requerido del primer semestre del producto D es de: {totalmc1}")
        totalmc2= unidadesd2*mcd2
        print(f"El material C requerido del segundo semestre del producto D es de: {totalmc2}")

        input("Presione enter para continuar...")
        borrar()
        
        print("PRODUCTO D\n")
        totala2009d= totalunidadesd*mad
        print(f"Total de material A requerido del producto D es de: {totala2009d}")
        totalb2009d= totalunidadesd*mbd
        print(f"Total de material B requerido del producto D es de: {totalb2009d}")
        totalc2009d= totalunidadesd*mcd
        print(f"Total de material C requerido del producto D es de: {totalc2009d}")

        input("Presione enter para continuar...")
        borrar()
        
        #Producto Di
        unidadesdi = unidades_a_producir_di_1sem
        unidadesdi2 = unidades_a_producir_di_2sem
        totalunidadesdi= unidadesdi+unidadesdi2
        #Material A Producto Di
        print("PRODUCTO Di\n")
        madi=int(input("Ingrese el requerimiento de material A del primer semestre: "))
        madi2=int(input("Ingrese el requerimiento de material A del segundo semestre: "))
        totalma1di=  unidadesdi*madi
        print(f"El material A requerido del primer semestre del producto Di es de: {totalma1di}")
        totalma2di= unidadesdi2*madi2
        print(f"El material A requerido del segundo semestre del producto Di es de: {totalma2di}")

        input("Presione enter para continuar...")
        borrar()
        
        #Material B Producto Di
        print("PRODUCTO Di\n")
        mbdi=int(input("Ingrese el requerimiento de material B del primer semestre: "))
        mbdi2=int(input("Ingrese el requerimiento de material B del segundo semestre: "))
        totalmb1di=  unidadesdi*mbdi
        print(f"El material B requerido del primer semestre del producto Di es de: {totalmb1di}")
        totalmb2di= unidadesdi2*mbdi2
        print(f"El material B requerido del segundo semestre del producto Di es de: {totalmb2di}")

        input("Presione enter para continuar...")
        borrar()
        
        #Material C Producto Di
        print("PRODUCTO Di\n")
        mcdi=int(input("Ingrese el requerimiento de material C del primer semestre: "))
        mcdi2=int(input("Ingrese el requerimiento de material C del segundo semestre: "))
        totalmc1di=  unidadesdi*mcdi
        print(f"El material C requerido del primer semestre del producto Di es de: {totalmc1di}")
        totalmc2di= unidadesdi2*mcdi2
        print(f"El material C requerido del segundo semestre del producto Di es de: {totalmc2di}")

        input("Presione enter para continuar...")
        borrar()
        
        print("PRODUCTO Di\n")
        totala2009di= totalunidadesdi*madi
        print(f"Total de material A requerido del producto Di es de: {totala2009di}")
        totalb2009di= totalunidadesdi*mbdi
        print(f"Total de material B requerido del producto Di es de: {totalb2009di}")
        totalc2009di= totalunidadesdi*mcdi
        print(f"Total de material C requerido del producto Di es de: {totalc2009di}")

        input("Presione enter para continuar...")
        borrar()
        
        #Producto Z
        unidadesz=unidades_a_producir_z_1sem
        unidadesz2=unidades_a_producir_z_2sem
        totalunidadesz= unidadesz+unidadesz2
        #Material A Producto Z
        print("PRODUCTO Z\n")
        maz=int(input("Ingrese el requerimiento de material A del primer semestre: "))
        maz2=int(input("ingrese el requerimiento de material A del segundo semestre: "))
        totalma1z=  unidadesz*maz
        print(f"El material A requerido del primer semestre del producto Z es de: {totalma1z}")
        totalma2z= unidadesz2*maz2
        print(f"El material A requerido del segundo semestre del producto Z es de: {totalma2z}")

        input("Presione enter para continuar...")
        borrar()
        
        #Material B Producto Z
        print("PRODUCTO Z\n")
        mbz=int(input("Ingrese el requerimiento de material B del primer semestre: "))
        mbz2=int(input("Ingrese el requerimiento de material B del segundo semestre: "))
        totalmb1z=  unidadesz*mbz
        print(f"El material B requerido del primer semestre del producto Z es de: {totalmb1z}")
        totalmb2z= unidadesz2*mbz2
        print(f"El material B requerido del segundo semestre del producto Z es de: {totalmb2z}")

        input("Presione enter para continuar...")
        borrar()
        
        #Material C Producto Z
        print("PRODUCTO Z\n")
        mcz=int(input("ingrese el requerimiento de material C del primer semestre: "))
        mcz2=int(input("ingrese el requerimiento de material C del segundo semestre: "))
        totalmc1z=  unidadesz*mcz
        print(f"El material C requerido del primer semestre del producto Z es de: {totalmc1z}")
        totalmc2z= unidadesz2*mcz2
        print(f"El material C requerido del segundo semestre del producto Z es de: {totalmc2z}")

        input("Presione enter para continuar...")
        borrar()
        
        print("PRODUCTO Z\n")
        totala2009z= totalunidadesz*maz
        print(f"Total de material A requerido del producto Z es de: {totala2009z}")
        totalb2009z= totalunidadesz*mbz
        print(f"Total de material B requerido del producto Z es de: {totalb2009z}")
        totalc2009z= totalunidadesz*mcz
        print(f"Total de material C requerido del producto Z es de: {totalc2009z}")

        input("Presione enter para continuar...")
        borrar()

        print("TOTAL DE REQUERIMIENTOS producto A (gramos)")
        total_req_a_1sem = (totalma1 + totalma1di + totalma1z)
        total_req_b_1sem = (totalmb1 + totalmb1di + totalmb1z)
        total_req_c_1sem = (totalmc1 + totalmc1di + totalmc1z)
        print("\nPRIMER SEMESTRE")
        print(f"Material A: {total_req_a_1sem}\nMaterial B: {total_req_b_1sem}\nMaterial C: {total_req_c_1sem}")

        total_req_a_2sem = (totalma2 + totalma2di + totalma2z)
        total_req_b_2sem = (totalmb2 + totalmb2di + totalmb2z)
        total_req_c_2sem = (totalmc2 + totalmc2di + totalmc2z)
        print("\nSEGUNDO SEMESTRE")
        print(f"Material A: {total_req_a_2sem}\nMaterial B: {total_req_b_2sem}\nMaterial C: {total_req_c_2sem}")

        total_req_a_2009 = (totala2009d + totala2009di + totala2009z)
        total_req_b_2009 = (totalb2009d + totalb2009di + totalb2009z)
        total_req_c_2009 = (totalc2009d + totalc2009di + totalc2009z)
        print("\nTOTAL 2009")
        print(f"Material A: {total_req_a_2009}\nMaterial B: {total_req_b_2009}\nMaterial C: {total_req_c_2009}")

        input("Presione enter para continuar...")
        borrar()
        
    elif respuestaMenu == 5:
        print('Selecccionó Presupuesto de Compra de Materiales\n')
        print(' ')
        #material a 1 semestre
        print("Material A, 1 semestre")
        req_mat_a_1 = total_req_a_1sem
        inv_final_a_1 = int(input("Ingrese inventario final: "))
        total_materiales_a_1 = (req_mat_a_1 + inv_final_a_1)
        print(f"El total de materiales es de {total_materiales_a_1}")
        inv_inicial_a_1 = int(input("Ingrese inventario inicial: "))
        material_comprar_a_1 = (total_materiales_a_1 - inv_inicial_a_1)
        precio_compra_a_1 = int(input("Ingrese precio de compra: "))
        total_material_a_1_pesos = (material_comprar_a_1 * precio_compra_a_1)
        print(f"El Total de material A del semestre 1 en $ es: ${total_material_a_1_pesos}")

        input("Presione enter para continuar...")
        borrar()

        #material a 2 semestre
        print("Material A, 2 semestre")
        req_mat_a_2 = total_req_a_2sem
        inv_final_a_2 = int(input("Ingrese inventario final: "))
        total_materiales_a_2 = (req_mat_a_2 + inv_final_a_2)
        print(f"El total de materiales es de {total_materiales_a_2}")
        inv_inicial_a_2 = int(input("Ingrese inventario inicial: "))
        material_comprar_a_2 = (total_materiales_a_2 - inv_inicial_a_2)
        precio_compra_a_2 = int(input("Ingrese precio de compra: "))
        total_material_a_2_pesos = (material_comprar_a_2 * precio_compra_a_2)
        print(f"El Total de material A del semestre 2 en $ es: ${total_material_a_2_pesos}")

        input("Presione enter para continuar...")
        borrar()


        #material a total 2009
        print("Material A, Total 2009")
        req_mat_a_2009 = total_req_a_2009
        inv_final_a_2009 = int(input("Ingrese inventario final: "))
        total_materiales_a_2009 = (req_mat_a_2009 + inv_final_a_2009)
        print(f"El total de materiales es de {total_materiales_a_2009}")
        inv_inicial_a_2009 = int(input("Ingrese inventario inicial: "))
        material_comprar_a_2009 = (total_materiales_a_2009 - inv_inicial_a_2009)
        precio_compra_a_2009 = int(input("Ingrese precio de compra: "))
        total_material_a_2009_pesos = (total_material_a_1_pesos + total_material_a_2_pesos)
        print(f"El Total de material A del 2009 en $ es: ${total_material_a_2009_pesos}")

        input("Presione enter para continuar...")
        borrar()

        #material b 1 semestre
        print("Material B, 1 semestre")
        req_mat_b_1 = total_req_b_1sem
        inv_final_b_1 = int(input("Ingrese inventario final: "))
        total_materiales_b_1 = (req_mat_b_1 + inv_final_b_1)
        print(f"El total de materiales es de {total_materiales_b_1}")
        inv_inicial_b_1 = int(input("Ingrese inventario inicial: "))
        material_comprar_b_1 = (total_materiales_b_1 - inv_inicial_b_1)
        precio_compra_b_1 = int(input("Ingrese precio de compra: "))
        total_material_b_1_pesos = (material_comprar_b_1 * precio_compra_b_1)
        print(f"El Total de material B del semestre 1 en $ es: ${total_material_b_1_pesos}")

        input("Presione enter para continuar...")
        borrar()

        #material b 2 semestre
        print("Material B, 2 semestre")
        req_mat_b_2 = total_req_b_2sem
        inv_final_b_2 = int(input("Ingrese inventario final: "))
        total_materiales_b_2 = (req_mat_b_2 + inv_final_b_2)
        print(f"El total de materiales es de {total_materiales_b_2}")
        inv_inicial_b_2 = int(input("Ingrese inventario inicial: "))
        material_comprar_b_2 = (total_materiales_b_2 - inv_inicial_b_2)
        precio_compra_b_2 = int(input("Ingrese precio de compra: "))
        total_material_b_2_pesos = (material_comprar_b_2 * precio_compra_b_2)
        print(f"El Total de material B del semestre 2 en $ es: ${total_material_b_2_pesos}")

        input("Presione enter para continuar...")
        borrar()

        #material b total 2009
        print("Material A, Total 2009")
        req_mat_b_2009 = total_req_b_2009
        inv_final_b_2009 = int(input("Ingrese inventario final: "))
        total_materiales_b_2009 = (req_mat_b_2009 + inv_final_b_2009)
        print(f"El total de materiales es de {total_materiales_b_2009}")
        inv_inicial_b_2009 = int(input("Ingrese inventario inicial: "))
        material_comprar_b_2009 = (total_materiales_b_2009 - inv_inicial_b_2009)
        precio_compra_b_2009 = int(input("Ingrese precio de compra: "))
        total_material_b_2009_pesos = (total_material_b_1_pesos + total_material_b_2_pesos)
        print(f"El Total de material B del 2009 en $ es: ${total_material_b_2009_pesos}")
    
        input("Presione enter para continuar...")
        borrar()

        #material c 1 semestre
        print("Material C, 1 semestre")
        req_mat_c_1 = total_req_c_1sem
        inv_final_c_1 = int(input("Ingrese inventario final: "))
        total_materiales_c_1 = (req_mat_c_1 + inv_final_c_1)
        print(f"El total de materiales es de {total_materiales_c_1}")
        inv_inicial_c_1 = int(input("Ingrese inventario inicial: "))
        material_comprar_c_1 = (total_materiales_c_1 - inv_inicial_c_1)
        precio_compra_c_1 = int(input("Ingrese precio de compra: "))
        total_material_c_1_pesos = (material_comprar_c_1 * precio_compra_c_1)
        print(f"El Total de material C del semestre 1 en $ es: ${total_material_c_1_pesos}")

        input("Presione enter para continuar...")
        borrar()

        #material c 2 semestre
        print("Material C, 2 semestre")
        req_mat_c_2 = total_req_c_2sem
        inv_final_c_2 = int(input("Ingrese inventario final: "))
        total_materiales_c_2 = (req_mat_c_2 + inv_final_c_2)
        print(f"El total de materiales es de {total_materiales_c_2}")
        inv_inicial_c_2 = int(input("Ingrese inventario inicial: "))
        material_comprar_c_2 = (total_materiales_c_2 - inv_inicial_c_2)
        precio_compra_c_2 = int(input("Ingrese precio de compra: "))
        total_material_c_2_pesos = (material_comprar_c_2 * precio_compra_c_2)
        print(f"El Total de material C del semestre 2 en $ es: ${total_material_c_2_pesos}")

        input("Presione enter para continuar...")
        borrar()

        #material c total 2009
        print("Material C, Total 2009")
        req_mat_c_2009 = total_req_c_2009
        inv_final_c_2009 = int(input("Ingrese inventario final: "))
        total_materiales_c_2009 = (req_mat_c_2009 + inv_final_c_2009)
        print(f"El total de materiales es de {total_materiales_c_2009}")
        inv_inicial_c_2009 = int(input("Ingrese inventario inicial: "))
        material_comprar_c_2009 = (total_materiales_c_2009 - inv_inicial_c_2009)
        precio_compra_c_2009 = int(input("Ingrese precio de compra: "))
        total_material_c_2009_pesos = (total_material_c_1_pesos + total_material_c_2_pesos)
        print(f"El Total de material C del 2009 en $ es: ${total_material_c_2009_pesos}")

        input("Presione enter para continuar...")
        borrar()

        #COMPRAS TOTALES
        compra_total_1 = (total_material_a_1_pesos + total_material_b_1_pesos + total_material_c_1_pesos)
        compra_total_2 = (total_material_a_2_pesos + total_material_b_2_pesos + total_material_c_2_pesos)
        compra_total_2009 = (total_material_a_2009_pesos + total_material_b_2009_pesos + total_material_c_2009_pesos)
        print("COMPRAS TOTALES")
        print(f"1. Semestre: {compra_total_1}\n2. Semestre: {compra_total_2}\nTotal 2009: {compra_total_2009}")

        input("Presione enter para continuar...")
        borrar()


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
