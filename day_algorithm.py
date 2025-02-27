import datetime

class InvalidDateException(Exception):
    def __init__(self, niz):
        super().__init__("'" + niz + "' ni veljaven datum")
    
class InvalidEMSOException(Exception):
    def __init__(self, niz):
        super().__init__("'" + niz + "' ni veljavna EMŠO številka")

def prestopno(leto):
    '''preveri, ali je dano leto prestopno'''
    if leto%4 == 0:
        if leto%400 == 0:
            return True
        elif leto%100 == 0:
            return False
        else:
            return True
    else:
        return False

mes = [1, 3, 5, 7, 8, 10 ,12]

def izracunaj_stevilo_dni(mesec, leto):
    if mesec == 2:
        if prestopno(leto):
            return 29
        else:
            return 28
    elif mesec in mes:
        return 31
    else:
        return 30

class Datum:

    def __init__(self, dan=None, mesec=None, leto=None):
        
        cas = datetime.datetime.now()
        self.dan = cas.day if dan is None else dan
        self.mesec = cas.month if mesec is None else mesec
        self.leto = cas.year if leto is None else leto
        if not self.veljaven():
            datum = '{}.{}.{}'.format(self.dan, self.mesec, self.leto)
            raise InvalidDateException(datum)

    def veljaven(self):
        
        dan, mesec, leto = self.dan, self.mesec, self.leto
        return (isinstance(leto, int) and leto >= 1900 and
            isinstance(mesec, int) and 1 <= mesec <= 12 and
            isinstance(dan, int) and 1 <= dan <= izracunaj_stevilo_dni(mesec, leto))


    def __str__(self):
        return '{}.{}.{}'.format(self.dan, self.mesec, self.leto)

    def __repr__(self):
        return 'Datum({}, {}, {})'.format(self.dan, self.mesec, self.leto)


    def __lt__(self, d):
      return (self.leto, self.mesec, self.dan) < (d.leto, d.mesec, d.dan)

    def __eq__(self, d):
      return (self.leto, self.mesec, self.dan) == (d.leto, d.mesec, d.dan)

    def dan_v_letu(self):
        st = 0
        for mesec in range(1, self.mesec):
            st += izracunaj_stevilo_dni(mesec, self.leto)
        return st + self.dan
                    
            
    def dan_v_dobi(datum):
        st = Datum.dan_v_letu(datum)
        for x in range(1900, datum.leto):
            if prestopno(x):
                st += 366
            else:
                st += 365
        return st
    
    def stevilo_dni(self, datum):
        if datum is None:
            datum = Datum()
        return datum.dan_v_dobi() - self.dan_v_dobi()
    
    def izracunaj_koncni_datum(self, st_dni):
        dan_v_dobi = self.dan_v_dobi() + st_dni
        leto = 1900
        while True:
            dni_v_letu = 366 if prestopno(leto) else 365
            if dan_v_dobi <= dni_v_letu:
                break
            dan_v_dobi -= dni_v_letu
            leto += 1

        mesec = 1
        while True:
            dni_v_mesecu = izracunaj_stevilo_dni(mesec, leto)
            if dan_v_dobi <= dni_v_mesecu:
                break
            dan_v_dobi -= dni_v_mesecu
            mesec += 1

        return Datum(dan_v_dobi, mesec, leto)


    @staticmethod
    def parse(niz):
        razrez = niz.split('.')
        if len(razrez) == 3:
            return Datum(int(razrez[0]), int(razrez[1]), int(razrez[2]))
        else:
            raise InvalidDateException(niz)
        
    @staticmethod
    def emso(niz):
        try:
            leto = (1000 if niz[4] == '9' else 2000) + int(niz[4:7])
            return Datum(int(niz[:2]), int(niz[2:4]), leto)
        except:
            raise InvalidEMSOException(niz)

    @staticmethod
    def datumi(mesec, leto):
        for d in range(izracunaj_stevilo_dni(mesec, leto)):
            yield Datum(d+1, mesec, leto)

def najmanjsi(vhod):
    x = None
    with open(vhod, 'r') as file:
        for line in file:
            d = Datum.parse(line)
            if x is None or d < x:
                x = d
    return x

def uredi(vhod, izhod):
    d = []
    with open(vhod, 'r') as file:
        for line in file:
            d.append(Datum.parse(line))
    with open(izhod, 'w') as f:
        for date in sorted(d):
            print(date, file = f)

#stevilo dni med dan in datum
dan = Datum(3, 3, 2022)
datum = Datum(13, 10, 2024)
print(dan.stevilo_dni(datum))

#konci datum po danem stevilu dneh
zac_dat = Datum(9, 12, 2023)
st_dni = 1863
#print(zac_dat.izracunaj_koncni_datum(st_dni)) 