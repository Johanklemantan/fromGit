# def Hashtag (a):

#     if a == "":
#         return False #untuk return False saat inputnya empty string
#     else:
#         sentence = a.split() #membuat jadi list default spasi
#         hasil = "#" #untuk mulai dengan hashtag
#         for b in sentence :
#             capital = str(b).capitalize() #untuk setiap kata mulai dengan huruf kapital
#             hasil += capital 
#     if len(hasil) > 140: #untuk return False saat jumlah char lebih dari 140
#         return False
#     else :
#         return hasil

# kalimat = input("Masukkan kalimatnya disini : ")
# print(Hashtag(kalimat))

# a = 'hari'
# b = a.split()
# print(b)


# def create_phone_number(notel):
#     hasil="("
#     for index in range(0,len(notel)):
#         if len(notel[index])!=1:
#             return f"ERROR : Inputan ke- {index} tidak sesuai format"
#         else:
#             if index == 2:
#                 hasil += notel[index] + ") " #untuk menambah ") " setelah angka ke 3
#             elif index == 5:
#                 hasil += notel[index] + "-" #untuk menambah "-" setelah angka ke 6
#             else :
#                 hasil += notel[index]
#     return hasil



# myList = []
# for a in range (1,11):
#     myList.append(input(f"Angka ke-{a} (harus 1 digit)= "))
# print (f"Angka yang kamu input adalah {myList}")
# print (f"Jadi nomor teleponmu berdasarkan nomor yang kamu input adalah {create_phone_number(myList)}")



def asc(gjl):
    '''
    mengurutkan angka ganjil kecil ke besar dengan bubble sort
    '''
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(len(gjl)-1):
            if gjl[i] > gjl [i+1]:
                swap += 1
                gjl[i],gjl[i+1]=gjl[i+1],gjl[i]
    print(gjl)
    return gjl
    

def dsc(gnp):
    '''
    mengurutkan angka genap besar ke kecil dengan bubble sort
    '''
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(len(gnp)-1):
            if gnp[i] < gnp [i+1]:
                swap += 1
                gnp[i],gnp[i+1]=gnp[i+1],gnp[i]
    print(gnp)
    return gnp
    

def sort_odd_even(inputan):
    if inputan == []:
        return f"Input list kosong {inputan}" # return list kosong bila diinput list kosong
    else:
        pos = []
        odd = []
        even = []
        for s in range(len(inputan)):
            if inputan[s]=="":
                inputan[s]="0"  #error handling apabila saat penginputan ada empty string
        for b in range(len(inputan)):
            if int(inputan[b])%2==0:
                pos.append(1) # mencatat posisi genap
                even.append(inputan[b]) #mengumpulkan angka genap
            else :
                pos.append(0) #mencatat posisi ganjil
                odd.append(inputan[b]) #mengumpulkan angka ganjil
        odd = asc(odd)
        even = dsc(even)
        odd_index = 0
        even_index = 0
        hasil = []
        for k in pos :
            if k == 0:
                hasil.append(odd[odd_index])
                odd_index += 1
            if k == 1:
                hasil.append(even[even_index])
                even_index += 1
        return f"Setelah disort sesuai ketentuan : {hasil}"
    


# cara 1
myList = []
qty = (input("Mau berapa angka ? "))
if qty=="" or int(qty)<1 :
    print (f"Angka yang kamu input adalah {myList}")
    print(f"Input list kosong {myList}")
else:
    qty = int(qty)
    for a in range (1,qty+1):
        myList.append(input(f"Angka ke-{a}= "))
    print (f"Angka yang kamu input adalah {myList}")
    print(f"{sort_odd_even(myList)}")

# cara 2
# myList = [5,3,2,8,1,4]
# sort_odd_even(myList)




# def sort_odd_even(num):

# #case of an empty string, return empty string
#     if num==[]:
#         return num

#     else:
# #misahin dulu ganjil dan genap menjadi 2 list berbeda untuk mempermudah sorting
#         ganjil=[]
#         genap=[]
#         for data in num:
#             if data%2==0:
#                 genap.append(data)
#             else:
#                 ganjil.append(data)

# #bubble sort ganjil
#         for angka in range(len(ganjil)-1):
#             for angka1 in range(len(ganjil)-angka-1):
#                 if ganjil[angka1]>ganjil[angka1+1]:
#                     ganjil[angka1],ganjil[angka1+1]=ganjil[angka1+1],ganjil[angka1]

# #bubble sort genap
#         for angka2 in range(len(genap)-1):
#             for angka3 in range(len(genap)-angka2-1):
#                 if genap[angka3]<genap[angka3+1]:
#                     genap[angka3],genap[angka3+1]=genap[angka3+1],genap[angka3]
#         print('genap:',genap)
#         print('ganjil:',ganjil)

# #membuat empty list untuk nampung hasil susunan angka ganjil genap supaya ssuai keinginan
#         lstbaru=[]

# #membuat indexing utk ganjil dan genap
#         idxgjl=0
#         idxgnp=0
     
#         for nums in num:
# #masukin angka dari list "genap" yang udah sorted di tempat angka awal ("num") yang tadinya genap, 
#             if nums%2==0:
#                 lstbaru.append(genap[idxgnp])
# #indexnya dimajuin terus setiap udah masuk 1
#                 idxgnp+=1
# #masukin angka ganjil yang sudah sorted di angka yang tadinya di tempat angka awal ("num") yang juga emang ganjil
#             else:
#                 lstbaru.append(ganjil[idxgjl])
# #indexnya dimajuin terus setiap udah masuk 1
#                 idxgjl+=1

#         return lstbaru

# #normal case
# test1=sort_odd_even([1,2,4,6,3,5,7,9,8,10])
# print(test1)

# # #test other cases
# # testing=sort_odd_even([1,2,3,4,5,6,7,8,9,10,11,12])
# # print(testing)

# #case of an empty list
# test2=sort_odd_even([])
# print(test2)

