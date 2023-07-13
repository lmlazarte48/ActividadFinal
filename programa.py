#Desarrollar un programa en Python que permita a un docente almacenar una lista con los datos
#de 20 alumnos, con su sus nombres completos y las notas numéricas que ha obtenido a lo largo
#del año.

print("\033[H\033[J")

lista1=[]   #Alumnos
lista2=[]   #Nota 1   
lista3=[]   #Nota 2
lista4=[]   #Nota 3

def menu(): #Menu principal
    print("\n")
    print("MENU\n\n1-Nuevo\n")
    print("2-Mostrar Lista de Alumnos\n3-Mostar Notas\n4-Mostrar Promedio de Notas\n5-Mostrar Nota Media de todos los Alumnos\n6-Mostar Nota Media de los Aprobados\n7-Mostrar Nota Media de los Suspendidos\n")
    print("8-Salir\n")
    opcion=input("Ingrese una opción: ")
    return opcion

def orden():    #Ordena las listas
    for i in range(len(lista1)-1):        
        menor=i 
        for j in range(i+1, len(lista1)):
            if lista1[j]<lista1[menor]:
                menor=j
        if menor!=i:
            lista1[menor], lista1[i] = lista1[i], lista1[menor]
            lista2[menor], lista2[i] = lista2[i], lista2[menor]
            lista3[menor], lista3[i] = lista3[i], lista3[menor]
            lista4[menor], lista4[i] = lista4[i], lista4[menor]
            
def listados(): #Genera listados y calculos
    prom=0
    num=0
    if op=="3":
        print (f'{"NOMBRE": <{19}}'+f'{"NOTA1": <{7}}'+f'{"NOTA2": <{7}}'+f'{"NOTA3": <{7}}')
    elif op=="4":
        print (f'{"NOMBRE": <{19}}'+f'{"PROMEDIO": <{7}}')
    for i in range(len(lista1)):
        nombre=lista1[i]
        nota1=int(lista2[i])
        nota2=int(lista3[i])
        nota3=int(lista4[i])
        if op=="3":
            print(f'{nombre: <{20}}', f'{nota1: <{6}}', f'{nota2: <{6}}', f'{nota3: <{6}}')
        elif op=="4":
            prom=(nota1+nota2+nota3)/3
            print(f'{nombre: <{20}}', f'{round(prom,2): <{6}}')
        elif op=="5":
            prom=prom+((nota1+nota2+nota3)/3)
        elif op=="6":
            if ((nota1+nota2+nota3)/3)>6:
                prom=prom+((nota1+nota2+nota3)/3)
                num=num+1
        elif op=="7":
            if ((nota1+nota2+nota3)/3)<7:
                prom=prom+((nota1+nota2+nota3)/3)
                num=num+1
    if op=="5":    
        print ("NOTA MEDIA GENERAL: ", round(prom/len(lista1),2))
    elif op=="6":
        print ("NOTA MEDIA APROBADOS: ", round(prom/num,2))
    elif op=="7":
        print ("NOTA MEDIA SUSPENDIDOS: ", round((prom/num),2))
        
        
op=(menu()) #Llama a menu principal
while op!="8":
    if op=="1":
        conf="S"
        while conf=="S" or conf=="s":
            print("\n")
            nombre=input("Ingrese el nombre del alumno: ")
            nota1=input("Ingrese nota 1: ")
            nota2=input("Ingrese nota 2: ")
            nota3=input("Ingrese nota 3: ")
            conf=input("Confirma? S/N: ")
            if conf=="S" or conf=="s":
                lista1.append(nombre)
                lista2.append(nota1)
                lista3.append(nota2)
                lista4.append(nota3)
                print(nombre, nota1, nota2, nota3) 
            conf=input("Agrega otro archivo? S/N: ")
        orden() #Ordena tablas
    elif op=="2":
        print("\n")
        print ("ALUMNOS")
        for i in range(len(lista1)):
            nombre=lista1[i]
            print(nombre)   #Muestra listado de alumnos
    elif op=="3" or op=="4" or op=="5" or op=="6" or op=="7":
        listados()
    else:
        print("Opción no válida!!") #Avisa opcion incorrecta ingresada
                     
    op=(menu())        

           
        

    