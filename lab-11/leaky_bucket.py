import time
import random


def bktInput(a, b, bucket_size = 512):
    if(a > bucket_size):
        print("Bucket overflow")
    else:
        time.sleep(2)
        while(a > b):
            print(f'{b} Bytes outputed ')
            a -= b
            time.sleep(2)
        if(a > 0):
            print(f'Last {a} byte sent')
        print('Bucket output success')
    
output_rate = int(input('Enter output rate : '))
for i in range(5):
    time.sleep(2)
    pktsize = random.randint(1,1000)
    print(f'Packet no : {i} packet size : {pktsize}')
    bktInput(pktsize,output_rate)