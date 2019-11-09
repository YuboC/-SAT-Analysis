# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 13:56:02 2019

@author: n56vv
"""
class School:
    name = ""
    num = 0
    avgRead = 0
    avgMath = 0
    avgWrite = 0
    sumAvg = 0
    math_mind = 0
    def fromCSV(self, row):
        self.name = row[1]
        self.num = float(row[2])
        self.avgRead = float(row[3])
        self.avgMath = float(row[4])
        self.avgWrite = float(row[5])
        self.sumAvg = (self.avgRead + self.avgMath + self.avgWrite)
        self.math_mind =  self.avgMath / max(self.avgRead, self.avgWrite) 
    
    
    #Bubble Sort
'''    
    def GetMathMindScore(self,row):
        for i in range(len(self.math_mind)-1):
            switch = False
            for j in range(len(self.math_mind) -i-1):
                if self.math_mind[j] > self.math_mind[j+1]:
                    self.math_mind[j], self.math_mind[j+1] = self.math_mind[j+1],self.math_mind[j]
                    switch = True
                if not switch:
                    return 
 '''       
f = open("2012_SAT_Results.csv")
import csv
reader = csv.reader(f)
next(reader)

#=======================

data = []

for row in reader:
    if row[2] != "s":
    
        school = School()
        school.fromCSV(row)
        #school.GetMathMindScore(row)
        data.append(school)
       
minScore = 9999
maxScore = -1
sumS = 0
for i in data:    
    sumS = (i.avgRead + i.avgMath + i.avgWrite)
    if sumS < minScore:
        minScore = sumS
    if sumS > maxScore:
        maxScore = sumS
print("Maximun score is: ", maxScore)
print("Minimun score is: ", minScore)

#===========================

a = 0
b = 0
c = 0
d = 0
e = 0
sch_size = []
sch_score = []
size_of_sch = [0,100,200,500,1000]
totala = 0
totalb = 0
totalc = 0
totald = 0
totale = 0 

for school in data:
       
    num_taker = school.num
    if num_taker <= 100:
        a += 1
        totala += school.sumAvg
        
    elif num_taker <= 200:
        b += 1
        totalb += school.sumAvg
    elif num_taker <= 500:
        c += 1
        totalc += school.sumAvg
    elif num_taker <= 1000:
        d += 1
        totald += school.sumAvg
    else: 
        e += 1
        totale += school.sumAvg
    
sch_size=[a,b,c,d,e]
sch_score=[totala/a,totalb/b,totalc/c,totald/d,totale/e]
    
import matplotlib.pyplot as plt
plt.plot(sch_score)

print("\nTest taker size from 0 to 100:    ",totala/a)
print("Test taker size from 1000 to 200: ",totalb/b)
print("Test taker size from 200 to 500:  ",totalc/c) 
print("Test taker size from 500 to 1000: ",totald/d) 
print("Test taker size from 1000:        ",totale/e)

sch = {}
sch_list = []
count=0
top_sch = sorted(data, key = lambda x: x.math_mind, reverse = True) 


for school in top_sch:
    if not school.name in sch:
        
        sch[school.name] = school.name
        sch[school.math_mind] = school.math_mind 
        count += 1        

for school in sch:
    if count != 5:
        sch_list.append(sch[school])
        
while count < 5:
    top_sch.name = top_sch.math_mind
    count += 1
   
print("\nthe top 1 highest math schools are: ", sch_list[0])
print("the top 2 highest math schools are: ", sch_list[2])
print("the top 3 highest math schools are: ", sch_list[4])
print("the top 4 highest math schools are: ", sch_list[6])
print("the top 5 highest math schools are: ", sch_list[8])