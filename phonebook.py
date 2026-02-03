## in this project i will be doing one phone book

contacts =[]

def register_contact():
        ##here we will take the info of the person plus the number
        
        name = input('How do you want to save the name of the contact?:\n').strip().lower()
        name = verify_name(name)
        #that was a late thought, if the name was already used, i dont want the user to have to change, instead i will auto add the 2 in front of the name
        while True:
            try:
                number = int(input('Insert the number of the phone\n'))
                break
            except ValueError:
                print('Just numbers please!')
        contacts.append({'name': name, 'number':number})
        print('Contact saved')
        
def edit_contact():
        #here you can change the name of the contact
        name = input('Type the name of the contact that you want to change\n').strip().lower()
       
        for i,contact in enumerate(contacts):
           
            if contact['name'] == name:
                new_name = input('Type the new name\n').strip().lower()
                new_name = verify_name(new_name)
                contact['name'] = new_name
                print ('Name successfully updated!')
                return
            
        print ('Contact not found')

def remove_contact():
        ##here you can remove the contact of the phone list
        name = input('Type the name of the contact that you want to remove\n').lower().strip()
        for i, contact in enumerate(contacts):
            if contact['name'] == name:
                contacts.pop(i)
                print('Successfully removed.')
                return
        print('Name not found.')

def all_contacts():
    #it shows it all
    for i in range(len(contacts)):
        print(f"Name: {contacts[i]['name']}, Number: {contacts[i]['number']}\n")

def show_number():
    #this one show all the numbers and names just by typing some letters,for exemple if you type 'sus', it will show you all Susans an Susies!
    name = input('Type the name of the contact that you want to see\n').lower()
    see = False

    for i in contacts:
        if name in i['name'].lower():
            print(f"{i['name']} --> {i['number']}")
            see = True
    if not see:
         print('No contacts found')

def verify_name(name):
    ##i think this one is my best work yet, so clean
    #use this to verify if the name is already being using on the list that you want
    #be sure that the () info is the name that you used for the input
    if not any(i['name'] == name for i in contacts):
        return name
    counter = 2
    while any(i['name'] == f"{name} {counter}" for i in contacts):
        counter += 1
    return f"{name} {counter}"

def base_screen():
    select_option = int(input('Select your option:\n' \
            '1.Add one contact\n' \
            '2.Show all contacts\n' \
            '3.Edit one contact\n'
            '4.Browse one phone number\n' \
            '5.Remove old numbers\n'
            '6.Exit\n'))
    return select_option
    
def main():
    while True:
        try:
            select_option = base_screen()
            if select_option == 1:
                register_contact()

            elif select_option == 2:
                all_contacts()
            elif select_option == 3:
                edit_contact()
            elif select_option == 4:
                show_number()
            elif select_option == 5:
                remove_contact()
            elif select_option == 6:
                break
            if select_option not in range(1,6):
                print('Select one valid option')

        except ValueError:
            print('Select just numbers')    
if __name__ == '__main__':
    main()