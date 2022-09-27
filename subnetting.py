def FLSM(ip_num,defaultsubnet,subnet):
    k=1
    while True:
            c=2**k
            if c>=ip_num:
                break
            else:
                k+=1
    if c<255:
            l=defaultsubnet[2]
            print("The Default Subnet Mask of Class C:",defaultsubnet[2])
    elif c<65025:
            l=defaultsubnet[1]
            print("The Default Subnet Mask of Class B:",defaultsubnet[1])
    elif c<16581375:
            l=defaultsubnet[0]
            print("The Default Subnet Mask of Class A:",defaultsubnet[0])
    e=(32-k)*"1"
    f=k*'0'
    g=e+f
    i=str(g[0:8])+str(g[8:16])+str(g[16:24])+str(g[24::])
    j=subnet[l]
    print("The Binary Representation Of New Subnet Mask is:",g[0:8]+"."+str(g[8:16])+"."+str(g[16:24])+"."+str(g[24::]))
    h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
    print("The New Subnet Mask Value is",'.'.join(h))
    print("The Prefix Length of New SubnetMask is:",i.count('1'))
    z=i.count('1')-j.count('1')
    print("No of Networks :",int(2**(z)))
    print("No of Hosts :",c)
def VLSM(ip_num,defaultsubnet,subnet):#Variable Length Subnet Mask
      for i in range(len(ip_num)):
        k=1
        print("The Details of",ip_num[i],"Hosts are:")
        a=0
        a=int(ip_num[i])
        while True:
            c=2**k
            if c>=a:
                break
            else:
                k+=1
        if c<255:
            l=defaultsubnet[2]
            print("The Default Subnet Mask of Class C:",defaultsubnet[2])
        elif c<65025:
            l=defaultsubnet[1]
            print("The Default Subnet Mask of Class B:",defaultsubnet[1])
        elif c<16581375:
            l=defaultsubnet[0]
            print("The Default Subnet Mask of Class A:",defaultsubnet[0])
        e=(32-k)*"1"
        f=k*'0'
        g=e+f
        i=str(g[0:8])+str(g[8:16])+str(g[16:24])+str(g[24::])
        j=subnet[l]
        print("The Binary Representation Of New Subnet Mask is:",g[0:8]+"."+str(g[8:16])+"."+str(g[16:24])+"."+str(g[24::]))
        h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
        print("The New Subnet Mask Value is",'.'.join(h))
        print("The Prefix Length of New SubnetMask is:",i.count('1'))
        z=i.count('1')-j.count('1')
        print("No of Networks :",int(2**(z)))
        print("No of Hosts :",c)
        print("\n")
#Main Program
print("Subnetting calculator")
print("This Subnetting Calculator calculates Subnetting Using VLSM ,FLSM or by giving Manual_IP Address Methods")
print("------------------------------------------------------------------------------------------------")
print("This will Show the No of Available Hosts,Networks including their ranges,usable IP'S, Netword ID'S and Broadcast Address")
print("------------------------------------------------------------------------------------------------")
print("Which type of subnetting method do you want to choose either FLSM or VLSM or Manual_ip ?")
method=input()
defaultsubnet=['255.0.0.0','255.255.0.0','255.255.255.0','255.255.255.255']
subnet={'255.0.0.0':'11111111.0.0.0','255.255.0.0':'11111111.11111111.0.0','255.255.255.0':'11111111.11111111.11111111.0','255.255.255.255':'11111111.11111111.11111111.1111111'}
if method=='FLSM'or method=="Flsm" or method=="flsm":
    print("How many IP's you required ?")
    ip_num=int(input())
    FLSM(ip_num,defaultsubnet,subnet)
elif method=='VLSM' or method=="Vlsm" or method=="vlsm":
    print("Enter the Number Of Hosts You need ..?")
    print("Enter the Hosts Value in Descending Order..!")
    ip_num=list(map(int,input().split()))
    VLSM(ip_num,defaultsubnet,subnet)
elif method=='Manual_IP' or method=='MANUAL_IP' or method=='manual_ip' or method=='Manual_ip'or method=='Manual_ip':
    print("Enter Your IP Address including its Prefix Value Eg:192.168.50.160/27")
    ip=input()
    l=ip.split('/')
    ip_address=l[0].split('.')
    if len(l)==2 and len(ip_address)==4:
        pre_len=int(l[1])
        hh=ip_address
        ls=[]
        if pre_len<=32:
            print("Do you want to choose Host range(YES or NO)..?")
            choice=input()
            if choice=='YES'or choice=='yes' or choice=='Yes':
                print("How Many Hosts You Require...?")
                host_range=int(input())
            else:
                host_range=0
    
            k=1
            ww=1
            while True:
                ss=2**ww
                if ss>host_range:
                    break
                ww+=1    
            
            while True:
                c=2**k
                if c>=int(l[1]):
                    break
                k+=1
            e=(32-k)*"1"
            f=k*'0'
            g=e+f
            h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24:32],2)))]
            print("The New Subnet Mask Value is",'.'.join(h))
            for v in range(len(ip_address)):
                z=int(ip_address[v])
                ls.append(z)
            #print(ls)    
            m=[]
            main=[]
            if int(ip_address[0])>=0 and int(ip_address[0])<=127:
                p=8
                #print("class A")
                nb=pre_len-p
                hb=32-pre_len
                new_nb=int(hb-ww)
            elif int(ip_address[0])>=128 and int(ip_address[0])<=191:
                p=16
                #print("class B")
                nb=pre_len-p
                hb=32-pre_len
                new_nb=int(hb-ww)
            elif int(ip_address[0])>=192 and int(ip_address[0])<=223:
                p=24
                #print("class")
                nb=pre_len-p
                hb=32-pre_len
                new_nb=hb-ww
            if choice=='YES'or choice=='Yes'  or choice=='yes':
                print("No.of Networks :",int(2**new_nb))
                print("No.of Hosts it supports :",(2**ww)-2)
                e=((32-k)+new_nb)*"1"
                f=ww*'0'
                g=e+f
                h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24:32],2)))]
                print("The New Subnet Mask Value is",'.'.join(h))
                for j in range(1,int(2**new_nb)+1):
                    for g in range((host_range+3)):
                        m.append('.'.join(hh))
                        ls[-1]=ls[-1]+1
                        hh[-1]=str(ls[-1])
                        if ls[-1]==256:
                            ls[-2]=ls[-2]+1
                            hh[-2]=str(ls[-2])
                            ls[-1]=0
                            hh[-1]=str(ls[-1])
                        if ls[-2]==256:
                            ls[-3]=ls[-3]+1
                            hh[-3]=str(ls[-3])
                            ls[-2]=0
                            hh[-2]=str(ls[-2])
                        if ls[-3]==256:
                            ls[0]=ls[0]+1
                            hh[0]=str(ls[0])
                            ls[-3]=0
                            hh[-3]=str(ls[-3])
                    print("Network :",j)        
                    print("Network ID :",m[0])
                    print("Broadcast ID :",m[-1])
                    print("Usable IP'S range:",m[1],"-",m[-2])
                    main.append(m)
                    m=[]
                    print("\n")
            elif choice=="NO" or choice=="No" or choice=="no":
                print("No.of Networks :",int(2**nb))
                print("No.of Host :",(2**hb)-2)
                i=0
                hh[-1]=str(i)
                for j in range(1,int(2**nb)+1):
                    for g in range(2**hb):
                        m.append('.'.join(hh))
                        i+=1
                        hh[-1]=str(i)
                        if i==256:
                            ls[-2]=ls[-2]+1
                            hh[-2]=str(ls[-2])
                            i=0
                            hh[-1]=str(i)
                        if ls[-2]==256:
                            ls[-3]=ls[-3]+1
                            hh[-3]=str(ls[-3])
                            ls[-2]=0
                            hh[-2]=str(ls[-2])
                        if ls[-3]==256:
                            ls[0]=ls[0]+1
                            hh[0]=str(ls[0])
                            ls[-3]=0
                            hh[-3]=str(ls[-3])
                    print("Network :",j)        
                    print("Network ID :",m[0])
                    print("Broadcast ID :",m[-1])
                    print("Usable IP'S range:",m[1],"-",m[-2])
                    main.append(m)
                    m=[]
                    print("\n")
        else:
            print("You Entered the Network Bits Beyond the IPV4 range i.e >32,Please Check it Once")
               
    else:
        print("You have not Entered the Correct IP Address,Please check once")

else:
    print("Goodbye....!You Have Entered Wrong Input")