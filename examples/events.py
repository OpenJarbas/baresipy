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


gateway = "your_sip.gateway.net"
user = "your_phone"
pswd = "your_password"

b = JokeBOT(user, pswd, gateway)

while b.running:
    sleep(1)
