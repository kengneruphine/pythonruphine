# program that read in 20 numbers using a list

# using the method set()
alist=[2,3,4,2,3,7,9,49,7,10,13,12,4,5,19,20,45,18,19,20]
clist = []
clist = list(set(alist)) # convert list to set then back to list agian
print clist

        # another method1
#list1 = sorted(set(alist))
#print list1

         #another method2
#blist = []
#for i in alist:
#	if i not in blist:
#		blist.append(i)

#print blist


        #another method3, preserves order
#print  dict.fromkeys(alist).keys()       