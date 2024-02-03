import tkinter as tk
import pygame 
pygame.mixer.init()

class ButtonGrid():
    #Button Grid gia ta sfx
    def __init__(self, root ,sfx_library):
        self.root=root
        self.sfx_lib=sfx_library
            
        button1=tk.Button(self.root,text=self.sfx_lib[1][9:18],command= lambda:self.play_sfx(self.sfx_lib[1]))
        button1.place(x=0,y=0,width=150,height=150)
        
        button2=tk.Button(self.root,text=self.sfx_lib[2][9:19],command= lambda:self.play_sfx(self.sfx_lib[2]))
        button2.place(x=150,y=0,width=150,height=150)
        
        button3=tk.Button(self.root,text=self.sfx_lib[3][9:25],command= lambda:self.play_sfx(self.sfx_lib[3]))
        button3.place(x=300,y=0,width=150,height=150)
        
        button4=tk.Button(self.root,text=self.sfx_lib[4][9:20],command= lambda:self.play_sfx(self.sfx_lib[4]))
        button4.place(x=0,y=150,width=150,height=150)
        
        button5=tk.Button(self.root,text='idk')
        button5.place(x=150,y=150,width=150,height=150)
        
        button6=tk.Button(self.root,text='Idk')
        button6.place(x=300,y=150,width=150,height=150)
    
    def play_sfx(self,sfx):
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load(sfx)
        pygame.mixer.music.play(loops=0)

#Sfx library
sfx_lib = {1:'Sounds/1.Vine boom.mp3',4:'Sounds/4.Fart reverb.mp3',3:'Sounds/3.Finnish Hospital.mp3',2:'Sounds/2.Metal pipe.mp3'}


#Root window
root = tk.Tk()
#150X150 ta dimensions ana button sto grid, an prostheseis button anebase ta dimensions
root.geometry('450x300') 
root.title('Sound Board')
ButtonGrid(root,sfx_lib)


#Telos prog
root.mainloop()