def Censor(text, word):
    Text = text + " "
    Word = (word + " ").lower()
    Trans = ""
    Censor = ""

    for q in range(len(word)):
        Censor += "*"

    i = 0
    while (i < len(Text)):

        ini = i
        i1 = 0

        for o in range(i, len(Text)):
            if (Text[o].lower() == Word[i1]):

                i1 += 1
                if (i1 == len(Word)):
                    #print(Text[i:(i+len(Word)-1)])
                    Trans += Censor
                    i += len(Word)-1
                    break

            else:
                for o1 in range(o, len(Text)):
                    if Text[o1] == " " or Text[o1] == "\n":
                        i = o1 + 1
                        if (o1 == len(Text)-1):
                            Trans += Text[ini:i-1]
                        else:
                            Trans += Text[ini:i]
                        break

                break

        else:
            i = len(Text)
            Trans += Text[ini:i]

    return Trans

print(Censor('hey. he heya Hey \nHey he', 'hEy'))
