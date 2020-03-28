RPi PowerPoint Controller
========================

Controll your PowerPoint presentations with RPi
-----------------------------------------------

How to do it
------------
1. Creat PowerPoint presentation
2. Download and install [VNC Viwer](https://www.realvnc.com/en/connect/download/viewer/raspberrypi/) on Raspberry Pi
3. Download and install [VNC Server](https://www.realvnc.com/en/connect/download/vnc/windows/) on your computer (Windows, Mac, Lunux)
4. Connect your RPi to compuer using VNC.
5. Build a circuit shown in [schematic](https://github.com/Akaj-lab/RPi_PowerPoint_Comtroller/blob/master/Schematic_RPi%20PowerPint%20Controller_Sheet_1_20200328124209.pdf)
6. Download [code.py](https://github.com/Akaj-lab/RPi_PowerPoint_Comtroller/blob/master/code.py) to your RPi
7. Install library `pynput` and `RPi` if you dont already have them. Try using `pip3 install pynput` and `pip3 install RPi` commands.
8. Present slideshow on computer
9. Run code.py and click on VNC Viwer window on RPi

Thats how you can controll PowerPoint presentation with RPi. Note that both RPi an computer must be connected to the network.

Contributing
------------
I would apriciate if you contribute to this priject. If you need any help send me message on vesoljec.jk@gmail.com
