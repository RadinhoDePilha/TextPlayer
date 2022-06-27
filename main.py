from PyPDF2 import PdfReader
from time import sleep
import os
from time import sleep
from pynput import keyboard
from pynput.keyboard import Listener, Key, Controller
from threading import Thread, Lock
import os

arquivo = ''
stop_all = False

def controles_release(key):
    pass

def controles(key):
    if key == keyboard.Key.esc:
        
        
        global stop_all
        global listener
        stop_all = True
        listener.stop()
    
    if key == keyboard.Key.right:
        listador.velocidade -= 0.01
    if key == keyboard.Key.left:
        listador.velocidade += 0.01

    if key == keyboard.Key.enter:
        listador.next = True

    if key == keyboard.Key.space:
        if listador.just_stop:
            listador.just_stop = False
        else:
            listador.just_stop = True
        
    if hasattr(key, 'char'):
        if key.char == 'i':
            if listador.info:
                listador.info = False
            else:
                listador.info = True



class Listador(Thread):
    """
    Display the words of a array
    """

    def __init__(self, archive, info = True):
        super().__init__()        
        self.reader = PdfReader(archive)
        self.pages = self.reader.getNumPages()
        self.velocidade = 0.25
        self.next = False
        self.just_stop = False
        self.info = info


    def run(self):
        for n in range(self.pages):
            page = self.reader.getPage(n)
            text = page.extract_text().split(sep=' ')
            
            
            for word in text:
                        os.system('clear')
                        print(word.center(50).replace('\n', '')) 
                        print('\n\n\n\n')
                        print(f'Delay: {self.velocidade:.2f} \
                              Page: {n}\n')

                        if self.info == True:
                            print('"Left/Right" change Delay' + '\
    "Enter" to next page')
                            print('"Space" to pause/run\
        ' + '        "ESC" to quit')
                            print('"i" to hide/show this helper'.center(50))

                        if len(word) > 7:
                            sleep(self.velocidade + 0.1)
                        else:
                            sleep(self.velocidade)
                        if self.next:
                            self.next = False
                            break
                        
                        while self.just_stop:
                            sleep(0.5)

                        global stop_all

                        if stop_all:
                            sleep(0.001)
                            os.system('clear')
                            quit()

                        
                    

if __name__ == '__main__':

    
    listador = Listador(arquivo) 
    listador.start()
    with Listener(on_press=controles, on_release=controles_release) as listener:
        listener.join()

    



    
   


            
            
    

