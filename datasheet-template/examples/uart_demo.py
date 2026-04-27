#!/usr/bin/env python3
"""UART register access demo used by the datasheet examples."""

from __future__ import annotations

import argparse

try:
    import serial
except ImportError:  # pragma: no cover - example fallback
    serial = None


def open_port(device: str, baudrate: int):
    if serial is None:
        raise RuntimeError("pyserial is required to run this example")
    return serial.Serial(device, baudrate=baudrate, timeout=1)


# tag::read_reg[]
def read_reg(port, address):
    port.write(f"READ {address:#06x}\n".encode())
    return port.readline().decode().strip()
# end::read_reg[]


def write_reg(port, address, value):
    port.write(f"WRITE {address:#06x} {value:#010x}\n".encode())
    return port.readline().decode().strip()


def parse_int(value: str) -> int:
    return int(value, 0)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read a register over UART.")
    parser.add_argument("--port", required=True, help="Serial port device")
    parser.add_argument("--baudrate", type=int, default=115200)
    parser.add_argument("--address", type=parse_int, required=True)
    args = parser.parse_args()

    with open_port(args.port, args.baudrate) as port:
        print(read_reg(port, args.address))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
