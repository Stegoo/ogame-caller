import threading
import time
import sys
try:
    import config
except:
    print("You need to create a config.py file containing your credentials.")
    sys.exit()
from ogame import Ogame

def check_if_under_attack(ogame_instance):
    while (42):
        under_attack = ogame_instance.is_under_attack()
        print('UNDER ATTACK', under_attack)
        call()
        timer = time.time()
        time.sleep(timer - time.time() + 60)

def call():
        c = Call('SIP/0671968084@provider')
        a = Application('Playback', 'hello-world')
        cf = CallFile(c, a)
        cf.spool()

def main():
    try:
        ogame_instance = Ogame(config.og_universe, config.og_login, config.og_password, config.og_domain)
        loop = threading.Thread(None, check_if_under_attack, args=[ogame_instance])
        loop.start()
        loop.join()
    except KeyboardInterrupt:
        loop.stop()

if __name__ == "__main__":
    main()
