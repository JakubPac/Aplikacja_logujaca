# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 12:27:48 2025

@author: jakub
"""

import tkinter as tk
from tkinter import messagebox

class AplikacjaLogujaca():
    
    def __init__(self, master):
        self.master = master
        master.title('Logowanie')
        
        self.label_username = tk.Label(master, text = 'Login:')
        self.label_username.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self.label_password = tk.Label(master, text = 'Hasło:')
        self.label_password.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.entry_password = tk.Entry(master)
        self.entry_password.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        self.loggin_b = tk.Button(master, text = 'Zaloguj', command = self. login)
        self.loggin_b.grid(row = 2, column = 0, columnspan = 2, pady = 10)
        
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        messagebox.showinfo('Info', f'Kliknąłe')