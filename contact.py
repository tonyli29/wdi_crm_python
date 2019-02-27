# class Contact:
#
#   contacts = []
#   next_id = 1
#
#   def __init__(self, first_name, last_name, email, note):
#     """This method should initialize the contact's attributes"""
#     self.first_name = first_name
#     self.last_name = last_name
#     self.email = email
#     self.note = note
#     self.id = Contact.next_id
#     Contact.next_id += 1
#
#
#   @classmethod
#   def create(cls, first_name, last_name, email, note):
#     """This method should call the initializer,
#     store the newly created contact, and then return it
#     """
#     new_contact = Contact(first_name, last_name, email, note)
#     Contact.contacts.append(new_contact)
#     return new_contact
#
#   @classmethod
#   def all(cls):
#     """This method should return all of the existing contacts"""
#
#   @classmethod
#   def find(cls):
#     """ This method should accept an id as an argument
#     and return the contact who has that id
#     """
#
#   def update(self):
#     """ This method should allow you to specify
#     1. which of the contact's attributes you want to update
#     2. the new value for that attribute
#     and then make the appropriate change to the contact
#     """
#
#
#   @classmethod
#   def find_by(cls):
#     """This method should work similarly to the find method above
#     but it should allow you to search for a contact using attributes other than id
#     by specifying both the name of the attribute and the value
#     eg. searching for 'first_name', 'Betty' should return the first contact named Betty
#     """
#
#
#   @classmethod
#   def delete_all(cls):
#     """This method should delete all of the contacts"""
#
#
#   def full_name(self):
#     """Returns the full (first and last) name of the contact"""
#
#
#   def delete(self):
#     """This method should delete the contact
#     HINT: Check the Array class docs for built-in methods that might be useful here
#     """
#
#   # Feel free to add other methods here, if you need them.
#

# Contact.create('h', 'l', '@gm', "leettter")
#
# print(len(Contact.contacts))
# list = Contact.contacts
# print(list)
# print(list[0].first_name)

from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField()
  note = TextField()

  class Meta:
    database = db

  def full_name(self):
    return "{} {}".format(self.first_name, self.last_name)

db.connect()
db.create_tables([Contact])
contact_1 = Contact.create(first_name='Tony', last_name='Li', email='litony1999@gmail.com', note='note')
contact_2 = Contact.create(first_name='Pham', last_name='Geh', email='Pham1345@gmail.com', note='sup fam')
contact_3 = Contact.create(first_name='Bill', last_name='Lee', email='Billy1989@gmail.com',note='hello it is me')
contact_4 = Contact.create(first_name='Betty', last_name='Maker', email='bettymakes@bitmaker.co', note='this is a note')









#
