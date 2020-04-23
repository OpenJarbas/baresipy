from baresipy import BareSIP
from time import sleep
from pyjokes import get_joke


class SIPBOT(BareSIP):
    def handle_call_ended(self, reason):
        self.say("Automated call ended, exiting")
        self.quit()

    def handle_call_established(self):
        self.stop_playing()
        self.say(get_joke())
        self.hang()

    def handle_call_ringing(self):
        self.say("I am calling the test phone")

    def handle_call_start(self):
        self.play("acdc.mp3", blocking=False)

    def handle_call_status(self, status):
        pass

    def handle_call_timestamp(self, timestr):
        pass

    def handle_login_failure(self):
        self.say("credentials are wrong")
        self.quit()

    def handle_login_success(self):
        self.say("credentials accepted")
        self.call("jarbas_laptop@sipx.mattkeys.net")

    def handle_mic_muted(self):
        pass

    def handle_mic_unmuted(self):
        pass

    def handle_ready(self):
        self.say("logging in")


gateway = "sipx.mattkeys.net"
user = "test_phone"
pswd = "1VDSSonPYxlC"

print("press ctrl+x to exit")

b = SIPBOT(user, pswd, gateway)

while b.running:
    sleep(1)
