import nltk
from nltk import CFG

grammar = CFG.fromstring("""
    S -> SN VS SN | SN VS
    SN -> SN Conj SNP | SNP
    SNP -> N SNP_A
    SNP_A -> SNP | Empty
    N -> NP | NF
    NP -> RP TP
    NF -> RF TF
    RP -> 'kitap' | 'kapı' | 'çocuk' | 'araba' | 'kadın'
    RF -> 'ev' | 'kedi' | 'göz' | 'gün' | 'öğretmen'
    TP -> 'lar' | Empty
    TF -> 'ler' | Empty
    Empty ->
    VS -> 'okur' | 'görür' | 'sever' | 'alır' | 'yapar'
    Conj -> 've' | 'veya'
""")

parser = nltk.ChartParser(grammar)

def sep(s):
    s = s.lower()
    d = {'kitaplar': 'kitap lar', 'kapılar': 'kapı lar', 'çocuklar': 'çocuk lar', 
         'arabalar': 'araba lar', 'kadınlar': 'kadın lar', 'evler': 'ev ler', 
         'kediler': 'kedi ler', 'gözler': 'göz ler', 'günler': 'gün ler', 
         'öğretmenler': 'öğretmen ler'}
    for k, v in d.items():
        s = s.replace(k, v)
    return s.split()

test = ["Çocuklar kitap okur", "Kediler ev görür", "Kadınlar araba sever",
        "Öğretmenler kitaplar okur", "Çocuklar ve kadınlar kitap okur",
        "Çocuklar kapılar veya arabalar görür", "Kediler ve çocuklar ev sever",
        "Çocukler kitap okur", "Evlar kedi görür", "Kitapler okur",
        "Çocuklar ve okur", "Kediler kapılar arabalar", "Araba sever"]

print("Quieres ver las pruebas o introducir tu oracion? (1 pruebas, 2 oracion)")
opt = int(input())

if opt == 1:
    for s in test:
        try:
            t = list(parser.parse(sep(s)))
            if t:
                print(f"\nVALIDA: {s}")
                t[0].pretty_print()
            else:
                print(f"\nINVALIDA: {s}")
        except:
            print(f"\nINVALIDA: {s}")
else:
    s = input("Escribe la oracion: ")
    try:
        t = list(parser.parse(sep(s)))
        if t:
            print(f"\nVALIDA: {s}")
            t[0].pretty_print()
        else:
            print(f"\nINVALIDA: {s}")
    except:
        print(f"\nINVALIDA: {s}")