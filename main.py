from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from data import *

#colors

co0 = "#444466" #black
co1 = "#feffff" #white
co2 = "#6f9fbd" #blue
co3 = "#403d3d" #ash

window = Tk()
window.title('Pokedex')
window.geometry('544x530')
window.resizable(width=False, height=False)
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

main_frame = Frame(window, width=540, height=306, bg=co1)
main_frame.grid(row=0, column=0, padx=1, pady=1)

def choose_pokemon(i):
    global label_icon_1, pokemon_image
    main_frame['bg'] = pokemon[i]['others'][1]

    pokemon_name['text'] = i
    pokemon_name['bg'] = pokemon[i]['others'][1]
    pokemon_type['text'] = pokemon[i]['type'][1]
    pokemon_type['bg'] = co3
    pokemon_number['text'] = pokemon[i]['type'][0]
    pokemon_number['bg'] = pokemon[i]['others'][1]


    image = pokemon[i]['others'][0]
    pokemon_image = Image.open(image)
    pokemon_image = pokemon_image.resize((250, 250))
    pokemon_image = ImageTk.PhotoImage(pokemon_image)

    label_icon_1 = Label(main_frame, image=pokemon_image, bg=pokemon[i]['others'][1])
    label_icon_1.place(x=60, y=50)

    if i == 'Pikachu':
        pokemon_name['fg'] = co0
    else:
        pokemon_name['fg'] = co1 

    # load status
    pokemon_hp['text'] = pokemon[i]['status'][0]
    pokemon_attack['text'] = pokemon[i]['status'][1]
    pokemon_defense['text'] = pokemon[i]['status'][2]
    pokemon_spatk['text'] = pokemon[i]['status'][3]
    pokemon_spdef['text'] = pokemon[i]['status'][4]
    pokemon_speed['text'] = pokemon[i]['status'][5]
    pokemon_total['text'] = pokemon[i]['status'][6]


    # load skills
    pokemon_hb_1['text'] = pokemon[i]['skills'][0]
    pokemon_hb_2['text'] = pokemon[i]['skills'][1]


    pokemon_type.lift()
    pokemon_number.lift()



pokemon_name = Label(main_frame, text="Pokemon name", anchor="center", font=("Ivy 20 bold"), fg=co1)
pokemon_name.place(x=15, y=15)

pokemon_type = Label(main_frame, text="Pokemon type", anchor="center", font=("Verdana 10 bold"), fg=co1)
pokemon_type.place(x=20, y=50)

pokemon_number = Label(main_frame, text="Pokemon number", anchor="center", font=("Verdana 13 bold"), fg=co0)
pokemon_number.place(x=20, y=75)

pokemon_type.lift()
pokemon_number.lift()


#pokemon images

#pokemon_image = Image.open('Images/pikachu_pixel.png')
#pokemon_image = pokemon_image.resize((260, 260))
#pokemon_image = ImageTk.PhotoImage(pokemon_image)

#label_icon_1 = Label(window, image=pokemon_image, bg=co1)
#label_icon_1.place(x=60, y=50)

#Pikachu status
pokemon_status = Label(window, text="Status", font=("Verdana 20"), bg=co1, fg=co0)
pokemon_status.place(x=15, y=310)

pokemon_hp = Label(window, text="HP: 35", font=("Verdana 10"), bg=co1, fg=co0)
pokemon_hp.place(x=20, y=360)

pokemon_attack = Label(window, text="Attack: 55", font=("Verdana 10"), bg=co1, fg=co0)
pokemon_attack.place(x=20, y=385)

pokemon_defense = Label(window, text="Defense: 40", font=("Verdana 10"), bg=co1, fg=co0)
pokemon_defense.place(x=20, y=410)

pokemon_spatk = Label(window, text="Sp. Atk: 50", font=("Verdana 10"), bg=co1, fg=co0) #Special Attack
pokemon_spatk.place(x=20, y=435)

pokemon_spdef = Label(window, text="Sp. Def: 50", font=("Verdana 10"), bg=co1, fg=co0) #Special Defense
pokemon_spdef.place(x=20, y=460)

pokemon_speed = Label(window, text="Speed: 90", font=("Verdana 10"), bg=co1, fg=co0)
pokemon_speed.place(x=20, y=485)

pokemon_total = Label(window, text="Total: 320", font=("Verdana 10 bold"), bg=co1, fg=co0)
pokemon_total.place(x=20, y=510)

#skills

pokemon_skill = Label(window, text="Skill", font=("Verdana 20"), bg=co1, fg=co0)
pokemon_skill.place(x=180, y=310)

pokemon_hb_1 = Label(window, text="Thunderbolt", font=("Verdana 10"), bg=co1, fg=co0)
pokemon_hb_1.place(x=195, y=360)

pokemon_hb_2 = Label(window, text="Electroweb", font=("Verdana 10"), bg=co1, fg=co0)
pokemon_hb_2.place(x=195, y=385)

#Pokemons

#Pikachu
img_pokemon_1 = Image.open('Images/pikachu_head.png')
img_pokemon_1 = img_pokemon_1.resize((40, 40))
img_pokemon_1 = ImageTk.PhotoImage(img_pokemon_1)

icon_1 = Button(window, text='Pikachu', command = lambda:choose_pokemon('Pikachu'), width=150, image=img_pokemon_1, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_1.place(x=375, y=2.5) #y=10


#Bulbasaur
img_pokemon_2 = Image.open('Images/bulbasaur_head.png')
img_pokemon_2 = img_pokemon_2.resize((40, 40))
img_pokemon_2 = ImageTk.PhotoImage(img_pokemon_2)

icon_2 = Button(window, text='Bulbasaur', command = lambda:choose_pokemon('Bulbasaur'), width=150, image=img_pokemon_2, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_2.place(x=375, y=53) #y=65


#Charmander
img_pokemon_3 = Image.open('Images/charmander_head.png')
img_pokemon_3 = img_pokemon_3.resize((40, 40))
img_pokemon_3 = ImageTk.PhotoImage(img_pokemon_3)

icon_3 = Button(window, text='Charmander', command = lambda:choose_pokemon('Charmander'), width=150, image=img_pokemon_3, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_3.place(x=375, y=104) #y=120


#Gyarados
img_pokemon_4 = Image.open('Images/gyarados_head.png')
img_pokemon_4 = img_pokemon_4.resize((40, 40))
img_pokemon_4 = ImageTk.PhotoImage(img_pokemon_4)

icon_4 = Button(window, text='Gyarados', command = lambda:choose_pokemon('Gyarados'), width=150, image=img_pokemon_4, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_4.place(x=375, y=155) #y=175


#Gengar
img_pokemon_5 = Image.open('Images/gengar_head.png')
img_pokemon_5 = img_pokemon_5.resize((40, 40))
img_pokemon_5 = ImageTk.PhotoImage(img_pokemon_5)

icon_5 = Button(window, text='Gengar', command = lambda:choose_pokemon('Gengar'), width=150, image=img_pokemon_5, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_5.place(x=375, y=206) #y=230


#Dragonite
img_pokemon_6 = Image.open('Images/dragonite_head.png')
img_pokemon_6 = img_pokemon_6.resize((40, 40))
img_pokemon_6 = ImageTk.PhotoImage(img_pokemon_6)

icon_6 = Button(window, text='Dragonite', command = lambda:choose_pokemon('Dragonite'), width=150, image=img_pokemon_6, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_6.place(x=375, y=257) #y285


choose_pokemon('Pikachu')
window.mainloop()