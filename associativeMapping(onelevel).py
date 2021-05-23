# Fully Associative mapping
def associative_Map_read(address):
    L=CL-1
    flag=0
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    bitsOftag = len(address) - bitsOfBlock
    Tn=address[:bitsOftag]
    Bs= address[bitsOftag:]
    
    for i in range(CL):
        if(cache[i] == 'null'):
            cache[i] = Tn
            print("Read miss")
            print("address NOT FOUND")
            print("Current Tag is replaced by an empty block in the cache line   "+ str(i))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
            break   
        elif(cache[i]==Tn ):
            print("Read hit")
            print("address FOUND in the cache line  "+str(i))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
            break
        elif i==L :
            flag=1
    if(flag==1):
        del cache[0]
        cache.append(Tn)
        r=cache[CL-2]
        print("Read miss")
        print("address NOT FOUND ")
        print("Current Tag is replaced by Tag "+r+"   in the cache line   "+str(L))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    
    print(cache)
        
def associative_Map_write(address):
    L=CL-1
    flag=0
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    bitsOftag = len(address) - bitsOfBlock
    Tn=address[:bitsOftag]
    Bs= address[bitsOftag:]
    
    for i in range(CL):
        if(cache[i] == 'null'):
            cache[i] = Tn
            print("Write miss")
            print("address NOT FOUND")
            print("Current Tag is replaced by an empty block in the cache line   "+ str(i))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
            break   
        elif(cache[i]==Tn ):
            print("Write hit")
            print("address FOUND, writing data to cache  in the cache line  "+str(i))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
            break
        elif i==L :
            flag=1
    if(flag==1):
        del cache[0]
        cache.append(Tn)
        r=cache[CL-2]
        print("Write miss")
        print("address NOT FOUND ")
        print("Current Tag is replaced by Tag "+r+"   in the cache line   "+str(L))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    
    print(cache)
        


    



CL = int(input("num of cache lines :")) 
B = int(input("block size :"))
request =input("Request :")
cache = ['null'] * CL

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
                
