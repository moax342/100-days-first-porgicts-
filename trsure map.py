

row1=['\\','\\','\\']
row2=['\\','\\','\\']
row3=['\\','\\','\\']
Tmap=[row1,row2,row3]
print("Below is the Main map")
print(f" {row1}\n,{row2}\n,{row3}")

position =input("where do you want the put the treasurer separate them by space?")
vertical_posion=int(position[0])
horizantal_position=int(position[1])-1

Tmap[vertical_posion][horizantal_position]="X"
print(f" {row1}\n,{row2}\n,{row3}")