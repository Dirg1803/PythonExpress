def registro_error(a):
    a=open("log_errores.txt","a")
    a.write("se ha registrado un error de ejecución")
    a.close()