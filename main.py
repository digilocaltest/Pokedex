import requests # getting data into python, popular apis, urllib an request
import tkinter as tk

## > fonts

small_font = ('Arial', 14)
medium_font = ('Arial', 18)
large_font = ('Arial', 30)

## -------

window = tk.Tk() # Creamos una nueva ventana

window.config(bg = '#253529') #Color del background
window.title('PokeDex') #Damos un titulo a la ventana
window.geometry("400x150+200+200") #Width Height

## funciones -----
# definimos nuestra funcion para coger de la bd
def get_pokemon_data(num):
  r = requests.get('https://pokeapi.co/api/v2/pokemon/'+ str(num)) # Llamammos a la api the pokemon y guardamos el resultado en r

  pokemon_dictionary = r.json() #pasamos json a python format

  return pokemon_dictionary # devolvemos el los datos solocitados

# nueva funcion para mostrar nuestros datos
def show_pokemon_data():
  pokemon_number = txt_pokemon_number.get() # Cogemos el numero escrito en la text area

  pokemon_data = get_pokemon_data(pokemon_number) #llamamos aApi funcion y le pasamos el numero del text area
  
  lbl_name_value.config(text = pokemon_data['name']) #Actualizamos el label name value ????? con el resultado de pokemon index ['Name']

## ------
## -- Interface
lbl_instructions = tk.Label(window,
text = 'Enter a number between 1 and 718',
font = small_font)

lbl_instructions.config(bg = '#253529', fg = '#FEFEFE')
lbl_instructions.pack() # añadimos nuetra primera label

txt_pokemon_number = tk.Entry(window) # Añadimos un text area como input y lo agregamos a window
txt_pokemon_number.pack()

btn_get_info = tk.Button(window, text = 'Get Data!',
command = show_pokemon_data)
btn_get_info.pack() # añadimos un boton para recoger los datos

## Añadimos mas labels para mostrar los datos que recogeremos

lbl_name_text = tk.Label(window,
text = 'Name: ',
bg = '#1A1110',
fg = '#FEFEFE',
font = medium_font)
lbl_name_text.pack()
lbl_name_value = tk.Label(window, text = '???',
bg = '#1A1110',
fg = '#FEFEFE',
font = large_font)
lbl_name_value.pack()

## ---

window.mainloop()



