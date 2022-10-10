import PySimpleGUI as sg
from pyperclip import copy

FILE_TO_READ = 'input.txt'
NOT_EXISTING_SYMBOL = '生'
assert len(NOT_EXISTING_SYMBOL) == 1

sg.theme('Dark Purple 6')

layout = [[text_box := sg.Multiline('Theme Browser', size=(40, 10)), sg.Button('Previous'), sg.Button('Next'), sg.Exit()] ]
window = sg.Window('Translatedby helper').Layout(layout)

lines = open('input.txt').read().replace('\n\n', NOT_EXISTING_SYMBOL)
abzacs = list(lines.split(NOT_EXISTING_SYMBOL))

i = 0

def update_clipboard_and_textbox():
    if i in range(len(abzacs)):
        copy(abzacs[i])
        text_box.update(value=abzacs[i])


while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    if event == 'Previous':
        if i != 0:
            i -= 1
        update_clipboard_and_textbox()

    elif event == 'Next':
        if i != len(abzacs) - 1:
            i += 1
        update_clipboard_and_textbox()

window.Close()

# copy('123')
