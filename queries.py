import pprint
queries = [
    ['all',
     'acido hipocloroso, acido ortofosforico, acido nitroso, acido carbonico, acido selenico'],
    ['all',
     'HBO2, H2CO3, HPO3, H2SO3, HBrO3'],
    ['all',
     'HPO2, H4P2O7, H4SiO4, H6Si2O7, H2SiO3'],
    ['all',
     'Bromato (III) de hidrogeno, Nitrato (III) de hidrogeno, Ortofosfato (III) de hidrogeno'],
    ['all',
     'HNO3, Nitrato (III) de hidrogeno, acido sulfuroso, tretraoxosulfato de dihidrogeno, HClO4, ortofosfato (V) de hidrogeno'],
    ['all',
     'acido hipocloroso, acido sulfurico, acido nitrico, acido periodico, acido nitroso, acido perbromico, acido metafosforico, acido sulfuroso, acido ortofosforico, acido carbonico, acido difosforico'],
    ['all',
     ['hidroxido ' + i for i in 'de escandio (III), de galio, de manganeso (III), de sodio, talico, de potasio, de cadmio, de uranio, de rubidio, de cesio, de tantalio (V), de platino (IV)'.split(', ')]],
    ['all',
     'trioxido de dinitrogeno, oxido de magnesio, monoxido de mercurio, oxido plumbico, oxido de aluminio, oxido cobaltico, oxido de plata (I), trioxido de dihierro, trioxido de cromo, oxido de germanio (IV), pentoxido de dibismuto, oxido de estaño (II)'],
    ['all',
     ['hidroxido de ' + i for i in 'rodio, renio, paladio, manganeso, iridio, osmio'.split(', ')]],
]
if __name__ == "__main__":
    pprint.pprint(queries)
    
