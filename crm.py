from contact import Contact


class CRM:
  def main_menu(self):
      while True:
          self.print_main_menu()
          user_selected = int(input())
          if user_selected > 6:
              print('Number is out of range')
          self.call_option(user_selected)


  def print_main_menu(self):
      print('[1] Add a new contact')
      print('[2] Modify an existing contact')
      print('[3] Delete a contact')
      print('[4] Display all the contacts')
      print('[5] Search by attribute')
      print('[6] Exit')
      print('Enter a number: ')

  def call_option(self, user_selected):
      if user_selected == 1:
          self.add_new_contact()
      elif user_selected == 2:
          self.modify_existing_contact()
      elif user_selected == 3:
          self.delete_contact()
      elif user_selected == 4:
          self.display_all_contacts()
      elif user_selected == 5:
          self.search_by_attribute()
      elif user_selected == 6:
          exit()
  def add_new_contact(self):
      print('Enter First Name')
      first_name = input()
      print('Enter Last Name')
      last_name = input()
      print('Enter Email')
      email = input()
      print('Enter note')
      note = input()

      Contact.create(first_name, last_name, email, note)

  def modify_existing_contact(self):
      print('Who would you like to edit?')
      contact_list = Contact.contacts
      for idx, contact in enumerate(contact_list):
          print(f"[{idx}] {contact.first_name}")
          # need to add a way to keep repeating this so we dont have to go back to main menu everytime
          # if i > len(contact_list):
          #     i = 0
      request = int(input())
      print('You have selected user ' + contact_list[request].first_name + ' ' + contact_list[request].last_name)
      print('What would you like to change?')
      print('[0] First Name')
      print('[1] Last Name')
      print('[2] Email')
      print('[3] note')
      request_change = int(input())
      if request_change == 0:
          print("What would you like to change {} {}'s name to?'".format(contact_list[request].first_name, contact_list[request].last_name))
          changed = input()
          contact_list[request].first_name = changed
      elif request_change == 1:
          print("What would you like to change {} {}'s last name to?'".format(contact_list[request].first_name, contact_list[request].last_name))
          changed = input()
          contact_list[request].last_name = changed
      elif request_change == 2:
          print("What would you like to change {} {}'s email to?'".format(contact_list[request].first_name, contact_list[request].last_name))
          changed = input()
          contact_list[request].email = changed
      elif request_change == 3:
          print("What would you like to change {} {}'s note to?'".format(contact_list[request].first_name, contact_list[request].last_name))
          changed = input()
          contact_list[request].note = changed
      else:
          print("Please enter a valid number")

  def delete_contact(self):
      contact_list = Contact.contacts
      print('Who would you like to remove?')
      for idx, contact in enumerate(contact_list):
          print(f"[{idx}] {contact.first_name}")
      choice = int(input())
      print('{} has been removed'.format(contact_list[choice].first_name))
      del contact_list[choice]


  def display_all_contacts(self):
      contact_list = Contact.contacts
      for people in contact_list:
          print(people.first_name + ' ' + people.last_name + '    ' + people.email + '    ' + people.note)

  def search_by_attribute(self):
      pass

a_crm_app = CRM()
a_crm_app.main_menu()
