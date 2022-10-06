# Arkanoid-Multi

## Overview

The Arkanoid-multi holds Arkanoid and Tournament Arkanoid ROMs and bank-switches them with an ATTiny.

Press and hold the on-board button, or wire-up an external button, to switch between games.

See [KLOV thread](https://forums.arcade-museum.com/threads/arkanoid-freeplay-rom.508179/) for more details.

[![Video](https://img.youtube.com/vi/AsMQ4WYeM8E/maxresdefault.jpg)](https://www.youtube.com/watch?v=AsMQ4WYeM8E)
[![Video](https://img.youtube.com/vi/M5QKxrMqJa0/maxresdefault.jpg)](https://www.youtube.com/watch?v=M5QKxrMqJa0)
    
## Print Arkanoid Multi PCB

The PCB can be printed from the [Arkanoid Multi PCBWay Shared Project](https://www.pcbway.com/project/shareproject/Arkanoid_Multi_PCB_v1_1_5169cf60.html) or Gerber files and DesignSpark files can be found in this repo in the 'PCB' folder.

The Multi PCB hosts a 27c160 in 16-bit mode and delivers data in parallel to the vacated color-PROM sockets. The ATTiny controls bank-switching of this EPROM, as well as the other 5 EPROMS on the game board, waits for a button to be held down for 4 seconds, and then increments its address lines. Address lines A0 to A3 can be hooked up to switch between up to 16 different games (in theory). A reset line is used to reset the game board when a switch has been made.

## Print MCU Bypass PCB

This solution works in conjunction with the MCU Bypass PCB by @mdeslaur on GitHub / KLOV. These can be printed from the [MCU Bypass PCBWay Shared Project](https://www.pcbway.com/project/shareproject/Arkanoid_MCU_Bypass_PCB_v1_2_2c4eb5f2.html) or Gerber files are available from the [Arkanoid MCU Bypass](https://github.com/mdeslaur/arkanoid-mpu-bypass) repo on GitHub.

Arkanoid and Tournament Arkanoid use different MCUs as a form of copy protection, so this is bypassed entirely by some code changes based upon the 'arkatayt' boot ROMs. 68705 are becoming more scarce so not requiring them is a great benefit to help further preserve Arkanoid PCBs.

## Add ROMs

Add the following ROM zip files to 'source' dir:

- arkanoid.zip
- arkatayt.zip
- arkatour.zip

## Create Patch files

Create the following files using 'xdelta patcher' on arkatayt and arkatour ROMs, and copy them to 'source' dir. Instructions can be found in the [KLOV thread](https://forums.arcade-museum.com/threads/arkanoid-freeplay-rom.508179/). Patch files for xdelta (by @mdeslaur) can be found in the 'patch' directory. These add freeplay, bypass the MCU and address a few bugs. 

- a75-27_patched.ic17
- a75-28_patched.ic16
- ic81-v_patched.3f
- ic82-w_patched.5f

## Run Script

Run the python3 script 'make_multi_roms.py':

``` python make_multi_roms.py ```

## Burn EPROMs

The 'output' dir should now contain the following files for burning to EPROMs:

- multi_color_proms.bin (27c160)
- multi_ic16_ic82.bin (27c512)
- multi_ic17_ic81.bin (27c512)
- multi_ic62.bin (27c512)
- multi_ic63.bin (27c512)
- multi_ic64.bin (27c512)

## Burn ATTiny

The binary in 'ATTiny85_Bankswitch' can be burnt to an ATTiny85.

Hold the button for 4 seconds to switch game.

If you would like a different switching mechanism, or you want to target a different ATTiny (13, 25 or 45), then all the code can be found at the [Multi ROM Controller](https://github.com/Phillrb/multi_rom_controller) repo on GitHub.

## Construct Mod

The Arkanoid-Multi PCB fits into the three sockets from the color PROMs and hosts the 27c160, ATTiny and a push button. Please keep your original ICs safe as you may want to remove the mod in the future.

The A0 line needs to be wired to pin 1 of all five 27c512 EPROMs. Pin 1 should not make a connection with the hosting PCB. These EPROMs should be fitted into round turned-pin socket strips. Heat up and remove the round pin socket that pin 1 of the EPROM will go into so that there is an air-gap between pin 1 and the hosting PCB. You may need to slightly trim pin 1 of the EPROM so that it doesn't make contact.

Wire the NXT line to an external button. Arkanoid conveniently has 'P1 button 2' on the edge connector wired up (22) but does not make use of it, or alternatively use the 'P1 Start button' (12). Arkanoid is 'Taito Classic' pinout.

The last line that needs to be hooked up is the RST line. Solder a wire from it to pin 1 of IC32 (LS273) as this is the CPU reset line. 

## Arkanoid Freeplay ROM Dipswitch Settings

DIPS -> OFF or ON
1. Cocktail or Upright
2. Credit or Freeplay
3. Lives 3 or 5
4. Bonus at 20K/60K or 20k only
5. Difficulty Easy or Hard
6. Test mode off or on
7. Screen Normal or Inverted
8. Continued play off or on

## Links

- [GitHub repo for Arkanoid Multi with docco, scripts and gerbers](https://github.com/Phillrb/arkanoid_multi)
- [GitHub repo for MCU Bypass with docco and gerbers](https://github.com/mdeslaur/arkanoid-mpu-bypass)
- [GitHub repo for ATTiny mutli-ROM-controller](https://github.com/Phillrb/multi_rom_controller)
- [PCBWay shared project for Arkanoid Multi PCB](https://www.pcbway.com/project/shareproject/Arkanoid_Multi_PCB_v1_1_5169cf60.html)
- [PCBWay shared project for MCU Bypass PCB (with permission)](https://www.pcbway.com/project/shareproject/Arkanoid_MCU_Bypass_PCB_v1_2_2c4eb5f2.html)
- [KLOV thread](https://forums.arcade-museum.com/threads/arkanoid-freeplay-rom.508179/)
