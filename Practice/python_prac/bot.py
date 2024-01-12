import os
import time
import pyautogui
import pyperclip

def open_vscode():
    pyautogui.click(x=100, y=100) 
    time.sleep(5)  

def create_markdown_file(file_name):
    pyautogui.hotkey('ctrl', 'n')  
    time.sleep(2)
    pyautogui.write(file_name)
    pyautogui.press('enter')
    time.sleep(2)

def write_code_to_file(code):
    pyperclip.copy(code)
    pyautogui.hotkey('ctrl', 'v')  
    time.sleep(2)

def save_file():
    pyautogui.hotkey('ctrl', 's')  
    time.sleep(2)

def run_code():
    pyautogui.hotkey('f5')
    time.sleep(5)

if __name__ == "__main__":
    open_vscode()

    create_markdown_file('try.js')


    random_code = """
    console.log('Hello World!');
    function add(a, b) {
        return a + b;
    }
    console.log(add(1, 2));

    function subtract(a, b) {
        return a - b;
    }
    console.log(subtract(1, 2));
    
    function multiply(a, b) {
        return a * b;
    }
    console.log(multiply(1, 2));

    function divide(a, b) {
        return a / b;
    }
    console.log(divide(1, 2)); 
    """

    write_code_to_file(random_code)
    save_file()
    run_code()