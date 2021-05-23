def setAssociative_Map_read(address):
    flag =0
    L=Linescache2-1
    M=Linescache1-1
    a=0
    stop=0
    count=0
    setNo=int(CL / S)
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    bitsOfSet =(int(setNo)-1).bit_length()
    bitsOftag = len(address) -(bitsOfBlock+bitsOfSet)
    Tn=address[:bitsOftag]
    Sn= address[bitsOftag:(bitsOftag+bitsOfSet)]
    Bs= address[(bitsOftag+bitsOfSet):]
    tag=int(Tn, 2)
    word =int(Bs , 2)
    Set = int(Sn,2)
    search=cache1[Set]
    search2= cache2[Set]

    for i in range(Linescache1):
        
        if(search[i]==Tn ):
            print("Read hit")
            print("address FOUND in a cache level 1 ")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
            stop=1
            break
    if(stop==0):
        
        for i in range(Linescache2):
            if(search2[i]==Tn ):
                print("Read hit")
                print("address FOUND in a cache level 2")
                print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
                a=1
                break 
    if (stop==0)  : 
           
        if(a==1 or a==0 ):
            for i in range(Linescache1):
                if(search[i] == 'null'):
                    search[i] = Tn
                    print("Read miss")
                    print("address NOT FOUND in a cache level 1")
                    print("Current Tag is replaced by an empty block ")
                    print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
                    break   
            
                elif i==M :
                    flag=1
    if(flag==1):
    
        c=search[0]
        del search[0]
        search.append(Tn)
        r=search[Linescache1-2]
        print("Read miss")
        print("address NOT FOUND in a cache level 1")
        print("Current Tag is replaced by Tag "+r)
        print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
        if(search2[Linescache2-1]=='null'):
            search2[Linescache2-1]=c
        else:
            del search2[0]
            search2.append(c)
    if(stop==0):
        
        if(a==0):
            for i in range(Linescache2):
                if(search2[i] == 'null'):
                    search2[i] = Tn
                    print("Read miss")
                    print("address NOT FOUND in a cache level 2")
                    print("Current Tag is replaced by an empty block ")
                    print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
                    break   
            
                elif i==L :
                    count=1
    if(count==1):
        del search2[0]
        search2.append(Tn)
        r=search2[Linescache2-2]
        print("Read miss")
        print("address NOT FOUND in a cache level 2")
        print("Current Tag is replaced by Tag "+r)
        print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))

    print("cache1", end =" ") 
    print(cache1)
    print("cache2", end = " ")
    print(cache2)
def setAssociative_Map_write(address):
    flag =0
    L=Linescache2-1
    M=Linescache1-1
    a=0
    stop=0
    count=0
    setNo=int(CL / S)
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    bitsOfSet =(int(setNo)-1).bit_length()
    bitsOftag = len(address) -(bitsOfBlock+bitsOfSet)
    Tn=address[:bitsOftag]
    Sn= address[bitsOftag:(bitsOftag+bitsOfSet)]
    Bs= address[(bitsOftag+bitsOfSet):]
    tag=int(Tn, 2)
    word =int(Bs , 2)
    Set = int(Sn,2)
    search=cache1[Set]
    search2= cache2[Set]

    for i in range(Linescache1):
        
        if(search[i]==Tn ):
            print("Write hit")
            print("address FOUND in a cache level 1 ")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
            stop=1
            break
    if(stop==0):
        
        for i in range(Linescache2):
            if(search2[i]==Tn ):
                print("Write hit")
                print("address FOUND in a cache level 2")
                print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
                a=1
                break 
    if (stop==0)  : 
           
        if(a==1 or a==0 ):
            for i in range(Linescache1):
                if(search[i] == 'null'):
                    search[i] = Tn
                    print("Write miss")
                    print("address NOT FOUND in a cache level 1")
                    print("Current Tag is replaced by an empty block ")
                    print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
                    break   
            
                elif i==M :
                    flag=1
    if(flag==1):
    
        c=search[0]
        del search[0]
        search.append(Tn)
        r=search[Linescache1-2]
        print("Write miss")
        print("address NOT FOUND in a cache level 1")
        print("Current Tag is replaced by Tag "+r)
        print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
        if(search2[Linescache2-1]=='null'):
            search2[Linescache2-1]=c
        else:
            del search2[0]
            search2.append(c)
    if(stop==0):
        
        if(a==0):
            for i in range(Linescache2):
                if(search2[i] == 'null'):
                    search2[i] = Tn
                    print("Write miss")
                    print("address NOT FOUND in a cache level 2")
                    print("Current Tag is replaced by an empty block ")
                    print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
                    break   
            
                elif i==L :
                    count=1
    if(count==1):
        del search2[0]
        search2.append(Tn)
        r=search2[Linescache2-2]
        print("Write miss")
        print("address NOT FOUND in a cache level 2")
        print("Current Tag is replaced by Tag "+r)
        print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))

    print("cache1", end =" ") 
    print(cache1)
    print("cache2", end = " ")
    print(cache2)



CL = int(input("num of cache lines :")) 
B = int(input("block size :"))
S=int(input("Set: "))
request =input("Request :")
Linescache2 = int(CL/S)
Linescache1 =int(Linescache2/2)
cache1 =[]
cache2 =[]
for i in range(S):
    cache1.append([])
    for j in range(Linescache1):
        cache1[i].append('null')
for i in range(S):
    cache2.append([])
    for j in range(Linescache2):
        cache2[i].append('null')

while (request != 'stop'):
    if(request == 'Write'):
        address=input("CPU generates address :")
        data= input("data :")
        setAssociative_Map_write(address)
        request =input("Request :")
    else:
        address=input("CPU generates address :")
        setAssociative_Map_read(address)
        request = input("Request :")
