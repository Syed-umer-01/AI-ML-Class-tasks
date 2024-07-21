'''ls=[1,2,3,4,5,6,7,8]
ls0=iter(ls) 

print(next(ls0))
print(next(ls0))
print(next(ls0))
print(next(ls0))
print(next(ls0))
print(next(ls0))
print(next(ls0))'''''
# -------------------------------
#tuple

'''t = ('1,2,3,4,5,6',)
print(type(t))'''

'''tp= (1,2,3,4,5)
for i in tp:
    print(i)'''
    
'''tp=(1,2,3,4,5,6,8,9)
tp0=set(tp)
print(type(tp0))'''

# ---------------------------

'''fname=['aslam','ali']
lname=['ali','khan']
fullname=[]
for i in fname:
    for j in lname:
        fullname.append(i+" "+j)
print(fullname)
del fullname[2]
print(fullname)'''
# --------------------------

#enumerate
'''tp=('hello','umer')
en=enumerate(tp)
print(en)'''
# ---------------------------
# break, continue, pass statement
# a=12
# b=45
# if a<b:
#     #if we never want further if execuation then use pass
#     pass
# for i in range (15):
#     print(i)
#     if i==5:
#         break

'''marks=int(input('enter marks out of 100:'))
print('A') if marks>=80  else print('fail')'''
    


#list comprehension


# ls=['apple','banna','mango','orange']
# ls0=[i for i in ls if 'o' in i]
# print(ls0) 

fname=['aslam','ali']
lname=['ali','khan']
fullname=[]
for i in range(len(fname)):
    fullname.append(fname[i]+ ' '+lname[i])
print(fullname)

    
 

   
    
    



