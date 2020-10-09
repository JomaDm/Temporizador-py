import time
from console import *

class Temporizador():
  def __init__(self, tiempo):
    """
    docstring
    """
    self.tiempo = tiempo
    
  def establecerTiempo(self, tiempo):
    """
    docstring
    """
    self.tiempo = tiempo
  
  def establecerSeg(self, segundos):
    """
    docstring
    """
    self.tiempo.establecerSeg(segundos)
  
  def establcerMin(self, minutos):
    """
    docstring
    """
    self.tiempo.establcerMin(minutos)
    
  def establcerHora(self, horas):
    """
    docstring
    """
    self.tiempo.establcerHora(horas)
  
  def establcerDia(self, dia):
    """
    docstring
    """
    self.tiempo.establcerDia(dia)
    
  def iniciar(self):
    """
    docstring
    """
    while not self.tiempo.fin():            
      self.tiempo.decrementar()      
      self.tiempo.imprimir()   
      time.sleep(1)
      clearScreen()         
    
    print("FIN")