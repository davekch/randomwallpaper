#!/usr/bin/python2

import cairocffi as cairo
import random
import commands, sys
import argparse


COLORS = {
"blue"     : {"r": 0.109, "g": 0.127, "b": 0.627},
"turquoise": {"r": 0.149, "g": 0.752, "b": 0.811},
"red"      : {"r": 0.847, "g": 0.094, "b": 0.094},
"orange"   : {"r": 0.937, "g": 0.654, "b": 0.121},
"grey"     : {"r": 0.368, "g": 0.368, "b": 0.368},
"black"    : {"r": 0.000, "g": 0.000, "b": 0.000},
"white"    : {"r": 1.000, "g": 1.000, "b": 1.000}
}

THEMES = {
"submarine"  : {"BGC": COLORS["turquoise"], "FGC": COLORS["blue"]},
"poison"     : {"BGC": COLORS["grey"],      "FGC": COLORS["turquoise"]},
"poison_dark": {"BGC": COLORS["black"],     "FGC": COLORS["turquoise"]},
"fire"       : {"BGC": COLORS["red"],       "FGC": COLORS["orange"]},
"fire_dark"  : {"BGC": COLORS["black"],     "FGC": COLORS["red"]},
"pinky"      : {"BGC": COLORS["red"],       "FGC": COLORS["blue"]}
}

WIDTH, HEIGHT       = 1920, 1080
BGC_r, BGC_g, BGC_b = 0.149, 0.752, 0.811  # backgroundcolor in normalized rgb
FGC_r, FGC_g, FGC_b = 0,0,0                # foregroundcolor
EDGES               = 6


surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

context.scale(HEIGHT)



parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--color", help="Specify a color. Allowed arguments are: blue, turquoise, red, orange, grey, black, white, random")
group.add_argument("-t", "--theme", help="Select a theme. Allowed arguments are: submarine, poison, poison_dark, fire, fire_dark, pinky, random")
parser.add_argument("-p", "--picture", help="Specify a background picture")
args = parser.parse_args()

if args.color:
    if args.color=="random":
        args.color=random.choice([c for c in COLORS])
    try:
        c = COLORS[args.color]
        BGC_r, BGC_g, BGC_b = c["r"], c["g"], c["b"]
        if args.color=="black" or args.color=="grey":
            FGC_r, FGC_g, FGC_b = 1,1,1
    except:
        print "not a legit color!"
        sys.exit()
if args.theme:
    if args.theme=="random":
        args.theme=random.choice([t for t in THEMES])
    try:
        t = THEMES[args.theme]
        BGC_r, BGC_g, BGC_b = t["BGC"]["r"], t["BGC"]["g"], t["BGC"]["b"]
        FGC_r, FGC_g, FGC_b = t["FGC"]["r"], t["FGC"]["g"], t["FGC"]["b"]
    except:
        print "not a legit theme!"
        sys.exit()

if args.picture:
    try:
        img = cairo.ImageSurface.create_from_png(args.picture)
    except IOError:
        print "File not found!"
        sys.exit()
    except MemoryError:
        print "Must be png!"
        sys.exit()
    context.save()
    context.scale(1./HEIGHT)
    context.set_source_surface(img)
    context.paint()
    context.scale(HEIGHT)
    context.set_source_rgba(BGC_r, BGC_g, BGC_b, 0.2)
else:
    context.set_source_rgb(BGC_r, BGC_g, BGC_b)

context.stroke()
context.rectangle(0,0, 1.778,1)
context.fill()

x = [ random.uniform(0.5,1.3) for i in range(EDGES) ]
y = [ random.uniform(0.1,0.9) for i in range(EDGES) ]

for i in range(EDGES):
    context.set_source_rgba(FGC_r,FGC_g,FGC_b, random.uniform(0.1,0.6))
    context.move_to(x[i], y[i])
    context.line_to(x[(i+1)%EDGES], y[(i+1)%EDGES])
    context.line_to(x[(i+2)%EDGES], y[(i+2)%EDGES])
    context.fill()

context.stroke()

user = commands.getoutput("whoami")
surface.write_to_png("/home/"+user+"/.randombackground.png")
