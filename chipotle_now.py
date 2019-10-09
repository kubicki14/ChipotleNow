import sys
import argparse
import autopy
import datetime
from time import sleep
from screeninfo import get_monitors
from gtts import gTTS
from playsound import playsound

DEFAULT_WAIT = 1
SUPPORTED_RESOLUTIONS = ['2560 x 1440', '1920 x 1080']


def checkout(guest: bool = False):
    # TODO: Add new elif for logging in with DIFFERENT credentials than just using cached details from chrome.
    if guest:
        pass
    else:
        # Use log-in credentials (cached in chrome browser from before)
        mouse_click(1253.0, 712.0)  # Sign in button (assuming user + pass already cached in chrome

        # Since were using an account, it has the usual restaurant cached, going to click continue...
        mouse_click(1288.0, 796.0)  # Continue button

        mouse_click(1284.0, 949.0)  # Pick up time - Should default to most recent, press continue button again.

        autopy.key.tap(key=autopy.key.Code.PAGE_DOWN, modifiers=[])  # Move down the page a bit.

        mouse_click(1262.0, 897.0)  # Order Summary - Looks good, press continue again.

        mouse_click(1280.0, 1117.0)  # PRESS 'CONFIRM AND PLACE ORDER' (Assume payment information is valid).


def lanes_burrito_bowl(chips: bool = False):
    '''
    My burrito recipe order selection.
    :param chips:
    :return:
    '''
    mouse_click(1575.0, 969.0)  # Burrito bowl pic, click
    sleep(DEFAULT_WAIT)

    mouse_click(1016.0, 837.0)  # chicken
    autopy.key.tap(key=autopy.key.Code.PAGE_DOWN, modifiers=[])  # Move down the page a bit...
    mouse_click(997.0, 546.0)  # white rice
    mouse_click(1000.0, 839.0)  # black beans
    mouse_click(1362.0, 1151.0)  # fresh tomato salsa - mild
    autopy.key.tap(key=autopy.key.Code.PAGE_DOWN, modifiers=[])  # Move down the page a bit...
    mouse_click(994.0, 279.0)  # corn
    mouse_click(1359.0, 570.0)  # cheese
    mouse_click(994.0, 803.0)  # lettuce

    if chips:
        mouse_click(1019.0, 1059.0)  # chips

    mouse_click(1708.0, 864.0)  # 'add meal to bag' button
    sleep(DEFAULT_WAIT)

    mouse_click(1657.0, 560.0)  # checkout button
    sleep(DEFAULT_WAIT)


def mouse_click(x, y):
    autopy.mouse.move(x, y)  # fresh tomato salsa - mild
    sleep(DEFAULT_WAIT)
    autopy.mouse.click()
    sleep(DEFAULT_WAIT)


def go_to_chipotle():
    autopy.key.type_string(string='https://order.chipotle.com', wpm=80)
    autopy.key.tap(key=autopy.key.Code.RETURN, modifiers=[])


def to_the_left():
    # test move left once - WindowsKey + left arrow
    autopy.key.tap(key=autopy.key.Code.LEFT_ARROW, modifiers=[autopy.key.Modifier.META])


def open_chrome(league: bool = False):
    if league:
        # Win + D to escape borderless screen covering taskbar.
        autopy.key.tap(key='D', modifiers=[autopy.key.Modifier.META])

    mouse_click(21.0, 1425.0)  # Click Windows 10 Start Button
    autopy.key.type_string(string='chrome', wpm=120)
    autopy.key.tap(key=autopy.key.Code.RETURN, modifiers=[])


def choose_monitor(monitor_name: str = None):
    """
    Outputs the different monitor options you have available or returns the data regarding one if specified.
    :param monitor_name:
    :return:
    """
    for m in get_monitors():
        if monitor_name and monitor_name.lower() in m.name.lower():
            return m  # x, y, width, height
        else:
            print(str(m))
    print('Please specify part of the monitor name in parameters to choose the resolution to work with.')
    sys.exit(1)  # Break and let the user choose a monitor to specify from the list


def finish_yell_at_user():
    # Generate text-to-robot and output to speakers
    chipotle_ready_time = str((datetime.datetime.now() + datetime.timedelta(minutes=15)).time())
    print(chipotle_ready_time)
    ampm = 'AM' if int(chipotle_ready_time[:2]) < 12 else 'PM'
    finish_text = 'Fuck you asshole chipotle will be ready at {} {} {}'.format(chipotle_ready_time[:2],
                                                                               chipotle_ready_time[3:5], ampm)
    gTTS(text=finish_text, lang='en', slow=False).save('temp.mp3')  # This converts 19:00 -> 7:00pm
    playsound('temp.mp3')  # TODO: Find way to specify the speaker to use as a parameter...
    return finish_text


def main(monitor=None, league: bool = False, chips: bool = False, guest: bool = False):
    # Initialize
    print('You selected monitor {} with resolution {} x {}!'.format(monitor.name, str(monitor.width),
                                                                    str(monitor.height)))
    # Focus
    autopy.mouse.move(1, 1)
    if monitor.width == 2560 and monitor.height == 1440:
        open_chrome(league=league)
        # Let it load...(i5-2400 @ 3.1GHz o.o)
        sleep(DEFAULT_WAIT)
        go_to_chipotle()
        lanes_burrito_bowl(chips=chips)
        checkout(guest=guest)
        return finish_yell_at_user()

    elif monitor.width == 1920 and monitor.height == 1080:
        pass  # TODO: Make script mapping for 1080 primary display
    else:
        raise Exception('This monitor is not a supported resolution. Please select a monitor with one of these'
                        ' resolutions:\n {}'.format(str(SUPPORTED_RESOLUTIONS)))


if __name__ == '__main__':
    """
    LANE'S CHIPOTLE-NOW ORDERING SCRIPT

    PREREQS TO USE:
    - A GIANT 2560 x 1440 resolution screen - 1920x1080 coming soon....Mapping TBD
    - Google chrome installed & chipotle acc cached in chrome.
    - python 3.6.3 + pip install autopy
    - Windows (mileage may vary)
    
    Credits
    https://www.autopy.org/documentation/api-reference/index.html
    """
    parser = argparse.ArgumentParser(description='Parse arguments for chipotle ordering')
    parser.add_argument("--m", default=None, type=str, help="Name of a monitor; No input will show options.")
    # TODO: Implement: guest_checkout, then supply address param for guest, then supply cc info for guest checkout.
    # parser.add_argument("--address", default=None, type=str, help="Explicit address to order from closest chipotle.")
    parser.add_argument("--chips", default=False, action='store_true', help="Whether or not you want to order chips.")
    parser.add_argument("--league", default=False, action='store_true',
                        help="Whether or not league of legends is running.")
    args = parser.parse_args()

    playsound('temp.mp3')

    # Choose main monitor + resolution for scripting (based on name of monitor)
    selected_monitor = choose_monitor(monitor_name=args.m)

    main(monitor=selected_monitor, league=args.league, chips=args.chips)
    sys.exit()
