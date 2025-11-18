# Tailscaled-Mullvad-Signer-Py

This Python script automates the process of signing Mullvad nodes in a Tailscale network. It fetches the Tailscale lock status, identifies unsigned Mullvad nodes, and signs them automatically.

## Prerequisites

- Python 3.6 or higher
- Tailscale installed and configured on your system
- This script must be run on a signing node
- Sufficient permissions to run `tailscale lock` commands

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/privateoutlaw/Tailscaled-Mullvad-Signer-Py.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Tailscaled-Mullvad-Signer-Py
   ```

3. Ensure the script is executable:
   ```bash
   chmod +x mullvadsigner.py
   ```

## Usage

Run the script using Python:
```bash
python3 mullvadsigner.py
```

## Troubleshooting

- **Error fetching Tailscale status:** Ensure Tailscale is installed and you have the necessary permissions.
- **No Mullvad nodes found:** Verify that there are nodes with `.mullvad.ts.net` in their name.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
