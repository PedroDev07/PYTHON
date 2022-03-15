from matplotlib.colors import LinearSegmentedColormap


class Televisao:
    
    def __init__ (self):
        self.ligada=False
        self.canal = 5
        
    def power (self):
        if (self.ligada == True):
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal +=1
    def diminui_canal(self):
        self.canal -=1



liga = Televisao()


print(liga.ligada)
liga.power()
print(liga.ligada)
liga.power()
print(liga.ligada)


print(liga.canal)
liga.aumenta_canal()
print(liga.canal)
liga.diminui_canal()
print(liga.canal)