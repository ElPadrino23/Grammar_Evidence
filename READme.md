# Gramatica del Idioma Turco
Evidencia: Generacion y Limpieza de Gramatica

## Contexto
El turco es un idioma de la familia turca hablado por más de 80 millones de personas. PEro a diferencia del español o del ingles, en turco la mayoría de la informacion gramatical se construye agregando sufijos a la raiz de la palabra (OptiLingo, 2026). Y una de sus caracteristicas mas particulares es la armonia vocalica, una regla que obliga a que las vocales del sufijo coincidan con la ultima vocal de la raiz

Para esta evidencia escogi un subconjunto del turco enfocado en la formacion del plural y la estructura basica de  una oracion Sujeto-Objeto-Verbo (SOV), que es el orden natural del idioma

### Reglas del plural en turco
El turco tiene un unico sufijo de plural, y este cambia segun la armonia vocalica menor (Turkish Language Learning, 2025):

1. Sufijo `-lar`: se agrega cuando la ultima vocal de la raiz es posterior (a, ı, o, u). Por ejemplo: `kitap` (libro) -> `kitaplar` (libros)

2. Sufijo `-ler`: se agrega cuando la ultima vocal de la raiz es **frontal** (e, i, ö, ü). Ejemplo: `ev` (casa) -> `evler` (casas)

### Vocabulario
Sustantivos con vocal post (utilizan `-lar`):
* `kitap`: libro
* `kapı`: puerta
* `çocuk`: niño
* `araba`: coche
* `kadın`: mujer

Sustantivos con vocal inicial (toman `-ler`):
* `ev`: casa
* `kedi`: gato
* `göz`: ojo
* `gün`: día
* `öğretmen`: profesor

Verbos:
* `okur`: lee
* `görür`: ve
* `sever`: ama
* `alır`: toma
* `yapar`: hace

Conjunciones:
* `ve`: y
* `veya`: o

## Modelos

### Gramatica inicial (Con recursividad a la izquierda y ambiguedad)
```
S    -> SN VS SN | SN VS
SN   -> SN Conj SN | N
N    -> NP | NF
NP   -> RP TP
NF   -> RF TF
RP   -> 'kitap' | 'kapı' | 'çocuk' | 'araba' | 'kadın'
RF   -> 'ev' | 'kedi' | 'göz' | 'gün' | 'öğretmen'
TP   -> 'lar' | Empty
TF   -> 'ler' | Empty
Empty ->
VS   -> 'okur' | 'görür' | 'sever' | 'alır' | 'yapar'
Conj -> 've' | 'veya'
```
Para esto:
* `S`: oracion: Esta puede ser sujeto + verbo + objeto o solo sujeto + verbo
* `SN`: sintagma nominal. Puede ser un nombre o varios unidos por conjunción.
* `N`: nombre, separado en dos categorías según armonía vocálica.
* `NP` / `NF`: nombre con vocal posterior / frontal.
* `RP` / `RF`: raíz posterior / frontal.
* `TP` / `TF`: terminación de plural posterior (`lar`) / frontal (`ler`), o vacía si es singular.
* La separación entre raíz y terminación es lo que permite validar que el sufijo plural usado sea el correcto para esa raíz.
