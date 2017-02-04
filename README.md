# TVHeadend-Script-TV-Guide
Un progetto per acquisire la guida TV dei canali Italiani e mostrarla in [TVHeadend](https://tvheadend.org/).

### Breve descrizione

Basato su un precedente script creato da Mathias F. Svendsen ho riscrlitto lo script per le mie esigenze includendo miglioramenti complessivi nel codice. Per attivare/installare lo script procedete come segue:

* Copia lo script in /usr/bin/tv_grab_url
* Assegnare i permessi 777 a tv_grab_url (chmod 777 tv_grab_url)
* Riavviare TVheadend (/etc/init.d/tvheadend restart)
* Dalla WebGUI accedere al pannello Configuration > Channel > EPG Grabber > Internal Grabber > selezionare: XMLTV: TV Grab by URL > Save
    
Ulteriori informazioni disponibili sul mio [Blog](https://www.andreadraghetti.it/tvheadend-script-guida-tv/).

#### License

Copyright (c) 2017 Andrea Draghetti | [Twitter](https://twitter.com/andreaghetti) | [Blog](https://www.andreadraghetti.it)  
Released under the GPL 3 license.
