from tkinter import filedialog
from tkinter import *
from shutil import copy2
from PIL import ImageTk, Image
import math
import operator
import hist, cropping
pict_test = []

class coba:
    
    def __init__(self, ini):
        data = "3.png"
        text1="0"
        text2="0"
        text3="0"
        text4="0"
        text5="0"
        text6="0"
        text7="0"
        gambar = ""
        self.ini = ini
        self.initUI()
        var = StringVar()
        # var.set("DATA BENIGN : 25\tDATA MALIGNAN : 25")
        # self.judul = Message(ini, textvariable=var, relief=RAISED, width = 300 )
        # self.judul.grid(row=0, column=0, columnspan=2)

        
        self.lbllist = Label(ini, text="HASIL PERHITUNGAN KNN").grid(row=7, column=0, columnspan=3)

        self.table()
        self.tombol(NORMAL,DISABLED)
        self.gmr(data)
        self.kualifikasi(text1,text2,text3,text4,text5,text6,text7)

    def tombol(self, statusU, statusP):
        self.buttonUpload = Button(text="UPLOAD", width=6, command=self.upload, state=statusU)
        self.buttonUpload.grid(row=6, column=0, columnspan=2)

        self.buttonProses = Button(text="PROSES", width=6, command=self.hitung, state=statusP).grid(row=6, column=4)
    def kualifikasi(self, text1,text2,text3,text4,text5,text6,text7):
        self.lJ = Label( text="GLCM ").grid(row=0, column=5, columnspan = 2)
        self.l1 = Label( text="energy").grid(row=1, column=5, stick=W)
        self.l11 = Label( width=10, bg="white", text=text1 ).grid(row=1, column=6)
        
        self.l2 = Label( text="homogeneity").grid(row=2, column=5, stick=W)
        self.l12 = Label( width=10, bg="white", text=text2 ).grid(row=2, column=6)
        
        self.l3 = Label( text="contrast").grid(row=3, column=5, stick=W)
        self.l13 = Label( width=10, bg="white", text=text3 ).grid(row=3, column=6)

        self.lJJ = Label( text="HISTOGRAM").grid(row=0, column=2, columnspan = 2)
        self.l4 = Label( text="mean").grid(row=1, column=2)
        self.l14 = Label( width=10, bg="white", text=text4 ).grid(row=1, column=3)

        self.l5 = Label( text="std").grid(row=2, column=2)
        self.l15 = Label( width=10, bg="white", text=text5 ).grid(row=2, column=3)

        self.l6 = Label( text="skew").grid(row=3, column=2)
        self.l16 = Label( width=10, bg="white", text=text6 ).grid(row=3, column=3)

        self.l7 = Label( text="entr").grid(row=4, column=2)
        self.l17 = Label( width=10, bg="white", text=text7 ).grid(row=4, column=3)

    def gmr(self, data):
        img=Image.open(data)
        self.tkimage = ImageTk.PhotoImage(img)
        self.lblimage = Label(image=self.tkimage, width=70, height=70).grid(row=0, column=0, rowspan=5, columnspan =2)
    
    def initUI(self):
        self.ini.title("PERTHITUNGAN HISTOGRAM DAN GLCM")
        self.ini.geometry("700x300")

    def upload(self):
        self.tombol(DISABLED,NORMAL)
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("gambar files","*.png"),("all files","*.*")))
        gambar = str(filename)
        # copy2(filename, 'D:\Materi\Try All')
        # print('Selected : ', filename)
        gambar = cropping.cropping(gambar)
        self.gmr(gambar)
        hist.ke_glcm(gambar)
        pict_test.append(hist.data)
        # print(hist.data)
        text1 = round(hist.data[1]["energy"],4)
        text2 = round(hist.data[1]["homogeneity"],4)
        text3 = round(hist.data[1]["contrast"],4)
        text4 = round(hist.data[0]["mean"],4)
        text5 = round(hist.data[0]["std"],4)
        text6 = round(float(hist.data[0]["skew"]),4)
        text7 = round(float(hist.data[0]["entr"]),4)
        self.kualifikasi(text1,text2,text3,text4,text5,text6,text7)
    
    def hitung(self):
        jarak = 0
        import hist
        for i in range(len(hist.pict)):
            r=0
            for data in hist.pict[i][0].keys():
                # print(r)
                # x = input()
                r += pow(float(pict_test[0][0][data] - hist.pict[i][0][data]),2)
            for data in hist.pict[i][1].keys():
                r += pow(float(pict_test[0][1][data] - hist.pict[i][1][data]),2)
            # print(r)
            jarak = round(math.sqrt(r),2)
            hist.pict[i].append(jarak)
        # print(hist.pict[0][3])
        list.sort(hist.pict, key=operator.itemgetter(3))
        print(pict_test)
        print(hist.pict[0])
        self.tombol(NORMAL,DISABLED)
        baris=9
        lebar = 10
        for data in range(3):
            kolom = 0
            for D in range(4):
                if D is not 2:
                    if D is 0:
                        for prop in hist.pict[i][0].keys():
                            a = round(float(hist.pict[data][0][prop]),6)
                            b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                            kolom+=1
                    elif D is 1:
                        kolom-=1
                        for prop in hist.pict[i][1].keys():
                            a = round(hist.pict[data][1][prop],6)
                            b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                            kolom+=1
                    else:
                        a = round(hist.pict[data][D],6)
                        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                else:
                    kolom-=1
                    a = hist.pict[data][D]
                    b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                kolom+=1
            baris+=1


    def table(self):
        baris = 9    
        lebar = 10
    
        a = "mean"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 0)
            
        a = "std"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 1)
        
        a = "skew"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 2)
            
        a = "entr"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 3)
            
        a = "Energy"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 4)
            
        a = "Homogeneity"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 5)
            
        a = "Contrast"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 6)
            
        a = "Jenis"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 7)
            
        a = "Jarak"
        b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = 8, column = 8)
                        
        for data in range(3):
            kolom = 0
            for D in range(9):
                a = "-"
                b = Label(text=a, width = lebar, bg="white", relief=RIDGE).grid(row = baris, column = kolom)
                kolom+=1
            baris+=1
    


root = Tk()
app = coba(root)
root.mainloop()