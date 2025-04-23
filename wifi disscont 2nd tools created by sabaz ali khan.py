import os

def disconnect_ptcl_wifi():
    # Execute the command to disconnect from the PTCL WiFi network
    os.system('netsh wlan disconnect')

# Call the function to disconnect from the PTCL WiFi network
disconnect_ptcl_wifi()