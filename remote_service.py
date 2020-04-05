import evdev


class RemoteService(object):
    __instance = None

    def __new__(cls):
        # Singleton initializer
        if RemoteService.__instance is None:
            RemoteService.__instance = object.__new__(cls)
        return RemoteService.__instance

    is_listening = False

    def start_listening(self, on_key_pressed, device = '/dev/input/event1'):

        # TODO: Make sure the event exists and wait until it's ready.
        device = evdev.InputDevice(device)
        print(device)

        down = 1
        up = 0
        hold = 2

        RemoteService.is_listening = True

        for event in device.read_loop():

            if not RemoteService.is_listening: break
            if event.type == evdev.ecodes.EV_KEY and event.value == down:
                # print(evdev.categorize(event))
                key = evdev.ecodes.KEY[event.code]

                # The mute key is special since it will produce an array of keys
                if event.code == 113:
                    key = 'KEY_MUTE'

                print(key)
                on_key_pressed(key)


    def stop_listener(self):
        RemoteService.is_listening = False
