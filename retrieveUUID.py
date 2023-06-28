import asyncio
from bleak import BleakScanner, BleakClient


async def discover_device_services(target_device_address):
    scanner = BleakScanner()
    devices = await scanner.discover()
    target_device = next((d for d in devices if d.address == target_device_address), None)

    if target_device:
        async with BleakClient(target_device) as client:
            services = await client.get_services()
            for service in services:
                print(f"Service UUID: {service.uuid}")
                for char in service.characteristics:
                    print(f"Characteristic UUID: {char.uuid}")
    else:
        print(f"Target device ({target_device_address}) not found.")


# Usage example
target_device_address = "e4:70:b8:0c:f2:a5"  # Replace with the Bluetooth address of the target PC
loop = asyncio.get_event_loop()
loop.run_until_complete(discover_device_services(target_device_address))
