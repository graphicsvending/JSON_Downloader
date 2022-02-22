import requests
import PySimpleGUI as sg
import json


flag = 0

jsonfilepath = ""
json_url_1 = ""
 

#sg.theme('Black')
layout = [    
    [sg.Text(' '  * 100)], 
    [sg.Text('JSON URL:', size=(8,1)), sg.InputText(json_url_1, size=(70,1), key='-InputText_URL-')],
    [sg.Text(' '  * 100)], 

    [sg.Frame(layout=[ 
        #[sg.Text('File Folder', size=(13, 1), auto_size_text=False, justification='left'), sg.InputText(I_IMG_PATH, size=(53,1), key='-InputText_1-'), sg.FolderBrowse()],
        [sg.InputText('', size=(65,1), key='-JsonFilePath-'), sg.FileSaveAs('File Path', size=(10,2), file_types=(('Json Files', '*.json'),),)]],
        #[sg.InputText(I_TARGET_FILE, size=(53,1), key='-InputText_2-', visible=False)]],
    title='',title_color='white')],  

    [sg.Text(' '  * 100)],

    [sg.Multiline('JSON will be shown here!', size=(79, 6), key='-MultilineText_1-')],
    # [sg.InputText('', size=(65,1), key='-JsonFilePath-'), sg.FileSaveAs('File Path', file_types=(('Json Files', '*.json'),),)],
   
      
    [sg.Text('_'  * 82, justification='center')], 
    [sg.Text(' '  * 100)],
    [sg.Button('Download', size=(15, 2), disabled=True), sg.Text(' '  * 73), sg.Quit(size=(15, 2))],
    [sg.Text(' '  * 100)]    
]     

# Create the window
window = sg.Window('JSON Downloader V 1.0', layout, default_element_size=(40, 1), grab_anywhere=False) 




while True:

    #------------------------------------------------------------------------------------------------#

    event, values = window.read(timeout=0)
    
    if event == 'Quit' or event == sg.WIN_CLOSED:
        break  
    
    #------------------------------------------------------------------------------------------------#

    if str(values['-InputText_URL-']) != "":
        if str(values['-JsonFilePath-']) != "":
            window['Download'].update(disabled=False)
            if event == 'Download':
                
                json_url_1 = str(values['-InputText_URL-'])
                
                jsonfilepath = str(values['-JsonFilePath-'])
                
                flag = 1


    if flag == 1:
        

        #download Json file
        myfile = requests.get(json_url_1, allow_redirects=True)
        open(jsonfilepath,'wb').write(myfile.content)

        f = open(jsonfilepath)
        data = json.load(f)

        window['-MultilineText_1-'].update(value = str(data))
        f.close()

        sg.popup_ok('Udated Successfully!')
        flag = 0
        # window['Save Calibration'].update(disabled=True)



window.close()
#------------------------------------------------------------------------------------------------#