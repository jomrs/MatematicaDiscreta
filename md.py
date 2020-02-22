import math

d1 = "Daytrip took it to 10 (hey) Oh, here we go, please let me know Off we go, dont leave me in the cold If I take you everywhere, then well, you wouldnt know how to walk If I spoke on your behalf, then well, you wouldnt know how to talk If I gave you everything and everything is what I bought I can take it all back, I never cared bout what you though"
d2 = "I got room in my fume She fill my mind up with ideas Im the highest in the room (its lit) Hope I make it outta here (lets go!)"
d3 = "I get those goosebumps every time Yeah, you come around, yeah You ease my mind, you make everything feel fine Worry about those comments Im way too numb, yeah, it's way too dumb, yeah I get those goosebumps every time, I need the Heimlich Throw that to the side, yeah I get those goosebumps every time Yeah, when youre not around When you throw that to the side, yeah I get those goosebumps every time, yeah"
d4 = "Sun is down, freezin' cold Thats how we already know winters here My dawg would prolly do it for a Louis belt Thats just all he know, he dont know nothin else I tried to show em Yeah I tried to show em Yeah, yeah Yeah, yeah, yeah Gone on you with the pick and roll Young LaFlame, he in sicko mode"

bow_d1 = d1.split(" ")
bow_d2 = d2.split(" ")
bow_d3 = d3.split(" ")
bow_d4 = d4.split(" ")

unique_words = set(bow_d1).union(set(bow_d2)).union(set(bow_d3)).union(set(bow_d4))

tc_d1 = dict.fromkeys(unique_words, 0)
for w in bow_d1:
    tc_d1[w] += 1

tc_d2 = dict.fromkeys(unique_words, 0)
for w in bow_d2:
    tc_d2[w] += 1

tc_d3 = dict.fromkeys(unique_words, 0)
for w in bow_d3:
    tc_d3[w] += 1

tc_d4 = dict.fromkeys(unique_words, 0)
for w in bow_d4:
    tc_d4[w] += 1

tf_d1 = {}
total = float(len(bow_d1))
for w, c in tc_d1.items():
    tf_d1[w] = c / total

tf_d2 = {}
total = float(len(bow_d2))
for w, c in tc_d2.items():
    tf_d2[w] = c / total

tf_d3 = {}
total = float(len(bow_d3))
for w, c in tc_d3.items():
    tf_d3[w] = c / total

tf_d4 = {}
total = float(len(bow_d4))
for w, c in tc_d4.items():
    tf_d4[w] = c / total

#print(tf_d2)

documents = [tc_d1, tc_d2, tc_d3, tc_d4]
N = len(documents)
idf = dict.fromkeys(unique_words, 0)
for d in documents:
    for w, c in d.items():
        if c > 0:
            idf[w] += 1
for w,c in idf.items():
    idf[w] = math.log(N / float(c))


tf_idf_d1 = {}
for w, c in tf_d1.items():
    tf_idf_d1[w] = c * idf[w]

tf_idf_d2 = {}
for w, c in tf_d2.items():
    tf_idf_d2[w] = c * idf[w]

tf_idf_d3 = {}
for w, c in tf_d3.items():
    tf_idf_d3[w] = c * idf[w]

tf_idf_d4 = {}
for w, c in tf_d4.items():
    tf_idf_d4[w] = c * idf[w]

# distância entre d1 e d2
ds = []
for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d2[w]
    ds.append(dif * dif)
soma = 0
for i in ds:
    soma += i
dist_d1_d2 = math.sqrt(soma)

ds = []
for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d3[w]
    ds.append(dif * dif)
soma = 0
for i in ds:
    soma += i
dist_d1_d3 = math.sqrt(soma)

ds = []
for w in unique_words:
    dif = tf_idf_d1[w] - tf_idf_d4[w]
    ds.append(dif * dif)
soma = 0
for i in ds:
    soma += i
dist_d1_d4 = math.sqrt(soma)

ds = []
for w in unique_words:
    dif = tf_idf_d2[w] - tf_idf_d3[w]
    ds.append(dif * dif)
soma = 0
for i in ds:
    soma += i
dist_d2_d3 = math.sqrt(soma)

ds = []
for w in unique_words:
    dif = tf_idf_d2[w] - tf_idf_d4[w]
    ds.append(dif * dif)
soma = 0
for i in ds:
    soma += i
dist_d2_d4 = math.sqrt(soma)

ds = []
for w in unique_words:
    dif = tf_idf_d3[w] - tf_idf_d4[w]
    ds.append(dif * dif)
soma = 0
for i in ds:
    soma += i
dist_d3_d4 = math.sqrt(soma)

print(dist_d1_d2)
print(dist_d1_d3)
print(dist_d1_d4)
print(dist_d2_d3)
print(dist_d2_d4)
print(dist_d3_d4)