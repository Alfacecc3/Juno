# Juno
### JUNO SPEAKING VERSION ###

per eseguire lo speaking di Juno è necessario usare un file visual basic supportato solo dai computer con windows.
questo documento prende gli argomenti da un file di testo generato da Juno. per permettere a juno di sapere cosa dire
bisogna sostituire nel file vbs la linea "EDIT ME" con il percorso del file. per ottenerlo basta cliccare con il tasto destro sul file e andare su proprietà, cliccare poi sul percorso e copiarlo. incollare poi il testo al posto della linea EDIT ME lasciando le virgolette dove sono e aggiungere \txtforTxtMkr.txt alla fine, prima delle virgolette.
adesso se juno dovesse essere eseguito restituirebbe un errore perchè la libreria SpeechRecognition non è installata, quindi prendere il percorso del file .whl ed eseguire il cmd in quel percorso, adesso scrivere nel cmd:

pip install [nomefile].whl

senza parentesi quadre e sostituire nomefile con il nome del file in .whl .
juno adesso può essere eseguito, se dovesse restituire un errore allora eseguire

pip install SpeechRecognition

questo installerà l'ultima versione di speech_recognition e juno sarà pronto a parlare se eseguito online. se anche questa volta si genera un errore significa che il computer non ha un microfono disponibile, per risolvere questo problema basta collegare delle cuffie o auricolari CON MICROFONO nello slot di ingresso audio del computer. se il file continua a crashare anche dopo queste operazioni 
contatta lo sviluppatore su:

ceccocamilletti3@gmail.com
