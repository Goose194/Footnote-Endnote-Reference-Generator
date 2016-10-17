#from tkinter import font
#import tkinter as tk
#root = tk.Tk()
#italicised = tkFont.Font(slant='italic')

def optionlist():
    #determines type of source
    global option
    option = input("Is your reference from a:\n1. book \
        \n2. chapter \
	\n3. journal article \
	\n4. lecture\n5. a document or publication produced by a Government, International Organisation, Corporation or NGO\n6. an article in a newspaper or magazine \
	\n7. a television or radio broadcast \
	\n8. a website/blog/twitter \
	\n9. online e-book \
	\n10. material accessed by an e-reader \
	\n11. secondary referencing \
	\nType the corresponding number to select.")

def authorchecker():
    #informs user of correct reference syntax for name
    if option in ['1','2','3','4','6','8','9','10','11']:
        global authorname
        authorname = input("Type the author's name in the following manner: Waltz, K. ")

    elif option in ['5','7']:
        global authorname2
        authorname2 = input("Type the publisher's/tv program's/radio station's/Government's name ")

    else:
        print("Type a number corresponding to one of the values 1 - 11.")
        optionlist()
        authorchecker()

def titlechecker():
    #informs user of correct reference syntax for title
    if option in ['2','3','4','5','6','8']:
        global titlename
        titlename = input("Type the title in the following manner: 'The Agent-Structure Problem in International Relations Theory' ")

    elif option in ['1','9']:
        global titlename2
        titlename2 = input("Type the title in the following manner: Theory of International Politics, but in ITALICS. ")

    else:
        print("Type a number corresponding to one of the values 1 - 11.")
        optionlist()
        titlechecker()

def secondtitlechecker():
    #informs user of correct syntax for booktitle
    if option in ['2','3','6']:
        global secondtitle
        secondtitle = input("Type the book's title in the following manner: International Organisation, but in ITALICS. ")

def editorchecker():
    #informs user of correct syntax for edited volume
    if option in ['2']:
        global editor
        editor = input("Type the editor's name. ")

def publishdetailchecker():
    #informs the user of correct syntax for publishing information
    if option in ['1','2','5','9']:
        global publishdet
        publishdet = input("Type the publisher information in the following manner: (Cambridge, Cambridge University Press, 1999) ")
        
def journalnumberchecker():
    #informs the user of the correct syntax for journal volume number
    if option in ['3']:
        global volumeno
        volumeno = input("Type the number of the journal volume. ")

def pagenumberchecker():
    #informs the user of the correct syntax for pagenumber
    if option in ['1','2','3','5','6','9']:
        global pagenumber
        pagenumber = input("Type the page number in the following manner: p.46 ")
    
def datechecker():
    #informs the user of the correct syntax for the date
    if option in ['4','6','7','8','10']:
        global date
        date = input("Type the date in the following manner: 20 August 2010 ")

                              
print("Welcome to the reference automator v 0.1")

optionlist()
authorchecker()
titlechecker()
secondtitlechecker()
editorchecker()
publishdetailchecker()
journalnumberchecker()
pagenumberchecker()
datechecker()

if option in ['1']:
    print(authorname , titlename2 , publishdet + "," + pagenumber + ".")

if option in ['2']:
    print(authorname , titlename + " in " + secondtitle + " edited by " + editor , publishdet + "," + pagenumber + ".")








