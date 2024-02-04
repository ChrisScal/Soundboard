import tkinter as tk
import pygame 
import os, sys
import linecache as linecache
pygame.mixer.init()
#Sfx library generator apo ton fakelo sounds
def sfx_dictionary_gen(dictionary=dict):
    for i in enumerate(os.listdir('Sounds')):
        temp_list = [i[1][2:-4],'Sounds/'+i[1],0.1]
        dictionary[i[0]+1]=temp_list


class ButtonGrid():
    #Button Grid gia ta sfx
    def __init__(self, root ,sfx_library,rows=int,collumns=int):
        self.root=root
        
        self.sfx_lib=sfx_library
        
        self.frame=tk.Frame(self.root)

        button1=tk.Button(self.frame,text=self.sfx_lib[1][0],command= lambda:self.play_sfx(self.sfx_lib[1][1],self.sfx_lib[1][2]))
        button1.grid(row=0,column=0,sticky='news')
        
        button2=tk.Button(self.frame,text=self.sfx_lib[2][0],command= lambda:self.play_sfx(self.sfx_lib[2][1],self.sfx_lib[2][2]))
        button2.grid(row=0,column=1,sticky='news')
        
        button3=tk.Button(self.frame,text=self.sfx_lib[3][0],command= lambda:self.play_sfx(self.sfx_lib[3][1],self.sfx_lib[3][2]))
        button3.grid(row=0,column=2,sticky='news')
        
        button4=tk.Button(self.frame,text=self.sfx_lib[4][0],command= lambda:self.play_sfx(self.sfx_lib[4][1],self.sfx_lib[4][2]))
        button4.grid(row=1,column=0,sticky='news')
        
        button5=tk.Button(self.frame,text='idk')
        button5.grid(row=1,column=1,sticky='news')
        
        button6=tk.Button(self.frame,text='Idk')
        button6.grid(row=1,column=2,sticky='news')
        
        self.frame.rowconfigure(tuple(range(rows)),weight=1)
        self.frame.columnconfigure(tuple(range(collumns)),weight=1)

        self.frame.pack(expand=1,fill='both')
    
    def play_sfx(self,sfx,sfx_volume):
        pygame.mixer.music.set_volume(sfx_volume)
        pygame.mixer.music.load(sfx)
        pygame.mixer.music.play(loops=0)

class Settings_Box():
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry('350x200')
        self.window.title('Default Settings')
        self.frame = tk.Frame(self.window)
        #Label
        info_label=tk.Label(self.window, text='Εισάγετε τα default rows, collumns και dimensions.')
        info_label.pack(pady=10)
        
        #Row Entry+Label
        self.rows=tk.StringVar()
        row_label=tk.Label(self.frame,text='Rows σε ακέραιο:')
        row_entry=tk.Entry(self.frame,textvariable=self.rows)
        row_label.grid(row=0,column=0)
        row_entry.grid(row=0,column=1)
        
        #Collumn Entry+Label
        self.collumns=tk.StringVar()
        collumn_label=tk.Label(self.frame,text='Collumns σε ακέραιο:')
        collumn_entry=tk.Entry(self.frame,textvariable=self.collumns)
        collumn_label.grid(row=1,column=0)
        collumn_entry.grid(row=1,column=1)
    
        #Dimensions Entry+Label
        self.dimensions=tk.StringVar()
        dimension_label=tk.Label(self.frame,text='Dimensions χωρισμένα με x:')
        dimension_entry=tk.Entry(self.frame,textvariable=self.dimensions)
        dimension_label.grid(row=2,column=0)
        dimension_entry.grid(row=2,column=1)
        
        #Apply
        apply_button=tk.Button(self.frame,text='Apply',command=lambda:self.settings_apply(True))
        apply_button.grid(row=3,column=0,pady=10,padx=10,sticky='news')
        
        
        #Default
        default_button=tk.Button(self.frame,text='Default',command=lambda:self.settings_apply(False))
        default_button.grid(row=3,column=1,pady=10,padx=10,sticky='news')
        
        #Quit
        quit_button=tk.Button(self.frame,text='Quit',command=lambda:self.quit())
        quit_button.grid(row=3,column=2,pady=10,padx=10,sticky='news')
        
        self.frame.rowconfigure(tuple(range(4)),weight=1)
        self.frame.columnconfigure(tuple(range(3)),weight=1)
        self.frame.pack(expand=1,fill='both')
        self.window.mainloop()
        
    def settings_apply(self,apply_or_default):
        if apply_or_default==True:
            f=open('Settings.txt','w')
            f.write(f'--Sfx dictionary--(Name, Path ,Volume)\nsfx=\n--Rows and Collumns--\nRows:{self.rows.get()}\nCollumns:{self.collumns.get()}\n--Dimensions--(WidthxHeight)\n{self.dimensions.get()}\n')
            f.close()
            self.window.destroy()
        else:
            f=open('Settings.txt','w')
            f.write(f'--Sfx dictionary--(Name, Path ,Volume)\nsfx=\n--Rows and Collumns--\nRows:2\nCollumns:3\n--Dimensions--(WidthxHeight)\n450x300\n')
            f.close()
            self.window.destroy()
            
    def quit(self):
        sys.exit()

#Elegxos an proyparxei etoimo sfx library sta settings
if 'Settings.txt' not in os.listdir():
    Settings_Box()

#Diabasma apo to Setting.txt
sfx_dictionary_line = linecache.getline('Settings.txt',2).strip('\n')
rows_line=int(linecache.getline('Settings.txt',4)[5])
collumns_line=int(linecache.getline('Settings.txt',5)[9])
dimensions_line = linecache.getline('Settings.txt',7).strip('\n')

    #Alliws
sfx={}
sfx_dictionary_gen(sfx)

#Root window
root = tk.Tk()
root.geometry(dimensions_line) 
root.title('Sound Board')
root.config(bg='skyblue')

ButtonGrid(root,sfx,rows_line,collumns_line)

#Telos prog
root.mainloop()