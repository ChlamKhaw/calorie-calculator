#calories calculator

g_rice = float(input("rice here : "))
g_egg = float(input("egg here : "))
g_carrot = float(input("carrot here : "))

def ricecal(x):

  energy = x * 1.3
  protein = x * 0.027
  carbohydrate = x * 0.282
  fat = x * 0.003

  return energy, protein, carbohydrate, fat

enrice, prorice, carborice, frice = ricecal(g_rice)

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

encarrot, procarrot, carbocarrot, fcarrot = carrotcal(g_carrot)

sum_energy = enrice + enegg + encarrot
sum_protein = prorice + proegg + procarrot
sum_carbo = carborice + carboegg + carbocarrot
sum_fat = frice + fegg + fcarrot

print("\nenergy :", sum_energy)
print("protein :", sum_protein)
print("carbohydrate :", sum_carbo)
print("fat :", sum_fat)