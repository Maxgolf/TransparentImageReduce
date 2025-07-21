# TransparentImageReduce

Batch tool to remove green screen backgrounds from images and resize them, optimized for `.webp` input. Powered by Python & Pillow.

## Why?

This was created because most online background removal tools have limits on how many images you can convert at once, making them a pain for bulk transparent conversion. This script solves that by handling everything locally, instantly, and with full control.

This tool was mainly built to process images created with the [FiveM Greenscreener](https://github.com/Bentix-cs/fivem-greenscreener) resource, which allows players to generate in-game screenshots with a green screen background for character art, thumbnails, etc.

## Features
- Supports `.webp`, `.png`, `.jpg`, `.jpeg`
- Removes green screen backgrounds with adjustable sensitivity
- Resizes images to 50% of original size (configurable)
- Saves as lossless transparent `.webp` images

## Setup

```bash
pip install -r requirements.txt
python remove_green_resize.py
```