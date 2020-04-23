from baresipy import BareSIP
from time import sleep

speech = "this is jarbas personal assistant speaking. this was a test"

audio = "examples/acdc.mp3"


to = "jarbas_laptop@sipx.mattkeys.net"

gateway = "sipx.mattkeys.net"
user = "test_phone"
pswd = "1VDSSonPYxlC"
debug = False

b = BareSIP(user, pswd, gateway, debug=debug)

b.call(to)

while b.running:
    sleep(0.5)
    if b.call_established:
        b.send_dtmf("123")

        b.speak(speech)
        b.speak("Goodbye")
        # b.send_audio(audio)
        b.hang()
        b.quit()
