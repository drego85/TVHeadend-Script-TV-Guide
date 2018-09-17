# TVHeadend Script Guida TV
Un progetto per acquisire la guida TV dei canali Italiani e mostrarla in [TVHeadend](https://tvheadend.org/).

#### Breve descrizione

Basato su un precedente script creato da Mathias F. Svendsen questo script permette di aggiungere le Guide TV Italiane in TVHeadend e i progetti ad esso correlati (es. Kodi).

#### Sofware Necessario

* python3

#### Installazione Automatica

* Copia il repository, o scaricare il file ZIP, nella propria Home Directory 
* Aprite il terminale, recatevi nella directory contenente gli script
* Eseguite il comando: _bash autoinstall.sh_
* Dalla WebGUI di TVHeadend accedere al pannello Configuration > Channel > EPG Grabber > EPG Grabber Modules > Selezionare e Attivare i tre Grabber riconoscibili dall'etichetta "XMLTV: TV Italy"

Questa procedura automatica è stata testata con Ubuntu, Debian e Raspibian.

#### Installazione Manuale

Per attivare e installare lo script procedete come segue:

* Copiare i tre file tv_grab_italy_basic_url.py, tv_grab_italy_sky_url.py e tv_grab_italy_sport_movies_url.py all'interno della directory /usr/bin/
* Rinominare i tre file eliminando l'estensione (.py)
* Assegnare i permessi 777 ai tre file (chmod 777 tv_grab_italy*)
* Riavviare TVHeadend (/etc/init.d/tvheadend restart)
* Dalla WebGUI accedere al pannello Configuration > Channel > EPG Grabber > EPG Grabber Modules > Selezionare e Attivare  i tre Grabber riconoscibili dall'etichetta "XMLTV: TV Italy"

Comandi brevi per inizializzare gli script:

* sudo cp tv_grab_italy* /usr/bin/ 
* sudo mv /usr/bin/tv_grab_italy_basic_url.py /usr/bin/tv_grab_italy_basic_url 
* sudo mv /usr/bin/tv_grab_italy_sky_url.py /usr/bin/tv_grab_italy_sky_url
* sudo mv /usr/bin/tv_grab_italy_sport_movies_url.py /usr/bin/tv_grab_italy_sport_movies_url
* sudo chmod 777 /usr/bin/tv_grab_italy*
* sudo /etc/init.d/tvheadend restart

Ulteriori informazioni disponibili sul mio [Blog](https://www.andreadraghetti.it/tvheadend-script-guida-tv/).

#### License

Copyright (c) 2017 Andrea Draghetti | [Twitter](https://twitter.com/andreaghetti) | [Blog](https://www.andreadraghetti.it)  
Released under the GPL 3 license.
