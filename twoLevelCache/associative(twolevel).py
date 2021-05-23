
def associative_Map_read(address):
    flag =0
    L=CL-1
    M=cache_L1-1
    a=0
    stop=0
    count=0
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    bitsOftag = len(address) - bitsOfBlock
    Tn=address[:bitsOftag]
    Bs= address[bitsOftag:]
    
    for i in range(cache_L1):
        if(cache1[i]==Tn ):
            print("Read hit")
            print("address FOUND in the cache line  "+str(i)+"   and cache level 1")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
            stop=1
            break
    if(stop==0):
        # print(1)
        for i in range(CL):
            if(cache2[i]==Tn ):
                print("Read hit")
                print("address FOUND in the cache line  "+str(i)+"   and cache level 2")
                print("Tag:  "+Tn+"  Block Offset:  "+Bs)
                a=1
                break 


    if (stop==0)  : 
        # print(2)    
        if(a==1 or a==0 ):
            for i in range(cache_L1):
                if(cache1[i] == 'null'):
                    cache1[i] = Tn
                    print("Read miss")
                    print("address NOT FIND in a cache level 1")
                    print("Current Tag is replaced by an empty block in cache line   "+ str(i))
                    print("Tag:  "+Tn+"  Block Offset:  "+Bs)
                    break   
            
                elif i==M :
                    flag=1
    if(flag==1):
        # print(3)
        c=cache1[0]
        del cache1[0]
        cache1.append(Tn)
        r=cache1[cache_L1-2]
        print("Read miss")
        print("address NOT FIND in a cache level 1")
        print("Current Tag is replaced by Tag "+r+"   in cache line   "+str(L))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        if(cache2[CL-1]=='null'):
            cache2[CL-1]=c
        else:
            del cache2[0]
            cache2.append(c)
    
    if(stop==0):
        if(a==0):
            # print(4)
            for i in range(CL):
                if(cache2[i] == 'null'):
                    cache2[i] = Tn
                    print("Read miss")
                    print("address NOT FIND in a cache level 2")
                    print("Current Tag is replaced by an empty block in cache line   "+ str(i))
                    print("Tag:  "+Tn+"  Block Offset:  "+Bs)
                    break   
            
                elif i==L :
                    count=1
    if(count==1):
        # print(5)
        del cache2[0]
        cache2.append(Tn)
        r=cache2[CL-2]
        print("Read miss")
        print("address NOT FIND in a cache level 2")
        print("Current Tag is replaced by Tag "+r+"   in cache line   "+str(L))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)

    print("cache1", end =" ") 
    print(cache1)
    print("cache2", end = " ")
    print(cache2)

def associative_Map_write(address):
    flag =0
    L=CL-1
    M=cache_L1-1
    a=0
    stop=0
    count=0
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    bitsOftag = len(address) - bitsOfBlock
    Tn=address[:bitsOftag]
    Bs= address[bitsOftag:]
    
    for i in range(cache_L1):
        if(cache1[i]==Tn ):
            print("Write hit")
            print("address FOUND, writing data to cache  in the cache line   "+str(i)+"   and cache level 1")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
            stop=1
            break
    if(stop==0):
        # print(1)
        for i in range(CL):
            if(cache2[i]==Tn ):
                print("Write hit")
                print("address FOUND, writing data to cache  in the cache line   "+str(i)+"   and cache level 2")
                print("Tag:  "+Tn+"  Block Offset:  "+Bs)
                a=1
                break 


    if (stop==0)  : 
        # print(2)    
        if(a==1 or a==0 ):
            for i in range(cache_L1):
                if(cache1[i] == 'null'):
                    cache1[i] = Tn
                    print("Write miss")
                    print("address NOT FIND in a cache level 1")
                    print("Current Tag is replaced by an empty block in cache line   "+ str(i))
                    print("Tag:  "+Tn+"  Block Offset:  "+Bs)
                    break   
            
                elif i==M :
                    flag=1
    if(flag==1):
        # print(3)
        c=cache1[0]
        del cache1[0]
        cache1.append(Tn)
        r=cache1[cache_L1-2]
        print("Write miss")
        print("address NOT FIND in a cache level 1")
        print("Current Tag is replaced by Tag "+r+"   in cache line   "+str(L))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        if(cache2[CL-1]=='null'):
            cache2.append(c)
        else:
            del cache2[0]
            cache2.append(c)
    
    if(stop==0):
        if(a==0):
            # print(4)
            for i in range(CL):
                if(cache2[i] == 'null'):
                    cache2[i] = Tn
                    print("Write miss")
                    print("address NOT FIND in a cache level 2")
                    print("Current Tag is replaced by an empty block in cache line   "+ str(i))
                    print("Tag:  "+Tn+"  Block Offset:  "+Bs)
                    break   
            
                elif i==L :
                    count=1
    if(count==1):
        # print(5)
        del cache2[0]
        cache2.append(Tn)
        r=cache2[CL-2]
        print("Write miss")
        print("address NOT FIND in a cache level 2")
        print("Current Tag is replaced by Tag "+r+"   in cache line   "+str(L))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)

    print("cache1", end =" ") 
    print(cache1)
    print("cache2", end = " ")
    print(cache2)




CL = int(input("num of cache lines :")) 
B = int(input("block size :"))
request =input("Request :")
cache_L1 = int(CL/2)
cache2 = ['null'] * CL
cache1= ['null'] * cache_L1

while (request != 'stop'):
    if(request == 'Write'):
        address=input("CPU generates address :")
        data= input("data :")
        associative_Map_write(address)
        request =input("Request :")
    else:
        address=input("CPU generates address :")
        associative_Map_read(address)
        request = input("Request :")
                
