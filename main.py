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


lbl_instructions = tk.Label(window,
text = 'Enter a number between 1 and 718',
font = small_font)

lbl_instructions.config(bg = '#253529', fg = '#FEFEFE')
lbl_instructions.pack() # añadimos nuetra primera label

txt_pokemon_number = tk.Entry(window) # Añadimos un text area como input y lo agregamos a window
txt_pokemon_number.pack()

btn_get_info = tk.Button(window, text = 'Get Data!')
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


window.mainloop()