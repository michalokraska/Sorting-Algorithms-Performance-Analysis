import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1000000)


def Merge2(lst,start,mid,stop):
    list_pom=[]
    i,j=start,mid
    for _ in range(start,stop+1):
        if i==mid or (j<=stop and lst[j]<lst[i]):
            list_pom.append(lst[j])
            j+=1
        else:
            list_pom.append(lst[i])
            i+=1
    for k in range(start,stop+1):
        lst[k]=list_pom[k-start]

def MergeSort2(lst,start,stop):
    if stop-start<=1:
        return
    mid=(start+stop)//2
    MergeSort2(lst,start,mid)
    MergeSort2(lst,mid,stop)
    Merge2(lst,start,mid,stop)
    return lst




def Partition(lst,start,stop): 
    pivot=lst[stop]
    j=start
    for i in range(start,stop):
       if lst[i]<pivot:
           lst[i],lst[j]=lst[j],lst[i]
           j+=1
    lst[j],lst[stop]=lst[stop],lst[j]
    return j

def QuickSortR(lst,start,stop):
    if start>=stop:
        return
    stop1=Partition(lst,start,stop)-1
    start2=stop1+2
    QuickSortR(lst,start,stop1)
    QuickSortR(lst,start2,stop)

def QuickSort(lst):
    QuickSortR(lst,0,len(lst)-1)
    




def Merge_W(lst1,start,mid,stop):
    lst2=lst1[start:mid]
    lst3=lst1[mid:stop]
    lst2.append(math.inf)
    lst3.append(math.inf)
    i,j=0,0
    for k in range(start,stop):
        if lst2[i]<=lst3[j]:
            lst1[k]=lst2[i]
            i+=1
        else:
            lst1[k]=lst3[j]
            j+=1
            
def MergeSort_W(lst,start,stop):
    if stop-start<=1:
        return
    mid=(start+stop)//2
    MergeSort_W(lst,start,mid)
    MergeSort_W(lst,mid,stop)
    Merge_W(lst,start,mid,stop)
    return lst


def InsertSort(lst, start, stop):
    for i in range(start + 1, stop):
        key = lst[i]
        j = i - 1
        while j >= start and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        
def MergeSort_WI(lst,start,stop):
    if stop-start<=20:
        InsertSort(lst, start, stop)
        return
    mid=(start+stop)//2
    MergeSort_WI(lst,start,mid)
    MergeSort_WI(lst,mid,stop)
    Merge_W(lst,start,mid,stop)
    return lst

def QuickSortR_I(lst,start,stop):
    if stop - start <= 20:
        InsertSort(lst, start, stop)
        return
    if start>=stop:
        return
    stop1=Partition(lst,start,stop)-1
    start2=stop1+2
    QuickSortR(lst,start,stop1)
    QuickSortR(lst,start2,stop)

def QuickSort_I(lst):
    QuickSortR_I(lst,0,len(lst)-1)
    
siz=[15000]
def odch_stand(siz, val):

    merge_os=[]
    quick_os=[]    
    for i in range(30):
        lst=[random.randint(1, val) for g in range(i)]
        lst_copy = list(lst)
        
        a = time.time()
        MergeSort2(lst, 0, len(lst) - 1)
        b = time.time()
        merge_os.append(b-a)
        
        a = time.time()
        QuickSort(lst_copy)
        b = time.time()
        quick_os.append(b-a)
    
    merge_ods = np.std(merge_os)
    quick_ods = np.std(quick_os)
    
    print("odchylenie standardowe dla mergesort", merge_ods)
    print("odchylenie standardowe dla quicksort", quick_ods)

odch_stand(siz, 1000)

    
siz=[]
x=0
while x < 15000:
    x=x+1000
    siz.append(x)

def times(siz, val):
    timem=[]
    timeq=[]
    timem_w=[]
    timeq_I=[]
    timem_wI=[]
    for i in siz:
        lst=[random.randint(1, val) for g in range(i)]
        lst_copy=list(lst)
        lst_copy2=list(lst)
        lst_copy3=list(lst)
        lst_copy4=list(lst)
        
        a=time.time()
        MergeSort2(lst,0,len(lst)-1)
        b=time.time()
        timem.append(b-a)
    
        a=time.time()
        QuickSort(lst_copy)
        b=time.time()
        timeq.append(b-a)
        
        a=time.time()
        MergeSort_W(lst_copy2,0,len(lst))
        b=time.time()
        timem_w.append(b-a)
        
        a=time.time()
        QuickSort_I(lst_copy3)
        b=time.time()
        timeq_I.append(b-a)
        
        a=time.time()
        MergeSort_WI(lst_copy4,0,len(lst))
        b=time.time()
        timem_wI.append(b-a)
        
    return timem, timeq, timem_w, timeq_I, timem_wI

mergeshort, quickshort, mergeshort_w, quickshort_I, mergeshort_wI = times(siz, 20)
mergelong, quicklong, mergelong_w, quicklong_I, mergelong_wI = times(siz, 20000)


plt.figure(figsize=(14,6))

plt.subplot(3,2,1)
plt.plot(siz, mergeshort, label="mergesort", marker="o")
plt.plot(siz, quickshort, label="quicksort", marker="o")
plt.title("liczby z przedzialu 0-20")
plt.xlabel("rozmiar")
plt.ylabel("czas sortowania w sekundach")
plt.legend()
plt.grid(True)


plt.subplot(3, 2, 2)
plt.plot(siz, mergelong, label='MergeSort', marker='o')
plt.plot(siz, quicklong, label='QuickSort', marker='o')
plt.title('liczby z przedzialu 0-20000')
plt.xlabel('rozmiar')
plt.ylabel('czas sortowania w sekundach')
plt.legend()
plt.grid(True)


plt.subplot(3,2,3)
plt.plot(siz, mergeshort, label="mergesort", marker="o")
plt.plot(siz, quickshort, label="quicksort", marker="o")
plt.plot(siz, mergeshort_w, label='Merge z wartownikiem', marker='o')
plt.title("liczby z przedzialu 0-20")
plt.xlabel("rozmiar")
plt.ylabel("czas sortowania w sekundach")
plt.legend()
plt.grid(True)


plt.subplot(3, 2, 4)
plt.plot(siz, mergelong, label='MergeSort', marker='o')
plt.plot(siz, quicklong, label='QuickSort', marker='o')
plt.plot(siz, mergelong_w, label='Merge z wartownikiem', marker='o')
plt.title('liczby z przedzialu 0-20000')
plt.xlabel('rozmiar')
plt.ylabel('czas sortowania w sekundach')
plt.legend()
plt.grid(True)


plt.subplot(3,2,5)
plt.plot(siz, mergeshort, label="mergesort", marker="o")
plt.plot(siz, quickshort, label="quicksort", marker="o")
plt.plot(siz, mergeshort_w, label='Merge z wartownikiem', marker='o')
plt.plot(siz, quickshort_I, label="quicksort z intersortem", marker="o")
plt.plot(siz, mergeshort_wI, label='Merge z wartownikiem i intersortem', marker='o')
plt.title("liczby z przedzialu 0-20")
plt.xlabel("rozmiar")
plt.ylabel("czas sortowania w sekundach")
plt.legend()
plt.grid(True)


plt.subplot(3, 2, 6)
plt.plot(siz, mergelong, label='MergeSort', marker='o')
plt.plot(siz, quicklong, label='QuickSort', marker='o')
plt.plot(siz, mergelong_w, label='Merge z wartownikiem', marker='o')
plt.plot(siz, quicklong_I, label='QuickSort z intersortem', marker='o')
plt.plot(siz, mergelong_wI, label='Merge z wartownikiem i intersortem', marker='o')
plt.title('liczby z przedzialu 0-20000')
plt.xlabel('rozmiar')
plt.ylabel('czas sortowania w sekundach')
plt.legend()
plt.grid(True)


plt.suptitle('Porównanie MergeSort i QuickSort')
plt.tight_layout()
plt.show()


    
    



    

