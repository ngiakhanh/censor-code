def Censor(text, words):
    Text = text + " "
    Trans = ""

    Words = []
    for x in words:
        Words.append((x + " ").lower())

    Masks = []
    for x in words:
        Masks.append(("*") * len(x))

    i = 0
    while (i < len(Text)):

        ini = i
        i0 = 0
        i1 = 0
        #Check the next word in Text with all list of words in Words 
        while (i0 < len(Words)):
            o = i

            while (o < len(Text)):
                if (Text[o].lower() == Words[i0][i1]):
                    #Checking maybe ...
                    i1 += 1
                    o += 1

                    #If found: censor the word, add "*" to Trans and let i jump to the next one 
                    if (i1 == len(Words[i0])):
                        #print(Text[i:(i+len(Words[i0])-1)])
                        Trans += Masks[i0]
                        i += len(Words[i0])-1
                        break

                else:
                    #If found: censor the word, add "*" to Trans and let i jump to the next one 
                    if (i1 == len(Words[i0])-1 and Text[o].lower().isalpha() == False):
                        #print(Text[i:(i+len(Words[i0])-1)])
                        Trans += Masks[i0] + Text[o]
                        i += len(Words[i0])
                        break

                    #If not found
                    else:
                        #If we have checked all the words in Words or Text[o] = " ", "\n" or not a character
                        if (i0 == len(Words)-1 or Text[o] == " " or Text[o] == "\n" or Text[o].lower().isalpha() == False): 
                            #Find the next position of " " or "\n" or a character, let i jump to the position after them and add to Trans the uncensored(original) word
                            for o1 in range(o, len(Text)):
                                #If the next position is found
                                if (Text[o1] == " " or Text[o1] == "\n" or Text[o1].lower().isalpha() == False):
                                    i = o1 + 1
                                    #If o1 is the last character in Text, don't include it to trans
                                    if (o1 == len(Text)-1):
                                        Trans += Text[ini:i-1]
                                        break
                                    elif (Text[o1+1].lower().isalpha() == True):
                                        Trans += Text[ini:i]
                                        break

                            break
                        #If we haven't yet done checking, keep checking: jump to the next word in Words with the first character and restart to check the first character of the word being checked
                        else:
                            i0 += 1
                            i1 = 0
                            o = i

            #Done checking without finding: let i jump to the next word and add to Trans the uncensored(original) word
            else:
                i = len(Text)
                Trans += Text[ini:i]

            break
    return Trans

print(Censor('.kh.Long .Hai..\nLonga Khan Hai@', ['hEy','Khanh','Long','Hai'])) 
