# def Hashtag (a):

#     if a == "":
#         return False #untuk return False saat inputnya empty string
#     else:
#         sentence = a.split()
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



#NO 2
  
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


#NO 3


# def asc(gjl):
#     '''
#     mengurutkan angka ganjil kecil ke besar dengan bubble sort
#     '''
#     swap = 1
#     while swap > 0:
#         swap = 0
#         for i in range(len(gjl)-1):
#             if gjl[i] > gjl [i+1]:
#                 swap += 1
#                 gjl[i],gjl[i+1]=gjl[i+1],gjl[i]
#     return gjl

# def dsc(gnp):
#     '''
#     mengurutkan angka genap besar ke kecil dengan bubble sort
#     '''
#     swap = 1
#     while swap > 0:
#         swap = 0
#         for i in range(len(gnp)-1):
#             if gnp[i] < gnp [i+1]:
#                 swap += 1
#                 gnp[i],gnp[i+1]=gnp[i+1],gnp[i]
#     return gnp

# def sort_odd_even(inputan):
#     if inputan == []:
#         return f"Input list kosong {inputan}" # return list kosong bila diinput list kosong
#     else:
#         pos = []
#         odd = []
#         even = []
#         for s in range(len(inputan)):
#             if inputan[s]=="":
#                 inputan[s]="0"  #error handling apabila saat penginputan ada empty string
#         for b in range(len(inputan)):
#             if int(inputan[b])%2==0:
#                 pos.append(1) # mencatat posisi genap
#                 even.append(inputan[b]) #mengumpulkan angka genap
#             else :
#                 pos.append(0) #mencatat posisi ganjil
#                 odd.append(inputan[b]) #mengumpulkan angka ganjil
#         odd = asc(odd)
#         even = dsc(even)
#         odd_index = 0
#         even_index = 0
#         hasil = []
#         for k in pos :
#             if k == 0:
#                 hasil.append(odd[odd_index])
#                 odd_index += 1
#             if k == 1:
#                 hasil.append(even[even_index])
#                 even_index += 1
#         return f"Setelah disort sesuai ketentuan : {hasil}"
    


# # cara 1
# myList = []
# qty = (input("Mau berapa angka ? "))
# if qty=="" or int(qty)<1 :
#     print (f"Angka yang kamu input adalah {myList}")
#     print(f"Input list kosong {myList}")
# else:
#     qty = int(qty)
#     for a in range (1,qty+1):
#         myList.append(input(f"Angka ke-{a}= "))
#     print (f"Angka yang kamu input adalah {myList}")
#     print(f"{sort_odd_even(myList)}")

# cara 2
# myList = [5,3,2,8,1,4]
# sort_odd_even(myList)