import Checklist


def write_file(array, mode):
    file = open("memo.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("memo.csv", mode=mode, encoding='utf-8')
    for memo in array:
        file.write(Checklist.Checklist.to_string(memo))
        file.write('\n')
    file.close


def read_file():
    try:
        array = []
        file = open("memo.csv", "r", encoding='utf-8')
        memo = file.read().strip().split("\n")
        for n in memo:
            split_n = n.split(';')
            memo = Checklist.Checklist(
                id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
            array.append(memo)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array
