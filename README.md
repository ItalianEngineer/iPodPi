# iPodPi
A new repo dedicated to the iPodZero project.

The code is written by using Guy Dupont's click code, but to make things a bit easier, I have made an input processor in python to take the inputs from Dupont's click.c code, and spit it out through the python script. This is going to be useful when using the wheel to control a menu in python. The input interpreted by the c code and given to the python code can be coded to keyboard presses, or for more precise interactions like the game breakout, simply the positions. More detail will be in GitBook.

The clickwheel also uses pikeyd for its interface, and, I found that by using syproduction's configuration for pikeyd, I could map the iPod clickwheel bits to other keys such as Left Arrow or Right Arrow, so That revised file will also be here.

As for screen wiring (ST7789 Waveshare 2 inch LCD), I had DIN=19 CLK=23 CS=24 DC=22 RST=13 BL=12
