import wave as wv
from scipy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
character = input('Enter character to find: ')
startFrame = 0
endFrame = 0
if character == 'ð':
    startFrame = 0
    endFrame = 0
    pass
elif character == 'æ':
    startFrame = 34200
    endFrame = 34200
    pass
elif character == 't':
    startFrame = 64468
    endFrame = 64468
    pass

file = 'Phonetics.wav'
testFile = 'test2.wav'
averageThres = 4.825*10**15
stdThres = 6.9*10**15
fourierFreq = 658
phonTestList = 'ðæt kwɪk beɪʒ fɑːks dʒʌmpt ɪn ðʌ ɛɹ oʊvɚɹ iːtʃ θɪn dɑːɡ lʊk aʊt aɪ ʃaʊt fɔːɹ hiːz fɔɪld juː ɐɡɛn kɹiːeɪɾɪŋ keɪɑːs'
# ə = ʌ
# r = ɹ
# w = ʊ
# ə = ɚ
# i = i:
# a = ɑː
# ɔ = ɑː
# ɔ = ɔ:
newList = []
for i in phonTestList.split(' '):
    for j in range(len(i)):
        newList.append(j)
    
print(newList)
phonetics = {
    "ð" : [[0, 14248]],
    "æ" : [[14248, 29371]],
    "t" : [[29371, 36121]],
    "k" : [[59867, 68489],
           [89863, 99235]],
    "w" : [[68489, 81987]],
    "ɪ" : [[81987, 89863],
           [140726, 148602]],
    "b" : [[122981, 129478]],
    "e" : [[129478, 140726]],
    "ʒ" : [[148602, 166599]]
}
fourierAverages = {
    # sum of avg, sum of std, count
    "ð" : [0, 0, 0],
    "æ" : [0, 0, 0],
    "t" : [0, 0, 0],
    "k" : [0, 0, 0],
    "w" : [0, 0, 0],
    "ɪ" : [0, 0, 0],
    "b" : [0, 0, 0],
    "e" : [0, 0, 0],
    "ʒ" : [0, 0, 0]
}
openedFile = wv.open(file, 'rb')

T = 1.0 / openedFile.getframerate()
# Compressed or not
print(openedFile.getcompname())
# Frame rate
print(openedFile.getframerate())
# Returns number of bytes per sample
print(openedFile.getsampwidth())
# Returns total number of frames
print(openedFile.getnframes())
# Returns binary value of all frames
#openedFile.readframes(openedFile.getnframes())
# Each phonetic
lstk = []
lstae = []
for i in phonetics.keys():
    #print(i)
    # Each single array
    for j in phonetics[i]:
        #print(j)
        #print(j[1] - j[0])
        # Number of samples per phoneme
        N = 8*(j[1] - j[0])
        print(j[0], j[1])
        y = np.fromfile(file, dtype=int, count = 8*N, offset = 8*j[0])
        
        
        print(y)
        
        #               start        stop   samples
        x = np.linspace(8*float(j[0]), 8*float(j[1]), num = N, endpoint = False)
        #print(x)

        yf = fft(y)
        
        xf = fftfreq(N, T)[:N//2]
        #plt.figure()
        #plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]), label = f'Phonetic: {i}')
        fourierAverages[i][2] += 1
        fourierAverages[i][0] += np.average(2.0/N * np.abs(yf[0:N//2]))
        fourierAverages[i][1] += np.std(2.0/N * np.abs(yf[0:N//2]))
        #plt.legend()
        #plt.grid()
        #plt.title(f'Phonetics')
        #plt.ylabel('Amplitude')
        #plt.xlabel('Frequency')

#plt.show()
for i in phonetics.keys():
    fourierAverages[i][0] /= fourierAverages[i][2]
    fourierAverages[i][1] /= fourierAverages[i][2]
print(fourierAverages)

fourierFile = wv.open(testFile, 'rb')
print(fourierFile.getnframes())

fourierT = 1.0 / fourierFile.getframerate()
fourierN = 0
end = 0
start = startFrame
found = 0
while(fourierN < fourierFile.getnframes()):
    fourierN += fourierT*fourierFreq
    startFrame = endFrame
    while(endFrame < fourierFile.getnframes()):
        addedFrames = fourierFreq
        endFrame += addedFrames
        fourierN = 8*(endFrame - startFrame)
        print(fourierFile.getframerate())
        #y = np.fromfile(fourierFile, dtype=int, count = 8*N, offset = 8*startFrame)
        y = np.fromfile(testFile, dtype=int, count = 8*fourierN, offset = 8*startFrame)
        
        x = np.linspace(8*float(startFrame), 8*float(endFrame), num = fourierN, endpoint = False)
        #print(x)

        yf = fft(y)
        
        xf = fftfreq(fourierN, fourierT)[:fourierN//2]

        avg = np.average(2.0/fourierN * np.abs(yf[0:fourierN//2]))
        std = np.std(2.0/fourierN * np.abs(yf[0:fourierN//2]))
        print(endFrame)
        if((avg + averageThres >= fourierAverages[character][0] and 
            avg - averageThres <= fourierAverages[character][0]) or
            (std + stdThres >= fourierAverages[character][1] and 
            std - stdThres <= fourierAverages[character][1])):
            print('HEY YOU HAVE A MATCH STUPID')
            found = 1
            plt.plot(xf, 2.0/fourierN * np.abs(yf[0:fourierN//2]), label = f'Phonetic: {endFrame}')
            #plt.legend()
            plt.grid()
            plt.title(f'Phonetics')
            plt.ylabel('Amplitude')
            plt.xlabel('Frequency')
            if(found == 2):
                end = endFrame
            
        else:
            print('No match')
            if(found == 1):
                found = 2
                end = endFrame - fourierFreq
                plt.plot(xf, 2.0/fourierN * np.abs(yf[0:fourierN//2]), label = f'Phonetic: {endFrame}')
                #plt.legend()
                plt.grid()
                plt.title(f'Phonetics')
                plt.ylabel('Amplitude')
                plt.xlabel('Frequency')
                #plt.show()
                plt.figure()
                plt.plot(xf, 2.0/fourierN * np.abs(yf[0:fourierN//2]), label = f'Phonetic: {endFrame}')
                #plt.legend()
                plt.grid()
                plt.title(f'Phonetics')
                plt.ylabel('Amplitude')
                plt.xlabel('Frequency')
                plt.show()
                break
    break

print(f'Start: {start}, End: {end}')
#print(x)
