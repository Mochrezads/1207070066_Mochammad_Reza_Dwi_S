import numpy as np # import library numpy
import imageio #membaca dan menulis berbagai data gambar
import matplotlib.pyplot as plt  #mengimpor modul pyplot dari matplotlib ke namespace dengan nama lebih pendek plt .

img = imageio.imread("gambar4.jpg") #Untuk membaca gambar
img_height = img.shape[0] #Tinggi mewakili jumlah baris piksel dalam gambar atau jumlah piksel dalam setiap kolom array gambar.
img_width = img.shape[1] #Lebar mewakili jumlah kolom piksel dalam gambar atau jumlah piksel di setiap baris array gambar.
img_channel = img.shape[2]#Jumlah Saluran mewakili jumlah komponen yang digunakan untuk mewakili setiap piksel.

img_inversi = np.zeros(img.shape, dtype=np.uint8) #Fungsi ini akan membuat gambar yang dimanipulasi menjadi sebuah file.png atau ekstensi 

#gambar di inversi ke grayscale
def inversi_grayscale(nilai): 
    for y in range(0, img_height):#variabel x pada range 0 untuk tinggi
        for x in range(0, img_width): #variabel x pada range 0 untuk lebar
            red = img[y][x][0] #red
            green = img[y][x][1]#green
            blue = img[y][x][2]#blue
            gray = (int(red) + int(green) + int(blue)) / 3 #gray didapat dari intred+green+blue
            gray = nilai - gray #gray didapat dari nilai-gray
            img_inversi[y][x] = (gray, gray, gray) #img_inversi gray gray gray
#gambar di inversi ke rgb
def inversi_rgb(nilai): #inversi rgb
    for y in range(0, img_height):#variabel x pada range 0 untuk tinggi
        for x in range(0, img_width):#variabel x pada range 0 untuk lebar
            red = img[y][x][0] #red
            red = nilai - red #red didapat dari nilai-red
            green = img[y][x][1] #green
            green = nilai - green #green didapat dari nilai - green
            blue = img[y][x][2] #blue
            blue = nilai - blue#blue didapat dari nilai-blue
            img_inversi[y][x] = (red, green, blue) #inversi RGB

inversi_grayscale(255) #grayslace di inversi menjadi 255
plt.imshow(img_inversi) #Fungsi matplotlib imshow () membantu menampilkan gambar. Tetapi plt.imshow () tidak berfungsi tanpa fungsi mpimg.imread ()
plt.title("Inversi Grayscale") #menampilkan tulisan
plt.show() #untuk memanggil library

inversi_rgb(255) #rgb di inversi menjadi 255
plt.imshow(img_inversi) #Fungsi matplotlib imshow () membantu menampilkan gambar. Tetapi plt.imshow () tidak berfungsi tanpa fungsi mpimg.imread ()
plt.title("Inversi RGB") #menampilkan tulisan
plt.show() #untuk memanggil library

img_log = np.zeros(img.shape, dtype=np.uint8) #img 

def log(c): #untuk menghitung logaritma natural dari c
    for y in range(0, img_height):#variabel x pada range 0 untuk tinggi
        for x in range(0, img_width):#variabel x pada range 0 untuk lebar
            red = img[y][x][0] #red
            green = img[y][x][1] #green
            blue = img[y][x][2]#blue
            gray = (int(red) + int(green) + int(blue)) / 3 #gray didapat dari intred+green+blue
            gray = int(c * np.log(gray + 1)) #gray
            if gray > 255: #apabila gray lebih dari 255
                gray = 255 #gray akan sama dengan 255
            if gray < 0:#jika gray kurang dari 0
                gray = 0 #maka gray akan 0
            img_log[y][x] = (gray, gray, gray) #img_log gray gray gray

log(30) #log 30
plt.imshow(img_log) #Fungsi matplotlib imshow () membantu menampilkan gambar. Tetapi plt.imshow () tidak berfungsi tanpa fungsi mpimg.imread ()
plt.title("Log") #menampilkan tulisan
plt.show() #untuk memanggil library

img_inlog = np.zeros(img.shape, dtype=np.uint8) #untuk mendapatkan akar dari sebuah angka

def inlog(c):#untuk menghitung logaritma natural dari c
    for y in range(0, img_height):#variabel y tinggi range 0
        for x in range(0, img_width):#variabel x lebar range 0
            red = img[y][x][0] #red
            green = img[y][x][1] #green
            blue = img[y][x][2] #blue
            gray = (int(red) + int(green) + int(blue)) / 3 #gray didapat dari intred+green+blue
            gray = int(c * np.log(255 - gray + 1))
            if gray > 255: #apabila gray lebih dari 255
                gray = 255 #gray akan sama dengan 255
            if gray < 0: #jika gray kurang dari 0
                gray = 0 #maka gray akan 0
            img_inlog[y][x] = (gray, gray, gray)#img_inlogdi dapat dari gray,gray,gray

inlog(30) #inlognya 30
plt.imshow(img_inlog) #Fungsi matplotlib imshow () membantu menampilkan gambar. Tetapi plt.imshow () tidak berfungsi tanpa fungsi mpimg.imread ()
plt.title("Inversi & Log") #menampilkan tulisan
plt.show() #untuk memanggil library

img_nthpower = np.zeros(img.shape, dtype=np.uint8) #untuk mendapatkan akar dari sebuah angka

def nthpower(c, y): #menjadi pertanda bahwa blok kode program adalah sebuah fungsi
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):#variabel x pada range 0 untuk tinggi
        for x in range(0, img_width):#variabel x pada range 0 untuk lebar
            red = img[y][x][0] #red
            green = img[y][x][1] #green
            blue = img[y][x][2] #blue
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, thy))
            if gray > 255: #apabila gray lebih dari 255
                gray = 255 #gray akan sama dengan 255
            if gray < 0: #jika gray kurang dari 0
                gray = 0 #maka gray akan 0
            img_nthpower[y][x] = (gray, gray, gray)

nthpower(50, 100) #untuk mendapatkan akar dari sebuah angka
plt.imshow(img_nthpower) #Fungsi matplotlib imshow () membantu menampilkan gambar. Tetapi plt.imshow () tidak berfungsi tanpa fungsi mpimg.imread ()
plt.title("Nth Power") #menampilkan tulisan
plt.show() #untuk memanggil library

img_nthrootpower = np.zeros(img.shape, dtype=np.uint8) #untuk mendapatkan akar dari sebuah angka

def nthrootpower(c, y): #menjadi pertanda bahwa blok kode program adalah sebuah fungsi
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):#variabel y pada range 0 untuk tingginya
        for x in range(0, img_width):#variabel x pada range 0 untuk lebar
            red = img[y][x][0] #red
            green = img[y][x][1] #green
            blue = img[y][x][2] #blue
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255: #apabila gray lebih dari 255
                gray = 255 #gray akan sama dengan 255
            if gray < 0: #jika gray kurang dari 0
                gray = 0 #maka gray akan 0
            img_nthpower[y][x] = (gray, gray, gray)

nthrootpower(50, 100) #untuk mendapatkan akar dari sebuah angka
plt.imshow(img_nthrootpower) #Fungsi matplotlib imshow () membantu menampilkan gambar. Tetapi plt.imshow () tidak berfungsi tanpa fungsi mpimg.imread ()
plt.title("Nth Root Power") #menampilkan tulisan
plt.show() #untuk memanggil library