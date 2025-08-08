from machine import Pin, I2C, ADC, PWM
import time

# Pin setup
led1 = Pin(15, Pin.OUT)                 # act as digital actuator
led2 = PWM(Pin(12, Pin.OUT))            # act as analog actuator
led2.freq(100)
button = Pin(14, Pin.IN, Pin.PULL_UP)   # act as digital sensor
pot = ADC(26)                           # act as analog sensor

while True:
    val = pot.read_u16()
    led2.duty_u16(val)

    brightness = val * 100.0/65535
    val = val * 5.0/65535

    if button.value() == 1:  # Tombol ditekan
        led1.on()
    else:                    # Tombol dilepas
        led1.off()

    print(f"ADC: {val:.1f} -- Brightness {brightness:.1f}%")
    time.sleep(0.1)         # Debounce sederhana
