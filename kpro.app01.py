import streamlit as st
import PySimpleGUI as sg
from datetime import datetime
import tkinter

st.header('K-Project 打刻アプリ')

sg.theme('DarkGreen5')

choices = ('織田信長', '豊臣秀吉', '徳川家康', '武田信玄', '上杉謙信', '川村兼康')

gs = 0
fs = 24

layout = [
        [sg.Text('デジタル時計')],
        [sg.Text('00:00:00', key='clock', font=('Helvetica', 72))],
    
        [sg.Button("出勤",size=(gs),font=('MS UI Gothic', fs),key="出勤"),
        sg.Button("退勤",size=(gs),font=('MS UI Gothic', fs),key="退勤"),
        sg.Button("休憩",size=(gs),font=('MS UI Gothic', fs),key="休憩")],
               
        [sg.Listbox(choices, size=(gs, len(choices)),font=('MS UI Gothic', fs), key='社員名')],
        
        [sg.Text("ファイル"),sg.InputText(),sg.FileBrowse(key="file")],[sg.Submit()]]

win = sg.Window('時計', layout)

#------------------------------------------------------------------------------------------------------
while True:
    event, val = win.read(timeout=100)
    if event in ('Exit', 'Quit', None):
        break
    
    s = datetime.now().strftime('%H:%M:%S')
    win['clock'].update(s)

win.close()


 
