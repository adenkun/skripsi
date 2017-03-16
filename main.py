# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import pandas
import csv
#komentar
data = data = pandas.read_csv('master_data.csv')
    
input_slope = pandas.read_csv('master_slope.csv')

masukan = pandas.read_csv('master_input.csv')

slope=float(input_slope['slope'][0])

intercept=float(input_slope['intercept'][0])

SigmoidCoef = 1.00

Emdataave = 0.44
yave = 0.10

Bias = 1.00

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

def normalisasiEmisi(e):
    Emnorm = float((e-Emmin)/(Emmax-Emmin))
    """print("Emisi Normalisasi: ",Emnorm)"""
    return(Emnorm)
    
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
        
def hiddenh1(a, b, c, d):
    h1 = float((normalisasiT(a)*WTmin) + (normalisasiEC(b)*WECmin) + (normalisasiVWC(c)*WVWCmin) + (Bias*WBmin))
    """print("h1: ",h1)"""
    return(h1)
    
def hiddenh2(a, b, c, d):
    h2 = float(normalisasiT(a)*WTave + normalisasiEC(b)*WECave + normalisasiVWC(c)*WVWCave + Bias*WBave)
    """print("h2: ",h2)"""
    return(h2)
    
def hiddenh3(a, b, c, d):
    h3 = float(normalisasiT(a)*WTmax + normalisasiEC(b)*WECmax + normalisasiVWC(c)*WVWCmax + Bias*WBmax)
    """print("h3: ",h3)"""
    return(h3)
    
def hiddenh4(a, b, c, d):
    h4 = float(normalisasiT(a)*WTdev + normalisasiEC(b)*WECdev + normalisasiVWC(c)*WVWCdev + Bias*WBdev)
    """print("h4: ",h4)"""
    return(h4)
        
def sigmoid(a, b):
    sig = float(1 / (1 + math.exp(-a * b)))
    return(sig)

def h11(a, b, c, d):
    h11 = float(sigmoid(SigmoidCoef, hiddenh1(a, b, c, d)))
    """print("h11: ",h11)"""
    return(h11)
    
def h22(a, b, c, d):
    h22 = float(sigmoid(SigmoidCoef, hiddenh2(a, b, c, d)))
    """print("h22: ",h22)"""
    return(h22)
    
def h33(a, b, c, d):
    h33 = float(sigmoid(SigmoidCoef, hiddenh3(a, b, c, d)))
    """print("h33: ",h33)"""
    return(h33)
    
def h44(a, b, c, d):
    h44 = float(sigmoid(SigmoidCoef, hiddenh4(a, b, c, d)))
    """print("h44: ",h44)"""
    return(h44)
        
def y(a, b, c, d):
    y = float(Wh11*h11(a, b, c, d) + Wh22*h22(a, b, c, d) + Wh33*h33(a, b, c, d) + Wh44*h44(a, b, c, d))
    """print("Nilai y: ",y)"""
    return(y)
    
def y2(a, b, c, d):
    y2 = float((slope * y(a, b, c, d)) + intercept)
    """print("Nilai y2: ",y2)"""
    return(y2)
        
def estimasi(a, b, c, d):
    estimasi = float(Emmin + y2(a, b, c, d) * (Emmax - Emmin))
    """print("Estimasi: ",i ,": ", estimasi)"""
    return(estimasi)
        
def co2(a, b, c, d):
    estimasi1 = estimasi(a, b, c, d)
    co2 = float(abs(Emisi - estimasi1))
    """print("Selisih",i ,": ", co2)"""
    return(co2)
    
    
n = int(raw_input('Jumlah Data: '))
i = 0

for x in xrange(i, n):
    T = masukan['T'][i]
    EC = masukan['EC'][i]
    VWC = masukan['VWC'][i]
    Emisi = masukan['Emisi'][i]
    i = i + 1
    
    estimasico2 = estimasi(T, EC, VWC, Emisi)
    selisih = co2(T, EC, VWC, Emisi)
    
    databaru = [(estimasico2, selisih)]   
    with open('hasil.csv', 'a') as filecsv:
        datafile = csv.writer(filecsv)
        datafile.writerows(databaru)
    filecsv.close()
