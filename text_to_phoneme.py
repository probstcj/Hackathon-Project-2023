from phonemizer import phonemize

text = ["That quick beige fox jumped in the air over each thin dog, Look out, I shout, for he's foiled you again, creating chaos."]

phonemized = phonemize(text, language='en-us', backend='espeak')
print(phonemized)