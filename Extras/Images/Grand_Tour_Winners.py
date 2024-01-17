import data

T = set(data.tourWinners)
G = set(data.giroWinners)
V = set(data.vueltaWinners)


for name in (T & G & V):
    print(name)

# Bernard Hinault
# Vincenzo Nibali
# Alberto Contador
# Jacques Anquetil
# Eddy Merckx
# Felice Gimondi