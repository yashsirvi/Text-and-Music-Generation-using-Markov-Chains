import pprint

def get_chord_blocks():
    file = open('./data/chords.txt', 'r')
    Lines = file.readlines()
    count=0
    chord_blocks={}
    for line in Lines:
        if(line!="\n"):
            count+=1
            chords=line.split()
            for i in range(len(chords)):
                if chords[i] in chord_blocks:
                    chord_blocks[chords[i%len(chords)]].append(chords[(i+1)%len(chords)])
                else:
                    chord_blocks[chords[i%len(chords)]]=[chords[(i+1)%len(chords)]]
    return chord_blocks

block=get_chord_blocks()

pp=pprint.PrettyPrinter()
pp.pprint(block)