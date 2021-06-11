def isByte(byte):
    if (len(str(byte)) != 8):
        return False
    for i in str(byte):
        if i not in ("0","1"):
            return False
    return True


def scan():
    not_empty_first = open("txt/notEmptyFirst.txt", "r")
    pointer = not_empty_first.read()
    while (pointer != "00"):
        print("Página " + pointer)
        file = open(f"txt/{pointer}.txt", "r")
        text = file.read()
        bitmap = text[2:7]
        reader_position = 7
        slot = 1
        for bit in bitmap:
            print("Registro " + str(slot) + ":", end="")
            if (bit == "1"):
                print(text[reader_position:(reader_position+8)])
                reader_position = reader_position + 8
            else:
                print("Disponível")
            slot += 1
        pointer = text[0:2]
        file.close()
        print("")
    not_empty_first.close()


def seek(byte):
    if not isByte(byte):
        print("Valor não é um byte!")
        return 0
    not_empty_first = open("txt/notEmptyFirst.txt", "r")
    pointer = not_empty_first.read()
    while (pointer != "00"):
        file = open(f"txt/{pointer}.txt", "r")
        text = file.read()
        bitmap = text[2:7]
        reader_position = 7
        slot = 1
        for bit in bitmap:
            if (bit == "1"):
                if ((text[reader_position:(reader_position+8)]) == str(byte)):
                    file.close()
                    return int(pointer), slot
                reader_position = reader_position + 8
            slot += 1
        pointer = text[0:2]
        file.close()
    not_empty_first.close()
    print("Registro não encontrado!")


def delete(byte):
    if not isByte(byte):
        print("Valor não é um byte!")
        return 0
    not_empty_first = open("txt/notEmptyFirst.txt", "r")
    pointer = not_empty_first.read()
    last_pointer = "notEmptyFirst"
    while (pointer != "00"):
        file = open(f"txt/{pointer}.txt", "r+")
        text = file.read()
        bitmap = text[2:7]
        reader_position = 7
        slot = 1
        for bit in bitmap:
            if (bit == "1"):
                if ((text[reader_position:(reader_position+8)]) == str(byte)):
                    text = text[0:reader_position] + \
                        text[reader_position+8:]
                    array_text = list(text)
                    array_text[slot+1] = "0"
                    new_text = "".join(array_text)
                    file.seek(0)
                    file.write(new_text)
                    file.truncate()
                    file.close()
                    bitmap = new_text[2:7]
                    if (bitmap == "00000"):
                        empty_dir = open("txt/emptyDir.txt", "a")
                        empty_dir.write(pointer)
                        empty_dir.close()
                        pointer = text[0:2]
                        file = open(f"txt/{last_pointer}.txt", "r+")
                        text = file.read()
                        text = pointer + text[2:]
                        file.seek(0)
                        file.write(text)
                        file.truncate()
                        file.close()
                        
                    return 0
                reader_position = reader_position + 8
            slot += 1
        last_pointer = pointer
        pointer = text[0:2]
        file.close()
    not_empty_first.close()
    print("Valor não encontrado!")


def insert(byte):
    if not isByte(byte):
        print("Valor não é um byte!")
        return 0
    not_empty_first = open("txt/notEmptyFirst.txt", "r")
    pointer = not_empty_first.read()
    last_pointer = "notEmptyFirst"
    while (pointer != "00"):
        file = open(f"txt/{pointer}.txt", "r+")
        text = file.read()
        bitmap = text[2:7]
        reader_position = 7
        slot = 1
        for bit in bitmap:
            if (bit == "0"):
                array_text1 = list(text[0:reader_position])
                array_text1[slot+1] = "1"
                array_text2 = list(text[reader_position:])
                new_text = array_text1 + list(str(byte)) + array_text2
                aux = "".join([item for item in new_text])
                file.seek(0)
                file.write(aux)
                file.truncate
                file.close()
                return 0
            slot = slot + 1
        last_pointer = pointer
        pointer = text[0:2]
        file.close()
    empty_dir = open("txt/emptyDir.txt", "r+")
    empty_dir_text = empty_dir.read()
    pointer = empty_dir_text[-2:]
    empty_dir_text = empty_dir_text[0:-2]
    empty_dir.seek(0)
    empty_dir.write(empty_dir_text)
    empty_dir.truncate()
    empty_dir.close()
    file = open(f"txt/{last_pointer}.txt", "r+")
    text = file.read()
    text = pointer + text[2:]
    file.seek(0)
    file.write(text)
    file.truncate()
    file.close
    file = open(f"txt/{pointer}.txt", "r+")
    text = "0010000" + str(byte)
    file.seek(0)
    file.write(text)
    file.truncate()
    file.close()

#Execução das funções
#scan()
#seek("byte")
#delete("byte")
#insert("byte")