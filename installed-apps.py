import winreg

def get_installed_apps():
    # The key where the installed apps are stored in the Windows registry
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    # The list to store the names of the installed apps
    installed_apps = []

    # Iterate over all the subkeys under the key and get the name of each installed app
    for i in range(0, winreg.QueryInfoKey(key)[0]):
        subkey = winreg.EnumKey(key, i)
        subkey_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" + "\\" + subkey
        subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path)
        try:
            # Get the name of the app and add it to the list
            display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
            installed_apps.append(display_name)
        except:
            # If there is an error, skip this app
            continue
    return installed_apps

# Get the list of installed apps and print it
apps = get_installed_apps()
for app in apps:
    print(app)

input("Press Enter to exit")
