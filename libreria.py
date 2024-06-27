def lista_del_personal1():
    listpersonal=[]
    while (True):
        print("Ingrese si quiere ver o agregar los datos del personal")
        print("1) Ver datos del personal")
        print("2) Agregar datos")
        print("3) Volver")
        res=int(input())
        if res<1 or res>3:
            print("Opciòn no valida")
        elif res==1:
            print(listpersonal)
            print("Si desea volver precione cualquier tecla")
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
                print("Ingrese el segundo nombre")
                nom2=input()
                if nom2:
                    listpersonal.append(nom2)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while (True):
                print("Ingrese el primer apellido")
                ape1=input()
                if ape1:
                    listpersonal.append(ape1)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while (True):
                print("Ingrese el segundo apellido")
                ape2=input()
                if ape2:
                    listpersonal.append(ape2)
                    break
                else:
                    print("No se puede dejar en blanco")

            def generar_rut_con_dv(rut_bas, dv):
                return f"{rut_bas}-{dv.upper()}"
            
            while (True):

                print("Porfavor ingrese su rut sin digito de verificacion y sin puntos")
                rut_bas=input()
                print("Porfavor ingrese el codigo de verificaciòn")
                dv=input()
                if rut_bas and dv:
                    rut_completo = generar_rut_con_dv(rut_bas, dv)
                    listpersonal.append(rut_completo)
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
                    print("No se puede dejar en blanco")
        elif res==3:
            break




"""****************************************************************************************************************
opcion 1      """

def menu_principal():
    listamenor=[]
    while (True):
        print("======= Menú Principal =======")
        print("1) Ingresar datos del menor ")
        print("2) Consultar datos del menor")
        print("3) Salir                    ")
        respuesta = int(input("Ingrese el número de la opción que desea: "))
        if respuesta<1 or respuesta>3:
            print("opcion invalida")

        elif respuesta==1:
            while (True):
                print("Escriba el primer nombre del menor")
                nom1=input()
                if nom1:
                    listamenor.append(nom1)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while (True):
                print("Escriba el segundo nombre del menor")
                nom2=input()
                if nom2:
                    listamenor.append(nom2)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while (True):
                print("Ingrese la fecha de nacimiento del menor (Formato DD/MM/AAAA)")
                año=input()
                if año:
                    listamenor.append(año)
                    break
                else:
                    print ("No se puede dejar en blanco")
            
            while (True):
                print("Ingrese la sala a la que pertenece ( Debe tener 1 letra mayúscula,2 números del 0-5 )")
                sala=input()
                if sala:
                    listamenor.append(sala)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            def generar_rut_con_dv(rut_bas, dv):
                return f"{rut_bas}-{dv.upper()}"
            
            while (True):

                print("Porfavor ingrese su rut sin digito de verificacion y sin puntos")
                rut_bas=input()
                print("Porfavor ingrese el codigo de verificaciòn")
                dv=input()
                if rut_bas and dv:
                    rut_completo = generar_rut_con_dv(rut_bas, dv)
                    listamenor.append(rut_completo)
                    break
                else:
                    print("No se puede dejar en blanco")
            
            while (True):
                print("Ingrese la nacionalidad del menor")
                nacionalidad=input()
                if nacionalidad:
                    listamenor.append(nacionalidad)
                    break
                else:
                    print("No se puede dejar en blanco")
       
        elif respuesta==2:
            print(listamenor)
            print("Si desea volver al menu precione cualquier tecla")
            res90=input()
        
        elif respuesta==3:
            break




    