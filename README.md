# Random-Wallpaper-Generator
Python-script that generates PNGs of random geometric figures to be used as a wallpaper.

![examples](examples.png)

### Download

```bash
git clone https://github.com/davekch/randomwallpaper.git
```
**Requirements:**
 - python 2.7
 - cairocffi
```bash
pip install cairocffi
```

### Usage
#### Options

 - `-c COLOR`: specify the color of the image. Valid values for `COLOR` are blue, turquoise, red, orange, grey, black and random. Default is turquoise.
 You can add arbitrary colors in normalized RGB to the script if you wish!
 - `-t THEME`: specify a theme. A theme is a combination of a foreground- and background-color. You can either set a color OR a theme. Valid values for `THEME` are submarine, poison, poison_dark, fire, fire_dark, pinky and random
 - `--fg R G B`: specify a foreground color in normalized RGB
 - `--bg R G B`: specify a background color in normalized RGB
 - `-p PICTURE`: specify an image (png) as background.
 - `-s OUTPUT`: save the output .png as OUTPUT
 - `-h`: display a short help message.

Running the script (`python randombackground.py` or `./randombackground.py`) will place `.randombackground.png` in your home-directory. This way you can easily use the script to create a new wallpaper everytime you log in.

For example if you use i3, you could add the line

```
exec_always "~/dir/to/script/randombackground.py; feh --bg-fill /home/me/.randombackground.png"
```
to your `config`-file. Make sure to `chmod +x randombackground.py` first if you do this :) .
