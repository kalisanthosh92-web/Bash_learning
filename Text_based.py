print(f'{' Note Taking App ':=^50}\n')

list_process = [
    ["1","Create new notes"],
    ["2","Update notes"],
    ["3","Delete notes"],
    ["4", "view notes"],
    ["5","Quit"],
]

notes = []
def all_notes():
    len_of_notes = len(notes)
    if len_of_notes > 0:
        for i in range(len_of_notes):
            print(f'\t{i+1}. {notes[i][0]} - {notes[i][1]}')
            print()
    else:
        print('There are no notes yet.')
 
while True :
      
    for i in range(len(list_process)):
        print(f'{i+1}. {list_process[i][1]}')
    print()      


    choose = int(input("Enter number action: "))
    if choose in range(1,5):
        print(f"choice: ", list_process[choose-1][1])
        print()
    else:
        print("choice: Quit")


    if choose == 1:
        new_header = input("Enter your note's Title: ").title()
        new_notes = input("Enter your notes: ").capitalize()
        notes.append([new_header, new_notes])
        print(f"\n{"-" * 70}")
    elif choose == 2:
        all_notes()
        selected_note = int(input("Select notes number: "))
        if selected_note <= len(notes):
            print('what do you want to update:')
            print('1. To update the title.')
            print('2. To update the note.')
            print('3. To quit.')
            update_choice = int(input('Enter your choice[1-3]:'))
            if update_choice == 1:
                update_notes = input("Enter update notes title: ")
                notes[selected_note-1][0] = update_notes
            elif update_choice ==2:
                update_notes = input("Enter update notes title: ")
                notes[selected_note-1][1] = update_notes
            else:
                continue
        else:
            print('Note selected is not present.')
        print(f"\n{"-" * 70}")
    elif choose == 3:
        all_notes()
        print()
        delete_notes = int(input("Select note number to remove: "))
        if delete_notes <= len(notes):
            del notes[delete_notes-1]
            print('Note Successfully deleted.')
            print("Successfully updated. ")
        else :
            print('No note exists with that index,Please choose proper.')
        print(f"\n{"-" * 70}")
        continue
    elif choose == 4:
        all_notes()
        print(f"\n{"-" * 70}")
    else:
        print('exiting The app.')
        print("All notes Saved!")
        break

   
