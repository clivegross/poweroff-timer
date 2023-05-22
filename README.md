Poweroff Timer
-----------------------------

Python 3 script for stopping a Linux based system after an uptime limit elpases. Use as a fallback to automatically poweroff servers that cost money to run, eg AWS EC2.

The program checks the system uptime every 5min and shuts down if `TIME_LIMIT` is exceeded. Set `TIME_LIMIT` in `poweroff-timer.py`. Start the program by executing:

    python poweroff-timer.py

### Run as a service using systemctl

1. Download this repo into `/usr/local/bin/poweroff-timer` (or wherever you like)
1. Edit `poweroff-timer.service` if required. Configured to run script from `/usr/local/bin/poweroff-timer`
1. Copy the systemd unit file to systemd: `cp poweroff-timer.service /etc/systemd/system/`
1. Then run it with:

```
sudo systemctl start poweroff-timer    # Runs the script now
sudo systemctl enable poweroff-timer   # Sets the script to run every boot
journalctl -u poweroff-timer.service   # Check systemd journal for errors
```

To disable the service:

```
sudo systemctl disable poweroff-timer  # Sets the script to not run
```

To stop the service:

```
sudo systemctl stop poweroff-timer    # Stops the script now
```

To reload the service after changing, eg `TIME_LIMIT` adjustment:

```
sudo systemctl stop poweroff-timer
sudo systemctl daemon-reload
sudo systemctl start poweroff-timer
journalctl -u poweroff-timer.service
```
