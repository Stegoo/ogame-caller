import threading
import time
import sys
from random import randint
try:
    import config
except:
    print("You need to create a config.py file containing your credentials.")
    sys.exit()
from ogame import Ogame
import asterisk

def check_if_under_attack(ogame_instance):
    while (42):
        is_attacked = ogame_instance.is_under_attack()
        print('UNDER ATTACK: %s' % is_attacked)
        if is_attacked:
            asterisk.call()
        timer = time.time()
        next_check = randint(60,90) * 60
        print('next check in : %s seconds' % next_check)
        time.sleep(timer - time.time() + next_check)

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
