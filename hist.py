import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import skew, entropy
from skimage import io, color, filters, feature, img_as_ubyte, morphology
import os

path = 'D:\\Materi\\Try All\\Data Test\\'
data = []
c = []
def ke_glcm(gambar):
    hasil_glcm = {
        "energy" : 0,
        "homogeneity" : 0,
        "contrast" : 0
        }
    hasil_hist = {
        "mean" : 0,
        "std" : 0,
        "skew" : 0,
        "entr" : 0
    }
    img_read = cv2.imread(gambar, 0)
    his, bin_edges= np.histogram(img_read)
    hist=cv2.calcHist([img_read],[0],None,[256],[0,256])
    hasil_hist["mean"] = np.mean(hist)
    hasil_hist["std"] = np.std(hist)
    hasil_hist["skew"] = skew(hist)
    hasil_hist["entr"] = entropy(hist)
    ret, bw_img = cv2.threshold(img_read, 50,255,cv2.THRESH_BINARY)
    data.append(hasil_hist)

    img_conv=img_as_ubyte(bw_img)
    glcm = feature.greycomatrix(img_conv, [1], [0], symmetric=True, normed=True)
    for prop in hasil_glcm.keys():
        hasil_glcm[prop] = float(feature.greycoprops(glcm, prop))
    data.append(hasil_glcm)


pict = []
for jenis in os.listdir(path):
    folder = path+jenis
    for isi in os.listdir(folder):
        data=[]
        gambar = path+jenis+'\\'+isi
        ke_glcm(gambar)
        if jenis == "Benign":
            data.append("Benign")
        elif jenis == "Malignant":
            data.append("Malignant")
        pict.append(data)
        data=[]


