from datetime import datetime
import uuid


class Checklist:
    def __init__(self, id=str(uuid.uuid1())[0:3], title="текст", body="текст", date=str(datetime.now().strftime("%d.%m.%Y  %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(checklist):
        return checklist.id

    def get_title(checklist):
        return checklist.title

    def get_body(checklist):
        return checklist.body

    def get_date(checklist):
        return checklist.date

    def set_id(checklist):
        checklist.id = str(uuid.uuid1())[0:3]

    def set_title(checklist, title):
        checklist.title = title

    def set_body(checklist, body):
        checklist.body = body

    def set_date(checklist):
        checklist.date = str(datetime.now().strftime("%d.%m.%Y  %H:%M:%S"))

    def to_string(checklist):
        return checklist.id + '; ' + checklist.title + '; ' + checklist.body + ';  ' + checklist.date

    def map_note(checklist):
        return '\nID: ' + checklist.id + '\n' + 'Название: ' + checklist.title + '\n' + 'Описание: ' + checklist.body + '\n' + 'Дата публикации: ' + checklist.date











