from baresipy import BareSIP
from time import sleep
from pyjokes import get_joke


class JokeBOT(BareSIP):
    def handle_incoming_call(self, number):
        self.accept_call()

    def handle_call_established(self):
        self.speak(get_joke())
        self.hang()


gateway = "sipx.mattkeys.net"
user = "test_phone"
pswd = "1VDSSonPYxlC"

b = JokeBOT(user, pswd, gateway)

while b.running:
    sleep(1)
