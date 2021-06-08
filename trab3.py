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

empty_dir = open("txt/emptyDir.txt", "r")
not_empty_dir = open("txt/notEmptyDir.txt", "r")

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
        for line in not_empty_dir:
            file = open(f"txt/{line.strip()}.txt", "r")
            text = file.read()
            text_array = text.split("\n")
            slots = text_array[2:-1]

            print(slots)

            # def seek(self, byte):

            # def delete(self, byte):

            # def insert(self, byte):


rene = Page(0, 0, 0, 0)

rene.scan()
