def registro(bd):
    user = str(input("\nIngrese su usuario: "))
    if user in bd:
        print("\nError, el usuario ya existe. ")
        return

    contra = str(input("\nIngrese la contraseña del usuario: "))
    bd[user] = contra
    print("\nSe ha ingresado correctamente el usuario. ")




def mostrar_datos(bd):
    
    if len(bd) == 0:
        print("\nNo existen datos registrados. ")
        return
    print("\n<----------  USUARIOS REGISTRADOS ---------->\n")
    for user, contra in bd.items():
        print(f"\nUsuario: {user} | Contraseña: {contra}\n")

def inicio_sesion(bd):
    
    user_sesion = str(input("\nIngrese su usuario: "))
    if user_sesion not in bd:
        print(f"\nNo existe ningún usuario llamado {user_sesion}")
        return
    contra_sesion = str(input("\nIngrese su contraseña: "))
    if contra_sesion != bd[user_sesion]:
        print("La contraseña es incorrecta. ")
        return
    print("\nHa ingresado sesión correctamente. ")
    
    




base_datos = {}


try:

    while True:
        print("\n<----------  MENU ----------> \n")
        print("01- Registrar usuario. ")
        print("02- Mostrar usuarios. ")
        print("03- Iniciar sesión. ")
        print("04- Salir. \n")
        
        opcion = int(input("Ingrese una opción: "))
        while opcion not in [1,2,3,4]:
            opcion = int(input("Opción no válida, por favor ingrese nuevamente una opción: "))
        if opcion == 1:
            registro(base_datos)
        elif opcion == 2: 
            mostrar_datos(base_datos)
        elif opcion == 3:
            inicio_sesion(base_datos)
        else:
            break

except:
    print("Se ha generado un error. ")