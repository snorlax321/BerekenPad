import random

def calculate_path(invoer):
    invoer = invoer.lower()
    count = 0
    for x in invoer:
        count += 1
    if count < 8:
        print("input more directions so that it is plauseable")
        return
    pos = 1.1
    path = []  # keeps track of previous coords
    directions = []  # stores the directions for later print
    original_path = []  # stores the og path for comparison
    loop1 = True

    while loop1:
        # resets all variables for a new attempt
        path.clear()  
        directions.clear()
        original_path.clear()
        pos = 1.1  
        path.append(pos)

        loop2 = True
        while loop2:
            for x in invoer:
                original_path.append(x)  # Store the original path

                if x == 'l':
                    new_pos = pos - 0.1
                    directions.append('l')
                elif x == 'r':
                    new_pos = pos + 0.1
                    directions.append('r')
                elif x == 'o':
                    new_pos = pos - 1
                    directions.append('o')
                elif x == 'n':
                    new_pos = pos + 1
                    directions.append('n')
                elif x == '?':
                    rand_choice = random.randint(0, 3)
                    if rand_choice == 0:
                        new_pos = pos - 0.1  # 'l'
                        directions.append('l')
                    elif rand_choice == 1:
                        new_pos = pos + 0.1  # 'r'
                        directions.append('r')
                    elif rand_choice == 2:
                        new_pos = pos - 1    # 'o'
                        directions.append('o')
                    elif rand_choice == 3:
                        new_pos = pos + 1    # 'n'
                        directions.append('n')
                print(pos, x)

                # Check if coord has already been crossed
                if new_pos in path:
                    print("Crossed a previous coordinate, restarting...")
                    
                    break
                else:
                    path.append(new_pos)
                    pos = new_pos

                # Check if position is 5.5
                if pos == 5.5:
                    
                    print("Success! Path:", path)
                    print("Directions taken:", ''.join(directions))
                    print("Original path:", ''.join(original_path))
                    return  # Exit the function on success
                
                

            else:
                # if it didn't break from the loop, continue
                continue
            # If it broke from the loop, restart
            break

        # After processing the entire path, check conditions
        if '?' not in invoer and pos != 5.5:
            print("The path does not contain '?', and it does not reach 5.5.")
            return

# runs function usage
invoer = input("Geef het pad: ")
calculate_path(invoer)
