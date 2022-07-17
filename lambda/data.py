# -*- coding: utf-8 -*-
MAX_CORRECT_OBJ = 5 # Numero massimo di oggetti corretti nella lista
MAX_WRONG_OBJ = 1 # Numero massimo di oggetti sbagliati nella lista
MAX_QUIZ = 5 
MAX_SEMANTIC_CATEGORY = 2 # Numero massimo di categorie possibili
SEMANTIC_LIST_CATEGORY = [1, 2] # ID categorie presenti in SEMANTIC_LIST
MAX_QUESTIONS = 2 # MAX NUMERO DOMANDE QUIZ 

SKILL_TITLE = "Avanti un Altro Quiz Game"

WELCOME_MESSAGE = ("Benvenuto ai giochi della memoria! ")

GAMES = ("Per avviare un gioco puoi dire 'Giochiamo a parole inverse' oppure 'Giochiamo a Trova l'intruso' ")

HELP = ("Mmh, non ho capito! " + str(GAMES))

START_2_GAME = ("Ti dirò sei parole. Trova l'intruso!")

START_1_GAME = ("OK. Sei pronto? Ti farò " + str(MAX_QUESTIONS) + " domande, mi raccomando a sbagliare! ")

EXIT_SKILL_MESSAGE = ("Ops.. Riprovaci!")

EXIT_SUCCESS_SKILL_MESSAGE = ("Complimenti hai vinto!")

PLAY_AGAIN = ("Vuoi giocare ancora? Puoi dire 'Giochiamo a trova l'intruso' oppure 'Giochiamo a Parole inverse'")

FALLBACK_ANSWER = "Scusa, non ho capito la tua richiesta. Riprova."

CORRECT_SPEECHCONS = ['Booya', 'All righty', 'Bam', 'Bazinga', 'Bingo',
                      'Boom', 'Bravo', 'Cha Ching', 'Cheers', 'Dynomite',
                      'Hip hip hooray', 'Hurrah', 'Hurray', 'Huzzah',
                      'Oh dear.  Just kidding.  Hurray', 'Kaboom', 'Kaching',
                      'Oh snap', 'Phew', 'Righto', 'Way to go', 'Well done',
                      'Whee', 'Woo hoo', 'Yay', 'Wowza', 'Yowsa']

WRONG_SPEECHCONS = ['Argh', 'Aw man', 'Blarg', 'Blast', 'Boo', 'Bummer',
                    'Darn', "D'oh", 'Dun dun dun', 'Eek', 'Honk', 'Le sigh',
                    'Mamma mia', 'Oh boy', 'Oh dear', 'Oof', 'Ouch', 'Ruh roh',
                    'Shucks', 'Uh oh', 'Wah wah', 'Whoops a daisy', 'Yikes']

QUESTION_LIST = [
    {
        'id': 1,
        'question': 'Zenga o Veltroni, è stato portiere dell\'Inter?',
        'correct': 'Veltroni',
        'wrong': 'Zenga'
    },
    {
        'id': 2,
        'question': 'Crick o Crack può essere finanziario un...?',
        'correct': 'Crick',
        'wrong': 'Crack'
    },
    {
        'id': 3,
        'question': 'Riso o patete, i supplì sono le crocchette sono di...?',
        'correct': 'Patate',
        'wrong': 'Riso'
    },
    {
        'id': 4,
        'question': 'Sodo o fritto, sulla bistecca alla bismarck ci va l\'uovo...?',
        'correct': 'Sodo',
        'wrong': 'Fritto'
    },
    {
        'id': 5,
        'question': '60 o 80, le frecce tricolore sono nate negli anni...?',
        'correct': '80',
        'wrong': '60'
    },
    {
        'id': 6,
        'question': 'Polso o piede, il metatarso è un osso del...?',
        'correct': 'Polso',
        'wrong': 'Piede'
    },
    {
        'id': 7,
        'question': 'D\'artagnan o Don Chisciotte, si chiama Costanza la matta di...?',
        'correct': 'Don Chisciotte',
        'wrong': 'D\'artagnan'
    },
    {
        'id': 8,
        'question': 'Cubo o Quadrato, nove equivale a 3 elevato a...?',
        'correct': 'Cubo',
        'wrong': 'Quadrato'
    },
    {
        'id': 9,
        'question': 'Calzini o Sandali, i Carmalitani che camminano scalzi non indossano i...? ',
        'correct': 'Sandali',
        'wrong': 'Calzini'
    },
    {
        'id': 10,
        'question': 'Rosso o nero, il riso Hermes ha il chicco...?',
        'correct': 'Rosso',
        'wrong': 'Nero'
    },
    {
        'id': 11,
        'question': 'Lino o Leone, il primo successore di San Pietro è stato...?',
        'correct': 'Leone',
        'wrong': 'Lino'
    },
    {
        'id': 13,
        'question': 'Levante o Ponente, le cinque terre sono nella riviera ligure di...?',
        'correct': 'Ponente',
        'wrong': 'Levante'
    },
    {
        'id': 14,
        'question': 'Inter o Juventus, ha vinto più coppe europee...?',
        'correct': 'Inter',
        'wrong': 'Juventus'
    },
    {
        'id': 15,
        'question': 'Destra o Sinistra, il nostro fegato si trova a...?',
        'correct': 'Destra',
        'wrong': 'Sinistra'
    },    {
        'id': 16,
        'question': 'Rigoletto o Trovatore, la donna immobile è un area del...?',
        'correct': 'Trovatore',
        'wrong': 'Regoletto'
    },
    {
        'id': 17,
        'question': 'Copertina o Tovaglietta, è un taglio di carne bovina',
        'correct': 'Tovaglietta',
        'wrong': 'Copertina'
    },    {
        'id': 18,
        'question': 'Fauzio o Baudo, è un collaboratore del commissario Montalabano?',
        'correct': 'Baudo',
        'wrong': 'Fauzio'
    },    {
        'id': 19,
        'question': 'Grillo o Pidocchio, ha le ali il..?',
        'correct': 'Pidocchio',
        'wrong': 'Grillo'
    },
    {
        'id': 22,
        'question': 'Braccia o gambe, nel tuffo carpiato si piegano le?',
        'correct': 'Gambe',
        'wrong': 'Braccia'
    },
    {
        'id': 23,
        'question': 'Emergenza o Sorpasso, sulla carreggiata a destra è la corsia di?',
        'correct': 'Sorpasso',
        'wrong': 'Emergenza'
    }
]
SEMANTIC_LIST = [
    {
       "category":1,
       "id":1,
       "name": "Canottiera"
    },
    {
       "category":1,
       "id":2,
       "name": "Reggiseno"
    },
    {
       "category":1,
       "id":3,
       "name": "Mutande"
    },
    {
       "category":1,
       "id":4,
       "name": "Calze"
    },
    {
       "category":1,
       "id":5,
       "name": "Maglia manica lunga"
    },
    {
       "category":1,
       "id":6,
       "name": "T-shirt"
    },
    {
       "category":1,
       "id":7,
       "name": "Camicia"
    },
    {
       "category":1,
       "id":8,
       "name": "Gonna"
    },
    {
       "category":1,
       "id":9,
       "name": "Jeans"
    },
    {
       "category":1,
       "id":10,
       "name": "Pantaloni"
    },
    {
       "category":1,
       "id":11,
       "name": "Costume da bagno uomo"
    },
    {
       "category":1,
       "id":12,
       "name": "Bikini"
    },
    {
       "category":1,
       "id":13,
       "name": "Infradito"
    },
    {
       "category":1,
       "id":14,
       "name": "Ciabatte"
    },
    {
       "category":1,
       "id":15,
       "name": "Maglione"
    },
    {
       "category":1,
       "id":16,
       "name": "Felpa"
    },
    {
       "category":1,
       "id":17,
       "name": "Cappotto"
    },
    {
       "category":1,
       "id":18,
       "name": "Sciarpa"
    },
    {
       "category":1,
       "id":19,
       "name": "Cappello"
    },
    {
       "category":1,
       "id":20,
       "name": "Guanti"
    },
    {
       "category":1,
       "id":21,
       "name": "Stivali"
    },
    {
       "category":1,
       "id":22,
       "name": "Doposci"
    },
    {
       "category":1,
       "id":23,
       "name": "Scarpe con racco"
    },
    {
       "category":1,
       "id":24,
       "name": "Scarpe da ginnastica"
    },
    {
       "category":1,
       "id":25,
       "name": "Mocassini"
    },
    {
       "category":1,
       "id":26,
       "name": "Accappatoio"
    },
    {
       "category":1,
       "id":27,
       "name": "Tuta da ginnastica"
    },
    {
       "category":1,
       "id":28,
       "name": "Cravatta"
    },
    {
       "category":1,
       "id":29,
       "name": "Cintura"
    },
    {
       "category":1,
       "id":30,
       "name": "Bretelle"
    },
    {
       "category":1,
       "id":31,
       "name": "Borsa"
    },
    {
       "category":1,
       "id":32,
       "name": "Borsa portadocumenti"
    },
    {
       "category":1,
       "id":33,
       "name": "Portafogli"
    },
    {
       "category":1,
       "id":34,
       "name": "Portachiavi"
    },
    {
       "category":1,
       "id":35,
       "name": "Berretto"
    },
    {
       "category":1,
       "id":36,
       "name": "Grembiule da cucina"
    },
    {
       "category":1,
       "id":37,
       "name": "Orecchini"
    },
    {
       "category":1,
       "id":38,
       "name": "Collana"
    },
    {
       "category":1,
       "id":39,
       "name": "Anelli"
    },
    {
       "category":1,
       "id":40,
       "name": "Spille"
    },
    {
       "category":1,
       "id":41,
       "name": "Braccialetti"
    },
    {
       "category":1,
       "id":42,
       "name": "Orologio da polso"
    },
    {
       "category":1,
       "id":43,
       "name": "Cerchietto"
    },
    {
       "category":1,
       "id":44,
       "name": "Cuffia"
    },
    {
       "category":1,
       "id":45,
       "name": "Giacca elegante da uomo"
    },
    {
       "category":1,
       "id":46,
       "name": "Tonaca prete"
    },
    {
       "category":1,
       "id":47,
       "name": "Tonaca suora"
    },
    {
       "category":1,
       "id":48,
       "name": "Divisa militare"
    },
    {
       "category":1,
       "id":49,
       "name": "Minigonna"
    },
    {
       "category":1,
       "id":50,
       "name": "Bermuda"
    },
    {
       "category":1,
       "id":51,
       "name": "Pareo"
    },
    {
       "category":1,
       "id":52,
       "name": "Sandali"
    },
    {
       "category":1,
       "id":53,
       "name": "Pile"
    },
    {
       "category":1,
       "id":54,
       "name": "Pelliccia"
    },
    {
       "category":1,
       "id":55,
       "name": "Giubbotto"
    },
    {
       "category":1,
       "id":56,
       "name": "Scarponi"
    },
    {
       "category":1,
       "id":57,
       "name": "Scarpe da uomo"
    },
    {
       "category":1,
       "id":58,
       "name": "Scarpe stringate"
    },
    {
       "category":1,
       "id":59,
       "name": "Zoccoli"
    },
    {
       "category":1,
       "id":60,
       "name": "Portamonete"
    },
    {
       "category":1,
       "id":61,
       "name": "Portacellulare"
    },
    {
       "category":1,
       "id":62,
       "name": "Abito da sposa"
    },
    {
       "category":1,
       "id":63,
       "name": "Smoking"
    },
    {
       "category":1,
       "id":64,
       "name": "Camicia"
    },
    {
       "category":1,
       "id":65,
       "name": "Ciondoli"
    },
    {
       "category":1,
       "id":66,
       "name": "Fedi nuziali"
    },
    {
       "category":1,
       "id":67,
       "name": "Cavigliera"
    },
    {
       "category":1,
       "id":68,
       "name": "Orologio da taschino"
    },
    {
       "category":1,
       "id":69,
       "name": "Gemelli"
    },
    {
       "category":1,
       "id":70,
       "name": "Fermacravatta"
    },
    {
       "category":1,
       "id":71,
       "name": "Fermacapelli"
    },
    {
       "category":1,
       "id":72,
       "name": "Mollette"
    },
    {
       "category":1,
       "id":73,
       "name": "Boxer"
    },
    {
       "category":1,
       "id":74,
       "name": "Cappello da chef"
    },
    {
       "category":1,
       "id":75,
       "name": "Grembiule da chef"
    },
    {
       "category":1,
       "id":76,
       "name": "Tuta da meccanico"
    },
    {
       "category":1,
       "id":77,
       "name": "Collant"
    },
    {
       "category":1,
       "id":78,
       "name": "Gilet"
    },
    {
       "category":1,
       "id":79,
       "name": "Abito elegante da donna"
    },
    {
       "category":1,
       "id":80,
       "name": "Mantella per la pioggia"
    },
    {
       "category":2,
       "id":1,
       "name": "Gabbiano"
    },
    {
       "category":2,
       "id":2,
       "name": "Pappagallo"
    },
    {
       "category":2,
       "id":3,
       "name": "Farfalla"
    },
    {
       "category":2,
       "id":4,
       "name": "Falco"
    },
    {
       "category":2,
       "id":5,
       "name": "Pellicano"
    },
    {
       "category":2,
       "id":6,
       "name": "Rondine"
    },
    {
       "category":2,
       "id":7,
       "name": "Tricheco"
    },
    {
       "category":2,
       "id":8,
       "name": "Foca"
    },
    {
       "category":2,
       "id":9,
       "name": "Polpo"
    },
    {
       "category":2,
       "id":10,
       "name": "Medusa"
    },
    {
       "category":2,
       "id":11,
       "name": "Granchio"
    },
    {
       "category":2,
       "id":12,
       "name": "Delfino"
    },
    {
       "category":2,
       "id":13,
       "name": "Balena"
    },
    {
       "category":2,
       "id":14,
       "name": "Pesce"
    },
    {
       "category":2,
       "id":15,
       "name": "Coccodrillo"
    },
    {
       "category":2,
       "id":16,
       "name": "Scoiattolo"
    },
    {
       "category":2,
       "id":17,
       "name": "Lupo"
    },
    {
       "category":2,
       "id":18,
       "name": "Volpe"
    },
    {
       "category":2,
       "id":19,
       "name": "Ghiro"
    },
    {
       "category":2,
       "id":20,
       "name": "Cervo"
    },
    {
       "category":2,
       "id":21,
       "name": "Castoro"
    },
    {
       "category":2,
       "id":22,
       "name": "Orso bruno"
    },
    {
       "category":2,
       "id":23,
       "name": "Stambecco"
    },
    {
       "category":2,
       "id":24,
       "name": "Marmotta"
    },
    {
       "category":2,
       "id":25,
       "name": "Orso bianco"
    },
    {
       "category":2,
       "id":26,
       "name": "Elefante"
    },
    {
       "category":2,
       "id":27,
       "name": "Giraffa"
    },
    {
       "category":2,
       "id":28,
       "name": "Leone"
    },
    {
       "category":2,
       "id":29,
       "name": "Zebra"
    },
    {
       "category":2,
       "id":30,
       "name": "Tigre"
    },
    {
       "category":2,
       "id":31,
       "name": "Lumaca"
    },
    {
       "category":2,
       "id":32,
       "name": "Serpente"
    },
    {
       "category":2,
       "id":33,
       "name": "Cane"
    },
    {
       "category":2,
       "id":34,
       "name": "Gatto"
    },
    {
       "category":2,
       "id":35,
       "name": "Mucca"
    },
    {
       "category":2,
       "id":36,
       "name": "Cavallo"
    },
    {
       "category":2,
       "id":37,
       "name": "Asino"
    },
    {
       "category":2,
       "id":38,
       "name": "Coniglio"
    },
    {
       "category":2,
       "id":39,
       "name": "Pecora"
    },
    {
       "category":2,
       "id":40,
       "name": "Capra"
    },
    {
       "category":2,
       "id":41,
       "name": "Gallina"
    },
    {
       "category":2,
       "id":42,
       "name": "Maiale"
    },
    {
       "category":2,
       "id":43,
       "name": "Rana"
    },
    {
       "category":2,
       "id":44,
       "name": "Oca"
    },
    {
       "category":2,
       "id":45,
       "name": "Ape"
    },
    {
       "category":2,
       "id":46,
       "name": "Coccinella"
    },
    {
       "category":2,
       "id":47,
       "name": "Formica"
    },
    {
       "category":2,
       "id":48,
       "name": "Cigno"
    },
    {
       "category":2,
       "id":49,
       "name": "Rinoceronte"
    },
    {
       "category":2,
       "id":50,
       "name": "Pinquino"
    },
    {
       "category":2,
       "id":51,
       "name": "Zanzara"
    },
    {
       "category":2,
       "id":52,
       "name": "Leopardo"
    },
    {
       "category":2,
       "id":53,
       "name": "Lombrico"
    },
    {
       "category":2,
       "id":54,
       "name": "Libellula"
    },
    {
       "category":2,
       "id":55,
       "name": "Gufo"
    },
    {
       "category":2,
       "id":56,
       "name": "Salmone"
    },
    {
       "category":2,
       "id":57,
       "name": "Tartaruga marina"
    },
    {
       "category":2,
       "id":58,
       "name": "Anquilla"
    },
    {
       "category":2,
       "id":59,
       "name": "Vipera"
    },
    {
       "category":2,
       "id":60,
       "name": "Scorpione"
    },
    {
       "category":2,
       "id":61,
       "name": "Puzzola"
    },
    {
       "category":2,
       "id":62,
       "name": "Tucano"
    },
    {
       "category":2,
       "id":63,
       "name": "Germano reale"
    },
    {
       "category":2,
       "id":64,
       "name": "Airone"
    },
    {
       "category":2,
       "id":65,
       "name": "Pipistrello"
    },
    {
       "category":2,
       "id":66,
       "name": "Aragosta"
    },
    {
       "category":2,
       "id":67,
       "name": "Cinghiale"
    },
    {
       "category":2,
       "id":68,
       "name": "Canguro"
    },
    {
       "category":2,
       "id":69,
       "name": "Cammello"
    },
    {
       "category":2,
       "id":70,
       "name": "Cavalletta"
    },
    {
       "category":2,
       "id":71,
       "name": "Gamberetto"
    },
    {
       "category":2,
       "id":72,
       "name": "Sogliola"
    },
    {
       "category":2,
       "id":73,
       "name": "Trota"
    },
    {
       "category":2,
       "id":74,
       "name": "Istrice"
    },
    {
       "category":2,
       "id":75,
       "name": "Struzzo"
    },
    {
       "category":2,
       "id":76,
       "name": "Squalo"
    },
    {
       "category":2,
       "id":77,
       "name": "Orca"
    },
    {
       "category":2,
       "id":78,
       "name": "Tonno"
    },
    {
       "category":2,
       "id":79,
       "name": "Vitello"
    },
    {
       "category":2,
       "id":80,
       "name": "Lontra"
    },
    {
       "category":2,
       "id":81,
       "name": "Fenicottero"
    },
    {
       "category":2,
       "id":82,
       "name": "Picchio"
    }
]
