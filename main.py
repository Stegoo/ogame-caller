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
from ogame_constant import Ships, Speed, Missions, Buildings, Research, Defense
import asterisk

def send_ressources_to_main_planet(ogame_instance, from_planet, resources):
    ships = [(Ships['LargeCargo'], config.og_large_cargo_to_send)]
    speed = Speed['100%']
    where = {'galaxy': config.og_main_planet_coordonates[0], 'system': config.og_main_planet_coordonates[1], 'position': config.og_main_planet_coordonates[2]}
    mission = Missions['Transport']
    resources = {'metal': resources["metal"], 'crystal': resources["crystal"], 'deuterium': resources["deuterium"]}
    ogame_instance.send_fleet(from_planet, ships, speed, where, mission, resources)

def do_check(ogame_instance):
    while (42):
        is_attacked = ogame_instance.is_under_attack()
        resources = ogame_instance.get_resources(config.og_id_mother_planet)
        print('UNDER ATTACK: %s' % is_attacked)
        print(resources)
        if is_attacked:
            asterisk.call()

        if resources["metal"] > config.og_metal_threshold:
            for id_planet in config.og_planets:
                send_ressources_to_main_planet(ogame_instance, id_planet, resources)
                time.sleep(randint(5,12))

        timer = time.time()
        next_check = randint(60,120) * 60
        print('next check in : %s seconds' % next_check)
        time.sleep(timer - time.time() + next_check)

def main():
    try:
        ogame_instance = Ogame(config.og_universe, config.og_login, config.og_password, config.og_domain)
        loop = threading.Thread(None, do_check, args=[ogame_instance])
        loop.start()
        loop.join()
    except KeyboardInterrupt:
        loop.stop()

if __name__ == "__main__":
    main()
