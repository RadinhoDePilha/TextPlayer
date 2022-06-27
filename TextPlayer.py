from PyPDF2 import PdfReader
from time import sleep
from pathlib import Path
import os
from time import sleep
from pynput import keyboard
from pynput.keyboard import Listener, Key, Controller
from threading import Thread, Lock
import parser
import os

arquivo = ''
stop_all = False

def DO_NOTHING(key):
    pass

def controles(key):
    if key == keyboard.Key.esc:
        listador.quit = True
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

    def __init__(self, archive, page, info = True):
        super().__init__()        
        self.reader = PdfReader(archive)
        self.pages = self.reader.getNumPages()
        self.velocidade = 0.25
        self.next = False
        self.just_stop = False
        self.info = info
        self.quit = False
        self.page = page

    def run(self):
        for n in range(self.pages):
            page = self.reader.getPage(n)
            text = page.extract_text().split(sep=' ')
            if n > self.page:
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

                            if self.quit:
                                os.system('clear')
                                quit()

                        
                    

if __name__ == '__main__':
    arquivo = Path(parser.args.pdf_file)
    listador = Listador(arquivo, parser.args.page) 
    listador.start()
    with Listener(on_press=controles, on_release=DO_NOTHING) as listener:
        listener.join()

    



    
   


            
            
    

