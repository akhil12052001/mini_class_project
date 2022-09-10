from cProfile import label
import math
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

#creating empty list to define 
cardno=[]
name=[]
gender=[]
dob=[]
citytown=[]
maths=[]
phy=[]
chem=[]
total=[]

for i in range (0,30,1):
    cardno.append(i)
#give data manualy
name=['bhuvnesh','harish','shashank','ridha','ritika',
'akshaya','sameer','aditya','surya','clarence','kavya',
'rahul','srinidhi','gopi','sophia','goutami','tauseef',
'arshad','abirami','vetrivel','kalyan','monika','priya',
'deepika','siddharth','geeta','jk','jagan','nisha',
'naveen']
gender=['m','m','m','f','f','f','m','m','m','m','f','m','f','m','f','f','m','m','f'
,'m','m','f','f','f','m','f','m','m','f','m']
dob=['7 nov','3 jun','4 jan','5 may','17 nov','8 feb'
,'23 mar','15 mar','28 feb','6 dec','12 jan','30 apr',
'14 jan','6 may','23 july','22 sep','30 dec','14 dec',
'9 oct','30 aug','17 sep','15 mar','17 jul','13 may',
'26 dec','16 may','22 jul','4 mar','10 sep','13 oct']
citytown=['erode','salem','chennai','chennai',
'madurai','chennai','ambur','vellore','bangluru'
,'bangluru','chennai','bangluru','chennai','madurai'
,'trichcy','theni','trichy','chennai','erode','trichy'
,'vellore','bangluru','nagarcoil','bangluru','madurai',
'chennai','chennai','madurai','madurai','vellore']
maths=[68,62,57,42,87,71,81,84,74,63,64,97,52,65,89,76,
87,62,72,56,93,78,62,97,44,87,74,81,74,72]
phy=[64,45,54,53,64,92,82,92,64,88,72,92,64,73,62,58,86,81,
92,78,68,69,62,91,72,75,71,76,83,66]
chem=[78,91,77,78,89,84,87,76,51,73,68,92,71,89,93,90,43,67,97,
62,91,74,57,88,58,92,82,52,83,81]

for i in range(30):
    x=maths[i]+phy[i]+chem[i]
    total.append(x)
#print the data each student with card no using for loop
for i in range(len(cardno)):
    print("card no:-{}".format(cardno[i]))
    print("name:-{}".format(name[i]))
    print("DOB:-{}".format(dob[i]))
    print("Gender:-{}".format(gender[i]))
    print("city town:-{}".format(citytown[i]))
    print("maths marks:-{}".format(maths[i]))
    print("physics marks:-{}".format(phy[i]))
    print("chemistry marks:-{}".format(chem[i]))
    print("total marks:-{}".format(total[i]))
    

# find maximum marks in each subject and also find overall scorar


maxmath=maths[0]
for i in range(len(maths)):
    if(maths[i]>maxmath):
        maxmath=maths[i]
        

a=maths.index(maxmath)
print("{} is get maximum marks {} in mathematics".format(name[a],maxmath))

#find maximum marks of physics with the name who get maximum marks
maxphy=phy[0]
    

for i in range(len(phy)):
        if(phy[i]>maxphy):
            maxphy=phy[i]


a=phy.index(maxphy)
print("{} is get maximum marks {} in physics".format(name[a],maxphy))  
#find maximum marks of chemistry with the name who get maximum marks
maxchem=chem[0]
for i in range(len(chem)):
    if(chem[i]>maxchem):
        maxchem=chem[i]

a=chem.index(maxchem)
print("{} is get maximum marks {} in chemistry".format(name[a],maxchem))  
#find the overrall topper who get maximum marks
maxtotal=total[0]
for i in range(len(total)):
    if(total[i]>maxtotal):
        maxtotal=total[i]

a=total.index(maxtotal)
print("Overall topper of class {} get {} marks".format(name[a],maxtotal))
#find mode of mathematics subject

def mode():
    
    hcount=0
    temp=0
    modes=[]
    hcount=maths.count(maths[0])
    for x in range (0,len(maths)):
        temp=maths.count(maths[x])
        if temp>hcount:
            hcount=temp    
    for i in maths:
        if (maths.count(i)==hcount):
            modes.append(i)
    print('most frequent no of maths list is :',modes)
    print('number appeared',hcount,'times in maths list ')
mode()
#for standard deviation of physics

physum=0
for i in (phy):
        physum+=i

phymean=(physum/30)
meanphy="{:.2f}".format(phymean)
print('Mean of physics =',meanphy)
#for variance
phyvariance=[]
for i in  (phy):
    x=i-phymean
    y="{:.2f}".format(x)
    z=float(y)
    phyvariance.append(z)



#for deviation of physics
sqvariance=[]
for i in (phyvariance):
    a=i*i
    b="{:.2f}".format(a)
    c=float(b)
    sqvariance.append(c)

sqsum=0
for i in (sqvariance):
    sqsum+=i
    a="{:.2f}".format(sqsum)
    b=float(a)

deviation=sqsum/30
dev="{:.2f}".format(deviation)
phydeviation=float(dev)

#for standard deviation
stddev=(deviation)**(0.5)
print('standard deviation of physics is =',stddev)
#for count range in math
def range_math():
    
    min=maths[0]
    for a in maths:
        if a<min:
            min=a
    print("minimun value is :",min)
    max=maths[0]
    for b in maths:
        if b>max:
            max=a
    print("maximun value is :",max)
    range=((max-min))
    print('range of maths is :',range)

def range_phy():
    
    min=phy[0]
    for a in phy:
        if a<min:
            min=a
    print("minimun value is :",min)
    max=phy[0]
    for b in phy:
        if b>max:
            max=a
    print("maximun value is :",max)
    range=((max-min))
    print('range of physics is :',range)

def range_chem():
    
    min=chem[0]
    for a in chem:
        if a<min:
            min=a
    print("minimun value is :",min)
    max=chem[0]
    for b in chem:
        if b>max:
            max=a
    print("maximun value is :",max)
    range=((max-min))
    print('range of chemistry is :',range)
mathsmean=0
phymean=0
chemmean=0
#find mean of each subject using funtion 
def mean_math():
 print(maths)
 mathssum=0
 for i in (maths):
        mathssum+=i
 
 mathsmean=(mathssum/30)
 print('Mean of maths =',mathsmean)

def mean_phy():
 print(phy)
 physum=0
 for i in (phy):
        physum+=i
 
 phymean=(physum/30)
 print('Mean of physics =',phymean)
 
def mean_chem():
 print(chem)
 chemsum=0
 for i in (chem):
        chemsum+=i
 
 chemmean=(chemsum/30)
 print('Mean of chemistry =',chemmean)
 



#find variance of each subject also using function
def var_math():
 mathsdiff=[]
 for i in  (maths):
    mathsdiff.append(i-mathsmean)
 
 sqdiff=[]
 for i in (mathsdiff):
    a=i*i
    sqdiff.append(a)
 
 sqdiffsum=0
 for i in (sqdiff):
    sqdiffsum+=i
 
 variance=sqdiffsum/30
 var="{:.2f}".format(variance)
 print('variance of maths is=',var)

def var_phy():
   phydiff=[]
   for i in  (phy):
    phydiff.append(i-phymean)
   
   sqdiffphy=[]
   for i in (phydiff):
    a=i*i
    sqdiffphy.append(a)
   
   sqdiffphysum=0
   for i in (sqdiffphy):
    sqdiffphysum+=i
   
   variance=sqdiffphysum/30
   var="{:.2f}".format(variance)
   print('variance of physics is=',var)


def var_chem():
  chemdiff=[]
  for i in  (chem):
    chemdiff.append(i-chemmean)
  
  sqdiffchem=[]
  for i in (chemdiff):
    a=i*i
    sqdiffchem.append(a)
  
  sqdiffchemsum=0
  for i in (sqdiffchem):
    sqdiffchemsum+=i
  
  variance=sqdiffchemsum/30
  var="{:.2f}".format(variance)
  print('variance of chemistry is=',var)
# find medium of each subject
def med_math():
 
 n=len(maths)
 maths.sort()
 if n%2==0:
    median1=maths[n//2]
    median2=maths[n//2-1]
    median=(median1+median2)/2
 else:
    median=maths[n//2]
 print('median of maths is=',median)

def med_phy():
 
 n=len(phy)
 phy.sort()
 if n%2==0:
    median1=phy[n//2]
    median2=phy[n//2-1]
    median=(median1+median2)/2
 else:
    median=phy[n//2]
 print('median of physics is=',median)

def med_chem():
 
 n=len(chem)
 chem.sort()
 if n%2==0:
    median1=chem[n//2]
    median2=chem[n//2-1]
    median=(median1+median2)/2
 else:
    median=chem[n//2]
 print('median of chemistry is=',median)
range_math()
range_phy()
range_chem()
var_math()
var_phy()
var_chem()
med_math()
med_phy()
med_chem()




# find the  percentage of each subject    

mathssum=0
for i in (maths):
        mathssum+=i
print('total of math =',mathssum)
mathper=(mathssum/30)
print('pecentage of maths out of 100 is=',round(mathper),'%')
#physics percentage

physum=0
for i in (phy):
        physum+=i
print('total of physics =',physum)
phyper=(physum/30)
print('pecentage of physics out of 100 is=',round(phyper),'%')
#chemistry percentage

chemsum=0
for i in (chem):
        chemsum+=i
print('total of chemistry =',chemsum)
chemper=(chemsum/30)
print('pecentage of physics out of 100 is=',round(chemper),'%')

percentage=[]
percentage.append(round(mathper))
percentage.append(round(phyper))
percentage.append(round(chemper))
print((percentage))
#find avrage of each subject
sum=0
st_marks=[]
for i in(maths):
    sum=sum+i
    avgmath=sum/len(maths)
    mathsavg=round(avgmath)
st_marks.append(mathsavg)

print("avrage marks of maths is= ",mathsavg)
for i in(phy):
    sum=sum+i
    avgphy=sum/len(phy)
    phyavg=round(avgphy)
st_marks.append(phyavg)

print("avrage marks of maths is= ",phyavg)
for i in(chem):
    sum=sum+i
    avgchem=sum/len(chem)
    chemavg=round(avgchem)
st_marks.append(chemavg)
print("avrage marks of chemistry is= ",chemavg)


# we plot bar graph of avrage score in each subject
subject_name=['maths','physics','chemistry']
print(st_marks)



plt.bar(subject_name,st_marks,color='blue',width=0.2,label=subject_name)
plt.xlabel("subject names")
plt.ylabel("student's avg marks")

plt.title("Student each subject avrage marks")
plt.show()
       
# find maths percentage    

mathssum=0
for i in (maths):
        mathssum+=i
mathper=(mathssum/30)
print('pecentage of maths out of 100 is=',round(mathper),'%')
# find physics percentage

physum=0
for i in (phy):
        physum+=i
phyper=(physum/30)
print('pecentage of physics out of 100 is=',round(phyper),'%')
# find chemistry percentage

chemsum=0
for i in (chem):
        chemsum+=i
chemper=(chemsum/30)
print('pecentage of physics out of 100 is=',round(chemper),'%')
sub=['math','physics','chemistry']
percentage=[]
percentage.append(round(mathper))
percentage.append(round(phyper))
percentage.append(round(chemper))
print((percentage))
# for visualization we use bar graph for better understanding

fig = plt.figure(figsize=(10,8))

plt.bar(sub,percentage,width=0.2,color='#9C3AF2') 
plt.xlabel('subjects')
plt.ylabel('percentage marks of suject')

plt.title('subject wise percentage')
plt.show()
    
# calculate gender wise percentage and plot on graph 

count_m=0  
count_f=0   
for i in gender:    
    if i=='m':        
        count_m+=1
    elif i=='f':       
        count_f+=1
print('male=',count_m)    
print('female=',count_f)   
avg_male=((count_m/30)*100)   
avg_female=((count_f/30)*100)   
print('male percentages=',round(avg_male))
print('female percentages=',round(avg_female))
percentage=[] 
percentage.append(round(avg_male))  
percentage.append(round(avg_female))  

gender=['male','female'] 
# for visualization we use pie chart for better understanding
#plot pie chart for male v/s female 
plt.pie(percentage,labels=gender,autopct='%2.1f%%')
plt.title('percentage male vs female')
plt.show()


