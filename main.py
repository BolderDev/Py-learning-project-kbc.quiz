kbc=["who is the PM of India? : ", "Who is the President of India? : ", "who is nations bird of India? : ", "who is national animal of India? : ","In which language Microsoft OS is written? : ", "who is known as iron man of India? : ","who is known as father of India? : "]
answer=["Narendra Modi", "Dropadi Murmu", "Peacock", "Tiger","c++","Vallabh Bhai Patel","Mahatma Gandhi"]
amount=[1000,3000,5000,10000,40000,100000,320000]
winningamt=[0,0,0,10000,10000,10000,320000]

for i in range(len(kbc)):
    print("This question is for Rs.", amount[i])
    a=input(str(kbc[i]))

    if(a==answer[i]):
        print(True)

    else:
        print(False)
        print("you have won Rs.", winningamt[i])
        break
