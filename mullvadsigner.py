#!/usr/bin/env python3

import json
import subprocess
import time

def get_tailscale_status():
    """Fetch the Tailscale lock status as JSON."""
    result = subprocess.run(["tailscale", "lock", "status", "--json"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error fetching Tailscale status:", result.stderr)
        return None
    return json.loads(result.stdout)

def main():
    status = get_tailscale_status()
    if not status:
        return

    nodes = status.get("FilteredPeers", [])
    nodes_mullvad = [node for node in nodes if ".mullvad.ts.net" in node.get("Name", "")]

    count_total = len(nodes)
    count_mullvad = len(nodes_mullvad)

    print(f"unsigned nodes: {count_total} total, {count_mullvad} Mullvad")

    if count_mullvad == 0:
        print("no Mullvad nodes need to be signed")
        return

    print("signing Mullvad nodes...")

    for node in nodes_mullvad:
        print(f"signing {node['Name']}")
        subprocess.run(["tailscale", "lock", "sign", node["NodeKey"]])
        time.sleep(0.1)

    print("all Mullvad nodes successfully signed")

if __name__ == "__main__":
    main()
