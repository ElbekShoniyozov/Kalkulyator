def qushuv(x,y):
    print("Natija: =  ",x+y)
def ayiruv(x,y):
    print("Natija: =  ",x-y)
def kupaytiruv(x,y):
    print("Natija: =  ",x*y)
def buluv(x,y):
    print("Natija: =  ",x/y)

raqam1=int(input("Birinchi raqamni kiriting:  "))
amal=input("Amalni kiriting:  ")
raqam2=int(input("Ikkinchi raqamni kiriting:  "))

if amal==('+'):
    qushuv(raqam1,raqam2)
if amal==('-'):
    ayiruv(raqam1,raqam2)
if amal==('*'):
    kupaytiruv(raqam1,raqam2)
if amal==('/'):
    buluv(raqam1,raqam2)