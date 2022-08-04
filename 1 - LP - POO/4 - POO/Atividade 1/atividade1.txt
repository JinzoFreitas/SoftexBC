# Softex - Recife
# Janderson Freitas

'''
Classifique dois objetos materiais e dois abstratos. Insira, no mínimo, três métodos e três atributos para cada.
'''

#Create class car: Material Object
class Car:
    def __init__(self, brand: str, model: str, color: str, on = False, speed = 0.0):
        self.brand = brand
        self.model = model
        self.color = color  
    def turn_on(self) -> bool:
        self.on = True
    def speed_up(self) -> float:
        if self.on == True :
            self.speed += 1
        else:
            print("The car turn off, cant't speed up! ")    
    def brake(self) -> float:
        if self.on == True :
            while self.speed > 0:
                self.speed -= 1      
    def turn_off(self) -> bool:
        self.on = False
        while self.speed > 0:
            self.brake(self)
    def show_status(self):
        print(f'Car Turn On: {self.on}')
        print(f'Speed: {self.speed}')        

#Create class Book: Material Object
class Book:
    def __init__(self, title: str, rows: int, n_pages: int, dir: str):
        self.title = title
        self.rows = rows
        self.n_pages = n_pages
        self.dir = dir
    def Read(self):
        with open(self.dir, 'w+') as book:
            print(book.read())
    def Writer(self): 
        with open(self.dir, 'a') as book:
            text = input('write here: ')
            print(book.write(text))       
    def Delete(self, all = False, row = 0):
        if all == True:
            with open(self.dir, 'a') as book:
                book.write('')
        if row != 0:      
            with open(self.dir, 'w+') as book:
                lines = book.readlines()
                count = 1
                with open(self.dir, 'w') as bk:
                    for line in lines:
                        # remove specific line
                        if count == row:
                            bk.write('')
                
# Class Sound: Abstract Object
class Sound:
    def __init__(self, tone: str, timbre: str, height: str, level: int, status = False) -> str:
        self.tone = tone
        self.timbre = timbre
        self.height = height
        self.level = level
    def play(self):
        self.status = True
    def tune(self, tones, tuning = 0):
        tones = ['C','C#','D','D#','E','F','F#','G', 'G#','A', 'A#','B']
        for i in range(len(tones)):
            if self.tone == tones[i]:
                self.tone = tones[i + tuning]
                break
        print(self.tone)
    def adjust_level(self, count = 0):
        self.level += count

# Class Communication: Abstract Object
class Communication:
    def __init__(self, issuer: str, receiver: str, message: str, channel: str, language: str ) -> str:
        self.issuer = issuer
        self.receiver = receiver
        self.message = message
        self.channel = channel
        self.language = language
    def Write_Message(self):
        text = input('Write the message: ')
        self.message = text
    def Read_message(self):
        print(self.message)
    def Translate_message(self, new_language: str):
        from googletrans import Translator
        translator = Translator()
        self.Language = new_language
        self.message = translator.translate(self.message, dest=new_language)
        print(self.message)