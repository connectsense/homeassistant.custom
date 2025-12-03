# ConnectSense Rebooter Pro — Home Assistant Custom Integration

This repository hosts the custom integration for ConnectSense Rebooter Pro, ready for manual installation or addition as a HACS custom repository.

## Installation
- Copy the folder `custom_components/connectsense` from this repository into your Home Assistant `config/custom_components/` directory, then restart Home Assistant.
- Or, in HACS: add `https://github.com/connectsense/homeassistant.custom` as a custom repository (type: Integration), install, and restart.

## Logging (optional)
Add to `configuration.yaml` to enable debug logging for troubleshooting:

```
logger:
  default: info
  logs:
    zeroconf: info
    homeassistant.components.zeroconf: debug
    custom_components.connectsense: debug
```

## What to expect after setup
- The device appears in Overview as “Rebooter Pro 10XXXXX” with reboot and outlet controls.
- Under Settings → Devices & Services → Devices you’ll see the Rebooter Pro device entry.
- Under Settings → Devices & Services → Integrations it shows as the Rebooter Pro integration entry.

Manual setup: Settings → Devices & Services → Add integration → search for “Rebooter Pro”, provide host/IP (default `rebooter-pro.local`), and submit.
