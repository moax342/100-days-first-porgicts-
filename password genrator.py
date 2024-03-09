from random import choice,shuffle
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
         ,'p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
symbles=['!','@','#','$','%','&','*','(',')']
print("wilcome to the password genrator ")
n_letters=int(input("how many letter do you want "))
n_numbers=int(input("how many number do you want"))
n_symbles=int(input("how many symbel do you want"))

password=[]
password=[choice(letters) for l in range(n_letters)]
password += [choice(symbols) for char in range(n_numbers)]
password += [choice(numbers) for n in range(n_symbles)]    
shuffle(password)
final_password="".join(password)
print(f'your password is : {final_password}')
