import numpy as np # import library numpy
import imageio #membaca dan menulis berbagai data gambar
import matplotlib.pyplot as plt #mengimpor modul pyplot dari matplotlib ke namespace dengan nama lebih pendek plt .
img = imageio.imread("gambar4.jpg") #Untuk membaca gambar

#
img_height = img.shape[0] #Tinggi mewakili jumlah baris piksel dalam gambar atau jumlah piksel dalam setiap kolom array gambar.
img_width = img.shape[1]#Lebar mewakili jumlah kolom piksel dalam gambar atau jumlah piksel di setiap baris array gambar.
img_channel = img.shape[2]#Jumlah Saluran mewakili jumlah komponen yang digunakan untuk mewakili setiap piksel.
img_type = img.dtype #bekerja secara default dengan array numpy.

#membuat gambar flip vertical/horizontal
img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)
#membuat gambar menjadi horizontal dengan ketentuan yang telah ditentukan yaitu 0
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]
#membuat gambar menjadi vertical dengan ketentuan yang telah ditentukan yaitu 0
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]

plt.imshow(img_flip_horizontal)#menampilkan gambar horizontal
plt.title("Flip Horizontal")#menampilkan tulisan
plt.show() #untuk memanggil library
plt.imshow(img_flip_vertical)#menampilkan gambar vertikal
plt.title("Flip Vertical") #menampilkan tulisan
plt.show() #untuk memanggil library