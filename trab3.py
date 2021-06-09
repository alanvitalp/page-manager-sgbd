pag_um = open("txt/1.txt", "r")
pag_dois = open("txt/2.txt", "r")
pag_tres = open("txt/3.txt", "r")
pag_quatro = open("txt/4.txt", "r")
pag_cinco = open("txt/5.txt", "r")
pag_seis = open("txt/6.txt", "r")
pag_sete = open("txt/7.txt", "r")
pag_oito = open("txt/8.txt", "r")
pag_nove = open("txt/9.txt", "r")
pag_dez = open("txt/10.txt", "r")
pag_onze = open("txt/11.txt", "r")
pag_doze = open("txt/12.txt", "r")
pag_treze = open("txt/13.txt", "r")
pag_catorze = open("txt/14.txt", "r")
pag_quinze = open("txt/15.txt", "r")
pag_dezesseis = open("txt/16.txt", "r")
pag_dezessete = open("txt/17.txt", "r")
pag_dezoito = open("txt/18.txt", "r")
pag_dezenove = open("txt/19.txt", "r")
pag_vinte = open("txt/20.txt", "r")

pages = [
    pag_um,
    pag_dois,
    pag_tres,
    pag_quatro,
    pag_cinco,
    pag_seis,
    pag_sete,
    pag_oito,
    pag_nove,
    pag_dez,
    pag_onze,
    pag_doze,
    pag_treze,
    pag_catorze,
    pag_quinze,
    pag_dezesseis,
    pag_dezessete,
    pag_dezoito,
    pag_dezenove,
    pag_vinte,
]


class Registro:
    def __init__(self, page_id, slot, data):
        self.page_id = page_id
        self.slot = slot
        self.data = data


class Page:
    def __init__(self, pageID, num_slots, bitmap, regs):
        self.num_slots = num_slots
        self.bitmap = bitmap
        self.regs = regs
        self.id = pageID

    def scan(self):
        empty_dir = open("txt/emptyDir.txt", "r")
        not_empty_dir = open("txt/notEmptyDir.txt", "r")

        for line in not_empty_dir:
            print("Página " + line)
            file = open(f"txt/{line.strip()}.txt", "r")
            text = file.read()
            bitmap = text[0:5]
            reader_position = 5
            slot = 1
            for bit in bitmap:
                print("Registro " + str(slot) + ":", end="")
                if (bit == "1"):
                    print(text[reader_position:(reader_position+8)])
                    reader_position = reader_position + 8
                else:
                    print("Disponível")
                slot += 1

            # text_array = text.split("\n")
            # slots = text_array[2:8]
            # print("\nPágina " + line)
            # i=1
            # for slot in slots:
            #    print("Registro " + str(i) + ":", end="")
            #    if (slot == ""):
            #        print("Disponível")
            #    else:
            #        print(slot)
            #    i+=1

    def seek(self, byte):
        empty_dir = open("txt/emptyDir.txt", "r")
        not_empty_dir = open("txt/notEmptyDir.txt", "r")

        for line in not_empty_dir:
            file = open(f"txt/{line.strip()}.txt", "r")
            text = file.read()
            bitmap = text[0:5]
            reader_position = 5
            slot = 1
            line = line.strip("\n")
            for bit in bitmap:
                if (bit == "1"):
                    if ((text[reader_position:(reader_position+8)]) == str(byte)):
                        return int(line), slot
                    reader_position = reader_position + 8
                slot += 1

    def delete(self, byte):
        not_empty_dir = open("txt/notEmptyDir.txt", "r")

        for line in not_empty_dir:
            file = open(f"txt/{line.strip()}.txt", "r+")
            text = file.read()
            bitmap = text[0:5]
            reader_position = 5
            slot = 1
            for bit in bitmap:
                if (bit == "1"):
                    if ((text[reader_position:(reader_position+8)]) == str(byte)):
                        text = text[0:reader_position] + \
                            text[reader_position+8:]
                        array_text = list(text)
                        array_text[slot-1] = "0"
                        new_text = "".join(array_text)
                        file.seek(0)
                        file.write(new_text)
                        file.truncate()
                        bitmap = new_text[0:5]
                        if (bitmap == "00000"):
                            not_empty_dir.close()
                
                            new_not_empty_file = open(
                                "txt/notEmptyDir.txt", "r")
                            empty_dir = open("txt/emptyDir.txt", "a")
                            new_lines = new_not_empty_file.readlines()
                            new_not_empty_file.close()

                            new_new_file = open(
                                "txt/notEmptyDir.txt", "w")
                            for item in new_lines:
                                if item.strip("\n") != line.strip("\n"):
                                    new_new_file.write(item)
                            empty_dir.write("\n"+line.strip("\n"))
                            empty_dir.close()
                        return 0
                    reader_position = reader_position + 8
                slot += 1
        not_empty_dir.close()

    def insert(self, byte):
        empty_dir = open("txt/emptyDir.txt", "r")
        not_empty_dir = open("txt/notEmptyDir.txt", "r")

        for line in not_empty_dir:
            file = open(f"txt/{line.strip()}.txt", "r+")
            text = file.read()
            bitmap = text[0:5]
            reader_position = 5
            slot = 1
            line = line.strip("\n")
            for bit in bitmap:
                if (bit == "0"):
                    array_text1 = list(text[0:reader_position])
                    array_text1[slot-1] = "1"
                    array_text2 = list(text[reader_position:])
                    new_text = array_text1 + list(str(byte)) + array_text2
                    aux = "".join([item for item in new_text])
                    file.seek(0)
                    file.write(aux)
                    file.truncate
                    return 0
        
        empty_dir.close()
        not_empty_dir.close()


rene = Page(0, 0, 0, 0)

rene.insert(11111111)
