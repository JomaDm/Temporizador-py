import math

class Tiempo():
  
  def __init__(self):
    """
    docstring
    """
    self.horas = 0
    self.minutos = 0
    self.segundos = 0
    self.dias = 0
    
  def __verificarTiempo(self):
    """
    docstring
    """
    if self.segundos >= 60:
      aux = self.segundos % 60
      self.segundos = self.segundos // 60
      self.minutos += aux
      
    if self.minutos >= 60:
      aux = self.minutos % 60
      self.minutos = self.minutos // 60
      self.horas += aux
      
    if self.horas >= 24:
      aux = self.horas % 24
      self.horas = self.horas // 60
      self.dias += aux
      
    if(self.segundos <= -1):
      self.minutos -= 1
      self.segundos = 59
    
    if(self.minutos <= -1):
      self.horas -= 1
      self.minutos = 59
    
    if(self.horas <= -1):
      self.dias -= 1
      self.horas = 23
      
  def decrementar(self, decremento=1):
    """
    docstring
    """
    self.segundos -=1
    self.__verificarTiempo()
    
  def aumentarSeg(self,aumento=1):
    """
    docstring
    """
    self.segundos +=aumento
    self.__verificarTiempo()
    
  def aumentarMin(self, aumento=1):
    """
    docstring
    """
    self.minutos +=aumento
    self.__verificarTiempo()
    
  
  def aumentarHora(self,aumento=1):
    """
    docstring
    """
    self.horas +=aumento
    self.__verificarTiempo()
    
  def aumentarDia(self, aumento=1):
    """
    docstring
    """
    self.dias +=aumento
    self.__verificarTiempo()
    
  def aumentar(self,segundos=1,minutos=1,horas=1,dias=1):
    """
    docstring
    """
    self.segundos +=segundos
    self.minutos +=minutos
    self.horas +=horas
    self.dias +=dias
    self.__verificarTiempo()
    
  def establecer(self,segundos=0,minutos=0,horas=0,dias=0):
    """
    docstring
    """
    self.segundos =segundos
    self.minutos =minutos
    self.horas =horas
    self.dias =dias
    self.__verificarTiempo()
    
  def establecerSeg(self, segundos):
    """
    docstring
    """
    self.segundos = segundos
    self.__verificarTiempo()
    
  def establecerMin(self, minutos):
    """
    docstring
    """
    self.minutos = minutos
    self.__verificarTiempo()
    
  def establecerHora(self, horas):
    """
    docstring
    """
    self.horas = horas
    self.__verificarTiempo()
  
  def establecerDia(self, dia):
    """
    docstring
    """
    self.dias = dia
    self.__verificarTiempo()
  
  def fin(self):
    """
    docstring
    """
    return self.segundos==0 and self.minutos==0 and self.horas==0 and self.dias==0
  
  def imprimir(self):
    """
    docstring
    """
    str_seg = str(self.segundos) if self.segundos >= 10 else "0"+str(self.segundos)
    str_min = str(self.minutos) if self.minutos >= 10 else "0"+str(self.minutos)
    str_hor = str(self.horas) if self.horas >= 10 else "0"+str(self.horas)
    str_dia = str(self.dias) if self.dias >= 10 else "0"+str(self.dias)
    print("\n\t"+str_dia+":"+str_hor+":"+str_min+":"+str_seg)