#pip install googletrans

from tkinter import *
from tkinter import ttk
#Translator, LANGUAGES
from googletrans import 

root = Tk()
root.geometry('1080x400')
root.config(bg = '#F2CCC3')
root.title("Language Translator")

#LANGUAGES.values()
language = list()
title_label = Label(root, text = "LANGUAGE TRANSLATOR", bg='#F2CCC3',font=("Sylfaen",18,"bold","italic"))
title_label.place(relx=0.5,rely=0.1, anchor=CENTER)


input_label = Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='#F2CCC3')
input_label.place(relx=0.02,rely=0.2, anchor=W)
#values= language
src_lang = ttk.Combobox(root, , width =22, state="readonly")
src_lang.place(relx=0.13,rely=0.2, anchor=W)
src_lang.set('english')


output_label = Label(root,text ="Output", font = 'arial 13 bold', bg ='#F2CCC3')
output_label.place(relx=0.81,rely=0.2, anchor=E)
#values= language
dest_lang = ttk.Combobox(root, , width =22, state="readonly")
dest_lang.place(relx=0.98,rely=0.2, anchor=E)
dest_lang.set('choose output language')

Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60, bg="#FFFCF9", bd=0)
Input_text.place(relx=0.02,rely=0.5, anchor=W)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60, bg="#FFFCF9", bd=0)
Output_text.place(relx=0.98,rely=0.5, anchor=E)

def Translate():
    translator = Translator()
    try:
        #src_lang.get() dest_lang.get()
        translated=translator.translate(text= Input_text.get(1.0, END) , src = , dest = )
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
    except:
        print("Try again")

    #Translate
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command =  , bg = '#E78F8E', activebackground = '#95A3A4',relief = FLAT)
trans_btn.place(relx=0.5,rely=0.85, anchor=CENTER )
footer_label = Label(root,text ="Created by whitehatjr team", font = 'arial 10 italic', bg ='#F2CCC3')
footer_label.place(relx=0.5,rely=0.97, anchor=CENTER)
root.mainloop()    
