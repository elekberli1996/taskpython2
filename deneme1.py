#task1
# import math
# list=[-3,-4,0,2,4,3,5,25,36,47,49,60,20,100,121]
# def testsqrt(a): 
#     if a<0:
#         return
#     b=math.sqrt(a)
#     c=round(b,2)
#     if b==c:
#         return a
    
# newlist2=[testsqrt(i) for i in list if testsqrt(i)!=None]
# print(newlist2)

####################3
#task2
# list=[1,2,3,4,5,6,7,8,9,10,10,"ali","ali",11,11]

# def yoxla(a):
#     newlist=[]
#     yoxla=0
#     for a in list:
#         for i in list:
#             if a==i:
#                 yoxla+=1
#         if yoxla==1:
#             newlist.append(a)    
#         yoxla=0 
#     return newlist    
 
# print(yoxla(list))

#taks3
# list=[1,2,3,4,5,6]
# def hasil(ededler):
#     hasil=1
#     for i in ededler:
#         hasil=hasil*i
#     return hasil

# print(hasil(list))

#task4

# a=100
# newlist=[ i for i in range(1,a) if(a%i==0)]
# print(newlist)

#task5 

# list=["may","iyun","iyul","aprel","sentyabr","yanvar"]
# newdict={k: len(k) for k  in list}
# print(newdict)

#task6


# list=["Emin Elekberli","Evez Elekberli","Inci Elekberli"]

# def getname(a):
#    list= a.split()
#    name=list[0].lower()
#    return name

# newList=[getname(i) for i in  list]
# print(newList)

#task7 

# list1=[3,4,5]
# list2=[4,5,6]
# newList=[]

# for i in range(len(list1)):
#     a=(list1[i]+list2[i])/2
#     newList.append(a)
# print(newList)
    

 
