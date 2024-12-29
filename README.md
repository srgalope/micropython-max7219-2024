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

## License
This project is licensed under the MIT License.
