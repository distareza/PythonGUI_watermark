# https://pillow.readthedocs.io/en/latest/handbook/tutorial.html
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, PSDraw

window = tkinter.Tk()
window.title("Python GUI Program")
window.minsize(width=640, height=480)
window.config(padx=50, pady=50)

labelFileName = tkinter.Label()
open_button = tkinter.Button(text='Open a File')
labelImageFrame = tkinter.Label()
watermark_button = tkinter.Button(text="Watermarking", state="disable")
saveimage_button = tkinter.Button(text="save", state="disable")

img = None
def select_file():
    filetypes = (
        ('image files', '*.jpg *.jpeg *.png'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)


    try:
        labelFileName.config(text=filename)
        global img
        img = Image.open(filename)
        img.filename = filename
        print(f"opening image: \"{filename}\"")
        print(f"format: {img.format}, size: {img.size}, mode: {img.mode}")

        showImage(img)
        watermark_button.config(state="normal")
        saveimage_button.config(state="normal")
    except Exception as ex:
        messagebox.showerror("Fail to open image", ex)

def showImage(img):
    thumbImg = img.copy()
    thumbImg.thumbnail(size=(400, 400)) # make thumbnail
    photoImg = ImageTk.PhotoImage(thumbImg)
    labelImageFrame.config(image=photoImg)
    labelImageFrame.image = photoImg

def watermarking():
    global img
    logo_img_path = "C:/tmp/ItIsMeDistaReza-circle.png"
    logo_img = Image.open(logo_img_path)

    img_width = img.size[0]
    img_height = img.size[1]
    logo_width = logo_img.size[0]
    logo_height = logo_img.size[1]

    img.paste(logo_img, (img_width-logo_width, img_height-logo_height))

    showImage(img)

def save_file():
    global img
    img_save_filename= ".".join(img.filename.split(".")[:-1]) + "-copy." + img.filename.split(".")[-1]
    print(f"saving as {img_save_filename}")
    img.save(img_save_filename)

open_button.config(command=select_file)
watermark_button.config(command=watermarking)
saveimage_button.config(command=save_file)

tkinter.Label(text="Watermark Image", font=('Arial 16')).grid(row=0, column=0, columnspan=3)
open_button.grid(row=2, column=1)
labelFileName.grid(row=2, column=2)
labelImageFrame.grid(row=3, column=1, columnspan=3)
watermark_button.grid(row=4, column=1)
saveimage_button.grid(row=4, column=2)


window.mainloop()