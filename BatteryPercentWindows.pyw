from time import sleep
import ctypes
from ctypes import wintypes
from os import startfile
from plyer import notification


icon_path = 'path\\to\\icon.ico'


class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
    ]


GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus

try:
    while True:
        status = SYSTEM_POWER_STATUS()

        if not GetSystemPowerStatus(ctypes.pointer(status)):
            break
        charging = status.ACLineStatus
        battery_percent = status.BatteryLifePercent

        if battery_percent >= 90 and charging:
            notification.notify('Battery Sufficiently Charged',
                                f'Battery charged to {battery_percent}%. Please unplug your AC adapter', app_icon=r'F:\MyPythonScripts\Battery\battery.ico')
            sleep(120)
        elif battery_percent <= 20 and not charging:
            message = f'Battery is at {battery_percent}%. Please plug-in your AC adapter'
            notification.notify('Battery Low', message, app_icon=r'F:\MyPythonScripts\Battery\battery.ico')
            sleep(120)
        else:
            sleep(1)
except:
    startfile(__file__)
