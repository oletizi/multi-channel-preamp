# Low Cut Module - Pultec Three-Band EQ

## Overview
The Low Cut module provides frequency-selective attenuation in the low frequency range, typically covering 20Hz, 30Hz, 60Hz, and 100Hz. This is a passive RC network that reduces low-frequency content.

## Circuit Description
The low cut section uses a capacitor network to create frequency-selective attenuation. Different capacitor values are selected via a rotary switch to target specific frequencies.

## Components

### Capacitors (Film, Non-Polarized)
- C23: 33nF
- C24: 47nF

### Connectors (Screw Terminals)
- J_IN: Signal input from previous stage
- J_OUT: Signal output to next stage
- J_CUT_SEL_RET: Low cut frequency selector return
- J_CUT_LVL: Low cut level control connection
- J_GND: Ground connection

### Controls
- Cut Level: Variable control (external potentiometer)
- Frequency Selector: Rotary switch (external)

## Interface Specifications

### Input
- Impedance: Matches output stage impedance
- Connection: 2-position screw terminal (Signal, Ground)

### Output
- Impedance: Feeds into next module or output stage
- Connection: 2-position screw terminal (Signal, Ground)

### Control Connections
- Frequency Selector Return: 3-position screw terminal
- Level Control: 2-position screw terminal

## PCB Specifications
- Board Size: TBD (optimize for components)
- Layer Count: 2-layer
- Mounting: 4x mounting holes, M3 size
- Connector Type: Screw terminals throughout

## Bill of Materials

| Ref | Qty | Value | Description | Suggested P/N |
|-----|-----|-------|-------------|---------------|
| C23 | 1 | 33nF | Film capacitor, 5%, 100V | Vishay MKT1813333104 |
| C24 | 1 | 47nF | Film capacitor, 5%, 100V | Vishay MKT1813447104 |
| J_IN | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_OUT | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_CUT_SEL_RET | 1 | 3-pos | Screw terminal 5.08mm | Phoenix 1757022 |
| J_CUT_LVL | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_GND | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |

## Assembly Notes
1. Install screw terminals first
2. Install capacitors (observe orientation markings if any)
3. Verify all solder joints
4. Test continuity before integration

## Testing Procedure
1. Visual inspection of solder joints
2. Continuity test: IN to OUT (should show capacitive coupling)
3. Resistance test: Verify no shorts to ground
4. Integration test: Connect to input/output stages and verify signal flow

## Integration
- Connects between: Input stage → Low Cut → Low Boost → High Boost → High Cut → Output stage
- External connections required: Frequency selector switch, level control potentiometer

## Revision History
- v1.0: Initial design extracted from monolithic schematic
