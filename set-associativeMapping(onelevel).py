# K-way Set Associative
def setAssociative_Map_read(address):
    flag=0
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    setNo=int(CL / S)
    if (CL==1):
        bitsOfSet = setNo
    else:
        bitsOfSet =(int(setNo)-1).bit_length()
    bitsOftag = len(address) -(bitsOfBlock+bitsOfSet)
    Tn=address[:bitsOftag]
    Sn= address[bitsOftag:(bitsOftag+bitsOfSet)]
    Bs= address[(bitsOftag+bitsOfSet):]
    tag=int(Tn, 2)
    word =int(Bs , 2)
    Set = int(Sn,2)
    # print(Set)
    search=cache[Set]
    for i in range(setNo):
        if(search[i] == 'null'):
            search[i] = Tn
            print("Read miss")
            print("address NOT FOUND")
            print("Current Tag is replaced by an empty block ")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
            break   
        elif(search[i]==Tn ):
            print("Read hit")
            print("address FOUND ")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
            break
        elif i==(setNo-1) :
            flag=1
    if(flag==1):
        del search[0]
        search.append(Tn)
        r=search[setNo-2]
        print("Read miss")
        print("address NOT FOUND ")
        print("Current Tag is replaced by Tag "+r)
        print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
    
    print(cache)

def setAssociative_Map_write(address):
    flag=0
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    setNo=int(CL / S)
    if (CL==1):
        bitsOfSet = setNo
    else:
        bitsOfSet =(int(setNo)-1).bit_length()
    bitsOftag = len(address) -(bitsOfBlock+bitsOfSet)
    Tn=address[:bitsOftag]
    Sn= address[bitsOftag:(bitsOftag+bitsOfSet)]
    Bs= address[(bitsOftag+bitsOfSet):]
    tag=int(Tn, 2)
    word =int(Bs , 2)
    Set = int(Sn,2)
    search=cache[Set]
    for i in range(setNo):
        if(search[i] == 'null'):
            search[i] = Tn
            print("Write miss")
            print("address NOT FOUND")
            print("Current Tag is replaced by an empty block ")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
            break   
        elif(search[i]==Tn ):
            print("Write hit")
            print("address FOUND, writing data to a cache ")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
            break
        elif i==(setNo-1) :
            flag=1
    if(flag==1):
        del search[0]
        search.append(Tn)
        r=search[setNo-2]
        print("Write miss")
        print("address NOT FOUND ")
        print("Current Tag is replaced by Tag "+r)
        print("Tag:  "+Tn+"  Block Offset:  "+Bs+ "  Set:  "+str(Set))
    
    print(cache)



CL = int(input("num of cache lines :")) 
B = int(input("block size :"))
S=int(input("Set: "))
request = input("Request :")
LinesInSet = int(CL/S)
cache =[]
for i in range(S):
    cache.append([])
    for j in range(LinesInSet):
        cache[i].append('null')

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
        
