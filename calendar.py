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
            raise ValueError("El día tiene estar entre 1 y 31")
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
        mes_nuevo = self.mes
        anyo_nuevo = self.anyo
        if self.mes == 1 or self.mes == 2:
            mes_nuevo += 12
            anyo_nuevo -= 1

        A = anyo_nuevo % 100
        B = anyo_nuevo // 100
        C = 2 - B + B // 4
        D = A // 4
        E = 13 * (mes_nuevo + 1) // 5
        F = A + C + D + E + self.dia

        return F % 7
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anyo}"


try:
    d = Dia(1970, 4, 25)
    print(d) #Imprime la fecha si se cumplen las condiciones
except ValueError as date:
    print(date) 

'''

0 = sábado, 1 = domingo, 2 = lunes, 3 = martes, 4 = miercoles, 5 = jueves, 6 = viernes

'''

try:
    d = Dia(1970, 4, 8)
    print(f"Día de la semana: {d.dia_semana}")  
except ValueError as date:
    print(date)
