import tkinter

def b(pos_h, pos_v, k): # Bandinieka kustības atzīmēšana
    if k == 'white': # Balta kustība
        if pos_v == 2: # Sākuma līnija, no kuras var aiziet tālāk
            c.create_oval(25+(pos_h-1)*70, 535-(pos_v+2-1)*70, 45+(pos_h-1)*70, 515-(pos_v+2-1)*70)
        c.create_oval(25+(pos_h-1)*70, 535-(pos_v)*70, 45+(pos_h-1)*70, 515-(pos_v)*70)
        # Krustiņi bandinieka nosišanas gājienam
        c.create_line(25+(pos_h)*70, 535-(pos_v)*70, 45+(pos_h)*70, 515-(pos_v)*70)    
        c.create_line(25+(pos_h)*70, 515-(pos_v)*70, 45+(pos_h)*70, 535-(pos_v)*70)
        c.create_line(25+(pos_h-2)*70, 535-(pos_v)*70, 45+(pos_h-2)*70, 515-(pos_v)*70)    
        c.create_line(25+(pos_h-2)*70, 515-(pos_v)*70, 45+(pos_h-2)*70, 535-(pos_v)*70) 
    elif k == 'black': # Melna kustība
        if pos_v == 7: # Sākuma līnija, no kuras var aiziet tālāk
            c.create_oval(25+(pos_h-1)*70, 535-(pos_v-2-1)*70, 45+(pos_h-1)*70, 515-(pos_v-2-1)*70)
        c.create_oval(25+(pos_h-1)*70, 535-(pos_v-1-1)*70, 45+(pos_h-1)*70, 515-(pos_v-1-1)*70)
        # Krustiņi bandinieka nosišanas gājienam
        c.create_line(25+(pos_h)*70, 535-(pos_v-1-1)*70, 45+(pos_h)*70, 515-(pos_v-1-1)*70)    
        c.create_line(25+(pos_h)*70, 515-(pos_v-1-1)*70, 45+(pos_h)*70, 535-(pos_v-1-1)*70)
        c.create_line(25+(pos_h-2)*70, 535-(pos_v-1-1)*70, 45+(pos_h-2)*70, 515-(pos_v-1-1)*70)    
        c.create_line(25+(pos_h-2)*70, 515-(pos_v-1-1)*70, 45+(pos_h-2)*70, 535-(pos_v-1-1)*70) 


def parbaude(a): # Datu korektības pārbaude (vesels skaitlis)
    try:
        a = int(a)
        return 't'
    except:
        return 'f'


def entry():
    # Laukuma atjaunošana pēc pogas piespiešanas
    c.delete('all')
    
    for i in range(1, 9):
        for j in range(1, 9):
            if (i + j)%2 != 0:
                c.create_rectangle(70*j - 70, 70*i - 70, 70*j, 70*i, fill='grey', outline='grey')   
                
    for i in range(8, 0, -1):
        l = tkinter.Label(w, text=f'{i}')
        l.place(x=20, y=45+(8-i)*70)
        
    for i in range(1, 9):
        l = tkinter.Label(w, text=f'{i}')
        l.place(x=65+(i-1)*70, y=590)    
        
    f = e1.get()
    k = e2.get()
    pos_v = e3.get()
    pos_h = e4.get()
    
    # Datu korektības pārbaude
    p1 = parbaude(pos_v)
    p2 = parbaude(pos_h)
    
    if p1 == 'f' or p2 == 'f':
        exit()
    else:
        pos_v = int(pos_v)
        pos_h = int(pos_h)
        
    #print('ku')
    #print(pos_v, pos_h)
    #print(f)
                    
    if pos_v < 1 or pos_h < 1:
        exit()
    elif pos_v > 8 or pos_h > 8:
        exit()
    
    # Krāsas nosaukuma maiņa
    if k == 'm':
        k = 'black'
    elif k == 'b':
        k = 'white'
    else:
        exit()
    
    # Figūras izvietošana laukumā
    c.create_rectangle(25+(pos_h-1)*70, 535-(pos_v-1)*70, 45+(pos_h-1)*70, 515-(pos_v-1)*70, fill=k, outline='black')      
    
    # Figūras gājienu zimēšana
    if f == 't': # tornis
        tornis(pos_h, pos_v)
    elif f == 'l': # laidnis
        laidnis(pos_h, pos_v)
    elif f == 'd': # dāma (kustās kā tornis un laidnis kopā)
        tornis(pos_h, pos_v)
        laidnis(pos_h, pos_v)
    elif f == 'k': # karalis
        karalis(pos_h, pos_v)
    elif f == 'b': # bandinieks
        if k == 'white': # balta pārbaude uz neiespējamo atrašanas vietu
            if pos_v == 1:
                c.create_line(25+(pos_h-1)*70, 535-(pos_v-1)*70, 45+(pos_h-1)*70, 515-(pos_v-1)*70, fill='red', width='10')    
                c.create_line(25+(pos_h-1)*70, 515-(pos_v-1)*70, 45+(pos_h-1)*70, 535-(pos_v-1)*70, fill='red', width='10')
            else:
                b(pos_h, pos_v, k)
        elif k == 'black': # melna pārbaude uz neiespējamo atrašanas vietu
            if pos_v == 8:
                c.create_line(25+(pos_h-1)*70, 535-(pos_v-1)*70, 45+(pos_h-1)*70, 515-(pos_v-1)*70, fill='red', width='10')    
                c.create_line(25+(pos_h-1)*70, 515-(pos_v-1)*70, 45+(pos_h-1)*70, 535-(pos_v-1)*70, fill='red', width='10') 
            else:
                b(pos_h, pos_v, k)
    elif f == 'z': # zirdziņš
        zirdzins(pos_h, pos_v, k)
    else:
        exit()
    
def tornis(pos_h, pos_v): # Torņa kustības atzīmēšana
    for i in range(1, 9):
        for j in range(1, 9):
            if i == pos_v and j == pos_h: # Nezīmē gājienu figūras atrašanas vietā
                continue
            else:
                if i == pos_v:
                    c.create_oval(25+(j-1)*70, 535-(i-1)*70, 45+(j-1)*70, 515-(i-1)*70)            
                if j == pos_h:
                    c.create_oval(25+(j-1)*70, 535-(i-1)*70, 45+(j-1)*70, 515-(i-1)*70)
                    
def laidnis(pos_h, pos_v): # Laidņa kustības atzīmēšana
    for i in range(1, 9):
        for j in range(1, 9):
            if i == pos_v and j == pos_h: # Nezīmē gājienu figūras atrašanas vietā
                continue
            else:
                if i < pos_v:
                    a = pos_v - i
                else:
                    a = i - pos_v
                if j < pos_h:
                    b = pos_h - j
                else:
                    b = j - pos_h
                if a == b:
                    c.create_oval(25+(j-1)*70, 535-(i-1)*70, 45+(j-1)*70, 515-(i-1)*70)
                
def karalis(pos_h, pos_v): # Karaļa kustības atzīmēšana
    for i in range(1, 9):
        for j in range(1, 9):
            if i == pos_v and j == pos_h: # Nezīmē gājienu figūras atrašanas vietā
                continue
            else:
                if i == pos_v + 1:
                    if j == pos_h - 1 or j == pos_h or j == pos_h + 1:
                        c.create_oval(25+(j-1)*70, 535-(i-1)*70, 45+(j-1)*70, 515-(i-1)*70)
                elif i == pos_v:
                    if j == pos_h - 1 or j == pos_h + 1:
                        c.create_oval(25+(j-1)*70, 535-(i-1)*70, 45+(j-1)*70, 515-(i-1)*70)
                elif i == pos_v -1:
                    if j == pos_h - 1 or j == pos_h or j == pos_h + 1:
                        c.create_oval(25+(j-1)*70, 535-(i-1)*70, 45+(j-1)*70, 515-(i-1)*70)      
                else:
                    continue
   
        
def zirdzins(pos_h, pos_v, k): # Zirdziņa kustības atzīmēšana
    if k == 'white' and pos_v == 1 and (pos_h == 2 or pos_h == 7): # Sākuma pozīcija spēlē 
        c.create_oval(25+(pos_h-2)*70, 535-(pos_v+1)*70, 45+(pos_h-2)*70, 515-(pos_v+1)*70)
        c.create_oval(25+(pos_h)*70, 535-(pos_v+1)*70, 45+(pos_h)*70, 515-(pos_v+1)*70)
    elif k == 'black' and pos_v == 8 and (pos_h == 2 or pos_h == 7): # Sākuma pozīcija spēlē 
        c.create_oval(25+(pos_h-2)*70, 535-(pos_v-3)*70, 45+(pos_h-2)*70, 515-(pos_v-3)*70)
        c.create_oval(25+(pos_h)*70, 535-(pos_v-3)*70, 45+(pos_h)*70, 515-(pos_v-3)*70)    
    else:
        c.create_oval(25+(pos_h-2)*70, 535-(pos_v+1)*70, 45+(pos_h-2)*70, 515-(pos_v+1)*70)
        c.create_oval(25+(pos_h)*70, 535-(pos_v+1)*70, 45+(pos_h)*70, 515-(pos_v+1)*70)   
        c.create_oval(25+(pos_h-2)*70, 535-(pos_v-3)*70, 45+(pos_h-2)*70, 515-(pos_v-3)*70)
        c.create_oval(25+(pos_h)*70, 535-(pos_v-3)*70, 45+(pos_h)*70, 515-(pos_v-3)*70)  
        c.create_oval(25+(pos_h-3)*70, 535-(pos_v)*70, 45+(pos_h-3)*70, 515-(pos_v)*70)
        c.create_oval(25+(pos_h+1)*70, 535-(pos_v-2)*70, 45+(pos_h+1)*70, 515-(pos_v-2)*70)   
        c.create_oval(25+(pos_h-3)*70, 535-(pos_v-2)*70, 45+(pos_h-3)*70, 515-(pos_v-2)*70)
        c.create_oval(25+(pos_h+1)*70, 535-(pos_v)*70, 45+(pos_h+1)*70, 515-(pos_v)*70)        

# Loga ģenerēšana
w = tkinter.Tk()
w.geometry('620x720')

# Kanvas ģenerēšana
c = tkinter.Canvas(w, width=560, height=560, background='white')
c.place(x=40, y=20)

# Laukuma zīmēšana
for i in range(1, 9):
    for j in range(1, 9):
        if (i + j)%2 != 0:
            c.create_rectangle(70*j - 70, 70*i - 70, 70*j, 70*i, fill='grey', outline='grey')   
            
for i in range(8, 0, -1):
    l = tkinter.Label(w, text=f'{i}')
    l.place(x=20, y=45+(8-i)*70)
    
for i in range(1, 9):
    l = tkinter.Label(w, text=f'{i}')
    l.place(x=65+(i-1)*70, y=590)
    
l1 = tkinter.Label(w, text='Ievadiet figūras veidu (b, d, k, t, l, z) --> ')
l1.place(x=25, y=620)

e1 = tkinter.Entry(w)
e1.place(x=240, y=620, width=20, height=20)

l2 = tkinter.Label(w, text='Ievadiet figūras krāsu (b, m) --> ')
l2.place(x=25, y=640)

e2 = tkinter.Entry(w)
e2.place(x=200, y=640, width=20, height=20)

l3 = tkinter.Label(w, text='Ievadiet pozīciju vertikāli --> ')
l3.place(x=25, y=660)

e3 = tkinter.Entry(w)
e3.place(x=180, y=660, width=20, height=20)

l4 = tkinter.Label(w, text='Ievadiet pozīciju horizontāli --> ')
l4.place(x=25, y=680)

e4 = tkinter.Entry(w)
e4.place(x=195, y=680, width=20, height=20)

b1 = tkinter.Button(w, text='Paradīt iespējamos gājienus', command=entry)
b1.place(x=280, y=640, width=155, height=25)

w.mainloop()