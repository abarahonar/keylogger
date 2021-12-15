# keylogger
A Python Keylogger, saving the timestamp, the pressed key and the event.

(1) Clone the git repository.

(2) Preferably create a virtual environment with Python 3. Then run 

```
pip install -r requirements.txt
```

to install all packages. 

(3) Then simply start the keylogger with the following command:

```
./keylogger start process output
```

The keylogger will run as a background process with the name `process` and store the output in the specified 
`output` file. Each event is registered as a CSV entry with the following form: _timestamp,type,key_. The _type_ can be 
either __RELEASE__ or __PRESS__.
