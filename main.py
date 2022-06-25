from PyPDF2 import PdfReader
from time import sleep
import os
from time import sleep
from pynput import keyboard
from pynput.keyboard import Listener
from threading import Thread, Lock
import os

arquivo = ''
stop_all = False

def controles(key):
    if key == keyboard.Key.esc:
        
        
        global stop_all
        global listener
        stop_all = True
        exit()
    
    if key == keyboard.Key.right:
        listador.velocidade -= 0.005
    
    if key == keyboard.Key.left:
        listador.velocidade += 0.005

    if key == keyboard.Key.enter:
        listador.next = True

class Listador(Thread):
    """
    Display the words of a array
    """

    def __init__(self, archive):
        super().__init__()        
        self.reader = PdfReader(archive)
        self.pages = self.reader.getNumPages()
        self.velocidade = 0.25
        self.next = False
        self.just_stop = False


    def run(self):
        self.lista_palavras()


    def lista_palavras(self):
        for n in range(self.pages):
            page = self.reader.getPage(n)
            text = page.extract_text().split(sep=' ')
            
            
            for word in text:
                        os.system('clear')
                        print(word.center(50).replace('\n', '')) 
                        print('\n\n\n\n')
                        print(f'speed: {self.velocidade:.2f} -- \
                            page: {n}')
                        if len(word) > 7:
                            sleep(self.velocidade + 0.1)
                        else:
                            sleep(self.velocidade)
                        if self.next:
                            self.next = False
                            break

                        global stop_all

                        if stop_all:
                            sleep(0.001)
                            os.system('clear')
                            quit()
                        
                        if self.just_stop:
                            pass
                            
                    
                    

if __name__ == '__main__':

    listador = Listador(arquivo)
    listador.start()

    with Listener(on_press=controles) as listener:
        listener.run()



    
   


            
            
    
