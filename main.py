from tkinter import *
from tkinter import filedialog
from pytube import YouTube


window = Tk()
window.geometry("500x500+500+100")
window.title("YT Downloader")
window.config(bg="#121212")
photo = PhotoImage(file="Yt-logo2.png")
window.iconphoto(False, photo)
window.resizable(False, False)
dir = ""


def openloc():
    global dir
    dir = filedialog.askdirectory()

    if(len(dir) > 1):
        path_loc.config(text=dir)
    else:
        path_error.config(text="Please Choose correct Path !")


def sel():
    global selected
    selected = var.get()


def download():
    glitch.config(
        text="Please wait for a while !")
    link = textbox.get()
    if(len(link) > 1):
        yt = YouTube(link)
        if(selected == 1):
            ytvd = yt.streams.filter(progressive=True).first()
        elif(selected == 2):
            ytvd = yt.streams.filter(progressive=True).last()
        elif(selected == 3):
            ytvd = yt.streams.filter(only_audio=True).first()

    else:
        url_error.config(text="Please Enter Proper URL")

    try:
        ytvd.download(dir)
        glitch.config(text="Downloaded Successfully !")
        path_loc.config(text="\t\t\t   ")
        textbox.delete(0, "end")
        name = ytvd.title
        size = ytvd.filesize/1024000
        size = round(size, 1)
        d_file.config(text="Name : "+name)
        d_size.config(text="Size : "+str(size)+" MB")
        d_loc.config(text="Path :" + dir)
    except:
        glitch.config(text="Download Failed.Please Try Again!")


head = Label(window, text=" Youtube Video/Audio Downloader ", background="#121212",
             foreground="#BB86FC", font=("Arial Rounded MT Bold", 16, "bold"))
head.pack(anchor="center", pady=10)
url = Label(window, text="Enter URL : ", background="#121212",
            foreground="#BB86FC", font=("Arial Rounded MT Bold", 12))
url.pack(anchor="nw", padx=20, pady=18)
texturl = StringVar()
textbox = Entry(window, width=55, textvariable=texturl)
textbox.place(x=120, y=70)
url_error = Label(window, background="#121212",
                  foreground="red", font=("Arial Rounded MT Bold", 9))
url_error.place(x=240, y=100)

path = Label(window, text="Choose Path :", background="#121212",
             foreground="#BB86FC", font=("Arial Rounded MT Bold", 12))
path.pack(anchor="nw", padx=18, pady=30)

path_loc = Label(window, text="\t\t\t   ", background="white",
                 foreground="black", font=("Arial Rounded MT Bold", 9))
path_loc.place(x=140, y=146)

pathway = Button(window, width=12, text="Select Path",
                 background="#BB86FC", foreground="#3700B3", relief="sunken", activeforeground="red", activebackground="#3700B3", command=openloc)
pathway.place(x=340, y=143)
path_error = Label(window, background="#121212",
                   foreground="red", font=("Arial Rounded MT Bold", 9))
path_error.place(x=218, y=178)

download_type = Label(window, text="Download Type : ", background="#121212",
                      foreground="#BB86FC", font=("Arial Rounded MT Bold", 12))
download_type.pack(anchor="nw", padx=19, pady=34)


var = IntVar()
R1 = Radiobutton(window, activebackground="#BB86FC", activeforeground="red",  bg="#121212", fg="#BB86FC", text="High Quaity Video", variable=var, value=1,
                 command=sel
                 )
R1.place(x=168, y=229)

R2 = Radiobutton(window, activebackground="#BB86FC", activeforeground="red",  bg="#121212", fg="#BB86FC", text="Low Quality Video", variable=var, value=2,
                 command=sel
                 )
R2.place(x=168, y=255)

R3 = Radiobutton(window, activebackground="#BB86FC", activeforeground="red",  bg="#121212", fg="#BB86FC", text="Audio", variable=var, value=3,
                 command=sel
                 )
R3.place(x=168, y=279)

button_d = Button(window, text=" Download ", width="36", background="#BB86FC", foreground="#3700B3",
                  relief="sunken", activeforeground="red", activebackground="#3700B3", command=download)
button_d.pack(anchor="center", pady=36)

glitch = Label(window, background="#121212",
               foreground="red", font=("Arial Rounded MT Bold", 9))
glitch.place(x=188, y=352)


d_file = Label(window,  background="#121212",
               foreground="#BB86FC", font=("Arial Rounded MT Bold", 9))
d_file.place(x=88, y=376)


d_size = Label(window,  background="#121212",
               foreground="#BB86FC", font=("Arial Rounded MT Bold", 9))
d_size.place(x=88, y=398)

d_loc = Label(window, background="#121212",
              foreground="#BB86FC", font=("Arial Rounded MT Bold", 9))
d_loc.place(x=88, y=424)

window.mainloop()
