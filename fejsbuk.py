
#poskrbi da se vse sploh zažene
# moduli in konstante

import bottle
import sqlite3

bottle.debug(True)          # dobimo več opozoril o napaki
datoteka_baze = "knjiga_obrazov.sqlite"

        
#funkcije#########################


@bottle.route('/prijatelji/<id>')

@bottle.view('prijatelji')

def prijatelji(id):
    c=baza.cursor()
    c.execute(""" SELECT ime, priimek FROM osebe WHERE id = ?""", [id])
    oseba = c.fetchone()
    if oseba is None:
        c.close()
        return {'obstaja', False}
    else:
        (ime, priimek) = oseba
        c.execute(
            """SELECT osebe.ime, osebe.priimek
               FROM osebe JOIN prijateljstva ON osebe.id = prijateljstva.drugi
               WHERE prijateljstva.prvi = ?""", [id])
        prijatelji = c.fetchall()
        c.close()
        return {
            'obstaja': True,
            'ime': ime,
            'priimek' : priimek,
            'prijatelji': prijatelji
        }
    


#################

baza = sqlite3.connect(datoteka_baze, isolation_level=None)

# povezava z bazo in zagon strežnika
bottle.run(host='localhost', port=8080)       #na teh vratih se odpre

######
