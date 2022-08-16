# Softex - Recife
# Janderson Freitas

'''
Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. Depois, desenvolva três ou mais objetos para testar o código.
'''

class Tuning:

    def __init__(self, name: str, tone: str):
        self.name = name
        self.tone = tone

    def tune(self, tuning):
        tones = ['C','C#','D','D#','E','F','F#','G', 'G#','A', 'A#','B']
        for i in range(len(tones)):
            if self.tone == tones[i]:
                aux = i + tuning
                if aux > 12:
                    self.tone = tones[aux%12]
                else:
                    self.tone = tones[aux]    
                break
    def show_tone(self):
        print(f'Name: {self.name} | Tone : {self.tone}')        

guitar_string_1 = Tuning('Frist string', 'C')
guitar_string_2 = Tuning('Second string', 'D#')
guitar_string_3 = Tuning('Third string', 'F')
guitar_string_4 = Tuning('Fourth string', 'B')
guitar_string_5 = Tuning('Fifth string', 'A')
guitar_string_6 = Tuning('Sixth string', 'G')

print("\nOut of tune strings:\n")
guitar_string_1.show_tone()
guitar_string_2.show_tone()
guitar_string_3.show_tone()
guitar_string_4.show_tone()
guitar_string_5.show_tone()
guitar_string_6.show_tone()

#Tuning strings to the standard guitar model
guitar_string_1.tune(4)
guitar_string_2.tune(-4)
guitar_string_3.tune(2)
guitar_string_4.tune(3)
guitar_string_5.tune(0)
guitar_string_6.tune(-3)

print("\nTune guitar strings:\n")
guitar_string_1.show_tone()
guitar_string_2.show_tone()
guitar_string_3.show_tone()
guitar_string_4.show_tone()
guitar_string_5.show_tone()
guitar_string_6.show_tone()