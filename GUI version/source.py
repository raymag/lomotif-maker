from tkinter import *
from tkinter import filedialog
import os

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.images_folder = ''
        self.audio_file = ''
        self.create_widgets()

    def create_widgets(self):
        self.images_folder_lb = Label(self, text="Diretório de Imagens")
        self.images_folder_lb.config(font=("Courier", 14))
        self.images_folder_lb.grid(row=0, column=0)
        self.images_folder_btn = Button(self, text="Selecionar", command=self.select_images)
        self.images_folder_btn['font'] = ("Courier", 10)
        self.images_folder_btn.grid(row=0, column=1)

        self.audio_file_lb = Label(self, text="Aúdio")
        self.audio_file_lb.config(font=("Courier", 14))
        self.audio_file_lb.grid(row=1, column=0)
        self.audio_file_btn = Button(self, text="Selecionar", command=self.select_audio)
        self.audio_file_btn['font'] = ("Courier", 10)
        self.audio_file_btn.grid(row=1, column=1)

        self.ren_btn = Button(self, text="Renomear Diretório", command=self.rename)
        self.ren_btn['font'] = ("Courier", 10)
        self.ren_btn.grid(row=2, column=1)
        
        self.gen_lomotif_btn = Button(self, text="Gerar Lomotif", command=self.gen_lomotif)
        self.gen_lomotif_btn['font'] = ("Courier", 10)
        self.gen_lomotif_btn.grid(row=2, column=0)
        
        self.clear_btn = Button(self, text="Limpar", command=self.clear)
        self.clear_btn['font'] = ("Courier", 10)

    def select_images(self):
        self.images_folder = filedialog.askdirectory(title="Selecionar Diretório de Imagens")
        if len(self.images_folder) > 60:
            self.images_folder_btn["text"] = self.images_folder[0:10]+"..."+self.images_folder[-50:-1]
        else:
            self.images_folder_btn["text"] = self.images_folder

        if self.images_folder == '':
            self.images_folder_btn["text"] = "Selecionar"

    def select_audio(self):
        self.audio_file = filedialog.askopenfilename(title="Selecionar Aúdio", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        if len(self.audio_file) > 60:
            self.audio_file_btn["text"] = self.audio_file[0:10]+"..."+self.audio_file[-50:-1]
        else:
            self.audio_file_btn["text"] = self.audio_file

        if self.audio_file == '':
            self.audio_file_btn["text"] = "Selecionar"

    def gen_lomotif(self):
        save_directory = 'mmk_movie_{}'
        i = 1
        while os.path.isdir(self.images_folder+'/'+save_directory.format(i)):
            i+=1
        save_directory = save_directory.format(i)
        os.mkdir(self.images_folder+'/'+save_directory)
        destiny = self.images_folder+'/'+save_directory+'/'
        
        img_total = 0
        for filename in os.listdir(self.images_folder):
            f = filename.split('.')
            if f[-1] == 'jpg':
                img_total+=1

        try:
            os.system('ffmpeg -f image2 -r 4/5 -i "{}" -vcodec mjpeg -b 5000 -q:v 1 -y "{}"'.format(self.images_folder+'/img_%01d.jpg', destiny+'mute.avi'))
            os.system('ffmpeg -i "{}" -i "{}" -codec copy -shortest "{}"'.format(destiny+'mute.avi', self.audio_file, destiny+'movie.avi'))
            os.remove(destiny+'mute.avi')
        except:
            pass
        os.system('explorer "{}"'.format(destiny.replace('/', '\\').replace('\\\\', '\\')))
    
    def rename(self):
        save_directory = 'mmk_pics_{}'
        i = 1
        while os.path.isdir(self.images_folder+'/'+save_directory.format(i)):
            i+=1
        save_directory = save_directory.format(i)
        os.mkdir(self.images_folder+'/'+save_directory)
        i=1
        destiny = self.images_folder+'/'+save_directory+'/'
        for filename in os.listdir(self.images_folder):
            f_ext = filename.split('.')[-1]
            if f_ext == 'jpg' or f_ext == 'jpeg' or f_ext == 'png':
                new_filename = 'img_'+str(i)+'.jpg'
                os.rename(self.images_folder+'/'+filename, '{}{}'.format(destiny, new_filename))
                i+=1
        i -= 1
        self.images_folder = destiny
        if len(self.images_folder) > 60:
            self.images_folder_btn["text"] = self.images_folder[0:10]+"..."+self.images_folder[-50:-1]
        else:
            self.images_folder_btn["text"] = self.images_folder
        os.system('explorer "{}"'.format(destiny.replace('/', '\\').replace('\\\\', '\\')))


    def clear(self):
        self.images_folder_btn["text"] = "Selecionar"
        self.images_folder = ""
        self.audio_file_btn["text"] = "Selecionar"
        self.audio_file = ""

app = App()
app.master.title("Lomotif Maker")
app.master.minsize(400, 150)
        
app.mainloop()
