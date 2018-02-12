#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from __future__ import print_function
import pprint
import sys


"""

Caractéristiques de Python
Langage de programmation puissant (champ des langages traditionnels) et simplicité
des langages de script et interpêtés.

Panneaux d'administration, antispam, audio, authentication, caching, command-line,
Concurrency, configuration, data validation, database, drivers, debugging,
deep learning, devops, e-commerce, emails, ERP,......

TIOBE Index : https://www.tiobe.com/tiobe-index/
https://oasis.sandstorm.io/

systèmes d’exploitation supportés : Windows, Unix, Linux, etc.,

Guido van Rossum (62 ans), développeur néerlandais, lancé en 1990, il y a 27 ans.

Langage de haut niveau (tableaux, dictionnaires, etc...)
Orienté objet
Souvent comparé aux langages de script d'Unix, conception propre et structuration.
Des extensions en C ; CPython, Jython, IronPython en C#.
Portabilité sur tous OS (raspberry) ; modules adaptés


Facile à apprendre : peu de mots clés..
Facile à lire : pas de $, pas de ; pas de ~  / LISIBILITE même en ne connaissant pas le langage
Facile à maintenir, modularité, documentation intégrée
Robuste : Gestionnaire d'exception, traceback
Efficace pour le prototypage rapide, en raison du nombre de modules déjà existants
Gestionnaire de mémoire : par opposition au C/C++ ; gestion de mémoire assurée par l'interpréteur
Interprêté et compilé en bytecode / comme Java
>>> Fichiers source : .py >> bytecode pyc/pyo


INSTALLATION : python.org OFFICIEL / compilable
Installé par défaut sur les Linux : python


Comment exécuter un programme ou des instructions python
Lancement de l'interpréteur interactif : python + iPython
Exécution de scripts depuis la ligne de commande  / #!/usr/bin/env ou /bin/env python  | chmod | exec (pas obligé py)
Utilisation d'un IDE : Eclipse +pydev/Liclipse, Pycharm, Idle
... Sur le web  /  Google App Engine / Lambdas AWS --> serverless

Documentation : online (python, readthedoc..) Pypi --> Python package index
Comparaison Perl / Java / Ruby / Javascript

Versions 2.7.14 (3/07/2010) et 3.6.2 (3/12/2008) - Pourquoi ? EOL fin 2020
Tester les postes
from __future__ import print_function


#2
Entrée/sortie
print()
Chaine de formatage
print "Session N°%u du langage %s" % (1, "Python")
Underscore

entrée:
a = raw_input('question ? ')

Commentaires et aide
help(print)
help(pprint)
help(pprint.PrettyPrinter)


# Un commentaire
print() # Autre commentaire

Si instruction sur plusieurs lignes \
Pas obligatoire si encadrées

Groupe d'instruction : if, while, def, class... >> :

def ma_fonction():
    "commentaire intégré"
    return True
help(ma_fonction)

Exemple aide Odoo, aide Erppeek

variables : identificateurs : lettre ou _
sensible à la casse

Guides de style : l'obligatoire et le conseillé... à intégrer dans un IDE


Pas à déclarer, mais pas accessible si non instancié
allocation mémoire automatique, compteur de réf, GC
on peut les effacer del (supprime la variable)
dynamiques, non typées

tout objet python possède :
. Une identité (son nom)
. Un type (lui-même un type)
. sa valeur

Type d'une variable (objet)
Outre les types standards, Code, Traceback, Slice...
isinstance(a,str)
isinstance(a,int)
isinstance(a,TestClass)

signification spéciale du _
_xxx : Ne pas importer lors d'un import de module
se réfère aussi à une variable ou classe privée
__init__ : noms spéciaux, convention (__name__, __main__, __doc__, __get_attr__, __set_attr__...)
_ comme variable jetable

int(), long(), float(), complex()
str(), unicode(), basestring()
list(), tuple()
type()
dict()
bool()
set(), frozenset()
object()
classmethod()
staticmethod()
super()
property()
file()

Accès séquentiel (+associatif) ou direct / stockage scalaire ou container / mise à jour


Opérateurs arithmétiques
+ - * / // % **
Affectation =
affectation concise +=
affectation multiple a, b, c = 1, 2, "chaine"  (intéressant avec un tuple)

de comparaison
< <= > >= == !=  (<>)
opérateurs logiques
and  or  not

Dans le and, permet de combiner avec ordre logique
a=False >>>> a and a.truc


inspecter un objet : str, repr()

True  False

variable spéciale None (null), idem pour tout objet "vide"

Nombres : int, bool, float (decimal dans decimal.Decimal)
True  False pour boolean

-------------------------------------------------

chaines, listes et tuple (séquences)


Chaînes
guillemets simple ou doubles
protection \'  \n....
Triples guillemets pour longues chaines
opérateurs +   *

accès à des éléments de la liste / Découpage

 0  1  2  3
 a  b  c  d
-4 -3 -2 -1

[:], [], [::]
indice 0 au début, -1 à la fin
inversion de chaine : [::-1]
un sur deux [::2]

opérateur spécial : % (printf)  "%#x" % 108 , %s %u %3.2f...

Substitution
from string import Template
s = Template('Il y a ${howmany} heures de ${what}')
print(s.substitute(what='cours', howmany=4))


Unicode
str


-------------------------

Fonctions intégrées

len()
max()
min()
zip()

Méthodes
.decode()
.encode()
.isnumeric()
.join()
.lower()
.replace()
.strip()
.upper()
.zfill()
.title()

-------------------------


Listes et tuples
liste = [1, 2, 3, 4]
tuple = (1, 2, 3, 4)
tuple = ('bonjour', 23.41, 2, 3, 4)
tuple = ( ('bonjour', 23.41), ('autre', 38.41))
Accès par indice

opérateurs spéciaux :
in
not in

Fonctions intégrées

sorted()
reversed()
enumerate()
zip()
sum()

Méthodes
.append()
.count()
.extend()
.index(obj)
.insert(index, obj)
.pop()
.remove()
.reverse()
.sort()


-------------------------


Dictionnaire:
définition : a = {'version': 17.10, 'name': 'The Artful Aardvak'}
a['version']
a['new'] = False
a
a.keys()
a.values()

>>> from collections import OrderedDict
>>> my_dictionary=OrderedDict()
>>> my_dictionary['foo']=3
>>> my_dictionar['aol']=1
>>> my_dictionary


Méthodes
.clear()
.copy()
.get(key)
.has_key()
.items()
.keys()
.iter... items/keys/values
.pop(key)
.update(dict2)
.values()

-------------------------

Ensembles
set
Union, différence, intersection....

s'initialise avec fonction fabrique set(iterable)
-------------------------



l'instruction IF
explication sur les blocs de codes
if
elif
else
une seule ligne possible : if () then mmm
attention au décalages
pas de switch

opérateur ternaire
return (isMember ? "$2.00" : "$10.00"); // en javascript
"$2.00" if isMember else "$10.00"

count = 0
while (count < 9):
  print('L'indice est :', count)
  count += 1

ATTENTION aux boucles infinies


for --> foreach
for x in v:
    Traitement

Explications sur indentation du code



séquences : données auxquelles on accède par un indice: string, list, dict, tuple
OU
itérateur :
Comment ça marche : fonction iter() renvoie un objet iterateur --> Classe implémentant __iter__, next
cet objet a une méthode next() > Lève une exception StopIteration

Fonctions qui renvoient des itérateurs : enumerate(), reverded()
fonctions any() ou all() si un au moins ou tous True

Nuance, objet résultant est un générateur, n'est pas chargé en mémoire

itérateurs : fichier, dictionnaire, ..


range - fonction qui renvoie une séquence
range(3)
range(100, 110)
range(100, 200, 100)


for letter in 'Ma chaîne':
    print('current letter:', letter)

st = 'Ma chaîne'
for i in range(len(st)):
    print('current letter:', st[i])

nameList = ['Maïwenn', "Romain", 'Elodie', 'Flavien']
for student in nameList:
    print(student)

for student in reversed(nameList):
    print(student)


Compréhension de liste
a=[(i, student) for i, student in enumerate(nameList)]

a=[(i, student) for i, student in enumerate(nameList,3)]


Itérer un dict avec une séquence en une ligne:
for i, b in enumerate(a.itervalues()):
    print i, b




Fichier: objet : méthodes : open (r/w/a/b)

EXCEPTIONS
IOError, AttributeError, keyError...

try/except
try/finally
try/except/finally


f = open('/home/antoine/Bureau/formation M33/logs/salonmnew.log-2018012')
try:
    f = open('/home/antoine/Bureau/formation M33/logs/salonmnew.log-201801')
except IOError:
    print('Impossible d'ouvrir le fichier')

parler de pass : instruction spéciale qui ne fait rien


SUR SEQUENCE :
maxlen = 0
f = open('/home/antoine/Bureau/formation M33/logs/salonmnew.log-20180128')
lines = f.readlines()
f.close()
for line in lines:
    print line
    print line.split(' ')[8]
    break

maxlen = 0
f = open('/home/antoine/Bureau/formation M33/logs/salonmnew.log-20180128')
lines = [x.split(' ')[8] for x in f.readlines()]
f.close()
for line in lines:
    print line
    break

SUR ITERATEUR
for line in open('/home/antoine/Bureau/formation M33/logs/salonmnew.log-20180128'):
    print line


for nameIndex in range(len(nameList)):
    print(nameList[nameIndex])

for i, student in enumerate(nameList):
    print(i, student)

------------------------------------

Dans toutes les boucles :
break
continue

------------------------------------

Fonctions

def multip(reference, amount, coef=2, *args, **kw_args):
    ''' Description de la fonction.
    bla bla bla

    :param string reference: la reference pour nom_fonction
    :param float amount: un montant en Euros

    :return ce que renvoie la fonction
    '''
    print args
    print kw_args
    amount = amount * coef
    return amount

Paramètres passé par référence
Renvoie toujours un résultat, si non transmis explicitement, c'est None


------------------------------------

Classes

Voir exemple de code 
Quelques remarques
Constructeur
Paramètre self
heritage : class Fille(Parent)


------------------------------------

Modules
Objectif : organiser logiquement le code ; chaque FICHIER est un module (extension .py)


Import de modules
import xxx
from xxx import pp
import xxx as pp

Attention à la portée, dans l'espace de nommage
plusieurs import d'un même module possible, il n'est CHARGE qu'une fois

notation pointée des variables au sein d'un module

fichier .egg, python package, comparable à un fichier .jar en java



------------------------------------

Les arguments de la ligne de commande :
sys.argv : len

Les fichiers
open, close, readlines, read..

Module os
unlink, rename, chmod, basename, dirname, exists, isfile....

Modules pratiques :
os, base64, csv, gzip, zipfile....


------------------------------------

virtuelnv myvirtualenv
source myvirtualenv/bin/activate

pip install nom_du_module  (pas besoin d'être root !)
checker avec 
import sys
sys.path

sys.modules

import pip
sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])

pip freeze
Pour sauvegarder

pip install -r /path/to/requirements.txt
Pour installer



Stratégies de recherches de modules : checker l'ancienneté, la documentation, le dynamisme du repo, 
l'utilisation réelle (Stack Overflow..), la "taille" (retion complexité-richesse / vitesse de prise en main)




------------------------------------


"""


class TestClass(object):
    """my very first class: FooClass"""
    version = 0.1 # attribut de classe (donnée) attribute data

    def __init__(self, name='Inconnu'):
        """constructeur"""
        self.name = name    # class instance (data) attribute
        print('Instance créée pour', name)

    def showname(self):
        """Attribut d'instance et nom de la classe"""
        print('Votre nom ', self.name)
        print('Le nom de ma classe', self.__class__.__name__)

    def showver(self):
        """Attribut de Classe"""
        print(self.version) # references FooClass.version

    def double(self, x):
        # n'utilise pas 'self' mais DOIT être transmis
        return x + x



if __name__ == '__main__':
    reload(sys)
    if hasattr(sys, "setdefaultencoding"):
        sys.setdefaultencoding("utf-8")
    pp = pprint.PrettyPrinter(indent=4)
    testClass = TestClass('Nom')
    testClass.showname()
    testClass.showver()
    print(testClass.double(4))


