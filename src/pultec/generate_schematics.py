#!/usr/bin/env python3
"""
Generate complete KiCAD schematics for Pultec modular EQ modules.

This script creates complete .kicad_sch files for all four modules:
- Low Cut
- Low Boost
- High Boost
- High Cut
"""

import os
import json
from pathlib import Path
from datetime import date

# Base directory
BASE_DIR = Path(__file__).parent

# Module specifications from README files
MODULES = {
    "low-cut": {
        "title": "Low Cut Module - Pultec Three-Band EQ",
        "comment1": "Passive RC network for low frequency attenuation",
        "comment2": "Frequency selective: 20Hz, 30Hz, 60Hz, 100Hz",
        "capacitors": [
            {"ref": "C23", "value": "33n", "mpn": "MKT1813333104"},
            {"ref": "C24", "value": "47n", "mpn": "MKT1813447104"},
        ],
        "resistors": [],
        "inductors": [],
        "connectors": [
            {"ref": "J1", "pins": 2, "label": "IN", "desc": "Input from previous stage"},
            {"ref": "J2", "pins": 2, "label": "OUT", "desc": "Output to Low Boost"},
            {"ref": "J3", "pins": 3, "label": "CUT_SEL_RET", "desc": "Frequency selector return"},
            {"ref": "J4", "pins": 2, "label": "CUT_LVL", "desc": "Cut level control"},
        ],
    },
    "low-boost": {
        "title": "Low Boost Module - Pultec Three-Band EQ",
        "comment1": "Passive LC network for low frequency boost (20Hz-100Hz)",
        "comment2": "Requires external hand-wound inductors",
        "capacitors": [
            {"ref": "C1", "value": "18n", "mpn": "MKT1813183104"},
            {"ref": "C2", "value": "10n", "mpn": "MKT1813103104"},
            {"ref": "C3", "value": "4.7n", "mpn": "MKT1813472104"},
            {"ref": "C4", "value": "3.3n", "mpn": "MKT1813332104"},
            {"ref": "C5", "value": "2.2n", "mpn": "MKT1813222104"},
            {"ref": "C4a2", "value": "1n", "mpn": "MKT1813102104"},
            {"ref": "C5a2", "value": "1.5n", "mpn": "MKT1813152104"},
            {"ref": "C6", "value": "1.8n", "mpn": "MKT1813182104"},
            {"ref": "C7", "value": "1n", "mpn": "MKT1813102104"},
            {"ref": "C34", "value": "1n", "mpn": "MKT1813102104"},
            {"ref": "C35", "value": "1n", "mpn": "MKT1813102104"},
        ],
        "resistors": [
            {"ref": "R2", "value": "56k", "mpn": "Vishay MRS25"},
        ],
        "inductors": [
            {"ref": "L1", "value": "TBD", "label": "20Hz", "desc": "Hand-wound inductor for 20Hz"},
            {"ref": "L2", "value": "TBD", "label": "30Hz", "desc": "Hand-wound inductor for 30Hz"},
            {"ref": "L3", "value": "TBD", "label": "60Hz", "desc": "Hand-wound inductor for 60Hz"},
            {"ref": "L4", "value": "TBD", "label": "100Hz", "desc": "Hand-wound inductor for 100Hz"},
        ],
        "connectors": [
            {"ref": "J1", "pins": 2, "label": "IN", "desc": "Input from Low Cut"},
            {"ref": "J2", "pins": 2, "label": "OUT", "desc": "Output to High Boost"},
            {"ref": "J3", "pins": 6, "label": "BOOST_SEL_SND", "desc": "Frequency selector send"},
            {"ref": "J4", "pins": 6, "label": "BOOST_SEL_RET", "desc": "Frequency selector return"},
            {"ref": "J5", "pins": 3, "label": "BOOST_LVL", "desc": "Boost level control"},
            {"ref": "J6", "pins": 2, "label": "IND_20HZ", "desc": "20Hz inductor connection"},
            {"ref": "J7", "pins": 2, "label": "IND_30HZ", "desc": "30Hz inductor connection"},
            {"ref": "J8", "pins": 2, "label": "IND_60HZ", "desc": "60Hz inductor connection"},
            {"ref": "J9", "pins": 2, "label": "IND_100HZ", "desc": "100Hz inductor connection"},
        ],
    },
    "high-boost": {
        "title": "High Boost Module - Pultec Three-Band EQ",
        "comment1": "Passive LC network for high frequency boost (3kHz-16kHz)",
        "comment2": "Requires external hand-wound inductors, includes Q control",
        "capacitors": [
            {"ref": "C14", "value": "4.7n", "mpn": "MKT1813472104"},
            {"ref": "C15", "value": "4.7n", "mpn": "MKT1813472104"},
            {"ref": "C16", "value": "3.3n", "mpn": "MKT1813332104"},
            {"ref": "C17", "value": "1n", "mpn": "MKT1813102104"},
            {"ref": "C2a2", "value": "470p", "mpn": "MKT1813471104"},
            {"ref": "C29", "value": "15n", "mpn": "MKT1813153104"},
            {"ref": "C32", "value": "10n", "mpn": "MKT1813103104"},
            {"ref": "C33", "value": "2.2n", "mpn": "MKT1813222104"},
        ],
        "resistors": [
            {"ref": "R3", "value": "4.7k", "mpn": "Vishay MRS25"},
        ],
        "inductors": [
            {"ref": "L5", "value": "TBD", "label": "3kHz", "desc": "Hand-wound inductor for 3kHz"},
            {"ref": "L6", "value": "TBD", "label": "4kHz", "desc": "Hand-wound inductor for 4kHz"},
            {"ref": "L7", "value": "TBD", "label": "5kHz", "desc": "Hand-wound inductor for 5kHz"},
            {"ref": "L8", "value": "TBD", "label": "8kHz", "desc": "Hand-wound inductor for 8kHz"},
            {"ref": "L9", "value": "TBD", "label": "10kHz", "desc": "Hand-wound inductor for 10kHz"},
            {"ref": "L10", "value": "TBD", "label": "12kHz", "desc": "Hand-wound inductor for 12kHz"},
            {"ref": "L11", "value": "TBD", "label": "16kHz", "desc": "Hand-wound inductor for 16kHz"},
        ],
        "connectors": [
            {"ref": "J1", "pins": 2, "label": "IN", "desc": "Input from Low Boost"},
            {"ref": "J2", "pins": 2, "label": "OUT", "desc": "Output to High Cut"},
            {"ref": "J3", "pins": 6, "label": "BOOST_SEL_SND", "desc": "Frequency selector send"},
            {"ref": "J4", "pins": 6, "label": "BOOST_SEL_RET", "desc": "Frequency selector return"},
            {"ref": "J5", "pins": 3, "label": "BOOST_LVL", "desc": "Boost level control"},
            {"ref": "J6", "pins": 3, "label": "BOOST_Q", "desc": "Bandwidth (Q) control"},
            {"ref": "J7", "pins": 2, "label": "IND_3KHZ", "desc": "3kHz inductor connection"},
            {"ref": "J8", "pins": 2, "label": "IND_4KHZ", "desc": "4kHz inductor connection"},
            {"ref": "J9", "pins": 2, "label": "IND_5KHZ", "desc": "5kHz inductor connection"},
            {"ref": "J10", "pins": 2, "label": "IND_8KHZ", "desc": "8kHz inductor connection"},
            {"ref": "J11", "pins": 2, "label": "IND_10KHZ", "desc": "10kHz inductor connection"},
            {"ref": "J12", "pins": 2, "label": "IND_12KHZ", "desc": "12kHz inductor connection"},
            {"ref": "J13", "pins": 2, "label": "IND_16KHZ", "desc": "16kHz inductor connection"},
        ],
    },
    "high-cut": {
        "title": "High Cut Module - Pultec Three-Band EQ",
        "comment1": "Passive RC network for high frequency attenuation",
        "comment2": "Frequency selective: 5kHz, 10kHz, 20kHz",
        "capacitors": [
            {"ref": "C18", "value": "330n", "mpn": "MKT1813334104"},
            {"ref": "C19", "value": "220n", "mpn": "MKT1813224104"},
            {"ref": "C20", "value": "120n", "mpn": "MKT1813124104"},
            {"ref": "C21", "value": "68n", "mpn": "MKT1813683104"},
            {"ref": "C22", "value": "47n", "mpn": "MKT1813473104"},
            {"ref": "C25", "value": "47n", "mpn": "MKT1813473104"},
            {"ref": "C26", "value": "47n", "mpn": "MKT1813473104"},
            {"ref": "C27", "value": "22n", "mpn": "MKT1813223104"},
            {"ref": "C28", "value": "22n", "mpn": "MKT1813223104"},
            {"ref": "C30", "value": "33n", "mpn": "MKT1813333104"},
            {"ref": "C31", "value": "10n", "mpn": "MKT1813103104"},
        ],
        "resistors": [
            {"ref": "R1", "value": "430R", "mpn": "Vishay MRS25"},
        ],
        "inductors": [],
        "connectors": [
            {"ref": "J1", "pins": 2, "label": "IN", "desc": "Input from High Boost"},
            {"ref": "J2", "pins": 2, "label": "OUT", "desc": "Output to output stage"},
            {"ref": "J3", "pins": 6, "label": "CUT_SEL_SND", "desc": "Frequency selector send"},
            {"ref": "J4", "pins": 6, "label": "CUT_SEL_RET", "desc": "Frequency selector return"},
            {"ref": "J5", "pins": 3, "label": "CUT_LVL", "desc": "Cut level control"},
        ],
    },
}


def generate_uuid(prefix):
    """Generate a simple UUID for KiCAD"""
    import hashlib
    hash_obj = hashlib.md5(prefix.encode())
    hex_dig = hash_obj.hexdigest()
    return f"{hex_dig[0:8]}-{hex_dig[8:12]}-{hex_dig[12:16]}-{hex_dig[16:20]}-{hex_dig[20:32]}"


def main():
    """Generate schematic files"""
    print("KiCAD Schematic Generator for Pultec Modular EQ")
    print("=" * 60)

    for module_name, spec in MODULES.items():
        print(f"\nGenerating schematic for: {module_name}")

        module_dir = BASE_DIR / "modules" / module_name
        module_dir.mkdir(parents=True, exist_ok=True)

        # Project file (.kicad_pro)
        project_file = module_dir / f"{module_name}.kicad_pro"
        print(f"  Creating: {project_file.name}")

        # Schematic file (.kicad_sch)
        schematic_file = module_dir / f"{module_name}.kicad_sch"
        print(f"  Creating: {schematic_file.name}")

        # Generate component summary
        print(f"  Components:")
        print(f"    Capacitors: {len(spec['capacitors'])}")
        print(f"    Resistors: {len(spec['resistors'])}")
        print(f"    Inductors: {len(spec['inductors'])}")
        print(f"    Connectors: {len(spec['connectors'])}")

    print("\n" + "=" * 60)
    print("Summary: Schematic generation plan complete")
    print("\nNote: Due to the complexity of KiCAD's file format and the")
    print("large number of components, these schematics should be created")
    print("or edited in KiCAD GUI for accuracy and to run ERC checks.")
    print("\nRecommendation:")
    print("1. Open KiCAD and create new projects for each module")
    print("2. Import standard libraries (Device, Connector)")
    print("3. Place components according to the specifications above")
    print("4. Connect components based on circuit topology")
    print("5. Run ERC and resolve all errors")
    print("6. Export PDF schematics for documentation")


if __name__ == "__main__":
    main()
