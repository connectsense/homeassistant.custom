# <img src="brands/connectsense/icon.png" alt="ConnectSense" width="50" height="50"/> ConnectSense Rebooter Pro

The **ConnectSense integration** integrates the [Rebooter Pro](https://www.gridconnect.com/products/rebooter-pro) from [Grid Connect Inc](https://www.gridconnect.com). It discovers devices via Zeroconf or by manually entering hostname/IP. The integration exposes the outlet switch, a reboot button, an optional Intelligent Reboot configuration, device triggers for reboot events, and optional push notifications.

Follow the installation steps below.

## Installation

<details>
<summary>With HACS</summary>

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)

1. In HACS, add this repo as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories/) (type: Integration). Or use the button below.
[![Open your Home Assistant instance and open this repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=connectsense&repository=homeassistant.custom&category=integration)
2. Install the integration from HACS.
3. Restart Home Assistant.

</details>

<details>
<summary>Manual</summary>

Copy `custom_components/connectsense` into `<config>/custom_components/connectsense` (your HA config directory), then restart Home Assistant.

</details>

## Prerequisites

The Rebooter Pro should be added to your network using one of the following methods.

### Local Configuration via Web Browser
1. Power the Rebooter Pro.
2. Connect to its Wi-Fi (CS-RBTR-*).
3. Open a browser and visit [http://192.168.250.1/](http://192.168.250.1/).
4. Follow remaining instructions in the browser.

### ConnectSense App (cloud access and account required)
1. Open the app store and install the **ConnectSense** app.
2. Create an account.
3. Click the **+** sign to Add a Device.
4. Select **Rebooter Pro**.
5. Follow remaining instructions in the app.

## Adding a Rebooter Pro Integration
The Rebooter Pro should be discovered automatically under Settings → Devices & Services

You can also add manually via Settings → Devices & Services → **Add Integration** → search “ConnectSense”. Or use the button below.

[![add integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start?domain=connectsense)

Then provide the Rebooter Pro hostname/IP (default `rebooter-pro.local`).

Key options (available in the options flow):
- Power Cycle Time (10–65535 seconds)
- Auto-reboot after Power Outage
- Intelligent Reboot (ping monitoring)
- Outage Time (2–10 minutes)
- Redetection Delay (0–10 minutes)
- Maximum Reboot Attempts (or unlimited)
- Outage Condition (ANY vs ALL targets)
- Up to 5 ping targets (hosts/IPs)
- Notifications: enable, notify service, and per-event toggles (OFF/ON/REBOOT)

## Supported functionality

### Controls

- **Reboot Now Button**: Immediately power-cycles the outlet.
- **Toggle Power Switch**: Turns the controlled outlet on/off.

### Configuration

- **Power Outage Auto Reboot Switch**: If enabled, the equipment will reboot after power is restored.
- **Intelligent Reboot Switch**: If enabled, the equipment will reboot on Internet/Ping failures (logic in integrations options).

### Device triggers

- `reboot_started_any`
- `reboot_started_power_fail`
- `reboot_started_ping_fail`

### Services

- `connectsense.send_test_notification`
  - `entry_id` (optional): Target config entry (auto-selected if only one exists).
  - `title`, `message` (optional): Custom text.
  - `code` (optional): 1=OFF, 2=ON, 3=REBOOTING (auto message).
  - Uses the notify service configured in options.

## Diagnostics

Diagnostics are available per config entry. Sensitive fields (host, webhook IDs/tokens) are redacted.

## Known limitations

- No device actions or entity events are exposed.
- Ensure Home Assistant can generate a reachable webhook URL (set an internal/external URL if needed) so the device can send notifications back to HA.

## Troubleshooting

### Cannot connect during setup

- Verify the device is reachable at the provided host/IP over HTTPS.
- If zeroconf is not offered, add manually; mDNS may be blocked on the network.
- Check SSL settings if using an IP/hostname that differs from the certificate.

### Notifications not working

- Ensure a working notify service is set in options.
- Make sure Home Assistant has an internal/external URL configured so the device can receive webhook callbacks.

## Removing the integration

Remove via Settings → Devices & Services → ConnectSense → Delete. The webhook is unregistered and entities are removed.

## Compatibility
Tested with Home Assistant 2025.11.3 and newer.

