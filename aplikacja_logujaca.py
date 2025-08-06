# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 12:27:48 2025

@author: jakub
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

class BazaUzytkownikow():
    
    def __init__(self, db_name = 'users_db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()
        
    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
                  CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL
                      )
                  ''')
        self.conn.commit()
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def dodaj_uzytkownika(self, username, password):
        c = self.conn.cursor()
        try:
            haslo_hash = self.hash_password(password)
            c.execute('''
                      INSERT INTO users (username, password) VALUES (?, ?)
                      ''', (username, haslo_hash))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        
    def sprawdz_uzytkownika(self, username, password):
        c = self.conn.cursor()
        haslo_hash = self.hash_password(password)
        c.execute('''
                  SELECT * FROM users WHERE username = ? AND password = ?
                  ''', (username, haslo_hash))
        return c.fetchone() is not None
    
    def zamknij_polaczenie(self):
        self.conn.close()
        
class AplikacjaLogujaca():
    
    def __init__(self, master):
        self.master = master
        self.baza = BazaUzytkownikow()
        master.title('Logowanie')
        
        self.frame_login = tk.Frame(master)
        self.frame_register = tk.Frame(master)
        
        self.create_login_widgets()
        self.create_register_widgets()

        self.frame_login.grid(row = 0, column = 0, sticky = 'nsew')      
        
    def create_login_widgets(self):
        self.label_username = tk.Label(self.frame_login, text = 'Login:')
        self.label_username.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.entry_username = tk.Entry(self.frame_login)
        self.entry_username.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self.label_password = tk.Label(self.frame_login, text = 'Hasło:')
        self.label_password.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.entry_password = tk.Entry(self.frame_login, show = '*')
        self.entry_password.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        self.loggin_b = tk.Button(self.frame_login, text = 'Zaloguj', command = self.login)
        self.loggin_b.grid(row = 2, column = 0, columnspan = 2, pady = 10)
        
        self.to_register_b = tk.Button(self.frame_login, text = 'Zarejestruj sie', command = self.show_register)
        self.to_register_b.grid(row = 3, column = 0, columnspan = 2, pady = 5)
    
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if not username or not password:
            messagebox.showerror('Błąd', 'Proszę wypełnić wszystkie pola.')
            return
        if self.baza.sprawdz_uzytkownika(username, password):
            messagebox.showinfo('Info', f'Użytkownik {username} zalogowany!')
        else:
            messagebox.showerror('Bład', f'Błąd nieprawidłowy login lub hasło!')
    
    def show_register(self):
        self.frame_login.grid_forget()
        self.frame_register.grid(row = 0, column = 0, sticky = 'nsew')
        
    def create_register_widgets(self):
        self.reg_label_username = tk.Label(self.frame_register, text = 'Login:')
        self.reg_label_username.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.reg_entry_username = tk.Entry(self.frame_register)
        self.reg_entry_username.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self.reg_label_password = tk.Label(self.frame_register, text = 'Hasło:')
        self.reg_label_password.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.reg_entry_password = tk.Entry(self.frame_register, show = '*')
        self.reg_entry_password.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        self.reg_label_password2 = tk.Label(self.frame_register, text = 'Powtórz hasło:')
        self.reg_label_password2.grid(row = 2, column = 0)
        
        self.reg_entry_password2 = tk.Entry(self.frame_register, show = '*')
        self.reg_entry_password2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        self.register_b = tk.Button(self.frame_register, text = 'Zarejestruj', command = self.register)
        self.register_b.grid(row = 3, column = 0, columnspan = 2, pady = 10)
        
        self.to_login_b = tk.Button(self.frame_register, text = 'Zaloguj sie', command = self.show_login)
        self.to_login_b.grid(row = 4, column = 0, columnspan = 2, pady = 5)
        
    def register(self):
        username = self.reg_entry_username.get()
        password = self.reg_entry_password.get()
        password2 = self.reg_entry_password2.get()
        if not username or not password or not password2:
            messagebox.showerror('Błąd', 'Proszę wypełnić wszystkie pola.')
            return
        if password != password2:
            self.reg_entry_password.delete(0, tk.END)
            self.reg_entry_password2.delete(0, tk.END)
            messagebox.showerror('Bład', f'Hasła nie sa identyczne!!!')
        else:    
            if self.baza.dodaj_uzytkownika(username, password):
                messagebox.showinfo('Info', f'Utworzono konto dla {username}!')
                self.reg_entry_username.delete(0, tk.END)
                self.reg_entry_password.delete(0, tk.END)
                self.reg_entry_password2.delete(0, tk.END)
                self.show_login()
            else:
                messagebox.showerror('Błąd', 'Użytkownik już istnieje!')
       
    def show_login(self):
        self.frame_register.grid_forget()
        self.frame_login.grid(row = 0, column = 0, sticky = 'nsew')

    def on_closing(self):
        self.baza.zamknij_polaczenie()
        self.master.destroy()
    
if __name__ == '__main__':
    root = tk.Tk()
    log = AplikacjaLogujaca(root)
    root.protocol("WM_DELETE_WINDOW", log.on_closing)
    root.mainloop()