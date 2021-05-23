def direct_Map_read(address):
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    bitsOfLine =(int (CL)-1).bit_length()
    bitsOftag = len(address) -(bitsOfBlock+bitsOfLine)
    Tn=address[:bitsOftag]
    Ln= address[bitsOftag:(bitsOftag+bitsOfLine)]
    Bs= address[(bitsOftag+bitsOfLine):]
    tag=int(Tn, 2)
    word =int(Bs , 2)
    integer = int(Ln,2)
    n= integer % cache_L1
    if(cache1[n]==Tn ):
       
        print("Read hit")
        print("Address FOUND" +"  in the cache line  "+str(n)+"    and cache level 1" )
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    else :
        if(cache2[integer]==Tn ):
       
            print("Read hit")
            print("Address FOUND" +"  in the cache line  "+str(integer)+"    and cache level 2" )
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        
        elif(cache2[integer] == 'null'):
       
            print("Read miss")
            print("Address NOT FOUND in the cache level 2")
            cache2[integer] = Tn
            print("Current Tag is replaced by an empty block in cache line   "+str(integer))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        else:
            print("Read miss")
            print("Address NOT FOUND in the  cache level 2")
            replace = cache2[integer]
            cache2[integer] = Tn
            print("current Tag  is replaced by Tag   "+ replace+"  "+"in the cache line   "+ str(integer))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        if(cache1[n] == 'null'):
       
            print("Read miss")
            print("Address NOT FOUND in the cache level 1")
            cache1[n] = Tn
            print("Current Tag is replaced by an empty block in the cache line   "+str(n))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        else:
            print("Read miss")
            print("Address NOT FOUND in the  cache level 1")
            replace = cache1[n]
            cache1[n] = Tn
            print("current Tag  is replaced by Tag   "+ replace+"  "+"in the cache line   "+ str(n))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    print("cache1", end = " ") 
    print(cache1)
    print("cache2", end = " ")
    print(cache2)


def direct_Map_write(address):
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    bitsOfLine =(int (CL)-1).bit_length()
    bitsOftag = len(address) -(bitsOfBlock+bitsOfLine)
    Tn=address[:bitsOftag]
    Ln= address[bitsOftag:(bitsOftag+bitsOfLine)]
    Bs= address[(bitsOftag+bitsOfLine):]
    tag=int(Tn, 2)
    word =int(Bs , 2)
    integer = int(Ln,2)
    n= integer % cache_L1
    if(cache1[n]==Tn ):
       
        print("Write hit")
        print("address FOUND, writing data to cache  in the cache line  "+str(n) + "   and cache level one")
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    else :
        if(cache2[integer]==Tn ):
       
            print("Write hit")
            print("address FOUND, writing data to cache  in the cache line"+str(integer)+"  and cache level two")
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        
        elif(cache2[integer] == 'null'):
       
            print("Write miss")
            print("Address NOT FOUND in the cache level two")
            cache2[integer] = Tn
            print("Current Tag is replaced by an empty block in the cache line   "+str(integer))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        else:
            print("Write miss")
            print("Address NOT FOUND in the cache level two")
            replace = cache2[integer]
            cache2[integer] = Tn
            print("current Tag  is replaced by Tag   "+ replace+"  "+"in the cache line   "+ str(integer))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        if(cache1[n] == 'null'):
       
            print("Write miss")
            print("Address NOT FOUND in the  cache level one")
            cache1[n] = Tn
            print("Current Tag is replaced by empty block in the cache line   "+str(n))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
        else:
            print("Write miss")
            print("Address NOT FOUND in the cache level one")
            replace = cache1[n]
            cache1[n] = Tn
            print("current Tag  is replaced by Tag   "+ replace+"  "+"in the cache line   "+ str(n))
            print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    print("cache1", end = " ") 
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
        direct_Map_write(address)
        request =input("Request :")
    else:
        address=input("CPU generates address :")
        direct_Map_read(address)
        request = input("Request :")