from tkinter import *
import tkinter.filedialog as tk_fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

image_path = ""
watermark_text = ""
img_in = Image
img_out = Image


def open_image():
    global img_in, image_path

    image_path = tk_fd.askopenfilename()

    img_in = Image.open(image_path)
    render_user_img = ImageTk.PhotoImage(img_in.resize((500, 500), Image.ANTIALIAS))

    panel = Label(desk_app, image=render_user_img)
    panel.image = render_user_img
    panel.grid(column=0, row=1)


def watermark():
    global img_in, img_out, watermark_text

    watermark_text = entry_text.get()

    img_in = img_in.convert("RGBA")

    txt = Image.new("RGBA", img_in.size, (255, 255, 255, 0))

    fnt = ImageFont.truetype("fonts/IndieFlower-Regular.ttf", 30)

    d = ImageDraw.Draw(txt)
    d.text((10, 10), watermark_text, font=fnt, fill=(255, 255, 255, 128))

    img_out = Image.alpha_composite(img_in, txt)

    # Show on GUI
    render_img_in = ImageTk.PhotoImage(img_out.resize((500, 500), Image.ANTIALIAS))

    panel = Label(desk_app, image=render_img_in)
    panel.image = render_img_in
    panel.grid(column=1, row=1)


def save_image():
    global image_path, img_out, watermark_text

    image_name = image_path.split('/')[-1].split(".")[0] + "WM_" + watermark_text
    print(image_name)
    img_out.save(f"Image with watermark/{image_name}.png")


desk_app = Tk(screenName="Image Watermarking")
desk_app.title("Img Watermarking")
desk_app.config(bg="#2966C9")
desk_app.geometry("1008x650")
desk_app.maxsize(1008, 650)

entry_text = Entry(width=70)
entry_text.insert(0, "Text Watermark")
entry_text.grid(column=0, row=0, columnspan=2, pady=15)

# Canvas for image selected
Canvas(bg="#2980B9", width=500, height=500).grid(column=0, row=1)

# Canvas for image generated
Canvas(bg="#2980B9", width=500, height=500).grid(column=1, row=1)

# Button to select an img file
select_file_button = Button(text="Select an image", command=open_image, highlightthickness=0)
select_file_button.grid(column=0, row=2, pady=10)

# Button to select an img file
select_file_button = Button(text="Apply watermark", command=watermark, highlightthickness=0)
select_file_button.grid(column=1, row=2, pady=10)

# Button to save an img file
select_file_button = Button(text="Save image", command=save_image, highlightthickness=0)
select_file_button.grid(column=0, row=3, columnspan=2, pady=15)


desk_app.mainloop()
