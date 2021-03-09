from pytube import YouTube
import os 
import PySimpleGUI as sg
from notifypy import Notify

notification = Notify()
notification.title = 'YouTube to mp3'

# choosing the new theme
my_new_theme = {'BACKGROUND': '#ffab91',
                'TEXT': 'black',
                'INPUT': 'white',
                'TEXT_INPUT': 'black',
                'SCROLL': '#c7e78b',
                'BUTTON': ('black', '#ff7043'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

sg.theme_add_new('MyNewTheme', my_new_theme)
sg.theme('My New Theme')

# creating layout for window
layout = [  [sg.Text("Please insert a valid video URL", font = 14)],
            [sg.InputText(size = (73,1))],
            [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
            [sg.Text("\t\t\t     "), sg.Button("Convert to mp3", font = "bold")]]

window = sg.Window('YouTube to mp3', layout)

while True:
    event, values = window.read()
    try:
        if event == sg.WIN_CLOSED:
            break
        if event == 'Convert to mp3':
            yt = YouTube(values[0])
            video = yt.streams.filter(only_audio=True).first() 

            destination = values[1]
            out_file = video.download(output_path=destination)

            base, ext = os.path.splitext(out_file) 
            new_file = base + '.mp3'
            os.rename(out_file, new_file) 
            os.remove(out_file)    
            
            window.close()

    except:
        print(yt.title + " has been successfully downloaded.")
        break
    

# sending notification
notification.message = yt.title + " has been successfully downloaded."
notification.send()

