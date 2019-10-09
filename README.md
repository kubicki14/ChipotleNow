This is a simple application/script that grabs me chipotle from my usual location by pressing buttons and keys.
Arguments that may be provided for chipotle_now.py: (e.g. --m=x, --league, --chips)
    - m="DISPLAY1" :-> Monitor name of the primary display you are using. If unsure of the name, don't give this param, & the program will       tell you your options.
    
    - chips :-> defaults to false, if you pass --chips you will get chips.
    
    - league :-> defaults to false, if you pass --league app will know to press (WIN+D) to minimize all to see taskbar.

    # TODO: Implement: guest_checkout, then supply address param for guest, then supply cc info for guest checkout.
    # TODO: Add new elif for logging in with DIFFERENT credentials than just using cached details from chrome.

PREREQS TO USE:
- A GIANT 2560 x 1440 resolution screen - 1920x1080 coming soon....Mapping TBD
- Google chrome installed & chipotle acc cached in chrome (w/ valid payment method).
- python 3.6.3 + pip installed requirements.txt
- Windows 10 (mileage may vary)



HOW TO USE:
  Fera not traveler, for this tool is simple if all prereqs are met!
  Open a console on your main screen, do a git clone of this repo, cd into the repo
  1. 'python chipotle_now.py'
    - This will output the monitors you have available to work with (name, + resolutions). Choose an option that is supported.

  2. 'python chipotle_now.py --m=DISPLAY2'
    - Replace DISPLAY2 with part of whatever the name of your primary display/monitor is (hopefully 2560 x 1440)

  3. Manually drive to Chipotle and eat your god dang foods!

  Enjoy.


 -Lane,
