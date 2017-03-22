# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import csv

data1 = open('master_data.csv')
data11 = csv.reader(data1)
data = list(data11)

data3 = open('master_data2.csv')
data33 = csv.reader(data3)
data2 = list(data33)
    
input_slope1 = open('master_slope.csv')
input_slope11 = csv.reader(input_slope1)
input_slope = list(input_slope11)

masukan1 = raw_input('Nama File: ')

masukan2 = open(masukan1 + '.csv')
masukan22 = csv.reader(masukan2)
masukan = list(masukan22)

slope = float(input_slope[1][4])

intercept = float(input_slope[1][5])

SigmoidCoef = float(data2[1][0])

Emdataave = float(data2[1][1])

yave = float(data2[1][2])

Bias = float(data2[1][3])

Emmin = float(data[1][5])
Emave = float(data[2][5])
Emmax = float(data[3][5])

Tmin = float(data[1][1])
Tave = float(data[2][1])
Tmax = float(data[3][1])

ECmin = float(data[1][2])
ECave = float(data[2][2])
ECmax = float(data[3][2])

VWCmin = float(data[1][3])
VWCave = float(data[2][3])
VWCmax = float(data[3][3])

WTmin = float(data[4][1])
WTave = float(data[5][1])
WTmax = float(data[6][1])
WTdev = float(data[7][1])

WECmin = float(data[4][2])
WECave = float(data[5][2])
WECmax = float(data[6][2])
WECdev = float(data[7][2])

WVWCmin = float(data[4][3])
WVWCave = float(data[5][3])
WVWCmax = float(data[6][3])
WVWCdev = float(data[7][3])

WBmin = float(data[4][4])
WBave = float(data[5][4])
WBmax = float(data[6][4])
WBdev = float(data[7][4])

Wh11 = float(input_slope[1][0])
Wh22 = float(input_slope[1][1])
Wh33 = float(input_slope[1][2])
Wh44 = float(input_slope[1][3])
"""
def normalisasiEmisi(e):
    Emnorm = float((e-Emmin)/(Emmax-Emmin))
    print("Emisi Normalisasi: ",Emnorm)
    return(Emnorm)
"""    
def normalisasiT(a):
    Tnorm = float((a-Tmin)/(Tmax-Tmin))
    """print("T Normalisasi: ",Tnorm)"""
    return(Tnorm)
    
def normalisasiEC(b):
    ECnorm = float((b-ECmin)/(ECmax-ECmin))
    """print("EC Normalisasi: ",ECnorm)"""
    return(ECnorm)
        
def normalisasiVWC(c):
    VWCnorm = float((c-VWCmin)/(VWCmax-VWCmin))
    """print("VWC Normalisasi: ",VWCnorm)"""
    return(VWCnorm)
        
def hiddenh1(a, b, c):
    h1 = float((normalisasiT(a)*WTmin) + (normalisasiEC(b)*WECmin) + (normalisasiVWC(c)*WVWCmin) + (Bias*WBmin))
    """print("h1: ",h1)"""
    return(h1)
    
def hiddenh2(a, b, c):
    h2 = float(normalisasiT(a)*WTave + normalisasiEC(b)*WECave + normalisasiVWC(c)*WVWCave + Bias*WBave)
    """print("h2: ",h2)"""
    return(h2)
    
def hiddenh3(a, b, c):
    h3 = float(normalisasiT(a)*WTmax + normalisasiEC(b)*WECmax + normalisasiVWC(c)*WVWCmax + Bias*WBmax)
    """print("h3: ",h3)"""
    return(h3)
    
def hiddenh4(a, b, c):
    h4 = float(normalisasiT(a)*WTdev + normalisasiEC(b)*WECdev + normalisasiVWC(c)*WVWCdev + Bias*WBdev)
    """print("h4: ",h4)"""
    return(h4)
        
def sigmoid(a, b):
    sig = float(1 / (1 + math.exp(-a * b)))
    return(sig)

def h11(a, b, c):
    h11 = float(sigmoid(SigmoidCoef, hiddenh1(a, b, c)))
    """print("h11: ",h11)"""
    return(h11)
    
def h22(a, b, c):
    h22 = float(sigmoid(SigmoidCoef, hiddenh2(a, b, c)))
    """print("h22: ",h22)"""
    return(h22)
    
def h33(a, b, c):
    h33 = float(sigmoid(SigmoidCoef, hiddenh3(a, b, c)))
    """print("h33: ",h33)"""
    return(h33)
    
def h44(a, b, c):
    h44 = float(sigmoid(SigmoidCoef, hiddenh4(a, b, c)))
    """print("h44: ",h44)"""
    return(h44)
        
def y(a, b, c):
    y = float(Wh11*h11(a, b, c) + Wh22*h22(a, b, c) + Wh33*h33(a, b, c) + Wh44*h44(a, b, c))
    """print("Nilai y: ",y)"""
    return(y)
    
def y2(a, b, c):
    y2 = float((slope * y(a, b, c)) + intercept)
    """print("Nilai y2: ",y2)"""
    return(y2)
        
def estimasi(a, b, c):
    estimasi = float(Emmin + y2(a, b, c) * (Emmax - Emmin))
    print("Estimasi: ", estimasi)
    return(estimasi)
"""    
T = float(raw_input('Suhu: '))
EC = float(raw_input('Konduktivitas Listrik: '))
VWC = float(raw_input('Kelembaban: '))

estimasico2 = estimasi(T, EC, VWC)
selisih = 0.01

databaru = [(estimasico2, selisih)]   
with open('hasil.csv', 'a') as filecsv:
    datafile = csv.writer(filecsv)
    datafile.writerows(databaru)
filecsv.close()
"""        
def co2(a, b, c, d):
    estimasi1 = estimasi(a, b, c, d)
    co2 = float(abs(Emisi - estimasi1))
    print("Estimasi",i ,": ", estimasi1)
    print("Selisih",i ,": ", co2)
    return(co2)  
    
n = 0
nilain = open(masukan1 + '.csv')
reader = csv.DictReader(nilain)
for x in reader:
    n += 1
nilain.close()

i = 1

for x in xrange(i, (n+1)):
    T = float(masukan[i][0])
    EC = float(masukan[i][1])
    VWC = float(masukan[i][2])
    i = i + 1
	
    estimasico2 = estimasi(T, EC, VWC)
    selisih = 0.01
    
    databaru = [(estimasico2, selisih)]   
    with open('hasil.csv', 'a') as filecsv:
        datafile = csv.writer(filecsv)
        datafile.writerows(databaru)
    filecsv.close()
