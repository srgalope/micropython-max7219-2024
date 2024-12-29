# 8x8 LED Matrix Icon Patterns for ESP32
# Author: Sam Galope (iam@samgalope.dev)
#
# Description:
# This script contains binary patterns for a variety of icons that can be displayed on an 8x8 LED matrix.
# These patterns are designed for use with the ESP32 microcontroller and can be used with the micropython-max7219 driver library.
# The project is currently working and the icons provided here can be displayed on the matrix using your ESP32.
# More icons will be added in future updates.
#
# Requirements:
# This code requires the following repo for the LED matrix driver:
# https://github.com/srgalope/micropython-max7219-2024
#
# Each icon is encoded as an 8x8 grid using binary strings where '1' lights up an LED and '0' keeps it off.
# You can use these patterns as-is or modify them to create animations, custom designs, or other projects.
#
# Copyright (c) 2024 Sam Galope
# This project is licensed under the MIT License - see the LICENSE file for details.


HEART = [
    "01100110",
    "11111111",
    "11111111",
    "11111111",
    "01111110",
    "00111100",
    "00011000",
    "00000000",
]

HEART_HOLLOW = [
    "01100110",
    "10011001",
    "10000001",
    "10000001",
    "01000010",
    "00100100",
    "00011000",
    "00000000",
]

HEART_MD_HOLLOW = [
    "00000000",
    "01100110",
    "01011010",
    "01000010",
    "00100100",
    "00011000",
    "00000000",
    "00000000",
]

HEART_SM_HOLLOW = [
    "00000000",
    "00000000",
    "00111100",
    "00111100",
    "00011000",
    "00000000",
    "00000000",
    "00000000",
]

STAR = [
    "00010000",
    "01010100",
    "00111000",
    "11111110",
    "00111000",
    "01010100",
    "00010000",
    "00000000",
]

STAR_MD = [
    "00000000",
    "01010100",
    "00111000",
    "11111110",
    "00111000",
    "01010100",
    "00000000",
    "00000000",
]

STAR_SM = [
    "00000000",
    "00000000",
    "00010000",
    "00111000",
    "00010000",
    "00000000",
    "00000000",
    "00000000",
]

CIRCLE = [
    "00111100",
    "01111110",
    "11111111",
    "11111111",
    "11111111",
    "11111111",
    "01111110",
    "00111100",
]

CIRCLE_HOLLOW = [
    "00111100",
    "01000010",
    "10000001",
    "10000001",
    "10000001",
    "10000001",
    "01000010",
    "00111100",
]

TRIANGLE = [
    "00000000",
    "00011000",
    "00011000",
    "00111100",
    "01111110",
    "01111110",
    "01111110",
    "00000000",
]

TRIANGLE_HOLLOW = [
    "00000000",
    "00011000",
    "00011000",
    "00100100",
    "01000010",
    "01111110",
    "01111110",
    "00000000",
]

ARROW_UP = [
    "00011000",
    "00111100",
    "01111110",
    "11111111",
    "00011000",
    "00011000",
    "00011000",
    "00011000",
]

ARROW_UP_HOLLOW = [
    "00011000",
    "00100100",
    "01000010",
    "11111111",
    "00011000",
    "00011000",
    "00011000",
    "00011000",
]

ARROW_DOWN = [
    "00011000",
    "00011000",
    "00011000",
    "00011000",
    "11111111",
    "01111110",
    "00111100",
    "00011000",
]

ARROW_DOWN_HOLLOW = [
    "00011000",
    "00011000",
    "00011000",
    "00011000",
    "11111111",
    "01000010",
    "00100100",
    "00011000",
]

ARROW_LEFT = [
    "00010000",
    "00110000",
    "01110000",
    "11111111",
    "11111111",
    "01110000",
    "00110000",
    "00010000",
]

ARROW_LEFT_HOLLOW = [
    "00010000",
    "00110000",
    "01010000",
    "10011111",
    "10011111",
    "01010000",
    "00110000",
    "00010000",
]

ARROW_RIGHT = [
    "00001000",
    "00001100",
    "00001110",
    "11111111",
    "11111111",
    "00001110",
    "00001100",
    "00001000",
]

ARROW_RIGHT_HOLLOW = [
    "00001000",
    "00001100",
    "00001010",
    "11111001",
    "11111001",
    "00001010",
    "00001100",
    "00001000",
]
