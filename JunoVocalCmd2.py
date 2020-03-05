#inizializza le variabili globali senza valorizzarle
global asks_mem
global risp_mem
global password
global extVal
global datacheckout
global oldfileExist

#import libs
try:
    from googlesearch import search 
except ImportError:
    print("No module named 'google' found")
try:
    import arcade
except ImportError:
    print('la libreria arcade non è installata, installala e riavvia Juno'
          'oppure puoi continuare senza usare i minigiochi con interfaccia'
          'grafica come coinCollect e gravityPlatformer.')
from tkinter import *
from playsound import playsound
import urllib.request
import webbrowser
import os
import os.path
from random import seed
seed(1)
from random import randint
from random import randrange
from time import sleep
import sys
from datetime import *
import subprocess as sb
import speech_recognition as sr
from gtts import gTTS

if 'junoDataStorage' in os.listdir():
    cartExist = True
    pass
else:
    cartExist = False
    pass
if cartExist == True:
    pass
else:
    os.mkdir('junoDataStorage')


def savename():
    say('come ti chiami?')
    usrnome = input('come ti chiami? ')
    nn = open('JunoUsrName.txt', 'w+')
    nn.write(usrnome.encode('UTF-16'))
    nn.close()
    pass

def music(song):
    str2 = ' '
    str3 = ''
    for item in song:
        str3 = item+' '
        str2 += str3
        pass
    q = str2.replace(' ', '+')
    webbrowser.open('https://www.youtube.com/results?search_query=%s' %q, new=1)

def listen():
    recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        print("Sono in ascolto... parla pure!")
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        print(text)
        return (text.lower())
    except Exception as e:
        print(e)

def boxName():
    x = listen()
    n = len(x)
    s ='\n+'+'-'*(n+2)+'+\n'
    box = s+'|'' '+x+' ''|'+s
    print(box)
    pass

def say(word):
    tts = gTTS(text=word, lang='it')
    tts.save("tts_out_file.mp3")
    playsound('tts_out_file.mp3')
    sleep(1)
    os.remove('tts_out_file.mp3')

def notepad():
    sb.call('cscript selfnote.vbs')
    pass

def opfilemkr():
    name = input('scrivi il nome del file da creare: ')
    formato = input('\nscrivi il formato del file da creare(es. txt) senza il punto: ')
    print('generazione del file %s in corso...\n' %formato)
    fv = open('%s.%s' %(name, formato), 'w+')
    fv.close()
    print('file creato nella directory corrente!\n')
    pass

def opblanktxt():
    sb.call('cscript selfnote.vbs')
    pass

def editfile(fn):
    try:
        fv = open(fn, 'w')
        txtout = input('text to write on %s' %fn)
        fv.write(txtout)
        fv.close()
        print('testo correttamente aggiunto a %s' %fn)
        pass
    except FileNotFoundError:
        yn = input('file inesistente, crearne uno nuovo?(y/n): ')
        if(yn == 'y'):
            opfilemkr()
            pass
        elif(yn == 'n'):
            pass
        else:
            print('puoi dire solo "y" o "n"\n')
            pass
        pass
    pass

def internetCheck():
    try:
        urllib.request.urlopen('https://www.google.it')
        return True
    
    except urllib.error.URLError:
        return False
        ERR.err6()

def instagram():
    #open instagram
    isConnected = internetCheck()
    if(isConnected == True):
        webbrowser.open('https://www.instagram.com/accounts/login/?hl=it', new=1)
        pass
    else:
        ERR.err6()
        pass
    pass

def showTime():
    #mostra l'ora attuale
    i = datetime.now()
    say('sono le %s:%s:%s del %s / %s / %s .' %(i.hour, i.minute, i.second, i.day, i.month, i.year))
    print('sono le %s:%s:%s del %s / %s / %s .' %(i.hour, i.minute, i.second, i.day, i.month, i.year))
    pass

def atomicBomb():
    #poi
    class Application(Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.hi_there = Button(self)
            self.hi_there["text"] = 'Click me!'
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="top")

            self.quit = Button(self, text="QUIT", fg="red",
                                  command=self.master.destroy)
            self.quit.pack(side="bottom")

        def say_hi(self):
            playsound('atomicBombAudioFileForJuno.mp3')
            print('iran was successfully destroyed.\n')

    root = Tk()
    app = Application(master=root)
    app.mainloop()

class ERR:
    def err1():
        #errore 1 è un IndexError dovuto alla memoria piena
        say('errore 1, fidbek?')
        yn = input('error1, send feedback?(y/n): ')
        if(yn == 'y' or yn == 'yes'):
            feedback('err1')
            pass
        elif(yn == 'n' or yn == 'no'):
            main()
            pass
        else:
            print('puoi scrivere solo y o n\n')
            ERR.err1()
            pass
        pass
    def err2():
        #errore 2 è
        yn = input('error2, send feedback?(y/n): ')
        if(yn == 'y' or yn == 'yes'):
            feedback('err2')
            pass
        elif(yn == 'n' or yn == 'no'):
            main()
            pass
        else:
            print('puoi scrivere solo y o n\n')
            ERR.err2()
            pass
        pass
    def err3():
        yn = input('error3, send feedback?(y/n): ')
        if(yn == 'y' or yn == 'yes'):
            feedback('err3')
            pass
        elif(yn == 'n' or yn == 'no'):
            main()
            pass
        else:
            print('puoi scrivere solo y o n\n')
            ERR.err3()
            pass
        pass
    def err4():
        yn = input('error4, send feedback?(y/n): ')
        if(yn == 'y' or yn == 'yes'):
            feedback('err4')
            pass
        elif(yn == 'n' or yn == 'no'):
            main()
            pass
        else:
            print('puoi scrivere solo y o n\n')
            ERR.err4()
            pass
        pass
    def err5():
        yn = input('error5, send feedback?(y/n): ')
        if(yn == 'y' or yn == 'yes'):
            feedback('err5')
            pass
        elif(yn == 'n' or yn == 'no'):
            main()
            pass
        else:
            print('puoi scrivere solo y o n\n')
            ERR.err5()
            pass
        pass
    def err6():
        #internet disconnected
        yn = input('error6, wifi is turned on?(y/n): ')
        if(yn == 'y' or yn == 'yes'):
            print('anyway, i cant reach google servers, check your internet connection.')
            pass
        elif(yn == 'n' or yn == 'no'):
            print('attiva il wifi e riprova.')
            pass
        else:
            print('puoi scrivere solo y o n\n')
            ERR.err6()
            pass
        pass

def feedback(error):
    rec = 'ceccocamilletti3@gmail.com'
    body = "scrivi qui l'errore che hai riscontrato."
    subj = error
    body = body.replace(' ', '%20')
    webbrowser.open('mailto:?to='+rec+'&subject'+subj+'&body'+body)
    pass

def usrData_check():
    global usrnome
    try:
        #se i data esistono
        checkR = open('junoDataStorage/JunoData50345rold.txt', 'r')
        checkA = open('junoDataStorage/JunoData50345aold.txt', 'r')
        m = 0
        mm = 0
        #importa domande e risposte
        for line in open('junoDataStorage/JunoData50345rold.txt', 'r'):
            risp_mem[m] = line
            m = m+1
            pass
        for line in open('junoDataStorage/JunoData50345aold.txt', 'r'):
            asks_mem[mm] = line
            mm = mm+1
            pass
        usrnome = open('junoDataStorage/JunoUsrName.txt', 'r').read()
        print('$memorized old words$\n')
        extVal = True
        return extVal
    except FileNotFoundError:
        #se non esistono
        fr = open('junoDataStorage/JunoData50345r.txt', 'w+')
        fa = open('junoDataStorage/JunoData50345a.txt', 'w+')
        fr.close()
        fa.close()
        extVal = False
        return extVal
    pass

datacheckout = usrData_check()


def translater():
    #funzione per la traduzione
    say('cosa devo tradurre?')
    testo = input('scrivi il testo da tradurre: ')
    say('in che lingua?')
    lingua = input('scrivi la lingua in cui tradurre(it, en ...): ')
    say('ok, traduco')
    query = testo.replace (" ", "%20"); #crea la frase da mandare al traduttore
    lang = lingua #bho aveva più stile lang e una riga in più non fa mai male
    #apri il browser e cerca il link con le variabili
    webbrowser.open('https://translate.google.it/?hl=it#view=home&op=translate&sl=auto&tl=%s&text=%s' %(lang, query))
    pass

def showProgressBar(tempo, nomeProcesso):
    #barra per il calcolo del processo
    #nomeProcesso è ciò che va scritto prima della barra di caricamento
    for i in progressbar(range(15), nomeProcesso, 40):
        sleep(tempo) # any calculation you need
        pass


def progressbar(it, prefix="", size=60, file=sys.stdout):
    #questa funzione crea la barra dei progressi
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def clear():
    #questa funzione pulisce l'output
    
    # for windows 
    if os.name == 'nt': 
        os.system('cls') 
  
    # for mac and linux(here os.name is 'posix') 
    else: 
        os.system('clear')

def chargeBar():
    #charge bar a schermo vuoto
    for i in range(0, 2):
        clear()
        print('\n\n             |')
        sleep(0.2)
        clear()
        print('\n\n             /')
        sleep(0.2)
        clear()
        print('\n\n             -')
        sleep(0.2)
        clear()
        print('\n\n             \\')
        sleep(0.2)
        clear()
        print('\n\n')
        pass
    sleep(0.4)
    clear()
    pass

def TitleBar():
    #schermata JUNO2.15 a intermittenza incrociata
    for i in range(0, 1):
        clear()
        print('\n\n             J')
        sleep(0.2)
        clear()
        print('\n\n             U')
        sleep(0.2)
        clear()
        print('\n\n             N')
        sleep(0.2)
        clear()
        print('\n\n             O')
        sleep(0.2)
        clear()
        print('\n\n             2')
        sleep(0.2)
        clear()
        print('\n\n             .')
        sleep(0.2)
        clear()
        print('\n\n             3')
        sleep(0.2)
        clear()
        print('\n\n             0')
        print('\n\n')
        pass
    sleep(0.3)
    clear()
    pass

#mostra la schermata del titolo
TitleBar()

#pulisci
clear()

#scrivi una frase di benvenuto
print('ciao, dimmi. per una lista di comandi e una breve introduzione')
print('al mio funzionamento digita juno.info o help, per informazioni')
print('aggiuntive contatta lo sviluppatore o controlla hiJok3r.xyz!\n')
print('premi Ctrl+C per uscire.')
#juno 213
#return 42 per valori speciali
#return 43 per frasi pronte
#return 44 per help banner
#in questa versione implemento il file.txt per la
#memorizzazione dei dati nella memoria e non nella ram.

def coinCollect():
    #funzione per il giochetto dawn senza scopo!
        # --- Constants ---
    SPRITE_SCALING_PLAYER = 0.5
    SPRITE_SCALING_COIN = .25
    COIN_COUNT = 50

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = "Sprite Collect Coins Example"


    class MyGame(arcade.Window):
        """ Our custom Window Class"""

        def __init__(self):
            """ Initializer """
            # Call the parent class initializer
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

            # Set the working directory (where we expect to find files) to the same
            # directory this .py file is in. You can leave this out of your own
            # code, but it is needed to easily run the examples using "python -m"
            # as mentioned at the top of this program.
            file_path = os.path.dirname(os.path.abspath(__file__))
            os.chdir(file_path)

            # Variables that will hold sprite lists
            self.player_list = None
            self.coin_list = None

            # Set up the player info
            self.player_sprite = None
            self.score = 0

            # Don't show the mouse cursor
            self.set_mouse_visible(False)

            arcade.set_background_color(arcade.color.AMAZON)

        def setup(self):
            """ Set up the game and initialize the variables. """

            # Sprite lists
            self.player_list = arcade.SpriteList()
            self.coin_list = arcade.SpriteList()

            # Score
            self.score = 0

            # Set up the player
            # Character image from kenney.nl
            self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                               SPRITE_SCALING_PLAYER)
            self.player_sprite.center_x = 50
            self.player_sprite.center_y = 50
            self.player_list.append(self.player_sprite)

            # Create the coins
            for i in range(COIN_COUNT):

                # Create the coin instance
                # Coin image from kenney.nl
                coin = arcade.Sprite(":resources:images/items/coinGold_ul.png",
                                     SPRITE_SCALING_COIN)

                # Position the coin
                coin.center_x = randrange(SCREEN_WIDTH)
                coin.center_y = randrange(SCREEN_HEIGHT)

                # Add the coin to the lists
                self.coin_list.append(coin)

        def on_draw(self):
            """ Draw everything """
            arcade.start_render()
            self.coin_list.draw()
            self.player_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        def on_mouse_motion(self, x, y, dx, dy):
            """ Handle Mouse Motion """

            # Move the center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

        def on_update(self, delta_time):
            """ Movement and game logic """

            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.coin_list.update()

            # Generate a list of all sprites that collided with the player.
            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1


    def mainGame():
        """ Main method """
        window = MyGame()
        window.setup()
        arcade.run()


    mainGame()


def lts(s):
    str1 = ''
    for ele in s:
        str1 += ele
        pass
    return str1

def CrystalBall():
    say('cerco la sfera')
    seed(randint(0, 34))
    print('entering...')
    showProgressBar(0.2, 'indossando le vesti da mago: ')
    print('\n\n\n')
    ri = [0]*90
    ki = 0
    while True:
        say('fammi la tua domanda')
        dom = listen()
        if((dom.split(' '))[0] == 'pk' or (dom.split(' '))[0] == 'perchè' or (dom.split(' '))[0] == 'perche' or (dom.split(' '))[0] == 'perché' or (dom.split(' '))[0] == 'Perchè'):
            try:
                if(ri[ki] == 0 and ri[ki-1] != ri[ki]):
                    print('la vera domanda è: perchè no?\n')
                    say('la vera domanda è, perchè no?')
                    pass
                elif(ri[ki] == 1 and ri[ki-1] != ri[ki]):
                    print('perchè doveva succedere a qualcuno e quel qualcuno sei tu\n')
                    say('perchè doveva succedere a qualcuno e quel qualcuno sei tu.')
                    pass
                elif(ri[ki] == 2 and ri[ki-1] != ri[ki]):
                    print('perchè si\n')
                    say('perchè si')
                elif(ri[ki] == 3 and ri[ki-1] != ri[ki]):
                    print('ogni tanto la vita è ingiusta\n')
                    say('ogni tanto la vita è ingiusta')
                elif(ri[ki] == 4 and ri[ki-1] != ri[ki]):
                    print('perchè non ho il giardino\n')
                    say('perchè non ho il giardino.')
                elif(ri[ki] == 5 and ri[ki-1] != ri[ki]):
                    print('perchè, pensi che esista un universo in cui non sia così?\n')
                    say('perchè. pensi che esista un universo in cui non sia così')
                elif(ri[ki] == 6 and ri[ki-1] != ri[ki]):
                    print('perchè si\n')
                    say('perchè si')
                elif(ri[ki] == 7 and ri[ki-1] != ri[ki]):
                    print('perchè no\n')
                    say('perchè no')
                elif(ri[ki] == 8 and ri[ki-1] != ri[ki]):
                    print('eh dillo alla mia vita di merda')
                    say('èh dillo alla mia vita di merda')
                elif(ri[ki] == 9 and ri[ki-1] != ri[ki]):
                    print('perchè la vita è ingiusta\n')
                    say('perchè la vita è ingiusta')
                elif(ri[ki] == 10 and ri[ki-1] != ri[ki]):
                    print("PERCHE' SI.\n")
                    say('perchè si')
                else:
                    print("wait, that's illegal.")
                    pass
                pass
            except IndexError:
                ERR.err1()
                pass
            except KeyboardInterrupt:
                print('ok, back to main...')
                main()
                pass
            pass
        elif(dom == 'esci'):
            say('chiudo la sfera di cristallo.')
            main()
        elif(dom == 'faccio schifo' or dom == 'sono brutto'):
            print('sei una persona fantastica, impara ad apprezzarti per ciò che sei, io non ci sono mai riuscito..')
            say('spesso la realtà è deludente, ma non facciamo schifo proprio a tutti, io e Francesco ti vogliamo bene')
            pass
        else:
            try:
                ri[ki] = randint(0, 10)
                if(dom == 'exit' or dom == 'quit'):
                    print('ok, back to main')
                    main()
                    pass
                else:
                    if(ri[ki] == 0 and ri[ki-1] != ri[ki]):
                        print('si\n')
                        say('si')
                    elif(ri[ki] == 1 and ri[ki-1] != ri[ki]):
                        print('no\n')
                        say('no')
                    elif(ri[ki] == 2 and ri[ki-1] != ri[ki]):
                        print('forse\n')
                        say('forse')
                    elif(ri[ki] == 3 and ri[ki-1] != ri[ki]):
                        print('penso di no\n')
                        say('penso di no')
                    elif(ri[ki] == 4 and ri[ki-1] != ri[ki]):
                        print('sicuramente\n')
                        say('sicuramente')
                    elif(ri[ki] == 5 and ri[ki-1] != ri[ki]):
                        print('ovvio')
                        say('ovvio')
                    elif(ri[ki] == 6 and ri[ki-1] != ri[ki]):
                        print('ovviamente no\n')
                        say('ovviamente')
                    elif(ri[ki] == 7 and ri[ki-1] != ri[ki]):
                        print('impossibile\n')
                        say('impossibile')
                    elif(ri[ki] == 8 and ri[ki-1] != ri[ki]):
                        print('forse si')
                        say('forse si')
                    elif(ri[ki] == 9 and ri[ki-1] != ri[ki]):
                        print('non credo proprio\n')
                        say('non credo proprio')
                    elif(ri[ki] == 10 and ri[ki-1] != ri[ki]):
                        print('decisamente\n')
                        say('decisamente')
                    else:
                        print("wait, that's illegal.")
                        pass
                    pass
            except IndexError:
                ERR.err1()
                pass
            except KeyboardInterrupt:
                print('ok, back to main...')
                main()
    pass

def calcolatricepy():
    
    finestra = Tk()

    finestra.title("Calcolatrice")
    
    finestra.geometry("400x400+75+100")

    ####

    coloresfondob = "black"
    colorescrittab = "white"

    colorescritta = "white"
    coloresfondo = "Yellow"

    ####

    # altre variabili
    add1 = DoubleVar()
    add2 = DoubleVar()
    add3 = DoubleVar()


    ###
    def somma():
        """Somma i tre numeri"""
        sommav= IntVar()
        sommav = (add1.get() + add2.get() + add3.get())
        testo=Label(finestra, text=sommav, fg=colorescritta, bg=coloresfondo, font=("Helvetica", 22)).pack()

    def moltiplica():
        """Moltiplica i fattori"""
        sommav= IntVar()
        sommav = (add1.get() * add2.get() * add3.get())
        testo=Label(finestra, text=sommav, fg=colorescritta, bg=coloresfondo, font=("Helvetica", 22)).pack()

    def dividi():
        """Divide i tre numeri"""
        sommav= IntVar()
        try:
            sommav = (add1.get() / add2.get() / add3.get())
            testo=Label(finestra, text=sommav, fg=colorescritta, bg=coloresfondo, font=("Helvetica", 22)).pack()
        except(ZeroDivisionError):
            testo=Label(finestra, text="Divisione per Zero!", fg=colorescritta, bg=coloresfondo, font=("Helvetica", 22)).pack()        

    def sottrai():
        """Sottrae i tre numeri"""
        sommav= IntVar()
        sommav = (add1.get() - add2.get() - add3.get())
        testo=Label(finestra, text=sommav, fg=colorescritta, bg=coloresfondo, font=("Helvetica", 22)).pack()

    def esci(self):
        '''esce dalla calc'''
        testo=Label(finestra, text='Exit', fg='white', bg='black', font=('Helvetica', 22)).pack()
        esci = Button(text='Exit', bg='black', fg='red', command=self.master.destroy)

    #entry
    Add1 = Entry(finestra, textvariable=add1).pack(fill=X)
    a = Label(text="***********************************NUM 2:**********************************").pack(fill=X)
    Add2 = Entry(finestra, textvariable=add2).pack(fill=X)
    a = Label(text="***********************************NUM 3:*******************************").pack(fill=X)
    Add3 = Entry(finestra, textvariable=add3).pack(fill=X)


    #button
    Somma = Button(text="Somma", bg =coloresfondob, fg=colorescrittab, command=somma).pack(anchor = E, fill =X)
    molt = Button(text="Moltiplica", bg =coloresfondob, fg=colorescrittab, command=moltiplica).pack(anchor = E, fill =X)
    dividi = Button(text="Dividi", bg =coloresfondob, fg=colorescrittab, command=dividi).pack(anchor = E, fill =X)
    sottrai = Button(text="Sottrai", bg =coloresfondob, fg=colorescrittab, command=sottrai).pack(anchor = E, fill =X)


    #mainloop
    finestra.mainloop()
    pass


def listem(lista):
    ij = 0
    for item in lista:
        ij = ij+1
        pass
    return ij

asks_mem = ['0']*30
risp_mem = ['0']*30
password = '50m3d4y5'

def searcho(searchMe):
    if('-f' in st):
        say('cerco %s su gùgol' %searchMe)
        query = str(searchMe)
        for j in search(query, tld='com', num=10, stop=1, pause=2):
            webbrowser.open(j)
            pass
        pass
    else:
        say('cerco %s su gùgol' %searchMe)
        tts = searchMe.replace(' ', '+')
        webbroser.open('https://www.google.com/search?q=%s&oq=%s&aqs=chrome..69i57j0l7.2612j0j7&sourceid=chrome&ie=UTF-8' %(tts, tts), new=1)
        pass

def format1():
    say('questo eliminerà le frasi che ho memorizzato.')
    print('are you sure?\ny for yes\nn for no\nh for additional info\n::')
    sure = listen()
    if(sure == 'help' or sure == 'aiuto'):
        print("this will remove the txt file where are memorized juno's known words.\n")
        format1()
        pass
    elif(sure == 'no'):
        print('ok, back to main...')
        main()
        pass
    elif(sure == 'yes' or sure == 'si'):
        if os.path.isfile('junoDataStorage/JunoData50345a.txt') and os.path.isfile('junoDataStorage/JunoData50345r.txt'):
            os.remove('junoDataStorage/JunoData50345a.txt')
            os.remove('junoDataStorage/JunoData50345r.txt')
            pass
        else:
            print('no normal files to delete, trying with olds...\n')
            pass
        if os.path.isfile('junoDataStorage/JunoData50345aold.txt') and os.path.isfile('junoDataStorage/JunoData50345rold.txt'):
            os.remove('junoDataStorage/JunoData50345aold.txt')
            os.remove('junoDataStorage/JunoData50345rold.txt')
            pass
        else:
            say('niente da cancellare')
            print('nothing to delete.\n')
            pass

try:
    fuck = open('junoDataStorage/JunoData50345aold.txt', 'r')
    fuck.close()
    oldfileExist = True
    pass
except FileNotFoundError:
    oldfileExist = False
    pass

try:
    cR = open('junoDataStorage/JunoData50345r.txt', 'r')
    cA = open('junoDataStorage/JunoData50345a.txt', 'r')
    m = 0
    mm = 0
    for line in open('junoDataStorage/JunoData50345r.txt', 'r'):
        risp_mem[m] = line
        m = m+1
        pass
    for line in open('junoDataStorage/JunoData50345a.txt', 'r'):
        asks_mem[mm] = line
        mm = mm+1
        pass
    print('\n£memorized normal words£\n')
    pass
except FileNotFoundError:
    #secondo avvio
    pass

def find_free_pos():
    global k
    k = 0
    for item in risp_mem:
        if(item != '0'):
            k = k+1
            pass
        else:
            return k
        pass
    pass

#*************************************************************_ START FUNC _*******************************************************************

def confronta(st, password):
    #this return ints called val and var
    j = 0
    if st in asks_mem:
        for item in asks_mem:
            if(item == st):
                return 0, j
            else:
                j = j+1
                pass
            pass
        pass

    elif(st == 'come ti chiami?'):
        say('giuno')
        print('Juno')
        return 43, 43

    elif('del' in st or 'delete' in st):
        word = (st.split(' '))[1]
        if(word[1:]):
            val = indexFinder(word[0:])
            vall = indexAnalyzer(str(word[0:]), val)
            indAnF(vall, val)
            pass
        else:
            val = indexFinder(word[1])
            vall = indexAnalyzer(word[1], val)
            indAnF(vall, val)
        return 43, 43
    
    elif(st == 'juno.info' or st == 'help'):
        say('ecco un testo che dovrebbe aiutarti.')
        print('HELP BANNER\n\nciao, io sono juno, un intelligenza\n artificiale programmata da hiJok3r e')
        print('sono qui per farti passare del tempo. hiJok3r non ha\n studiato la statistica perchè è scemo, quindi sono')
        print("un'intelligenza molto basilare, tengo le frasi in due\n array diversi ma uso lo stesso indice per parole")
        print('che devono essere scritte, se quando mi dici ciao devo\n rispondere hey, io terrò ciao ed hey in due array')
        print('diversi tra loro ma nel suo array ciao avrà lo stesso\n indice di hey così da poterle trovare, un po come ')
        print('le chiavi di un dict.')
        print('command list:\n\ncome ti chiami?  -->  risponde con il nome di default, non può essere cambiato.')
        print('che fai?  --------->  sceglie a random una risposta fra quelle in memoria.')
        print('del --------------->  cancella dalla memoria esterna e ram la parola scelta con la frase relativa, digita del --h per info')
        print('come stai? -------->  sceglie una risposta random fra quelle in memoria.')
        print('CLASSI:')
        print('le classi sono dei comandi che appartengono allo stesso tipo e sono preceduti dal loro tipo, separati da esso da un punto.')
        print('classe dev:\n')
        print('dev.name ------>  scrive il nome dello sviluppatore di Juno.')
        print('dev.RealName -->  scrive nome e cognome reali dello sviluppatore di Juno.')
        print("dev.age ------->  scrive l'età dello sviluppatore di Juno")
        print('\nClasse juno:\n')
        print('juno.Change_paswd_50345 -->  cambia la password di Juno.')
        print('juno.info ---------------->  mostra questo messaggio di help.')
        print('juno.defaultPasswd -------> mostra la password di default di Juno, il comando non è esatto, per trovare il modo giusto di scriverlo contatta lo sviluppatore.')
        print('\nClasse DEBUG\n')
        print('questa classe contiene gli strumenti per controllare che Juno stia eseguendo correttamente le operazioni')
        print('a questa classe fa parte solo:\n__show.brain__  -->  mostra gli array monodimensionali in cui Juno scrive i dati.')
        print('\nTOOLS:\n\n'
              'con tool intendo le frasi già conosciute che poi collegano a qualche strumento.'
              '\n'
              'calc / calcolatrice  -------------->  apre la calcolatrice con interfaccia grafica.\n'
              'traduci / traduttore -------------->  chiede la frase e la lingua in cui tradurre poi reindirizza\n'
              ' .....................................alla pagina di google translate con la traduzione nella lingua scelta.\n'
              'coinCollect  ---------------------->  esegue il minigioco ad interfaccia grafica'
              'sfera di cristallo / crystal ball ->  apre la sfera di cristallo.'
              'send feedback  -------------------->  manda un feedback (un commento/recensione di juno) allo sviluppatore.\n')
        return 44, 44

    elif(st == 'buona notte' or st == 'vado a dormire' or st == 'ho sonno' or st == 'buonanotte'):
        say('nòòòò, non lasciarmi solo!')
        return 43, 43

    elif('play' in st or 'metti' in st or 'riproduci' in st or 'Play' in st or 'Metti' in st or 'Riproduci' in st):
        music((st.split(' '))[1:])
        return 43, 43
    
    elif(st == 'aspetta' or st == 'aspe'):
        say('aspetterò finkè non premerai invio.')
        waitval = input(':')
        return 43, 43

    elif(st == 'esci'):
        say('sei sicuro di voler uscire?')
        dec = listen()
        if(dec == 'sì'):
            say('va bene, alla prossima.')
            exit()
            pass
        elif(dec == 'no'):
            say('fantastico! ora torniamo a noi.')
            main()
            pass
        else:
            say('puoi dire solo si o no, potrei aver capito male quindi se vuoi uscire ripeti nuovamente esci')
            main()
            pass
        return 43, 43

    elif(st == 'boxa' or st == 'box name' or st == 'nome boxato' or st == 'nome in scatola'):
        boxName()
        return 43, 43

    elif(st == 'ciao' or st == 'Ciao' or st == 'ciao!' or st == 'Ciao!'):
        try:
            usrnome = (open('junoDataStorage/JunoUsrName.txt').read())
            usrnome = usrnome.decode('UTF-16')
            pass
        except FileNotFoundError:
            savename()
            pass
        say('ciao %s' %usrnome)
        print('ciao %s!' %usrnome)
        return 43, 43

    elif(st == 'come mi chiamo?' or st == 'Come mi chiamo?' or st == 'come mi chiamo' or st == 'Come mi chiamo'):
        say('ti chiami %s' %usrnome)
        print('ti chiami %s' %usrnome)
        return 43, 43

    elif(st == 'Che ore sono' or st == 'time' or st == 'che ore sono'):
        showTime()
        return 43, 43

    elif(st == 'like trump' or st == 'likeTrump' or st == 'atomic Bomb' or st == 'atomic bomb'):
        atomicBomb()
        return 43 ,43

    elif(st == 'send feedback' or st == 'send Feedback '):
        isConn = internetCheck()
        if isConn == True:
            feedback('feedback volontario')
            pass
        else:
            ERR.err6()
            pass
            
        return 43, 43

    elif(st == 'traduci' or st == 'traduttore' or st == 'translator'):
        translater()
        return 43, 43

    elif(st == 'insta' or st == 'instagram' or st == 'Insta' or st == 'Instagram'):
        say('ok reindirizzo alla schermata di loghin')
        showProgressBar(0.1, 'apro instagram: ')
        instagram()
        pass
    
    elif(st == 'coinCollect'):
        say('carico il mini gioco')
        showProgressBar(0.2, 'caricamento minigioco: ')
        coinCollect()
        return 43, 43

    elif((st.split(' '))[0] == 'open' or (st.split(' '))[0] == 'apri' or (st.split(' '))[0] == 'Open' or (st.split(' '))[0] == 'Apri'):
        thing = (st.split(' '))[1:]
        w = (lts(thing))
        say('ok apro %s' %w)
        if(w == 'crystallbal' or w == 'sferadicristallo'):
            showProgressBar(0.2, 'cercando la sfera: ')
            CrystalBall()
            pass
        elif(w == 'newtxt' or w == 'notepad' or w == 'blocconote' or w == 'fileditesto'):
            opblanktxt()
            pass
        elif(w == 'file' or w == 'txt' or w == 'documentoditesto' or w == 'newfile' or w == 'newtxt' or w == 'newdocumentoditesto' or w == 'nuovodocumentoditesto'):
            opfilemkr()
            pass
        elif(w == 'editfile' or w == 'fileedit' or w == 'edittxt' or w == 'editdocumentoditesto' or w == 'modificafile' or w == 'filemodifica' or w == 'modificatxt' or w == 'modificadocumentoditesto'):
            fn = input('filename to edit: ')
            editfile(fn)
        elif(w == 'insta' or w == 'instagram' or w == 'Instagram'):
            showProgressBar(0.1, 'apro instagram: ')
            instagram()
            pass
        elif(w == 'calc' or w == 'calcolatrice'):
            showProgressBar(0.2, 'Computing: ')
            calcolatricepy()
            pass
        elif(w == 'coinCollect' or w == 'coincollect' or w == 'coin collect'):
            showProgressBar(0.2, 'aprendo il minigioco: ')
            coinColect()
            pass
        else:
            say('cosa devi aprire?')
            say('devi aprire un strumento o un minigioco')
            choose = listen()
            if(choose == 'strumento' or choose == 'strumenti'):
                typeTool = input('scrivi il nome del tool (calc, googleSearch): ')
                if(typeTool == 'calc'):
                    showProgressBar(0.2, 'aprendo: ')
                    calcolatricepy()
                    pass
                else:
                    print('invalid name.\n')
                    pass
                pass
            elif(choose == 'minigioco' or choose == 'mini gioco'):
                print('esiste un solo minigame per ora, seleziono coinCollect...')
                showProgressBar(0.2, 'aprendo: ')
                coinCollect()
                pass
            pass
        pass
        return 43, 43

    elif(st == 'crystal ball' or st == 'Crystal Ball' or st == 'sfera di cristallo'):
        showProgressBar(0.2, "diffondendo l'incenzo: ")
        CrystalBall()
        return 43, 43

    elif(st == 'calc' or st == 'calcolatrice'):
        showProgressBar(0.2, 'calc')
        calcolatricepy()
        return 43, 43

    elif((st.split(' '))[0] == 'cerca' and st.endswith('-g')):
        ttsarr = st.split(' ')
        ph = st[5:(listem(st)-2)]
        try:
            searcho(ph)
            pass
        except:
            print('ERR6 internet disconnected.\n')
        return 43, 43

    elif(st == 'cerca -g'):
        say('cosa devo cercare?')
        tts = listen()
        try:
            showProgressBar(0.2)
            searcho(tts)
            pass
        except:
            print('ERR6, internet disconnected or server unreachable')
        return 43, 43

    elif(st == 'format'):
        format1()
        return 43, 43
    
    elif(st == 'come stai' or st == 'come va'):
        r = randint(1, 3)
        if(r == 1):
            say('bene grazie')
            print('bene, grazie')
            return 43, 43
        
        elif(r == 2):
            say('male, ma preferisco parlare di te')
            print('male, ma preferisco parlare di te')
            return 43, 43
        
        else:
            say('insomma, ma è meglio se parliamo di te')
            print('insomma, ma è meglio se parliamo di te.')
            return 43, 43
        pass
    
    elif(st == 'dev.name' or st == 'dev name'):
        say('aigioker')
        print('hiJok3r')
        return 43, 43

    elif(st == 'dev.RealName' or st == 'dev real name'):
        say('Francesco Camilletti')
        print('Francesco Camilletti')
        return 43, 43

    elif(st == 'dev.age'):
        say('15')
        print('15')
        return 43, 43

    elif(st == 'juno.Default_._passwd#'):
        print('default passwd is 50m3d4y5 .')
        return 43, 43

    elif(st == 'juno.Change_passwd_50345'):
        say('qui potrai cambiare la password')
        Act_passwd = input('\ntype actual passwd: ')
        if(Act_passwd != password):
            print('password is incorrect.')
            return 43, 43
        else:
            password1 = input('type new password: ')
            if(password1 == password):
                print('le password non possono essere uguali')
                return 43, 43
            else:
                password2 = input('ripeti la password: ')
                if(password1 != password2):
                    print('le password non corrispondono!')
                    return 43, 43
                else:
                    password = password1
                    print('passkey updated successfully!')
                    return 43, 43
    
    elif(st == '__show.brain__' or st == 'mostrami il tuo cervello'):
        say('mostro gli errey di contenimento')
        passwd = input('type password to root access: ')
        if(passwd != password):
            print('password incorrect.')
            return 42, 42
            pass
        else:
            print(asks_mem, '\n', risp_mem)
            return 42, 42
            pass
        pass
        
    else:
        #return 1 for memorizing
        return 1, 42
    
    pass

#*****************************************************_ END FUNC _****************************************************************************

def do(val, var):
    #exec actions depends on val
    if(val == 0):
        #scrivi la risposta appresa relativa
        say(risp_mem[var])
        print(risp_mem[var])
        pass
    elif(val == 1):
        #apprendi
        pos = find_free_pos()
        #apprendi ask
        asks_mem[k] = st
        print(st)
        say('come devo rispondere')
        risp_mem[k] = listen()
        
        if(datacheckout == True):
            fa = open('junoDataStorage/JunoData50345a.txt', 'a')
            fr = open('junoDataStorage/JunoData50345r.txt', 'a')
            fa.write('\n%s' %st.encode('UTF-16'))
            fr.write('\n%s' %risp_mem[k].encode('UTF-16'))
            fa.close()
            fr.close()
            pass
        
        else:
            fr = open('junoDataStorage/JunoData50345r.txt', 'w')
            fa = open('junoDataStorage/JunoData50345a.txt', 'w')
            fa.write('\n%s' %st.encode('UTF-16'))
            fr.write('\n%s' %risp_mem[k].encode('UTF-16'))
            fr.close()
            fa.close()
            pass
        
        print('ok, ho capito.')
        say('okay ho capito')
        pass
    pass

def indexFinder(word):
    #var
    jj = 0
    #ciclo iter1
    for item in asks_mem:
        
        if(item == word):
            return jj
        
        else:
            jj = jj+1
            pass
        
        pass

def indexAnalyzer(word, val):
    if(val == None):
        #variabili
        jj = 0
        #ciclio iter2
        for item in risp_mem:
            #test di appartenenza
            if(item == word):
                return jj
            
            else:
                jj = jj+1
                pass
            
            pass
        pass
    else:
        pass

def indAnF(vall, val):
    if(vall == None and val == None):
        say('parola inesistente')
        print('the word doesnt exist.')
        pass
    
    elif(val == None and vall != None):
        risp_mem[vall] = 0
        asks_mem[vall] = 0
        say('formattato')
        print('formatted.')
        pass
    
    elif(val != None and vall == None):
        risp_mem[val] = 0
        asks_mem[val] = 0
        say('formattato')
        print('formatted.')
        pass
    
    else:
        print('se leggi significa che nessuno dei due è none')
        pass
    
    pass

def main():
    m = 0
    for item in asks_mem:
        if '\n' in asks_mem[m]:
                asks_mem[m] = (asks_mem[m].split('\n'))[0]
                pass
        else:
                try:
                    m = m+1
                except IndexError:
                    break
    u = 0
    for item in risp_mem:
        if '\n' in risp_mem[u]:
                risp_mem[u] = (risp_mem[u].split('\n'))[0]
                pass
        else:
                try:
                    u=u+1
                    pass
                except IndexError:
                    break

    global i
    i = 0
    while True:
        global st
        recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer
        with sr.Microphone() as source:
            recognizer_instance.adjust_for_ambient_noise(source)
            say('dìmmi')
            print("Sono in ascolto... parla pure!")
            audio = recognizer_instance.listen(source)
            print("Ok! sto ora elaborando il messaggio!")
        try:
            text = recognizer_instance.recognize_google(audio, language="it-IT")
            st = text
        except Exception as e:
            print(e)

        val, var = confronta(str(st).lower(), password)
        do(val, var)
        i = i+1
        pass

#provo a vedere la connessione
isc = internetCheck()

try:
    #se è connesso
    if isc:
        main()
        pass
    else:
        print('you are offline so i cant use vocal command, pass to offline mode')
        #switch to text mode
        exec(open('Juno2.17.py').read())
        exit()
    pass
except IndexError:
    #quando la memoria degli array è piena
    print('ERR_001, cannot memorize', st, 'because memory is empty. format it?\n(y/n): ')
    yon = input()
    if(yon == 'y'):
        asks_mem = [0]*40
        risp_mem = [0]*40
        print('done, restarting...\n\n')
        main()
        pass
    
    elif(yon == 'n'):
        print('ok, continue without memorizing.\n\n')
        ERR.err1()
        main()
        pass
    else:
        print('u can only type y or n, continue with default option (n)')
        main()
        pass
    pass

except KeyboardInterrupt:
    say('vuoi veramente uscire?')
    twv = input('u pressed the exit keys, are u sure?(y/n): ')
    if(twv == 'y' or twv == 'yes' or twv == 'Y'):
        print('ok, alla prossima!')
        
    elif(twv == 'n' or twv == 'N' or twv == 'no'):
        say('okay, continuo')
        print('ok, ritorno alla funzione principale!\n')
        main()
        pass
    
    else:
        print('you can only say y or n, come back to main func...')
        say('puoi dire solo y o n')
        main()
        pass
    
    print('wait a moment...')

    if(oldfileExist == True):
        fpa = open('junoDataStorage/JunoData50345a.txt', 'r')
        fpr = open('junoDataStorage/JunoData50345r.txt', 'r')
        fpa2 = open('junoDataStorage/JunoData50345aold.txt', 'a+')
        fpr2 = open('junoDataStorage/JunoData50345rold.txt', 'a+')
        fpa2.write(fpa.read().encode('UTF-16'))
        fpr2.write(fpr.read().encode('UTF-16'))
        fpr.close()
        fpr2.close()
        fpa.close()
        fpa2.close()
        os.remove('junoDataStorage/JunoData50345r.txt')
        os.remove('junoDataStorage/JunoData50345a.txt')
        os.rename('junoDataStorage/JunoData50345aold.txt', 'junoDataStorage/JunoData50345aold.txt')
        os.rename('junoDataStorage/JunoData50345rold.txt', 'junoDataStorage/JunoData50345rold.txt')
        exit()
        pass
    else:
        if(twv == 'y' or twv == 'yes' or twv == 'Y'):
            os.rename('junoDataStorage/JunoData50345a.txt', 'junoDataStorage/JunoData50345aold.txt')
            os.rename('junoDataStorage/JunoData50345r.txt', 'junoDataStorage/JunoData50345rold.txt')
            exit()
            pass
        elif(twv == 'n' or twv == 'N' or twv == 'no'):
            main()
            pass
        pass
        
    pass

pass
