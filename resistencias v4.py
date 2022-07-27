
def proceso1():
    # DEFINICION COLORES BANDAS y tolerancia
    dicbanda = {0:'Negro ',1:'Marron ',2:'Rojo ',3:'Naranja ',4:'Amarillo ',5:'Verde ',6:'Azul ',7:'Violeta ',8:'Gris ',9:'Blanco' }
    dictol = {5:'Dorado ',10:'Plateado ',20:'-- '}
    
    ####### Funcion para validar resistencia
    ######################################
    def Validacionresistencia(R):       ## Valida que la resistencia sea positiva 
        return (validresis)
    R = int(input('Se van a calcular los colores de la resistencia, ingresa su valor en Ohms: '))   
    RR = R
    if len(str(R)) == 1:
        R = '0'+ str(R)
    else:
        R = str(R)
    LonRConvertido = len(R) 
    if LonRConvertido >= 2 and RR >= 0 and RR < 99000000000 : 
       validresis = 1
    else: 
        print('Fuera de Rango')
        validresis = 0
        
    ####### Funcion para Validacion de tolerancia 
    ######################################
    def Validtoleranc(T):       ## Valida que la tolerancia este en los rangos especificos
        return (Validaciontolerancia)
    T = int(input('Ingresa Valor de tolerancia (5, 10 o 20): '))    
    if T == 5 or T == 10 or T == 20: 
        Validaciontolerancia = 1
    else: 
        print('Escoge un valor (5, 10 o 20): ')
        Validaciontolerancia = 0
        
     ##  Inicio del programa
     ################################################
    Validacionresistencia(R)
    #print("Resistencia valida // validresis: ",validresis)
    
    Validtoleranc(T)
    #print("Tolerancia valida // Validaciontolerancia: ",Validaciontolerancia)
    
    ################  Extraccion de caracteres y fin del programa 
    ################################################
    zz = R[:2]  ## dos primeros caracteres
    x = R[:1]  ## primer caracter
    y = R[1:2]  ## segundo caracter
    z = LonRConvertido -len(zz) ##  longitud de la cadena menos 2 caracteres iniciales
    
    if len(R) < 2: 
        print("Resistencia de:",R ,"OHMS, Tolerancia:", T, "%, Colores: ", dicbanda[int(x)], dicbanda[int(y)], dicbanda[0], ',Banda Tolerancia:', dictol[T])
    else: 
        print("Resistencia de:",R ,"OHMS, Tolerancia:", T, "%, Colores: ", dicbanda[int(x)], dicbanda[int(y)], dicbanda[int(z)], ',Banda Tolerancia:', dictol[T])

    
def proceso2():
  # Ingreso de cantidad de resistencias
  numeroresistencias = int(input('Vas a sumar resistencias en serie, ingresa cantidad de resistencia a sumar: '))   
     
  if numeroresistencias > 0:
          acumuladoRs = []; cant = 1; suma = 0 ## Definicion Variables
  
          while cant <= numeroresistencias: 
              resistenciaN = int(input('Ingresa resistencia a sumar')) 
              if resistenciaN >= 10 and resistenciaN <= 1000000000:
                  acumuladoRs.append(resistenciaN)  ## suma elemento a la lista
                  suma = suma + resistenciaN
                  cant = cant + 1 # Restantes = numeroresistencias - cant
              else:  
                  print('La resistecia debe ser positiva, >= 10 y <= 1000000000')
                  cant = cant; suma = suma
          else: 
              print('# Resistencias sumadas =',numeroresistencias,'\n Las resistencias en serie suman: ',suma,'Ohms')
              if int(input('\n\nDesea ver resistencias usadas ? \n1/si\n2/no ')) == 1: 
                  for element in acumuladoRs: print('Resistencia:',element,'Ohms')
  else:
      print('Debe ser numero positivo!!')  
      
      
def proceso3():
      # Ingreso de cantidad de resistencias
    numeroresistencias = int(input('Vas a sumar resistencias en paralelo, ingresa cantidad de resistencia a sumar: '))   
       
    if numeroresistencias > 0:
            acumulasincambio = []; acumuladoRs = []; cant = 1; suma = 0 ## Definicion Variables
    
            while cant <= numeroresistencias: 
                resistenciaN = int(input('Ingresa resistencia a sumar')) 
                if resistenciaN >= 10 and resistenciaN <= 1000000000:
                    acumulasincambio.append(resistenciaN) #guarda resistencia en una lista aparte
                    resistenciaN = 1/resistenciaN
                    acumuladoRs.append(resistenciaN)  ## suma elemento a la lista
                    suma = suma + resistenciaN
                    cant = cant + 1 # Restantes = numeroresistencias - cant
                else:  
                    print('La resistecia debe ser positiva, >= 10 y <= 1000000000')
                    cant = cant; suma = suma
            else: 
                print('# Resistencias sumadas =',numeroresistencias,'\n Las resistencias en paralelo suman: ',1/suma,'Ohms')
                if int(input('\n\nDesea ver resistencias usadas ? \n1/si\n2/no ')) == 1: 
                    for element in acumulasincambio: print('Resistencia:',element,'Ohms')
    else:
        print('Debe ser numero positivo!!')  
          
  
  
    
    
proceso = int(input('Ingresa proceso a realizar: \n 1 para calcular el color\n 2 para calcular resistencia en serie\n 3 para calcular resistencia en paralelo')) 
    
if proceso == 1: proceso1()
elif proceso == 2: proceso2()
elif proceso == 3: proceso3()
else: print('Entrada no valida')
    
    
    
    
    