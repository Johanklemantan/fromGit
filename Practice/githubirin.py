#NOMOR 1 FIX
def Hashtag(string):
    #untuk kondisi empty string
    if string=="":
        return False
    else:
    #splitting the string 
        splitted=string.split()
    #membuat list yang berisi kata2 dari string dengan huruf depan kapital semua
        capitalized=[]

    #membuat kata2 dari string supaya huruf depannya kapital semua    
        for i in splitted:
            capitalized.append(i.capitalize())
        print(capitalized)
    #string kosong buat nampung gabungan kata2 yang udah kapital depannya

        stringbaru="".join(capitalized)
        print(stringbaru)
        print('#'+ stringbaru)
        
        #  stringbaru=""
    #menggabungkan string yang huruf depan dari setiap katanya udah huruf kapital semua
        # for j in capitalized:
        #     stringbaru+=j

    #supaya depannya ada hashtagnya
        stringbaru="#"+stringbaru

    #kalau final result lebih dari 140 chars, return False
        if len(stringbaru)>140:
            return False
        else:
            return stringbaru
    #normal case, random capitalized words
tes=Hashtag(" Hello how are you dOing")
print(tes)