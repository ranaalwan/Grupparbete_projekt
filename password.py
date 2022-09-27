
tries=4
mainPassword="Rana@123"
inputPassword =input("Write your Password:")
while inputPassword != mainPassword: #true
    tries -=1
    print(f"Wrong Password , {'last' if tries==0 else tries } chance Left")
    inputPassword=input("Write your Password:")
    if tries == 0:
        print("All Tries is Finished.")
        break
       # print("will not print")

else:
    print("correct Password")