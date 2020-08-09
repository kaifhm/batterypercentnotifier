from time import sleep
from personal.instantMessage import pb
from personal.instantMessage import mobile
from personal.instantMessage import laptop
import ctypes
from ctypes import wintypes
from os import startfile
from plyer import notification


icon_path = r'F:\MyPythonScripts\Battery\battery.ico'


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

        if battery_percent > 89 and charging:
            try:
                pb.push_note(
                    '', f'Battery charged to {battery_percent}%', mobile, laptop)
            except:
                pass
            notification.notify('Battery Sufficiently Charged',
                                f'Battery charged to {battery_percent}%. Please unplug your AC adapter', app_icon=r'F:\MyPythonScripts\Battery\battery.ico')
            sleep(120)
        elif battery_percent < 21 and not charging:
            message = f'Battery is at {battery_percent}%. Please plug-in your AC adapter'
            try:
                pb.push_note('Battery Low!', message, mobile, laptop)
            except:
                pass
            notification.notify('Battery Low', message, app_icon=r'F:\MyPythonScripts\Battery\battery.ico')
            sleep(120)
        else:
            sleep(1)
except:
    startfile(r'F:\MyPythonScripts\Battery\Battery percent.pyw')
