import ctypes
from ctypes import wintypes
import comtypes.client
import psutil

# Definizione delle costanti
CLSID_TaskbarList = '{56FDF344-FD6D-11D0-958A-006097C9A090}'
IID_ITaskbarList = '{56FDF342-FD6D-11D0-958A-006097C9A090}'
GW_HWNDNEXT = 2

# Definizione di ITaskbarList
class ITaskbarList(comtypes.IUnknown):
    _iid_ = comtypes.GUID(IID_ITaskbarList)
    _methods_ = [
        comtypes.COMMETHOD([], ctypes.HRESULT, 'HrInit'),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'AddTab',
                           (['in'], wintypes.HWND, 'hwnd')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'DeleteTab',
                           (['in'], wintypes.HWND, 'hwnd')),
        comtypes.COMMETHOD([], ctypes.HRESULT, 'SetTabOrder',
                           (['in'], wintypes.HWND, 'hwndInsertBefore')),
    ]

# Funzione per nascondere una finestra specificata dalla taskbar e mantenerla nell'alt-tab
def hide_window_from_taskbar(hwnd):
    comtypes.CoInitialize()
    taskbar_list = comtypes.client.CreateObject(CLSID_TaskbarList, interface=ITaskbarList)
    taskbar_list.DeleteTab(hwnd)
    taskbar_list.SetTabOrder(0)  # Mantieni la finestra nell'alt-tab switcher
    comtypes.CoUninitialize()

# Funzione per mostrare una finestra specificata sulla taskbar
def show_window_on_taskbar(hwnd):
    comtypes.CoInitialize()
    taskbar_list = comtypes.client.CreateObject(CLSID_TaskbarList, interface=ITaskbarList)
    taskbar_list.AddTab(hwnd)
    taskbar_list.SetTabOrder(0)  # Mantieni la finestra nell'alt-tab switcher
    comtypes.CoUninitialize()

# Funzione per ottenere l'HWND di una finestra dal nome del processo
def get_window_handle_by_exe(exe_name):
    user32 = ctypes.windll.user32
    hwnd = user32.GetTopWindow(None)
    while hwnd:
        pid = wintypes.DWORD()
        tid = user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        try:
            process = psutil.Process(pid.value)
            if process.name().lower() == exe_name.lower():
                # Verifica che la finestra sia visibile e non minimizzata
                if user32.IsWindowVisible(hwnd) and user32.IsIconic(hwnd) == 0:
                    return hwnd
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
        hwnd = user32.GetWindow(hwnd, GW_HWNDNEXT)
    return None

# Funzione principale
def main():
    hidefrom = True  # Cambia questo valore per testare
    globalsHidefromT = True  # Cambia questo valore per testare

    # Specifica il nome del processo (file .exe) della finestra che vuoi nascondere
    exe_name = "notepad.exe"  # Cambia questo con il nome del file .exe della finestra che vuoi nascondere

    hwnd = get_window_handle_by_exe(exe_name)

    if hwnd:
        if hidefrom:
            if globalsHidefromT:
                hide_window_from_taskbar(hwnd)
                print(f"Finestra del processo '{exe_name}' nascosta dalla taskbar.")
            else:
                show_window_on_taskbar(hwnd)
                print(f"Finestra del processo '{exe_name}' mostrata sulla taskbar.")
    else:
        print(f"Finestra con processo '{exe_name}' non trovata.")

if __name__ == "__main__":
    main()
