"""
    program: cars&bikes system
    author: Sergio Mirazo
    version: 1.0.0
    date: JAN/29/2023
    *-*-*-*-**-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*--*-*-**-*-*-*-*-*-*-*-*
    description: A simple inventory management for a cars and bikes vendor
"""
resp = True


class Vehicle:
    def __init__(self, vh_type, model, year, color, price):
        self.model = model
        self.vh_type = vh_type
        self.color = color
        self.year = year
        self.price = price

    def __str__(self): 
        return f'Vehicle type is {self.vh_type}, model {self.model}, year {self.year}, color {self.color}, price {self.price}'

    def __repr__(self):
        return f'Vehicle(\'{self.vh_type}\', \'{self.model}\', \'{self.color}\', {self.year}, {self.price})'


def entry():
    item_0 = input('Enter the type of vehicle: ')
    item_1 = input('Enter the model of vehicle: ')
    item_2 = input('Enter the color of vehicle: ')
    item_3 = input('Enter the year of vehicle: ')
    item_4 = input('Enter the price of vehicle: ')
    v1 = Vehicle(item_0, item_1, item_2, item_3, item_4)
    return v1

print('###################################################################')
print('cars & bikes management system')
print('MENU:')
print('1 - Load data from a file')
print('2 - Entry a vehicle in a existing inventory file')
print('3 - Create a storage file')
print('4 - Search a vehicle by ID from a storage file')
print('5 - Exit')
print('###################################################################')
while resp:
    response = input('Select an entry: ')
    match response:
        case '1':
            name = str(input('Enter the name of the file with extension: '))
            file = open(name, 'r')
            data = file.readlines()
            file.close()
            for j in range(0, len(data)):
                print( str(data[j]) )
                print('_______________________________________________________________________')
            print('###################################################################')
            print('done!')
        case '2':
            store = []
            name = str(input('Enter the name of the file with extension: '))
            file = open(name, 'r')
            data = file.readlines()
            if data==' ':
                n = 1
            else:
                n = len(data)
            i = n
            file.close()
            file = open(name, 'a+')
            while i!=-1:
                response = input('Do you want to enter new data?: ')
                if response.lower()=='yes' or response.lower()=='y' or response.lower()=='yeah':
                    v1 = entry()
                    store.append('ID = '+str(i)+' '+str(v1))
                    i += 1
                else:
                    i = -1
                
            for j in range(0, len(store)):
                file.write( store[j]+'\n' )          
            file.close()
        case '3':
            name = str(input('Enter the name of the file with extension: '))
            try:
                file = open(name, 'x')
                print('done!')
                file.close()
            except FileExistsError:
                print('File already exists')
                response = input('Do you want to overwrite it?: ')
                if response.lower()=='yes' or response.lower=='y' or response.lower=='yeah':
                    file = open(name, 'w+')
                    print('Done!')
                    file.close()
                else:
                    print('alright')
                    pass
        case '4':
            name = str(input('Enter the name of the file with extension: '))
            file = open(name, 'r')
            data = file.readlines()
            file.close()
            entry = str(input('Enter the ID of the vehicle: '))
            for j in range(0, len(data)):
                querry = data[j]
                txt = querry.split()
                txt = txt[2]
                if txt==entry:
                    print(querry)
                    print('done!')
                else:
                    pass
        case '5':
            resp = False
