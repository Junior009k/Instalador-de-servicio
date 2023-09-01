def show_frame(frame1,frame2):
    frame1.pack_forget()
    frame2.pack()

def show_Configuration(frame1,frame2,frame3,frameC):
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frameC.pack()

def fixWord(word):
    print(word.split("'",2))
    p="'"
    if("('" in word):
        print(f"arreglamos la palabra {word.split(p,2)[1]}")
        return word.split(p,2)[1]
    return word
fixWord("Azul")
fixWord("('Azul')")