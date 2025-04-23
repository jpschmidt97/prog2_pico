# Original Source: https://github.com/robert-hh/BME280
# Minimal angepasst für gängigen MicroPython-Einsatz

import time
from machine import I2C

class BME280:
    def __init__(self, i2c, address=0x76):
        self.i2c = i2c
        self.address = address
        if self.address not in self.i2c.scan():
            raise Exception("BME280 not found at address 0x{:02x}".format(self.address))
        self._load_calibration()
        self.t_fine = 0

    def _read(self, addr, nbytes):
        return self.i2c.readfrom_mem(self.address, addr, nbytes)

    def _write(self, addr, data):
        self.i2c.writeto_mem(self.address, addr, bytes([data]))

    def _load_calibration(self):
        calib = self._read(0x88, 24)
        self.dig_T1 = int.from_bytes(calib[0:2], 'little')
        self.dig_T2 = int.from_bytes(calib[2:4], 'little', signed=True)
        self.dig_T3 = int.from_bytes(calib[4:6], 'little', signed=True)

        self.dig_P1 = int.from_bytes(calib[6:8], 'little')
        self.dig_P2 = int.from_bytes(calib[8:10], 'little', signed=True)
        self.dig_P3 = int.from_bytes(calib[10:12], 'little', signed=True)
        self.dig_P4 = int.from_bytes(calib[12:14], 'little', signed=True)
        self.dig_P5 = int.from_bytes(calib[14:16], 'little', signed=True)
        self.dig_P6 = int.from_bytes(calib[16:18], 'little', signed=True)
        self.dig_P7 = int.from_bytes(calib[18:20], 'little', signed=True)
        self.dig_P8 = int.from_bytes(calib[20:22], 'little', signed=True)
        self.dig_P9 = int.from_bytes(calib[22:24], 'little', signed=True)

        calib = self._read(0xA1, 1)
        self.dig_H1 = calib[0]
        calib = self._read(0xE1, 7)
        self.dig_H2 = int.from_bytes(calib[0:2], 'little', signed=True)
        self.dig_H3 = calib[2]
        e4 = calib[3]
        e5 = calib[4]
        e6 = calib[5]
        self.dig_H4 = (e4 << 4) | (e5 & 0x0F)
        self.dig_H5 = (e6 << 4) | (e5 >> 4)
        self.dig_H6 = calib[6]

        self._write(0xF2, 0x01)  # Humidity oversampling x1
        self._write(0xF4, 0x27)  # Pressure and Temperature oversampling x1, Mode normal
        self._write(0xF5, 0xA0)  # Standby 1000ms, Filter off

    def read_raw_data(self):
        data = self._read(0xF7, 8)
        adc_p = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
        adc_t = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
        adc_h = (data[6] << 8) | data[7]
        return adc_t, adc_p, adc_h

    def read_compensated_data(self):
        adc_t, adc_p, adc_h = self.read_raw_data()

        # Temperature compensation
        var1 = (((adc_t >> 3) - (self.dig_T1 << 1)) * self.dig_T2) >> 11
        var2 = (((((adc_t >> 4) - self.dig_T1) * ((adc_t >> 4) - self.dig_T1)) >> 12) * self.dig_T3) >> 14
        self.t_fine = var1 + var2
        T = (self.t_fine * 5 + 128) >> 8

        # Pressure compensation
        var1 = self.t_fine - 128000
        var2 = var1 * var1 * self.dig_P6
        var2 += ((var1 * self.dig_P5) << 17)
        var2 += (self.dig_P4 << 35)
        var1 = ((var1 * var1 * self.dig_P3) >> 8) + ((var1 * self.dig_P2) << 12)
        var1 = (((1 << 47) + var1) * self.dig_P1) >> 33
        if var1 == 0:
            P = 0
        else:
            p = 1048576 - adc_p
            p = (((p << 31) - var2) * 3125) // var1
            var1 = (self.dig_P9 * (p >> 13) * (p >> 13)) >> 25
            var2 = (self.dig_P8 * p) >> 19
            P = ((p + var1 + var2) >> 8) + (self.dig_P7 << 4)

        # Humidity compensation
        h = self.t_fine - 76800
        h = (((((adc_h << 14) - (self.dig_H4 << 20) - (self.dig_H5 * h)) + 16384) >> 15) *
             (((((((h * self.dig_H6) >> 10) * (((h * self.dig_H3) >> 11) + 32768)) >> 10) + 2097152) *
               self.dig_H2 + 8192) >> 14))
        h = h - (((((h >> 15) * (h >> 15)) >> 7) * self.dig_H1) >> 4)
        h = 0 if h < 0 else h
        h = 419430400 if h > 419430400 else h
        H = h >> 12

        return T, P, H