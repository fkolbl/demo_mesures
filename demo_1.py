import mesure as m
import sys
import time


T_pause = 0.2

if __name__ == '__main__':
    print('------------------------------')
    print('-- mesure de distance en cm --')
    print('------------------------------')

    try:
        for k, distance, _, _ in m.streem_distance():
            print(f'Mesure n° {k} - Distance : {distance}')
            time.sleep(T_pause)
    except KeyboardInterrupt:
        print('\nInterruption de la mesure')
        sys.exit(0)