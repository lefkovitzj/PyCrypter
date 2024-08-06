# PyCrypter
PyCrypter is a light-weight alternative to my <a href="https://github.com/lefkovitzj/PyPersonalVault/">PyPersonalVault project</a>. Designed to be started from the command line with or without arguments, this project performs fast AES encryption and decryption of files with a string password. 

The graphical user interface (GUI) used to show progress is built with CustomTkinter (pip install customtkinter). Cryptographic algorithms are sourced from the AES and PBKDF2 portions of the PyCryptodome package (pip install pycryptodomex), and various Python Standard Library modules are used throughout. Many thanks to the developers of and contributors to these excellent tools!

Currently on version 1.0.0, PyCrypter allows encryption or decryption using AES with a salted password. Multiple files can be selected for encryption or decryption in one run of the program, and each will generate a file with the same name (".bin" is added for encrypted files) as the original.

The necessary files to run PyPersonalVault are:
<ul> 
  <li>app.py </li>
  <li>utils.py</li>
  <li>encryption_utils.py</li>
</ul>

All files are necessary for the project to run core functionality. Run the project by executing the app.py file in the command line, IDE, or any other method to run a Python file.

When launched from the command line, there are optional arguments for the mode (-e or -d) and password (any valid string). If these are not provided, user input will be gathered from the console.

The following dependencies must be installed in order for the application to run:
<ul>
  <li><a href="https://pycryptodome.readthedocs.io/en/latest/src/installation.html" style="text-decoration:none"> PyCryptodome </a> - pip install pycryptodomex</li>
  <li><a href="https://customtkinter.tomschimansky.com/documentation/" style="text-decoration:none"> CustomTkinter </a> - pip install customtkinter</li>
</ul>

Feel free to reach out to me with ideas, questions, or other comments regarding this project by opening an Issue or by email at <a href="mailto:flaskdoggo@gmail.com" style="text-decoration:none">flaskdoggo@gmail.com</a>!
