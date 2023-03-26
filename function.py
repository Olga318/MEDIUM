import action
import Checklist
import view

number = 4


def add():
    checklist = view.create_checklist(number)
    array = action.read_file()
    for checklists in array:
        if Checklist.Checklist.get_id(checklist) == Checklist.Checklist.get_id(checklists):
            Checklist.Checklist.set_id(checklist)
    array.append(checklist)
    action.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = action.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for checklists in array:
        if text == 'all':
            logic = False
            print(Checklist.Checklist.map_note(checklists))
        if text == 'id':
            logic = False
            print('ID: ' + Checklist.Checklist.get_id(checklists))
        if text == 'date':
            logic = False
            if date in Checklist.Checklist.get_date(checklists):
                print(Checklist.Checklist.map_note(checklists))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = action.read_file()
    logic = True
    for memo in array:
        if id == Checklist.Checklist.get_id(memo):
            logic = False
            if text == 'edit':
                checklist = view.create_note(number)
                Checklist.Checklist.set_title(memo, checklist.get_title())
                Checklist.Checklist.set_body(memo, checklist.get_body())
                Checklist.Checklist.set_date(memo)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(memo)
                print('Заметка удалена...')
            if text == 'show':
                print(Checklist.Checklist.map_note(memo))
        if logic == True:
            print('Такой заметки нет, возможно, вы ввели неверный id')

    action.write_file(array, 'a')
