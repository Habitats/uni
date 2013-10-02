from sys import stdin, argv

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt 
        self.neste = None 

    
# Oppretter lenket liste
forste = None
siste = None

def spor(kubbe):
    # SKRIV DIN KODE HER
    max = siste.vekt;
    while(kubbe.neste != None):
        if(kubbe.vekt > max):
            max = kubbe.vekt;
        kubbe = kubbe.neste;
    return max;

listOfNum = {4, -1, 10, -10, 123}
for num in listOfNum:
    forrige_siste = siste;
    siste = Kubbe(int(num));
    if(forste == None):
        forste = siste;
    else: 
        forrige_siste.neste = siste;
        
#for linje in stdin:
#    forrige_siste = siste
#    siste = Kubbe(int(linje))
#    if forste == None:
#        forste = siste
#    else:
#        forrige_siste.neste = siste

    
# Kaller loesningsfunksjonen og skriver ut resultatet

print spor(forste)
