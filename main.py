import requests # getting data into python, popular apis, urllib an request
import tkinter as tk
from io import BytesIO # LIBRERIAS PARA UTILIZAR IMAGENES
from PIL import Image, ImageTk


## > fonts

small_font = ('Arial', 14)
medium_font = ('Arial', 18)
large_font = ('Arial', 30)

## -------

window = tk.Tk() # Creamos una nueva ventana

window.config(bg = '#253529') #Color del background
window.title('PokeDex') #Damos un titulo a la ventana
#window.geometry("400x450200+200") #Width Height

## funciones -----

# definimos nuestra funcion para DATOS API de la bd
def get_pokemon_data(num):
  
  r = requests.get('https://pokeapi.co/api/v2/pokemon/'+ str(num)) # Llamammos a la api the pokemon y guardamos el resultado en r

  pokemon_dictionary = r.json() #pasamos json a python format

  return pokemon_dictionary # devolvemos el los datos solocitados

# nueva funcion para mostrar nuestros datos
def show_pokemon_data():
  pokemon_number = txt_pokemon_number.get() # Cogemos el numero escrito en la text area
  txt_pokemon_number.delete(0,99) # limpiamos el text box
  pokemon_data = get_pokemon_data(pokemon_number) 
  pokemon_image = get_pokemon_image(pokemon_number)#llamamos aApi funcion y le pasamos el numero del text area
  #try get this data
  try:
    lbl_name_value.config(text = pokemon_data['name']) #Actualizamos el label name value ????? con el resultado de pokemon index ['Name']
    ## StATS
    lbl_HP_value.config(text = pokemon_data['stats'][5]['base_stat'])
    lbl_ATC_value.config(text = pokemon_data['stats'][4]['base_stat'])
    lbl_DEF_value.config(text = pokemon_data['stats'][3]['base_stat'])
    lbl_SPD_value.config(text = pokemon_data['stats'][0]['base_stat'])
    ## fin stats
    ## IMAGEN ------
    lbl_image.config(image = pokemon_image)
    lbl_image.image = pokemon_image
    ## FIN IMAGEN
    ## si no cambiamos el label_number box por, invalid choice
  except:
    txt_pokemon_number.insert(0, 'Invalid choice')

## funcion para coger y manipuar imagines para tkinter
def get_pokemon_image(num):
  #load data 
  image_bytes = requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+ str(num)+ ".png")

  #tkinter no carga images directamente. tenemos que convertirlos primero
  data_stream = BytesIO(image_bytes.content)
  # Despues utilizamos python image library para abrir data_stream
  pil_image = Image.open(data_stream)
  #Finalmente convertimos pil_image a algo que tkinter puede gestionar
  tk_image = ImageTk.PhotoImage(pil_image)
  # devolvermos nuestra image
  return tk_image
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
## resutl data labels
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

lbl_image = tk.Label(window)
lbl_image.config(bg = '#0093d5')
lbl_image.pack()


lbl_HP_text = tk.Label(window,
text = 'Hp: ',
bg = '#1A1110',
fg = '#FEFEFE',
font = medium_font)
lbl_HP_text.pack()
lbl_HP_value = tk.Label(window, text = '???',
bg = '#1A1110',
fg = '#FEFEFE',
font = large_font)
lbl_HP_value.pack()

lbl_ATC_text = tk.Label(window,
text = 'Atack: ',
bg = '#1A1110',
fg = '#FEFEFE',
font = medium_font)
lbl_ATC_text.pack()
lbl_ATC_value = tk.Label(window, text = '???',
bg = '#1A1110',
fg = '#FEFEFE',
font = large_font)
lbl_ATC_value.pack()

lbl_DEF_text = tk.Label(window,
text = 'Defense: ',
bg = '#1A1110',
fg = '#FEFEFE',
font = medium_font)
lbl_DEF_text.pack()
lbl_DEF_value = tk.Label(window, text = '???',
bg = '#1A1110',
fg = '#FEFEFE',
font = large_font)
lbl_DEF_value.pack()

lbl_SPD_text = tk.Label(window,
text = 'Speed: ',
bg = '#1A1110',
fg = '#FEFEFE',
font = medium_font)
lbl_SPD_text.pack()
lbl_SPD_value = tk.Label(window, text = '???',
bg = '#1A1110',
fg = '#FEFEFE',
font = large_font)
lbl_SPD_value.pack()

## ---

window.mainloop()



