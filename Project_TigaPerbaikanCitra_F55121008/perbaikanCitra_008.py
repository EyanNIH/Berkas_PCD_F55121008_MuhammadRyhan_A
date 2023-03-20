import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

class ImageEditor:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Perbaikan Citra")

        self.canvas_width = 900
        self.canvas_height = 500

        # Buat kanvas untuk menampilkan gambar
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        # Buat tombol untuk metode peningkatan citra
        self.button_sharpen = tk.Button(master, text="Pertajam", command=self.sharpen_image)
        self.button_sharpen.pack(side=tk.LEFT, padx=10)

        self.button_blur = tk.Button(master, text="Buram", command=self.blur_image)
        self.button_blur.pack(side=tk.LEFT, padx=10)

        self.button_brighten = tk.Button(master, text="Tambah Kecerahan", command=self.brighten_image)
        self.button_brighten.pack(side=tk.LEFT, padx=10)

        #  Tombol "Buka gambar" untuk membuka file gambar
        self.button_open = tk.Button(master, text="Buka Gambar", command=self.open_image)
        self.button_open.pack(side=tk.BOTTOM, pady=10)

    def open_image(self):
        # Buka dialog file untuk memilih file gambar
        file_path = filedialog.askopenfilename()

        # Buka gambar menggunakan package pillow
        self.image = Image.open(file_path)

        # Ubah ukuran gambar agar pas dengan kanvas
        self.image = self.image.resize((self.canvas_width, self.canvas_height))

        # Ubah gambar menjadi format Tkinter PhotoImage untuk ditampilkan di kanvas
        self.image_tk = ImageTk.PhotoImage(self.image)

        # Tampilkan gambar di atas kanvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

    def sharpen_image(self):
        # Terapkan filter pertajam ke gambar
        self.image = self.image.filter(ImageFilter.SHARPEN)

        # Perbarui gambar yang ditampilkan
        self.update_image()

    def blur_image(self):
        # Terapkan filter buram ke gambar
        self.image = self.image.filter(ImageFilter.BLUR)

        # Perbarui gambar yang ditampilkan
        self.update_image()

    def brighten_image(self):
        # Buat penambah kecerahan
        enhancer = ImageEnhance.Brightness(self.image)

        # Terapkan peningkatan kecerahan ke gambar
        self.image = enhancer.enhance(1.5)

        # Perbarui gambar yang ditampilkan
        self.update_image()

    def update_image(self):
        # Ubah ukuran gambar yang diperbarui agar pas dengan kanvas
        self.image = self.image.resize((self.canvas_width, self.canvas_height))

        # Ubah gambar yang diperbarui ke format Tkinter PhotoImage untuk ditampilkan di kanvas
        self.image_tk = ImageTk.PhotoImage(self.image)

        # Perbarui gambar yang ditampilkan di kanvas
        self.canvas.itemconfig(self.canvas.find_all()[0], image=self.image_tk)
# Buat jendela aplikasi
root = tk.Tk()
# Buat instance kelas ImageEditor
app = ImageEditor(root)
# Mulai putaran aplikasi
root.mainloop()
