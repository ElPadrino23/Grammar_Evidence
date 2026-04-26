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
`S`: oracion: Esta puede ser sujeto + verbo + objeto o solo sujeto + verbo

`SN`: sintagma nominal. Puede ser un nombre o varios, con una conjuncion

`N`: nombre, separado en dos categorias

`NP` / `NF`: nombre con vocal, ya sea posterior o frontal

`RP` / `RF`: raiz posterior o frontal

`TP` / `TF`: terminacion del plural  (`lar`) o del frontal (`ler`), en caso de que sea singular, de queda vacia

La separación entre raiz y terminacion es lo que nos permitira validar que el sufijo plural usado sea  correcto para esa raiz

### Eliminacion de ambigüedad
La regla `SN -> SN Conj SN | N` es ambigua. Una oracion con dos conjunciones como `çocuklar ve kadınlar ve kediler` puede generar dos áaboles distintos para formar la oracion, esto segun como se agrupen las palabras

Esto se elimina introduciendo un no terminal intermedio SNP:

```
SN  -> SN Conj SNP / SNP
SNP -> SNP / N
```

### Eliminacioon de recursividad izquierda
La regla anterior y SNP tiene recursividad a la izquierda, pero aplicando la transformación estándar `A -> A α | β` se reescribe como `A -> β A'` y `A' -> α A' | e`:
```
SN    -> SNP SN_A
SN_A  -> Conj SNP SN_A | Empty
SNP   -> N SNP_A
SNP_A -> SNP | Empty
```

### Gramatica final
```
S     -> SN VS SN / SN VS
SN    -> SNP SN_A
SN_A  -> Conj SNP SN_A / Empty
SNP   -> N SNP_A
SNP_A -> SNP / Empty
N     -> NP / NF
NP    -> RP TP
NF    -> RF TF
RP    -> 'kitap' / 'kapı' / 'çocuk' / 'araba' / 'kadın'
RF    -> 'ev' / 'kedi' / 'göz' / 'gün' / 'öğretmen'
TP    -> 'lar' / Empty
TF    -> 'ler' / Empty
Empty ->
VS    -> 'okur' / 'görür' / 'sever' / 'alır' / 'yapar'
Conj  -> 've' / 'veya'
```

## Implementacion
Lo implemente en Python usando la librería NLTK con CFG, para definir la gramatica y ChartParser para poder procesar y analizar las oraciones. Como la gramatica separa la raiz de el final, Entonces utilizamos la funcion para separar, la funcion es: separate que divide cada palabra en raiz y su sufijo (tipo:  `çocuklar` → `çocuk lar`) esto es lo que nos ayuda a validar que el sufijo usado sea el correcto: si alguien escribe `kitapler`, la funcion tratara de separarlo pero si no encuentra una regla que lo acepte `kitap ler` (porque `kitap` es raiz posterior y solo se puede combinar con `lar`) la oracion se rechaza


## Pruebas

### Oraciones aceptadas
1. `Çocuklar kitap okur` — Los niños leen libros
2. `Kediler ev görür` — Los gatos ven la casa
3. `Kadınlar araba sever` — Las mujeres aman el coche
4. `Öğretmenler kitaplar okur` — Los profesores leen libros
5. `Çocuklar ve kadınlar kitap okur` — Los niños y las mujeres leen libros
6. `Çocuklar kapılar veya arabalar görür` — Los niños ven puertas o coches
7. `Kediler ve çocuklar ev sever` — Los gatos y los niños aman la casa

### Oraciones rechazadas
1. `Çocukler kitap okur` — Plural incorrecto: `çocuk` necesita `-lar` no `-ler`
2. `Evlar kedi görür` — Plural incorrecto: `ev` necesita `-ler` no `-lar`
3. `Kitapler okur` — Plural incorrecto
4. `Çocuklar ve okur` —  sin segundo sustantivo
5. `Kediler kapılar arabalar` — sin verbo



## Referencias

Adams, M. D., Hollenbeck, C., & Might, M. (2016). On the complexity and performance of parsing with derivatives. *Proceedings of the 37th ACM SIGPLAN Conference on Programming Language Design and Implementation*, 224–236. https://doi.org/10.1145/2908080.2908128

NLTK. (s.f.). Natural Language Toolkit. https://www.nltk.org/

Turkish Language Learning. (15 de julio, 2025). Ultimate Turkish Grammar Guide. https://turkishlanguagelearning.com/turkish-grammar-rules/

Turkish Textbook. (21 de febrero, 2025). Vowel harmony. https://www.turkishtextbook.com/vowel-harmony/

Optilingo (5 de mayo, 2023) https://www.optilingo.com/blog/turkish/everything-about-the-turkish-language/
