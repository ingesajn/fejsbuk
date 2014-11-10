
#poskrbi da se vse sploh zažene

import bottle


#nove strani tuki:
@bottle.route('/')    #dostopanje - če greš na ta naslov boš dobil ta odgovor
def vsi_smo_fajni():
    return "VSI STE FAJN!!!"

@bottle.route('/kvadriraj/<x>')
def kvadriraj(x):
    return str(int(x) ** 2)
#klic: http://localhost:8080/kvadriraj/104


#
@bottle.route('/hello/<name>')
def index(name):
    return bottle.template('<b>Hello {{name}}</b>!', name=name)
#
bottle.run(host='localhost', port=8080)       #na teh vratih se odpre
