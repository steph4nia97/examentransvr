import statistics
import funciones as fn

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"] 

sueldos_trabajadores = {}

print ("__________________________________________________________________________________________")
print ("INICIALICE LOS SUELDOS EN LA OPCION 1 COMO PRIMERA INSTANCIA PORFAVOR.")
print ("__________________________________________________________________________________________")


while True:
    try:

        print ("")
        print ("MENU")
        print ("_______")
        print ("1- INICIALIZAR SUELDOS")
        print ("2- ASIGNAR SUELDOS ALEATORIOS")
        print ("3- CLASIFICAR SUELDOS")
        print ("4- ESTADISTICAS SUELDOS")
        print ("5- REPORTE DE SUELDOS")
        print ("6- SALIR DEL PROGRAMA")


        opcion = int (input("INGRESE OPCION : "))
        if opcion == 1:
            sueldos_trabajadores = {trabajador : 0 for trabajador in trabajadores}
            print ("SUELDOS INICIALIZADOS LISTOS PARA ASIGNAR ALEATOREO.")
        elif opcion == 2:
            if sueldos_trabajadores:
                sueldos_trabajadores = fn.asignar_sueldos(trabajadores)

            else:
                print ("INICIALIZAR SUELDOS PRIMERO PORFAVOR.")
        elif opcion ==3:
            if sueldos_trabajadores:
                fn.clasificar_sueldos(sueldos_trabajadores)
            else:
                print ("ASIGNAR LOS SUELDOS PORFAVOR")
        elif opcion ==4:
            if sueldos_trabajadores:
                max_sueldo, min_sueldo, promedio_sueldo = fn.estadisticas(sueldos_trabajadores)
                print ("maximo sueldo:",max_sueldo)
                print ("minimo sueldo: ", min_sueldo)
                print ("promedio de sueldos: ",promedio_sueldo)
            else:
                print ("ASIGNAR SUELDOS PORFAVOR")

        elif opcion ==5:
            if sueldos_trabajadores:
                fn.reporte_sueldos(sueldos_trabajadores)
                print ("REPORTE REALIZADO CON EXITO")
            else:
                print ("ASIGANAR SUELDOS PORFAVOR")
        elif opcion == 6:
            print ("FINALIZANDO PROGRAMA...")
            print ("Desarrolado por Stephania Muñoz")
            print ("RUT 19.339.999-1")
        else:
            print ("OPCION NO VALIDA, PORFAVOR INGRESAR OPCION DEL 1 AL 6.")
    except ValueError:
        print ("INGRESE UNA OPCION DEL 1 AL 6 PORFAVOR")



