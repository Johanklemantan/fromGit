# x = [0, 1.5, 243, 1341,4,43, 34, 1,343,1049]
# print(x)
# y = x.sort()
# print(y)

# x = [0, 1.5, 243, 1341,4,43, 34, 1,343,1049]
# # print(x.sort())
# x.sort()
# print(x)
# x.sort(reverse = True)
# print(x)
# x.sort(reverse = False)
# print(x)

# d = { "key1" : { "key2" : "item2" },
# "kucing" : [3,
# "jerapah"] };
# print(d["key1"]);
# print(d["key1"]["key2"]);
# print(d["kucing"]);
# print(d["kucing"][1]);

# t = (1, [0, "test"], { "a1" : True });
# print(t[2]["a1"]);
# print(t[1][1]);
# t[1][1] = "akan";
# print(t[1][1]);
# t[1] = "mark";
# print(t[1]);

# listNum = [ 1, 2, 3, 4, 5]
# listNum = [item * 2 for item in listNum]
# print(listNum)

# def times2(num) :
#     return num * 2
# listNum = [ 1, 2, 3, 4, 5]
# listNum = [times2(item) for item in listNum]
# print(listNum)

# import math;
# def reverseList(theList) :
#     for i in range(0, math.floor(len(theList)/2)) :
#         tempList = theList[i];
#         theList[i] = theList[len(theList) - 1 - i];
#         theList[len(theList) - 1 - i] = tempList;
#         return theList;
# print(reverseList([1,2,3,4,5,6,7,8]));

# x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1]
# def bubbleSort(list) :
#     for i in range(len(list), 0, -1) :
#         for j in range(0,i-1) :
#             if (list[j] > list[j + 1]) :
#                 temp = list[j];
#                 list[j] = list[j + 1];
#                 list[j + 1] = temp;
#         return list;
# print(bubbleSort(x));.


def fibo(x):
    data =[0,1]
    for i in range(2,x):
            data.append(data[i-2]+data[i-1])
    return data[x-1]
print(fibo(8))

def fibo(urut) :
    listData = [1,1];
    for i in range(2,urut):
        listData.append(listData[i-2] + listData[i-1]);
    return listData[urut-1];
print(fibo(8));