def direct_Map_read(address):
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    if (CL==1):
        bitsOfLine = 1
    else:
        bitsOfLine =(int (CL)-1).bit_length()
    bitsOftag = len(address) -(bitsOfBlock+bitsOfLine)
    Tn=address[:bitsOftag]
    Ln= address[bitsOftag:(bitsOftag+bitsOfLine)]
    Bs= address[(bitsOftag+bitsOfLine):]
    tag=int(Tn, 2)
    word =int(Bs , 2)
    integer = int(Ln,2)
    if(cache[integer] == 'null'):
       
        print("Read miss")
        print("Address NOT FOUND" +"  in the cache line  "+str(integer))
        cache[integer] = Tn
        print("Current Tag is replaced by an empty block in the cache line   "+str(integer))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    elif(cache[integer]==Tn ):
       
        print("Read hit")
        print("Address FOUND" +"  in the cache line  "+str(integer) )
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    else:
       
        print("Read miss")
        print("Address NOT FOUND" +"  in the cache line "+str(integer))
        replace = cache[integer]
        cache[integer] = Tn
        print("current Tag  is replaced by Tag   "+ replace+"  "+"in the cache line   "+ str(integer))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    
    print(cache)
    
def direct_Map_write(address):
    blockOffset= B * 4
    bitsOfBlock= (int(blockOffset)-1).bit_length()
    if (CL==1):
        bitsOfLine = 1
    else:
        bitsOfLine =(int (CL)-1).bit_length()
    bitsOftag = len(address) -(bitsOfBlock+bitsOfLine)
    Tn=address[:bitsOftag]
    Ln= address[bitsOftag:(bitsOftag+bitsOfLine)]
    Bs= address[(bitsOftag+bitsOfLine):]
    tag=int(Tn, 2)
    word =int(Bs , 2)
    integer = int(Ln,2)
    if(cache[integer] == 'null'):
       
       
        print("Write miss")
        print("Address  NOT FOUND" +"  in the cache line  "+str(integer))
        cache[integer] = Tn
        print("Current Tag is replaced by an empty block in the cache line "+str(integer))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    elif(cache[integer]==Tn ):
            
        print("Write hit")
        print("Address FOUND, writing data to cache" +"  in the cache line  "+str(integer))
        print("Tag:  "+Tn+"  Block Offset:  "+Bs)
    else:
            
        print("Write miss")
        print("Address NOT FOUND" +"  in the cache line "+str(integer))
        replace = cache[integer]
        cache[integer] = Tn
        print("current Tag is replaced by Tag   "+ replace+"  "+"in the cache line   "+ str(integer))
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
        direct_Map_write(address)
        request =input("Request :")
    else:
        address=input("CPU generates address :")
        direct_Map_read(address)
        request = input("Request :")
        
       
