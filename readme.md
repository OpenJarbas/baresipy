# Baresipy

A python wrapper around baresip

Make voip calls/bots from python!

# install

```bash
sudo apt-get install baresip
sudo apt-get install ffmpeg
pip install baresipy
```

# usage

scripted calls

```python
from baresipy import BareSIP
from time import sleep

to = "jarbas_laptop@sipx.mattkeys.net"

gateway = "sipx.xxxxx.net"
user = "xxxxx"
pswd = "xxxxxx"

b = BareSIP(user, pswd, gateway)

b.call(to)

while b.running:
    sleep(0.5)
    if b.call_established:
        b.send_dtmf("123")
        b.speak("this is jarbas personal assistant speaking. this was a test")
        b.speak("Goodbye")
        b.hang()
        b.quit()

```


handling events

```python
from baresipy import BareSIP
from time import sleep
from pyjokes import get_joke


class JokeBOT(BareSIP):
    def handle_incoming_call(self, number):
        self.accept_call()

    def handle_call_established(self):
        self.speak("Welcome to the jokes bot")
        self.speak(get_joke())
        self.speak("Goodbye")
        self.hang()


gateway = "sipx.xxxxx.net"
user = "xxxxxx"
pswd = "xxxx"

b = JokeBOT(user, pswd, gateway)

while b.running:
    sleep(1)

```

        
# Credits

This work as been sponsored by Matt Keys, [eZuce Inc](https://ezuce.com/)