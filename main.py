import tkinter as tk

window = tk.Tk() # Creamos una nueva ventana

window.title('PokeDex') #Damos un titulo a la ventana

lbl_instructions = tk.Label(window, text = 'Enter a number between 1 and 718')
lbl_instructions.pack() # añadimos nuetra primera label

txt_pokemon_number = tk.Entry(window) # Añadimos un text area como input y lo agregamos a window
txt_pokemon_number.pack()

btn_get_info = tk.Button(window, text = 'Get Data!')
btn_get_info.pack() # añadimos un boton para recoger los datos

## Añadimos mas labels para mostrar los datos que recogeremos

lbl_name_text = tk.Label(window, text = 'Name: ')
lbl_name_text.pack()
lbl_name_value = tk.Label(window, text = '???')
lbl_name_value.pack()


window.mainloop()