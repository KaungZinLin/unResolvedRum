import psutil
import tkinter as tk
import webbrowser

def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("unResolvedRum - About App")
    about_window.config(padx=25, pady=25)
    about_window.resizable(False, False)

    def github():
        webbrowser.open("https://github.com/KaungZinLin/unResolvedRum")

    unresolvedRum_label = tk.Label(about_window, text="unResolvedRum", font=('Areal', 25))
    unresolvedRum_label.grid(row=0, column=0, sticky='w')

    about_unresolvedRum_label = tk.Label(about_window, text="unResolvedRum is a Free and Open Source System Monitoring App for Mac.")
    about_unresolvedRum_label.grid(row=1, column=0, sticky='w')

    app_info_label = tk.Label(about_window, text="\nAPP INFO: ")
    app_info_label.grid(row=2, column=0, sticky='w')

    app_version_label = tk.Label(about_window, text="Version: 1.0 (Stable)")
    app_version_label.grid(row=3, column=0, sticky='w')

    release_date_label = tk.Label(about_window, text="Release Date: 28 June 2023")
    release_date_label.grid(row=4, column=0, sticky='w')

    more_label = tk.Label(about_window, text="\nMORE INFO: ")
    more_label.grid(row=5, column=0, sticky='w')

    github_button = tk.Button(about_window, text="GitHub", command=github)
    github_button.grid(row=6, column=0, sticky='w')

    copyright_label = tk.Label(about_window, text="\nCopyright 2023 unResolved Creations. Do not Distribute!")
    copyright_label.grid(row=7, column=0, sticky='w')

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage_gb():
    mem = psutil.virtual_memory()
    used = mem.used >> 30  # Convert to GB
    total = mem.total >> 30  # Convert to GB
    return f"{used}GB/{total}GB"

def get_ram_usage_percent():
    return psutil.virtual_memory().percent

def get_free_and_used_ram():
        mem = psutil.virtual_memory()
        used = mem.used >> 30  # Convert to GB
        free = mem.free >> 30  # Convert to GB
        total = mem.total >> 30  # Convert to GB
        return f"Used: {used}GB / Free: {free}GB / Total: {total}GB"


def get_gpu_usage():
    # This part of the code is still Work in Progress.
    # This part (feature) will be available in unResolvedRum v1.1.
    return "!WIP! - Work in Progress!"

def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery:
        return battery.percent
    else:
        return "N/A"

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        return battery.power_plugged
    else:
        return "N/A"

def update_labels():
    cpu_label["text"] = f"CPU Usage: {get_cpu_usage()}%"
    ram_label["text"] = f"RAM Usage (GB): {get_ram_usage_gb()}"
    ram_label_percent["text"] = f"RAM Usage (Percent): {get_ram_usage_percent()}%/100%"
    # free_and_used_ram_label["text"] = f"Ram Usage: {get_free_and_used_ram()}"
    gpu_label["text"] = f"GPU Usage: {get_gpu_usage()}"
    battery_label["text"] = f"Battery: {get_battery_percentage()}% ({'Plugged In' if get_battery_status() else 'Unplugged'})"
    total_disk_label["text"] = f"Total: {get_disk_total()} GBs"
    used_disk_label["text"] = f"Used: {get_disk_used()} GBs"
    free_disk_label["text"] = f"Free: {get_disk_free() }GBs"
    percent_label["text"] = f"Percentage: {get_disk_percent()}%"
    network_in["text"] = f"Network In: {get_network_bytes_in()} KBs"
    network_out["text"] = f"Network Out: {get_network_bytes_out()} KBs"
    root.after(1000, update_labels)  # Refresh rate: 1000ms (1 second)

def get_disk_total():
    usage = psutil.disk_usage('/')
    return round(convert_bytes_to_gbs(usage.total))

def get_disk_used():
    usage = psutil.disk_usage('/')
    return round(convert_bytes_to_gbs(usage.used))

def get_disk_free():
    usage = psutil.disk_usage('/')
    return round(convert_bytes_to_gbs(usage.free))

def get_disk_percent():
    usage = psutil.disk_usage('/')
    return usage.percent

def convert_bytes_to_gbs(bytes_value):
    return bytes_value / (1024 ** 3)

def get_network_bytes_out():
    stats = psutil.net_io_counters()
    bytes_sent = stats.bytes_sent
    kbs_sent = bytes_sent / 1024
    return kbs_sent

def get_network_bytes_in():
    stats = psutil.net_io_counters()
    bytes_recv = stats.bytes_recv
    kbs_recv = bytes_recv / 1024
    return kbs_recv

def quit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("unResolvedRum")
root.config(padx=25, pady=25)
root.resizable(False, False)

# Create labels to display system information
rum_logo_label = tk.Label(root, text="unResolvedRum", font=('Areal', 25))
rum_logo_label.grid(row=0, column=0, sticky='w')

cpu_section_label = tk.Label(root, text="\nCPU (Processor)")
cpu_section_label.grid(row=1, column=0, sticky='w')

cpu_label = tk.Label(root, text="CPU Usage: ")
cpu_label.grid(row=2, column=0, sticky='w')

ram_section_label = tk.Label(root, text="\nRAM (Memory)")
ram_section_label.grid(row=3, column=0, sticky='w')

ram_label = tk.Label(root, text="RAM Usage: ")
ram_label.grid(row=4, column=0, sticky='w')

ram_label_percent = tk.Label(root, text="RAM Usage (Percent): ")
ram_label_percent.grid(row=5, column=0, sticky='w')

free_and_used_ram_label = tk.Label(root, text="Free/ Used RAM: ")
# free_and_used_ram_label.grid(row=6, column=0, sticky='w')

gpu_section_label = tk.Label(root, text="\nGPU (Graphics)")
gpu_section_label.grid(row=7, column=0, sticky='w')

gpu_label = tk.Label(root, text="GPU Usage: ")
gpu_label.grid(row=8, column=0, sticky='w')

network_section_label = tk.Label(root, text="\nNETWORK")
network_section_label.grid(row=9, column=0, sticky='w')

network_in = tk.Label(root, text="Network In: ")
network_in.grid(row=10, column=0, sticky='w')

network_out = tk.Label(root, text="Network Out: ")
network_out.grid(row=11, column=0, sticky='w')

placeholder_label = tk.Label(root, text="")
placeholder_label.grid(row=19, column=0)

disk_label = tk.Label(root, text="\nDISK")
disk_label.grid(row=12, column=0, sticky='w')

total_disk_label = tk.Label(root, text="Total: ")
total_disk_label.grid(row=13, column=0, sticky='w')

used_disk_label = tk.Label(root, text="Used: ")
used_disk_label.grid(row=14, column=0, sticky='w')

free_disk_label = tk.Label(root, text="Free: ")
free_disk_label.grid(row=15, column=0, sticky='w')

percent_label = tk.Label(root, text="Percentage: ")
percent_label.grid(row=16, column=0, sticky='w')

battery_section_label = tk.Label(root, text="\nBATTERY")
battery_section_label.grid(row=17, column=0, sticky='w')

battery_label = tk.Label(root, text="Battery: ")
battery_label.grid(row=18, column=0, sticky='w')

about_app_button = tk.Button(root, text="About App", width=10, command=open_about_window)
about_app_button.grid(row=20, column=0, sticky='w')

quit_button = tk.Button(root, text="Quit App", width=10, command=quit_app)
quit_button.grid(row=21, column=0, sticky='w')

# Start updating labels
update_labels()

# Start the Tkinter event loop
root.mainloop()
