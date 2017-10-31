# TVHeadend Script Guida TV
Un progetto per acquisire la guida TV dei canali Italiani e mostrarla in [TVHeadend](https://tvheadend.org/).

### Breve descrizione

Basato su un precedente script creato da Mathias F. Svendsen ho riscritto lo script per le mie esigenze includendo miglioramenti complessivi nel codice. 

#### Sofware Necessario

* python3 
* lzma

#### Installazione

Per attivare e installare lo script procedete come segue:

* Copiare i tre file tv_grab_italy_basic_url.py, tv_grab_italy_sky_url.py e tv_grab_italy_sport_movies_url.py all'interno della directory /usr/bin/
* Rinominare i tre file eliminando l'estensione (.py)
* Assegnare i permessi 777 ai tre file (chmod 777 tv_grab_italy*)
* Riavviare TVHeadend (/etc/init.d/tvheadend restart)
* Dalla WebGUI accedere al pannello Configuration > Channel > EPG Grabber > EPG Grabber Modules > selezionare i tre Grabber riconoscibili dall'etichetta "XMLTV: TV Italy"

Ulteriori informazioni disponibili sul mio [Blog](https://www.andreadraghetti.it/tvheadend-script-guida-tv/).

#### License

Copyright (c) 2017 Andrea Draghetti | [Twitter](https://twitter.com/andreaghetti) | [Blog](https://www.andreadraghetti.it)  
Released under the GPL 3 license.
