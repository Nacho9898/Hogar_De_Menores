#Datos del personal
listpersonal=[]
opc=2
while opc==2:
    print("Ingrese si quiere ver o agregar los datos del personal")
    print("1) Ver Datos del Personal")
    print("2) Agregar datos")
    print("3) volver")
    res=int(input())
    if res<1 or res>3:
        print("Opción no valida")
    elif res==1:
        print(listpersonal)
        print("si desea volver precione cualquier tecla")
        res2=input()
    elif res==2:
        print("ingrese los nombres")
        nom=input()
        listpersonal.append(nom)
        print("ingrese los Apellidos")
        ape=input()
        listpersonal.append(ape)
        print("ingrese Rut")
        rut=input()
        listpersonal.append(rut)
        print("Ingrese su Nacionalidad")
        nac=input()
        listpersonal.append(nac)
        print("Ingrese si es voluntario o personal activo")
        vol_o_act=input()
        listpersonal.append(vol_o_act)
    elif res==3:
        break
            
