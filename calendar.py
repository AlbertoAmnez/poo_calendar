class Dia:

    def __init__(self, anyo=1970, mes=1, dia=1):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia
        self.dia_semana = self.calcular_dia_semana()

        
        self.validar_fecha()

    def validar_fecha(self):
        if self.mes < 1 or self.mes > 12:
            raise ValueError("El mes tiene que estar entre 1 y 12")
        
        if self.dia < 1 or self.dia > 31:
            raise ValueError("El dia tiene estar entre 1 y 31")
        '''

        Inicializamos la lista dias_por_mes con '0' para que coincidan los indices de la lista con los numeros de mes, ya que el indice empieza en 0 pero el mes empieza en 1.
        Asi, lo hago mas intuitivo haciendo coincidir el indice con el numero del mes.
        
        '''
        dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.anyo % 4 == 0 and (self.anyo % 100 != 0 or self.anyo % 400 == 0):
            dias_por_mes[2] = 29  
        
        if self.dia < 1 or self.dia > dias_por_mes[self.mes]:
            raise ValueError(f"El mes {self.mes} del año {self.anyo} no tiene {self.dia} dias")
    
    def calcular_dia_semana(self):
        mes_ajustado = self.mes
        anyo_ajustado = self.anyo
        if self.mes == 1 or self.mes == 2:
            mes_ajustado += 12
            anyo_ajustado -= 1

        A = anyo_ajustado % 100
        B = anyo_ajustado // 100
        C = 2 - B + B // 4
        D = A // 4
        E = 13 * (mes_ajustado + 1) // 5
        F = A + C + D + E + self.dia

        '''
        Al parecer el algoritmo de Zeller en el calendario gregoriano no tiene en cuenta los años bisiestos a partir del año 2000.
        Con esta pequeña correción lo que hará es que a partir del 2000, restará un dia para que nos de el resultado esperado
        '''

        if anyo_ajustado >= 2000:
            F -= 1

        return F % 7
    
    def info(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anyo}"
    
    '''
    Creo este metodo que retorna la cadena de texto correspondiente a la posicion del dia de la semana, por lo tanto si la posicion es [0] me devulve: "Sabado"
    '''

    def dia_semana_texto(self):
        dias_texto = ["Sabado", "Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        return dias_texto[self.dia_semana]

try:
    d = Dia(1995, 6, 25)
    print(d.info()) #Imprime la fecha si se cumplen las condiciones
    print(d.dia_semana_texto()) #Imprime el dia de la semana por nombre
except ValueError as date:
    print(date) 

'''

0 = sabado, 1 = domingo, 2 = lunes, 3 = martes, 4 = miercoles, 5 = jueves, 6 = viernes

'''

try:
    d = Dia(1970, 4, 25)
    print(f"Dia de la semana: {d.dia_semana}")  #Imprime dia de la semana como un numero
except ValueError as date:
    print(date)
