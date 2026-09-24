gender=input("What is your gender : ")
with open("data.txt","a") as file :
    file.write(f"\nGender : {gender}")
file.close()
with open("data.txt","r") as file:
    data=file.read()
    print(data)
file.close()