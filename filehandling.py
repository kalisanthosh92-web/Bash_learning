import os,sys

def note_checker(fname):
    if os.path.isfile(fname): 
        print(f'{fname} exists.')
        global file_note
        file_note = open(fname, 'r') 
        notes = file_note.read().splitlines()
        file_note.close()
        return True
    else:
        print(fname+' does not exist')
        sys.exit()
        return False






def all_notes():
    file_note = open(fname, 'r') 

    notes = file_note.read().splitlines()
    len_of_notes = len(notes)
    if len_of_notes > 0:
        for i in range(len_of_notes):
            print(f'\t{i+1}. {notes[i]}')
            print()
    
    else:
        print('There are no notes yet.')
    file_note.close()


fname = input('Enter filename: ')
note_checker(fname)


print(f'{' Note Taking App ':=^50}')

list_process = [
    ["1","Create new notes"],
    ["2","Update notes"],
    ["3","Delete notes"],
    ["4", "view notes"],
    ["5","Quit"],
]



file_note = open(fname, 'r') 
notes = file_note.read().splitlines()
file_note.close()


while note_checker :
    print()
    for i in range(len(list_process)):
        
        print(f'{i+1}. {list_process[i][1]}')
    print()  
    
    
    choice = input("Enter number action: ")
    if choice.lstrip('-').isdigit():
        choice = int(choice)

        if choice in range(1, 5):
            print('\n', "choice: ", list_process[choice - 1][1])
            
        else:
            print("choice: Quit")

    
    if choice == 1:
        new_header = input("Enter your note's title.").title()
        new_notes = input("Enter your notes: ").capitalize()
        notes.append(f'{new_header} - {new_notes}')
        file_note = open(fname, 'a')
        file_note.write(f'{notes[-1]}\n')
        file_note.flush()
        file_note.close()


    elif choice ==2:
        all_notes()
        
        while True:
            selected_note = input("Select notes number: ")
            if selected_note.lstrip('-').isdigit():
                selected_note = int(selected_note)
                if selected_note <= len(notes):
                    print('what do you want to update:')
                    print('1. To update the title.')
                    print('2. To update the note.')
                    print('3. To quit.')
                    selected_notes = notes[selected_note-1].split(' - ')
                    while True:
                        update_choice = input('Enter your choice[1-3]:')
                        if update_choice.lstrip('-').isdigit():
                            update_choice = int(update_choice)
                            
                            if update_choice == 1:
                                update_notes = input("Enter update notes title: ").capitalize()
                                selected_notes[0] = update_notes
                                notes[selected_note-1] = ' - '.join(selected_notes)
                                file_note = open(fname, 'w+')
                                file_note.write('\n'.join(notes))
                                file_note.flush()
                                file_note.close() 
                                print('Successfully updated.')
                            elif update_choice ==2:
                                update_notes = input("Enter update notes: ")
                                selected_notes[1] = update_notes
                                notes[selected_note-1] = ' - '.join(selected_notes)
                                file_note = open(fname, 'w+')
                                file_note.write('\n'.join(notes))
                                file_note.flush()
                                file_note.close()
                                print('Successfully updated.')
                            elif update_choice == 3:
                                print('quiting update.')
                            else:
                                print("Invalid choice.")
                                print('quiting update.')
                            break
                           
                        else:
                            print('Invalid update choice. Enter a number')
                    break       
                else:
                    print('Note selected is not present. Try again')
            else:
                print('Invalid input. Try again')
            


    elif choice == 3:
        all_notes()
        while True:
            user_input = input("Select notes number: ")
            if user_input.lstrip('-').isdigit():
                selected_note = int(user_input)
                if selected_note <= len(notes):
                    del notes[selected_note-1]
                    file_note = open(fname, 'w') 
                    file_note.write('\n'.join(notes))
                    file_note.flush()   
                    file_note.close()
                    print('Note deleted successfully.')
                    print('Successfully deleted.')
                    break
                else:
                    print('Note selected is not present.' )
                    print('enter valid number')
                
            else:
                print("Invalid input. Please enter a number.")

        
    elif choice == 4:
        all_notes()
        print()

    elif choice == 5:
        print("Quitting the app.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


