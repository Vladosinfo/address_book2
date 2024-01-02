from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError


    def validate(self, phone):
        if phone.isdigit() and len(phone) == 10:
            return True
        return False


class Record():
    def __init__(self, name):
        self.name = Name(name)  # Mandatory
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def edit_phone(self, phone, phone_new):
        phone_obj = self.find_phone(phone)
        # phone_obj: Phone = self.find_phone(phone)
        if phone_obj and phone_obj.validate(phone_new):
            phone_obj.value = phone_new
        else:
            raise ValueError


    def remove_phone(self, phone_r):
        p_obj = self.find_phone(phone_r)
        if p_obj:
            self.phones.remove(p_obj)


    def find_phone(self, phone_f):
        for phone in self.phones:
            if phone.value == phone_f: return phone


    def __str__(self):
        return f"Name: {self.name.value}; phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    
    def add_record(self, value):
        # self.data[value.name.value] = value.phones
        self.data[value.name.value] = value


    def find(self, name):
        if name in self.data.keys():
            record = Record(name)
            record.phones = self.data[name]
            return self.data.get(name)

    def delete(self, name):
        if name in self.data.keys():
            self.data.pop(name)



def main():
    abook = AddressBook()
    john_record = Record("John")
    john_record.add_phone("0962455835")
    john_record.add_phone("7777777777")

    abook.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    abook.add_record(jane_record)

    for name, record in abook.data.items():
        print(f"Name: {name}, record: {record}")

    john = abook.find("John")
    john.edit_phone("0962455835", "1112223333")

    found_phone = john.find_phone("1112223333")
    found_phone = john.find_phone("0962455835")
    print(f"{john.name}: {found_phone}") 

    abook.delete("Jane")

    for name, record in abook.data.items():
        print(f"Name: {name}, record: {record}")

if __name__ == "__main__":
    main()