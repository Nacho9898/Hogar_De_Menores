#Datos del personal
listpersonal=[]
opc=2
while opc==2:
    print("Ingrese si quiere ver o agregar los datos del personal")
    print("1) Ver Datos del Personal")
    print("2) Agregar datos")
    res=int(input())
    if res<1 or res>2:
        print("Opción no valida")
    elif res==1:
        print(listpersonal)
        print("si desea volver precione cualquier tecla")
        res2=input()
    elif res==2:

        while (True):
            print("ingrese el primer nombre")
            nom1=input()
            if nom1:
                listpersonal.append(nom1)
                break
            else:
                print("No se puede dejar en blanco")

        while (True):
            print("ingrese segundo nombre")
            nom2=input()
            if nom2:
                listpersonal.append(nom2)
                break
            else:
                print("No se puede dejar en blanco")

        while (True):
            print("ingrese primer apellido")
            ape1=input()
            if ape1:
                listpersonal.append(ape1)
                break
            else:
                print("No se puede dejar en blanco")

        while (True):   
            print("ingrese segundo apellido")
            ape2=input()
            if ape2:
                listpersonal.append(ape2) 
                break
            else:
                print("No se puede dejar en blanco")

        while (True):
            print("ingrese Rut")
            rut=input()
            if rut:
                listpersonal.append(rut)
                break
            else:
                print("No se puede dejar en blanco")
        
        while (True):
            print("Ingrese su Nacionalidad")
            nac=input()
            if nac:
                listpersonal.append(nac)
                break
            else:
                print("No se puede dejar en blanco")
        
        while (True):
            print("Ingrese si es voluntario o personal activo")
            vol_o_act=input()
            if vol_o_act:
                listpersonal.append(vol_o_act)
                break
            else:
                print ("No se puede dejar en blanco")
        
            
