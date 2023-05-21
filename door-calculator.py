print()
print()
print("DOOR MATERIAL CALCULATOR")
print()
print("For 35mm thick doors, dress timber framing to 25mm thick")
print("For 40mm thick doors, dress timber framing to 30mm thick")
print("All framing should be ripped to 50mm wide")
print()
print()
height = int(input("Height of Door(mm): "))
door_width = int(input("width of door(mm): "))
horiz_framing = door_width - 100 
len_stiles = height * 2
lock_block = int((height - 300) / 5)
total_material =  len_stiles + horiz_framing * 6

print()
print()
print("You need(mm):")
print()
print(f"6 length of framing at, {horiz_framing} x 50 x thickness(25/30)")
print()
print(f"2 length of framing at, {height + 5} x 50 x thickness(25/30)")
print()
print(f"2 sheets of 6mm plywood at, {height + 5} x {door_width}")
print()
print(f"Plus, 2 lock blocks at, {lock_block} x 70 x thickness(25/30) " )
print()
print("Total material required(mm): " + str(total_material) )




