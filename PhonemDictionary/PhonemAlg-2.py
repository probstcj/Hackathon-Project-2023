




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
#CHECK IF ITS DOUBLE, IF NOT JUST KEEP IT AS HOW IT IS.
for i in phonTestList.split(' '):
    for j in range(len(i)):
        string = ''
        if  i[j] =='i' and i[j+1]==":" :    
         string = "i:"  
        newList.append(string)
        if  i[j] =='ɪ' and i[j+1]=="ɹ" :    
         string = "ɪe"  
        newList.append(string)
        if i[j] == 'e'  and i[j+1] == 'ɪ':
         string = "eɪ"
         newList.append(string)     
        if i[j] == 'u'  and i[j+1] == ':':
         string = "u:"
         newList.append(string) 
        if i[j] == 'ɜ'  and i[j+1] == ':':
         string = "ɜ:"
         newList.append(string)
        if i[j] == 'o'  and i[j+1] == 'ː':
         string = "ɔ:"
         newList.append(string)
        if i[j] == 'ʊ'  and i[j+1] == 'ɹ':
         string = "ʊɚ"
         newList.append(string) 
        if i[j] == 'ɔ'  and i[j+1] == 'ɪ':
         string = "ɔɪ"
         newList.append(string)
        if i[j] == 'o'  and i[j+1] == 'ʊ':
         string = "ɚʊ"
         newList.append(string)     
        
         
         

print(newList)
