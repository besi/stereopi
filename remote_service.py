import time
import evdev
from selectors import DefaultSelector, EVENT_READ
import selectors

class RemoteService(object):
    __instance = None

    def __new__(cls):
        # Singleton initializer
        if RemoteService.__instance is None:
            RemoteService.__instance = object.__new__(cls)
        return RemoteService.__instance

    is_listening = False

    def start_listening(self, on_key_pressed, device_identifier = 'Swisscom'):
        all_devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        devices = []
        selector = selectors.DefaultSelector()
        
        while len(devices) == 0:
            print("Found %s devices" % len(all_devices))
            
            for device in all_devices:
                if device_identifier in device.name:
                    devices.append(device)
                    selector.register(device, selectors.EVENT_READ)
            time.sleep(5)
            all_devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

        print("Found %s" % devices[0])
        down = 1
        up = 0
        hold = 2

        RemoteService.is_listening = True


        while True:
            for key, mask in selector.select():
                device = key.fileobj
                for event in device.read():
                    if not RemoteService.is_listening: break
                    if event.type == evdev.ecodes.EV_KEY and event.value == down:
                        key = evdev.ecodes.KEY[event.code]

                        if event.code == 113:
                            key = 'KEY_MUTE'

                        print(key)
                        on_key_pressed(key)


    def stop_listener(self):
        RemoteService.is_listening = False

