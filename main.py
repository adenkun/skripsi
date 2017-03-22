# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import pandas
import csv

data = pandas.read_csv('master_data.csv')
    
input_slope = pandas.read_csv('master_slope.csv')

masukan1 = raw_input('Nama File: ')

masukan = pandas.read_csv(masukan1 + '.csv')

slope=float(input_slope['slope'][0])

intercept=float(input_slope['intercept'][0])

data2 = pandas.read_csv('master_data2.csv')

SigmoidCoef = float(data2['SigmoidCoef'][0])

Emdataave = float(data2['Emdataave'][0])
yave = float(data2['yave'][0])

Bias = float(data2['Bias'][0])

Emmin = float(data['Emisi'][0])
Emave = float(data['Emisi'][1])
Emmax = float(data['Emisi'][2])

Tmin = float(data['T'][0])
Tave = float(data['T'][1])
Tmax = float(data['T'][2])

ECmin = float(data['EC'][0])
ECave = float(data['EC'][1])
ECmax = float(data['EC'][2])

VWCmin = float(data['VWC'][0])
VWCave = float(data['VWC'][1])
VWCmax = float(data['VWC'][2])

WTmin = float(data['T'][4])
WTave = float(data['T'][5])
WTmax = float(data['T'][6])
WTdev = float(data['T'][7])

WECmin = float(data['EC'][4])
WECave = float(data['EC'][5])
WECmax = float(data['EC'][6])
WECdev = float(data['EC'][7])

WVWCmin = float(data['VWC'][4])
WVWCave = float(data['VWC'][5])
WVWCmax = float(data['VWC'][6])
WVWCdev = float(data['VWC'][7])

WBmin = float(data['Bias'][4])
WBave = float(data['Bias'][5])
WBmax = float(data['Bias'][6])
WBdev = float(data['Bias'][7])

Wh11 = float(input_slope['Wh11'][0])
Wh22 = float(input_slope['Wh22'][0])
Wh33 = float(input_slope['Wh33'][0])
Wh44 = float(input_slope['Wh44'][0])
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
i = 0

for x in xrange(i, n):
    T = masukan['T'][i]
    EC = masukan['EC'][i]
    VWC = masukan['VWC'][i]
    i = i + 1
    
    estimasico2 = estimasi(T, EC, VWC)
    selisih = 0.01
    
    databaru = [(estimasico2, selisih)]   
    with open('hasil.csv', 'a') as filecsv:
        datafile = csv.writer(filecsv)
        datafile.writerows(databaru)
    filecsv.close()
