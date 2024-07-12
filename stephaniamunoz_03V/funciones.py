import random
import csv

def asignar_sueldos(trabajadores):
    sueldos_trabajadores={} 
    for trabajador in trabajadores:
        sueldo=random.randint(300000,2500000)

        sueldos_trabajadores[trabajador]=sueldo

    print ("Sueldos generados.")     
    print (sueldos_trabajadores)

    return sueldos_trabajadores

    
def clasificar_sueldos(sueldos_trabajadores):
    menor800 = {}
    entre800y2m = {}
    mayor2m ={}


    for trabajador,sueldo in sueldos_trabajadores.items():
        if sueldo < 800000:
             menor800[trabajador] = sueldo
        elif sueldo >= 800000 and sueldo < 2000000:
             entre800y2m[trabajador] = sueldo
        else:
             mayor2m[trabajador] = sueldo

    print ("Total sueldos menores de 800.000: ", len(menor800))
    for trabajador,sueldo in menor800.items():
        print ("Trabajador:",trabajador,("con sueldo: "),sueldo)

    print ("Total sueldos entre 800.000 y 2.000.000: ", len(entre800y2m))
    for trabajador,sueldo in entre800y2m.items():
        print ("Trabajador:",trabajador,("con sueldo: "),sueldo)

    print ("Total sueldos mayores 2.000.000: ", len(mayor2m))
    for trabajador,sueldo in mayor2m.items():
        print ("Trabajador:",trabajador,("con sueldo: "),sueldo)
    


    
    total_sueldos = sum(sueldos_trabajadores.values())
    print ("TOTAL SUELDOS $", total_sueldos)
    return total_sueldos

def estadisticas(sueldos_trabajadores):
    sueldos_lista = list(sueldos_trabajadores.values())
    max_sueldo = max(sueldos_lista)
    min_sueldo = min(sueldos_lista)
    promedio_sueldo = sum(sueldos_lista)/ len(sueldos_lista)
    
    return max_sueldo,min_sueldo,promedio_sueldo

def reporte_sueldos(sueldos_trabajadores):
    with open ('reporte_sueldos','w',newline='') as archivo:
        escritor = csv.writer(archivo,delimiter=',')
        escritor.writerow(['Nombre','sueldo'])
        for trabajador,sueldo in sueldos_trabajadores.items():
            escritor.writerow([trabajador,sueldo])


    