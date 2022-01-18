mylist= []

def saveData(value):
    if value.lower().startswith(('what', 'how', 'who', 'where')):
        message = value + '?'
    else:
        message = value + '.'
    mylist.append(message.title())

#something = ''

while True:
    something = input('Say something: ')

    if something == '\\end':
        print(' '.join(mylist))
        break
    else:
        saveData(something)

