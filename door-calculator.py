repeat = "y"
while repeat == "y":

    print()
    print()
    print("DOOR MATERIAL CALCULATOR")
    print()
    print("For 35mm thick doors, dress timber framing to around 24mm thick")
    print("For 40mm thick doors, dress timber framing to around 29mm thick")
    print()
    print()
    height = int(input("Height of Door(mm):\n"))
    door_width = int(input("Width of door(mm):\n"))
    framing_width = int(input("Width you are ripping your framing to(mm):\n"))
    framing_thickness = int(input("Thickness of framing(mm):\n"))
    sliding_door = input("Sliding door mechanism to be fitted to the bottom?(type y or n):\n")
    horiz_framing = door_width - framing_width * 2
    len_stiles = height * 2
    lock_block = int((height - 300) / 5)
    total_material =  len_stiles + horiz_framing * 6
    new_sliding_door = sliding_door.lower()
    sliding_lock_block = int((height - 320) / 5)
    repeat = ""



    if new_sliding_door == "y":
        print()
        print()
        print("You will need(mm):")
        print()
        print(f"5 lengths of framing at, {horiz_framing}mm x {framing_width}mm x {framing_thickness}mm")
        print()
        print(f"1 bottom rail to suit sliding door mechanism at, {(horiz_framing + (framing_width*2))}mm x 70mm x {framing_thickness}mm")
        print()
        print(f"2 length of framing at, {height - 65}mm x {framing_width}mm x {framing_thickness}mm")
        print()
        print(f"2 sheets of 6mm plywood at, {height + 5} x {door_width}")
        print()
        print(f"Plus, 2 lock blocks at, {sliding_lock_block}mm x 70mm x {framing_thickness}mm")
        print()
        print(f"Total material required: {round(total_material/1000,2)} metres , plus 2 lock blocks" ) 
        print()
        print("""Remember to put bottom rail through the spindle for the sliding door mechanism
        before assembly""")
        print()
        

    elif new_sliding_door == "n":


        print()
        print()
        print("You need(mm):")
        print()
        print(f"6 length of framing at, {horiz_framing}mm x {framing_width}mm x {framing_thickness}mm")
        print()
        print(f"2 length of framing at, {height + 5}mm x {framing_width}mm x {framing_thickness}mm")
        print()
        print(f"2 sheets of 6mm plywood at, {height + 5}mm x {door_width}mm")
        print()
        print(f"Plus, 2 lock blocks at, {lock_block}mm x 70mm x {framing_thickness}mm " )
        print()
        print(f"Total material required: {round(total_material/1000,2)} metres, plus 2 lock blocks" )
        print()

    repeat = input("Do you want to calculate material for another door? Type y or n\n")



