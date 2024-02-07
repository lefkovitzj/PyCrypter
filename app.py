"""
    Author: AaronTook (https://AaronTook.github.io)
    Version: 1.0.0
    Version Launch Date: 2/6/2024
    File Last Modified: 2/6/2024
    Project Name: PyCrypter
    File Name: app.py
"""

# Python Standard Library Imports
import sys
import threading
# Third-party Module Imports
import customtkinter
# Project Imports
from utils import gui_get_files
from encryption_utils import encrypt_file, decrypt_file

alive_threads = dict()

class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()
    def stop(self):
        self._stop_event.set()
    def is_stopped(self):
        return self._stop_event.is_set()

def start_encrypt_thread(password, file_paths=[], alive_threads=alive_threads, thread_name = 'encrypt'):
    alive_threads[thread_name] = StoppableThread(target = encrypt_thread_process, args=(password, file_paths, alive_threads,thread_name))
    alive_threads[thread_name].start()
def stop_encrypt_thread(alive_threads=alive_threads, thread_name = 'encrypt'):
    try:
        alive_threads[thread_name].stop()
    except:
        pass
def start_decrypt_thread(password, file_paths=[], alive_threads=alive_threads, thread_name = 'decrypt'):
    alive_threads[thread_name] = StoppableThread(target = decrypt_thread_process, args=(password, file_paths, alive_threads,thread_name))
    alive_threads[thread_name].start()  
def stop_decrypt_thread(alive_threads=alive_threads, thread_name = 'decrypt'):
    try:
        alive_threads[thread_name].stop()
    except:
        pass
    
def encrypt_thread_process(password, file_paths=[], alive_threads=alive_threads, thread_name = 'encrypt'):
    # Disable start button.
    start_button.configure(state="disabled")
    root.update_idletasks()
    # Encrypt the files.
    num_file_paths = len(file_paths)
    encrypted_files = 0
    for i in range(num_file_paths):
        if (alive_threads[thread_name].is_stopped()):
            break
        file_path = file_paths[i]
        active_file_label.configure(text=f"Encrypting file: {file_path}")
        encrypt_file(file_path, password)
        encrypted_files += 1
        progress.set((i+1) * (1/num_file_paths))
        root.update_idletasks()
    # Disable stop button.
    stop_button.configure(state="disabled")
    active_file_label.configure(text=f"Encryption finished for {encrypted_files} of {num_file_paths} files...")
    root.update_idletasks()
    alive_threads.pop(thread_name)
def decrypt_thread_process(password, file_paths=[], alive_threads=alive_threads, thread_name = 'decrypt'):
    # Disable start button.
    start_button.configure(state="disabled")
    root.update_idletasks()
    # Encrypt the files.
    num_file_paths = len(file_paths)
    decrypted_files = 0
    for i in range(num_file_paths):
        if (alive_threads[thread_name].is_stopped()):
            break
        file_path = file_paths[i]
        active_file_label.configure(text=f"Decrypting file: {file_path}")
        decrypt_file(file_path, password)
        decrypted_files += 1
        progress.set((i+1) * (1/num_file_paths))
        root.update_idletasks()
    # Disable stop button.
    stop_button.configure(state="disabled")
    active_file_label.configure(text=f"Decryption finished for {decrypted_files} of {num_file_paths} files...")
    root.update_idletasks()
    alive_threads.pop(thread_name)

# Launch program with the format: python source_file_location.py (-e/-d) password
try:
    if len(sys.argv) == 3:
        mode = sys.argv[1]
        password = sys.argv[2]
    else:
        mode = input("Enter mode (-e or -d): ")
        password = input("Enter password (No Spaces): ")
    mode_base_text = ""
    mode_command = None
    source_file_loc = sys.argv[0]
    if mode.lower() == "-d":
        mode_base_text = "Decrypt"
        mode_command = start_decrypt_thread
        stop_command = stop_decrypt_thread
    elif mode.lower() == "-e":
        mode_base_text = "Encrypt"
        mode_command = start_encrypt_thread
        stop_command = stop_encrypt_thread
    else: 
        print("Invalid mode selected.")
    
    files_selected_full, files_selected_partial = gui_get_files()
    if len(files_selected_full) > 0 and mode_base_text != "":
        root = customtkinter.CTk()
        root.title(f"Folder {mode_base_text}ion Progress")
        progress = customtkinter.CTkProgressBar(root, orientation = 'horizontal', width=300, height=20, corner_radius = 0, border_color = "white", border_width=1, mode = 'determinate') 
        progress.grid(columnspan=2, row=0, column=0, pady = 20, padx=20) 
        progress.set(0)
        active_file_label = customtkinter.CTkLabel(root, text=f"{mode_base_text}ing File: ", anchor="nw", width=300, height=100, justify="left", wraplength=300)
        active_file_label.grid(columnspan=2, row=1, column=0)
        
        # This button will start the progress bar.
        start_button = customtkinter.CTkButton(root, text = 'Start', command = lambda: mode_command(password, files_selected_full))
        start_button.grid(row=2, column=0, pady = 10) 
        # This button will stop the progress bar 
        stop_button = customtkinter.CTkButton(root, text = 'Cancel', command = stop_command)
        stop_button.grid(row=2, column=1, pady = 10) 
        root.mainloop()
except IndexError:
    print("Command format invalid! Must be formatted as follows:\npython source_file_location.py (-e/-d) password")

        
    