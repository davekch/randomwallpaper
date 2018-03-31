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

 - `-c COLOR`: specify the color of the image. Valid values for `COLOR` are blue, turquoise, red, orange, grey and black. Default is turquoise.
 You can add arbitrary colors in normalized RGB to the script if you wish!
 - `-p PICTURE`: specify an image (png) as background.

Running the script (`python randombackground.py` or `./randombackground.py`) will place `.randombackground.png` in your home-directory. This way you can easily use the script to create a new wallpaper everytime you login.

For example if you use i3, you could add the line

```
exec_always "~/dir/to/script/randombackground.py; feh --bg-fill /home/me/.randombackground.png"
```
to your `config`-file. Make sure to `chmod +x randombackground.py` first if you do this :) .
