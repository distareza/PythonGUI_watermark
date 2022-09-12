# https://pillow.readthedocs.io/en/latest/handbook/tutorial.html
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

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
    img_width, img_height = img.size

    logo_img_path = "C:/tmp/ItIsMeDistaReza-circle.png"
    logo_img = Image.open(logo_img_path)
    margin = 5
    logo_img.thumbnail(size=( img_width/10, img_height/10 )) # logo 10% of the image

    logo_width, logo_height = logo_img.size
    img.paste(logo_img, (img_width-logo_width-margin, img_height-logo_height-margin))

    draw = ImageDraw.Draw(img)
    text = "copyright© 2022 Dista Reza"
    font = ImageFont.truetype("arial", 36)
    text_x, text_y, text_width, text_height = font.getbbox(text)
    text_pos = ( margin, img_height - text_height - margin)
    text_color = (255,255, 255)
    draw.text(text_pos, text, text_color, font)

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