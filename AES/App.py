from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
from simple_aes_cipher import AESCipher, generate_secret_key


root = tk.Tk()
root.title('Cryptography')
Font = ('times', 16, 'bold')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

class Win1:

    def __init__(self, master):
        self.master = master
        self.master.geometry('580x640+10+10')
        self.img = ImageTk.PhotoImage(Image.open('icon.png').resize((580, 260)))
        self.l0 = tk.Label(self.master, text='Encryption using simple AES cipher', font=('times', 24, 'bold'), bg='blue', fg='white')
        self.l0.pack(side='top', fill='both', expand='yes')
        self.panel = tk.Label(self.master, image=self.img)
        self.panel.pack(side='top', fill='both', expand='yes')
        self.frame = tk.Frame(self.master)
        self.l1 = tk.Label(self.master, text='Protect your valuable data from hackers by voice encryption', font=('times',16,'bold'), fg='blue')
        self.l1.pack()
        self.butnew('Click to Encrypt',  Win2)
        self.butnew('Click to Decrypt',  Win3)
        self.frame.pack(expand='true')


    def butnew(self, text, _class):
        tk.Button(self.frame, text=text,command=lambda: self.new_window( _class),width=15,height=3,font=('times',14,'bold'), bg='blue',fg='black').pack(side='left',padx=15)

    def new_window(self,  _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new)


class Win2:
    def encrypts(self):
        message = self.t1.get('1.0', tk.END)
        pass_phrase= self.tkey.get()
        secret_key=generate_secret_key(pass_phrase)
        print(secret_key)
        cipher = AESCipher(secret_key)
        ciphertext = cipher.encrypt(message)

        self.t2.delete('1.0', tk.END)
        self.t2.insert('1.0', ciphertext)

    def speak(self):
            r = sr.Recognizer()
            r.pause_threshold = 0.7
            r.energy_threshold = 400

            with sr.Microphone() as source:
                try:
                    audio = r.listen(source, timeout=5)
                    message = str(r.recognize_google(audio))
                    self.t1.focus()
                    self.t1.delete('1.0', END)
                    self.t1.insert('1.0', message)

                except sr.UnknownValueError:
                    print('Google Speech Recognition could not understand audio')

                except sr.RequestError as e:
                    print('Could not request results from Google Speech Recognition Service')

                else:
                    pass
    def speak1(self):
        r = sr.Recognizer()
        r.pause_threshold = 0.7
        r.energy_threshold = 400

        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=5)
                key = str(r.recognize_google(audio))
                self.tkey.focus()
                self.tkey.delete(0, END)
                self.tkey.insert(0, key)

            except sr.UnknownValueError:
                print('Google Speech Recognition could not understand audio')

            except sr.RequestError as e:
                print('Could not request results from Google Speech Recognition Service')

            else:
                pass            
    def __init__(self, master):
        
        self.master = master
        self.master.geometry('550x500+470+150')
        self.master.title('Encrypt your data')
        self.master.configure(background='palegreen')
        self.frame = tk.Frame(self.master,borderwidth=2)
        self.l1 = tk.Label(self.master, text='Plain Text (Text to Encrypt)',font= Font,bg='palegreen', fg='red2')
        self.l1.pack(expand='yes')
        self.t1 = tk.Text(self.master, height=5, width=40, borderwidth=1,relief='solid')
        self.t1.pack(expand='yes')
        self.btnSpeak = tk.Button(self.master, fg= 'white', font= Font, width= 10, text= 'Voice', bg= 'maroon', command= self.speak)
        self.btnSpeak.pack(expand='yes')

        self.lkey = tk.Label(self.master, text='Secret key', font=Font, bg='palegreen', fg='red2')
        self.lkey.pack(expand='yes')
        self.tkey = tk.Entry(self.master, width=55, borderwidth=1, relief='solid')
        self.tkey.pack(expand='yes')
        self.btnSpeak1 = tk.Button(self.master, text='Voice', command= self.speak1, font= Font, width= 10, bg= 'maroon',  fg= 'white')
        self.btnSpeak1.pack(expand='yes')

        self.b1 = tk.Button(self.master,text='Encrypt',command=self.encrypts,font=Font,bg='maroon',fg='white',width=10)
        self.b1.pack(expand='yes')
        self.l2 = tk.Label(self.master, text='Cipher Text (Encrypted Text)', font=Font,bg='palegreen', fg='red2')
        self.l2.pack(expand='yes')
        self.t2 = tk.Text(self.master, height=8, width=40, borderwidth=1, relief='solid',state='normal')
        self.t2.pack(expand='yes')
        self.quit = tk.Button(self.frame, text='Close', command=self.close_window,font=Font,bg='maroon',fg='white',width=10)
        self.quit.pack()
        self.frame.pack(expand='true')

    def close_window(self):
        self.master.destroy()


class Win3:

    def decrypts(self):

        ciphertext = self.t1.get('1.0', tk.END)
        ciphertext = ciphertext.strip()
        pass_phrase = self.tkey.get()
        secret_key = generate_secret_key(pass_phrase)
        print(secret_key)
        cipher = AESCipher(secret_key)
        message = cipher.decrypt(ciphertext)

        self.t2.delete('1.0', tk.END)
        self.t2.insert('1.0', message)
    def speak(self):
            r = sr.Recognizer()
            r.pause_threshold = 0.7
            r.energy_threshold = 400

            with sr.Microphone() as source:
                try:
                    audio = r.listen(source, timeout=5)
                    key = str(r.recognize_google(audio))
                    self.tkey.focus()
                    self.tkey.delete(0, END)
                    self.tkey.insert(0, key)

                except sr.UnknownValueError:
                    print('Google Speech Recognition could not understand audio')

                except sr.RequestError as e:
                    print('Could not request results from Google Speech Recognition Service')

                else:
                    pass

    def __init__(self, master):
        self.master = master
        self.master.geometry('550x500+900+150')
        self.master.title('Decrypt your data')
        self.master.configure(background='yellow')
        self.frame = tk.Frame(self.master, borderwidth=2)
        self.l1 = tk.Label(self.master, text='Cipher Text (Encrypted data)', font=Font, bg='yellow',fg='blue')
        self.l1.pack(expand='yes')
        self.t1 = tk.Text(self.master, height=8, width=40, borderwidth=1, relief='solid')
        self.t1.pack(expand='yes')

        self.lkey = tk.Label(self.master, text='Secret key', font=Font, bg='yellow', fg='blue')
        self.lkey.pack(expand='yes')
        self.tkey = tk.Entry(self.master, width=55, borderwidth=1, relief='solid')
        self.tkey.pack(expand='yes')
        self.btnSpeak = tk.Button(self.master, fg= 'white', font= Font, width= 10, text= 'Voice', bg= 'blue', command= self.speak)
        self.btnSpeak.pack(expand='yes')

        self.b1 = tk.Button(self.master, text='Decrypt', command=self.decrypts, font=Font, bg='blue', fg='white', width=10)
        self.b1.pack(expand='yes')
        self.l2 = tk.Label(self.master, text='Plain Text(Original message)', font=Font, bg='yellow', fg='blue')
        self.l2.pack(expand='yes')
        self.t2 = tk.Text(self.master, height=5, width=40, borderwidth=1, relief='solid', state='normal')
        self.t2.pack(expand='yes')
        self.quit = tk.Button(self.frame, text='Close', command=self.close_window, font=Font, bg='blue', fg='white', width=10)
        self.quit.pack()
        self.frame.pack(expand='true')

    def close_window(self):
        self.master.destroy()


app = Win1(root)
root.mainloop()
