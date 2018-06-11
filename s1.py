def Censor(text, word):
    Text = text + " "
    Word = word + " "
    Trans = ""
    Censor = ""

    for q in range(len(Word)-1):
        Censor += "*"

    i = 0
    while (i < len(Text)):

        ini = i
        i1 = 0

        for o in range(i, len(Text)):
            if (Text[o] == Word[i1]):

                i1 += 1
                if (i1 == len(Word)):
                    #print(Text[i:(i+len(Word)-1)])
                    Trans += Censor
                    i += len(Word)-1
                    break

            else:
                out = 0
                for o1 in range(o, len(Text)):
                    if Text[o1] == " ":
                        i = o1 + 1
                        if (o1 == len(Text)-1):
                            Trans += Text[ini:i-1]
                        else:
                            Trans += Text[ini:i]
                        break
                    out = o1

                else:
                    i = out
                #print(i)
                break

        else:
            i = len(Text)
            Trans += Text[ini:i]

    return Trans

print(Censor('heya he hey hey', 'hey'))
