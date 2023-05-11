import numpy as np # import library numpy
import imageio #membaca dan menulis berbagai data gambar
import matplotlib.pyplot as plt  #mengimpor modul pyplot dari matplotlib ke namespace dengan nama lebih pendek plt .

img = imageio.imread("gambar4.jpg") #Untuk membaca gambar
img_height = img.shape[0] #Tinggi mewakili jumlah baris piksel dalam gambar atau jumlah piksel dalam setiap kolom array gambar.
img_width = img.shape[1] #Lebar mewakili jumlah kolom piksel dalam gambar atau jumlah piksel di setiap baris array gambar.
img_channel = img.shape[2] #Jumlah Saluran mewakili jumlah komponen yang digunakan untuk mewakili setiap piksel.

img_grayscale = np.zeros(img.shape, dtype=np.uint8)
#diatur range
for y in range(0, img_height): #variabel y range 0
    for x in range(0, img_width):#variabel x lebar 0
        red = img[y][x][0] #red
        green = img[y][x][1] #green
        blue = img[y][x][2] #blue
        gray = (int(red) + int(green) + int(blue)) / 3 #gray int rgb
        img_grayscale[y][x] = (gray, gray, gray) #grayscale
        
plt.imshow(img_grayscale) #Fungsi matplotlib imshow () membantu menampilkan gambar. Tetapi plt.imshow () tidak berfungsi tanpa fungsi mpimg.imread ()
plt.title("Grayscale") #menampilkan tulisan
plt.show() #untuk memanggil library

#hg nya dibuat di range 256
hg = np.zeros((256))
#range x
for x in range(0, 256):#variabel x di range 0-256
    hg[x] = 0
#range y
for y in range(0, img_height): #variabel yketinggiannya 0
    for x in range(0, img_width): #untuk variabel x di range 0
        gray = img_grayscale[y][x][0]#grey scale
        hg[gray] += 1 #hg gray

# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()

bins = np.linspace(0, 256, 100)# membagi seluruh rentang nilai menjadi serangkaian interval
plt.hist(hg, bins, color="black", alpha=0.5)#untuk memplot histogram.
plt.title("Histogram") #menampilkan tulisan
plt.show() #untuk memanggil library
#Pada numpy, np.zeros dipakai untuk membuat array baru yang diisi dengan angka 0 sebanyak 640 secara vertikal (height) dan 480 secara horizontal (width). Karena berisi angka 0, maka jendela akan menghasilkan warna hitam. Dengan begitu jika kita ingin mendapatkan warna lain, misalnya warna putih, maka nilai di dalam img perlu ditambah dengan 255.
hgr = np.zeros((256))#membuat variabel red dengan nilai 256
hgg = np.zeros((256))#membuat variabel green dengan nilai 256
hgb = np.zeros((256))#membuat variabel blue dengan nilai 256
hgrgb = np.zeros((768))#membuat variabel rgb dengan nilai 256
#range x dimulai dari 0 warna hitam dan 256 putih
for x in range(0, 256):
    hgr[x] = 0 #histogram red
    hgg[x] = 0 #histogram green
    hgb[x] = 0 #histogram blue
#x berada pada range 0-768    
for x in range(0, 768):
    hgrgb[x] = 0 #histogram rgb
#range x dimulai dari 0-256
for x in range(0, 256):
    hgr[x] = 0 #histogram red
    hgg[x] = 0 #histogram green
    hgb[x] = 0 #histogram blue
# range x dimulai dari 0-768
for x in range(0, 768): # variabel x 0-768
    hgrgb[x] = 0 #histogram rgb

# th = int(256/64)
temp = [0] #temp =0
for y in range(0, img.shape[0]): #variabel y 
    for x in range(0, img.shape[1]):# variabel x
        red = int(img[y][x][0])#red
        green = int(img[y][x][1])#green
        blue = int(img[y][x][2])#blue
        green = green + 256#green
        blue = blue + 512#blue
# temp.append(green)
        hgrgb[red] += 1#histogram red
        hgrgb[green] += 1#histogram green
        hgrgb[blue] += 1#histogram blue

binsrgb = np.linspace(0, 768, 100) # membagi seluruh rentang nilai menjadi serangkaian interval
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)#untuk memplot histogram.
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue") #menampilkan tulisan
plt.show() #untuk memanggil library
#membuat range
for y in range(0, img_height):#variabel y pada ketinggian 0
    for x in range(0, img_width):#variabel x lebar nya di range 0
        red = img[y][x][0] #red 
        green = img[y][x][1]#green
        hgr[red] += 1 #histogram red
        hgg[green] += 1 #histogram green
        hgb[blue] += 1 #histogram blue

bins = np.linspace(0, 256, 100) # membagi seluruh rentang nilai menjadi serangkaian interval
plt.hist(hgr, bins, color="red", alpha=0.5)#untuk memplot histogram.
plt.title("Histogram Red") #menampilkan tulisan
plt.show() #untuk memanggil library

plt.hist(hgg, bins, color="green", alpha=0.5)#untuk memplot histogram.
plt.title("Histogram Green") #menampilkan tulisan
plt.show() #untuk memanggil library

plt.hist(hgb, bins, color="blue", alpha=0.5) #untuk memplot histogram.
plt.title("Histogram Blue") #menampilkan tulisan
plt.show() #untuk memanggil library
#range hgk 256
hgk = np.zeros((256))#histogram kualitatif
c = np.zeros((256))
#range x dimulai dari 0-256
for x in range(0, 256):#variabel x range 0-256
    hgk[x] = 0 #histogram kualitatif
    c[x] = 0
#range y
for y in range(0, img_height): #variabel y
    for x in range(0, img_width): #variabel x
        gray = img_grayscale[y][x][0] #gray
        hgk[gray] += 1 #histogram kumulatif gray
                
c[0] = hgk[0] #histogram kualitatif
for x in range(1, 256):#variabel x range 1-256
     c[x] = c[x-1] + hgk[x]

hmaxk = c[255]
#untuk x range 0-256
for x in range(0, 256): #variabel x range 0-256
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5) #untuk memplot histogram.
plt.title("Histogram Grayscale Kumulatif") #menampilkan tulisan
plt.show() #untuk memanggil library

hgh = np.zeros((256))#histogram hequalisasi
h = np.zeros((256))#256
c = np.zeros((256))#256
#untuk x di range 0-256
for x in range(0, 256):#variabel x range 0-256
    hgh[x] = 0 #histogrsm hequelisasi 0
    h[x] = 0
    c[x] = 0
#untuk y range heigh dan width di setel 0
for y in range(0, img_height): #variabel y tinggi 0
    for x in range(0, img_width): #variabel x lebar 0
        gray = img_grayscale[y][x][0] #gray
        hgh[gray] += 1 #histogram
                
h[0] = hgh[0] # histogram hequalisasi 0
for x in range(1, 256): #variabel x pada range 1-256
     h[x] = h[x-1] + hgh[x]

for x in range(0, 256): #variabel x pada range 0-256
     h[x] = h[x] / img_height / img_width

for x in range(0, 256):
    hgh[x] = 0 #histogram hequalisasi
    
for y in range(0, img_height):#variabel y pada range 0 untuk ketinggiannya
    for x in range(0, img_width):#variabel x pada range 0 untuk lebarnya
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

c[0] = hgh[0] #histogram hequalisasi 0
for x in range(1, 256):#variabel x range 1-256
     c[x] = c[x-1] + hgh[x]

hmaxk = c[255]
#untuk x dari range 0-256
for x in range(0, 256):#untuk x dari range 0-256
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5)#untuk memplot histogram.fungsi plot histogram yang banyak digunakan menggunakan np.histogram() dan merupakan dasar untuk fungsi plot panda.
plt.title("Histogram Grayscale Hequalisasi")#menampilkan tulisan
plt.show() #untuk memanggil library