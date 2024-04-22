import tkinter as tk

window = tk.Tk()
window.title("calcal")
window.minsize(width=500, height=600)

title_lable = tk.Label(master=window, text="calcal")
title_lable.pack()

title_rice = tk.Label(master=window, text="Rice")
title_rice.pack()

g_rice = tk.Entry(master=window)
g_rice.pack()

title_egg = tk.Label(master=window, text="Egg")
title_egg.pack()

g_egg = tk.Entry(master=window)
g_egg.pack()

def ricecal(x):

  energy = x * 1.3
  protein = x * 0.027
  carbohydrate = x * 0.282
  fat = x * 0.003

  riceen = ("%.2f" % energy)
  ricepro = ("%.2f" % protein)
  ricecarbo = ("%.2f" % carbohydrate)
  ricef = ("%.2f" % fat)

  return riceen, ricepro, ricecarbo, ricef

def eggcal():
    
  x = float(g_egg.get())
  energy = x * 70
  protein = x * 7.7
  carbohydrate = x
  fat = x * 8
  
  eggen = ("%.2f" % energy)
  eggpro = ("%.2f" % protein)
  eggcarbo = ("%.2f" % carbohydrate)
  eggf = ("%.2f" % fat)

  return eggen, eggpro, eggcarbo, eggf

def sumcal():

  sumen = float(ricecal(float(g_rice.get()))[0]) + float(eggcal(float(g_egg.get()))[0])
  #sumpro =
  #sumcarbo =
  #sumf =

  output_lable_energy.configure(text=sumen)
  #output_lable_protein.configure(text=ricepro)
  #output_lable_carbohydrate.configure(text=ricecarbo)
  #output_lable_fat.configure(text=ricef)

process_button = tk.Button(
  master=window, text="Process",
  command=sumcal)
process_button.pack()

output_lable_energy = tk.Label(master=window)
output_lable_energy.pack()

output_lable_protein = tk.Label(master=window)
output_lable_protein.pack()

output_lable_carbohydrate = tk.Label(master=window)
output_lable_carbohydrate.pack()

output_lable_fat = tk.Label(master=window)
output_lable_fat.pack()

window.mainloop()