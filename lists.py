# lists are mutable ,allows duplicate ,ordered
mylist = ["banana","apple","Orange"];
if "apple" in mylist:
    print("Yes");
else:
    print("No");
print(len(mylist));
# adding element
mylist.append("Strawberries");
print(mylist);
# insertion at position
mylist.insert(1,"Pineapple");
print(mylist)
# remove a particular element
mylist.remove("Orange");
print(mylist)
# sorting the list
mylist.sort();
print("Sorting list",mylist)
# reverse the list
mylist.reverse();
print(mylist)
# copy one list to another list 
a=mylist
print(a)
# copy one list to another list from one index to another
a1=mylist[0:1];
print(a1);

#we also select steps of index means how many steps after we print the elemnt
# example a[1,3,4,6,7,8] and we say a[::2] means we print after step 2 Ans =[1,4,7];
mylist1=[1,3,4,6,7,8]
a3=mylist1[::2];
print(a3);
# if we want to print in reverse order so we give negative steps 
s4=mylist1[:: -2];
print(s4);
# lists copy method 
# method 1 using = operator 
        # list_org=[1,2,3,4];
        # list_cpy=list_org;
        # print(list_cpy);
        # # if we want to add new items in list_cpy so those element also add in org becuase in this ,method we point both list at same index in memory
        # list_cpy.append(5);
        # print("Original",list_org)
        # print("Copy",list_cpy)
# method2
        # list_org=[1,2,3,4];
        # list_cpy=list_org.copy();
        # print(list_cpy);
        # list_cpy.append(5);
        # print("Original",list_org)
        # print("Copy",list_cpy)
# method 3
list_org=[1,2,3,4];
list_cpy=list_org[:];
print(list_cpy);
list_cpy.append(5);
print("Original",list_org)
print("Copy",list_cpy)

# method 4
list_cpy2=[i for i in mylist]
print(list_cpy2);