#calories calculator

g_egg = float(input("egg here : "))
g_carrot = float(input("carrot here : "))

def eggcal(x):
  
  energy = x * 70
  protein = x * 7.7
  carbohydrate = x
  fat = x * 8

  return energy, protein, carbohydrate, fat

enegg, proegg, carboegg, fegg = eggcal(g_egg)

def carrotcal(x):
  
  energy = x * 0.46
  protein = x * 0.009
  carbohydrate = x * 0.1
  fat = x * 0.002

  return energy, protein, carbohydrate, fat

energyc, proteinc, carbohydratec, fatc = carrotcal(g_carrot)

sum_energy = energyc + enegg
sum_protein = proteinc + proegg
sum_carbo = carbohydratec + carboegg
sum_fat = fatc + fegg

print("\nenergy :", sum_energy)
print("protein :", sum_protein)
print("carbohydrate :", sum_carbo)
print("fat :", sum_fat)