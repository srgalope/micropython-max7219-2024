# MicroPython MAX7219 8x8 LED Matrix

A MicroPython library for the MAX7219 8x8 LED matrix driver. This library supports cascading multiple matrices via SPI and leverages the [framebuf](http://docs.micropython.org/en/latest/pyboard/library/framebuf.html) module for graphics rendering.

Full documentation and examples are available on the [official website](https://www.samgalope.dev/2024/12/27/micropython-max7219-led-matrix-driver-documentation-working/).

---

## Wiring

| Pin | ESP32 Pin | Description           |
|-----|-----------|-----------------------|
| GND | GND       | Ground               |
| VCC | 5V        | Power Supply         |
| DIN | GPIO 23   | SPI MOSI (Data Input)|
| CS  | GPIO 5    | SPI SS (Chip Select) |
| CLK | GPIO 18   | SPI SCK (Clock)      |

### Notes:
1. **Common Ground**: Ensure the power supply ground (GND) is connected to the ESP32’s GND for stable operation.
2. **External Power Source**: Use a 5V power supply to avoid overloading the ESP32 when driving multiple matrices.

---

## Basic Usage

### Initialize the Driver
```python
from machine import Pin, SPI
import max7219

# Initialize SPI and MAX7219
spi = SPI(2, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))
cs = Pin(5, Pin.OUT)

# Create a display instance
matrix = max7219.Matrix8x8(spi, cs, 1)  # One 8x8 matrix

# Display text
matrix.fill(0)          # Clear the display
matrix.text('Hi!', 0, 0, 1)  # Display "Hi!"
matrix.show()           # Render the text

# Draw a pixel
matrix.pixel(3, 3, 1)   # Turn on the pixel at (3, 3)
matrix.show()

# Draw a Line
matrix.line(0, 0, 7, 7, 1)  # Diagonal line from top-left to bottom-right
matrix.show()

# Adjust Brightness
matrix.brightness(5)    # Set brightness level (0-15)

# Scrolling Text
from time import sleep
text = "Hello, World!"
for i in range(len(text) * 8):
    matrix.fill(0)
    matrix.text(text, -i, 0, 1)  # Scroll text
    matrix.show()
    sleep(0.1)
```

## How to Use the IconsLibrary module
### Show an icon
```python
from max7219 import Matrix8x8
from machine import Pin, SPI
from  time import sleep
import IconsLibrary

spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
matrix = Matrix8x8(spi, Pin(5), 1)

matrix.fill(0)  # Clear the display
matrix.brightness(0)

def display_pattern(display, pattern):
    for row_index, row_value in enumerate(pattern):
        for col_index, pixel in enumerate(row_value):
            if pixel == '1':  # If the pixel is on (1)
                display.pixel(col_index, row_index, 1)  # Turn on the pixel
    display.show()  # Update the display to reflect changes

display_pattern(matrix,IconsLibrary.HEART_HOLLOW,)
```

### Looping through the library
```python
from max7219 import Matrix8x8
from machine import Pin, SPI
from  time import sleep
import IconsLibrary

spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
matrix = Matrix8x8(spi, Pin(5), 1)

matrix.fill(0)  # Clear the display
matrix.brightness(0)

def display_pattern(display, pattern):
    for row_index, row_value in enumerate(pattern):
        for col_index, pixel in enumerate(row_value):
            if pixel == '1':  # If the pixel is on (1)
                display.pixel(col_index, row_index, 1)  # Turn on the pixel
    display.show()  # Update the display to reflect changes


ICONS = [
        IconsLibrary.HEART_SM_HOLLOW,
        IconsLibrary.HEART_MD_HOLLOW,
        IconsLibrary.HEART_HOLLOW,
        IconsLibrary.STAR,
        IconsLibrary.STAR_MD,
        IconsLibrary.STAR_SM,
        IconsLibrary.CIRCLE,
        IconsLibrary.CIRCLE_HOLLOW,
        IconsLibrary.TRIANGLE,
        IconsLibrary.TRIANGLE_HOLLOW,
        IconsLibrary.ARROW_UP,
        IconsLibrary.ARROW_UP_HOLLOW,
        IconsLibrary.ARROW_DOWN,
        IconsLibrary.ARROW_DOWN_HOLLOW,
        IconsLibrary.ARROW_LEFT,
        IconsLibrary.ARROW_LEFT_HOLLOW,
        IconsLibrary.ARROW_RIGHT,
        IconsLibrary.ARROW_RIGHT_HOLLOW,
        ]

pattern_length = len(ICONS)
while True:
    for i,pattern in enumerate(ICONS):
        display_pattern(matrix,pattern)
        matrix.fill(0)
        sleep(.2)
```


## License
This project is licensed under the MIT License.
