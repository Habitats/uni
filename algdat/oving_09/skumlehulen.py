from sys import stdin, stderr

# kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
# startrom er en liste med indeksene til nodene som tilsvarer startrommene.
# utganger er en liste med indeksene til nodene som tilsvarer utgangene.

def antallIsolerteStier(kapasiteter, startrom, utganger):
    # Du kan bruke metoden finnFlytsti for aa forenkle oppgaven.
    # SKRIV DIN KODE HER


# Finner en sti fra noden med indeks 'kilde' til noden med indeks 'sluk'
# med ledig kapasitet i et flytnettverk med flyt F og kapasitet C.
# Returnerer en liste hvor foerste element er indeksen til en av startnodene, 
# siste element er indeksen til en av utgangene, og elementene imellom er 
# indeksene til de andre nodene paa veien som ble funnet, i riktig rekkefoelge.
# Eksempel: en sti fra startnoden 4 til node 3, node 9, node 7 og til slutt til 
# utgangen 12 vil representeres som [4, 3, 9, 7, 12].

def finnFlytsti(kilde, sluk, F, C):
    n = len(F)
    oppdaget = [False] * n
    forelder = [None] * len(F)
    koe = [kilde]
    while koe:
        node = koe.pop(0)
        if node == sluk:
            # Har funnet sluken, lager en array med passerte noder
            sti = []
            i = node
            while True:
                sti.append(i)
                if i == kilde:
                    break
                i = forelder[i]
            sti.reverse()
            return sti;
        for nabo in range(n):
            if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                koe.append(nabo);
                oppdaget[nabo] = True;
                forelder[nabo] = node;
    return None

noder, _, _ = [int(x) for x in stdin.readline().split()]
startrom = [int(x) for x in stdin.readline().split()]
utganger = [int(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [int(nabo) for nabo in linje.split()]
    nabomatrise.append(naborad)
print antallIsolerteStier(nabomatrise, startrom, utganger)
