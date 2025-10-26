# High Cut Module - Pultec Three-Band EQ

## Overview
The High Cut module provides frequency-selective attenuation in the high frequency range, typically covering 5kHz, 10kHz, and 20kHz. This is a passive RC network that reduces high-frequency content for taming brightness or harshness.

## Circuit Description
The high cut section uses a capacitor network to create frequency-selective attenuation. Different capacitor values are selected via a rotary switch to target specific frequencies. The attenuation pad resistor (R1) provides loading for the network.

## Components

### Capacitors (Film, Non-Polarized)
- C18: 330nF
- C19: 220nF
- C20: 120nF
- C21: 68nF
- C22: 47nF
- C25: 47nF
- C26: 47nF
- C27: 22nF
- C28: 22nF
- C30: 33nF
- C31: 10nF

### Resistors
- R1: 430Ω, 1/4W, 1%

### Connectors (Screw Terminals)
- J_IN: Signal input from previous stage
- J_OUT: Signal output to next stage (output amplifier)
- J_CUT_SEL_SND: High cut frequency selector send
- J_CUT_SEL_RET: High cut frequency selector return
- J_CUT_LVL: High cut level control connection
- J_GND: Ground connection

### Controls
- Cut Level: Variable control (external potentiometer)
- Frequency Selector: Rotary switch (external)

## Interface Specifications

### Input
- Impedance: Matches High Boost module output
- Connection: 2-position screw terminal (Signal, Ground)

### Output
- Impedance: Feeds into output amplifier stage
- Connection: 2-position screw terminal (Signal, Ground)

### Control Connections
- Frequency Selector Send: 6-position screw terminal
- Frequency Selector Return: 6-position screw terminal
- Level Control: 3-position screw terminal

## PCB Specifications
- Board Size: TBD (moderate size due to component count)
- Layer Count: 2-layer
- Mounting: 4x mounting holes, M3 size
- Connector Type: Screw terminals throughout

## Bill of Materials

| Ref | Qty | Value | Description | Suggested P/N |
|-----|-----|-------|-------------|---------------|
| C18 | 1 | 330nF | Film capacitor, 5%, 100V | Vishay MKT1813334104 |
| C19 | 1 | 220nF | Film capacitor, 5%, 100V | Vishay MKT1813224104 |
| C20 | 1 | 120nF | Film capacitor, 5%, 100V | Vishay MKT1813124104 |
| C21 | 1 | 68nF | Film capacitor, 5%, 100V | Vishay MKT1813683104 |
| C22 | 1 | 47nF | Film capacitor, 5%, 100V | Vishay MKT1813473104 |
| C25 | 1 | 47nF | Film capacitor, 5%, 100V | Vishay MKT1813473104 |
| C26 | 1 | 47nF | Film capacitor, 5%, 100V | Vishay MKT1813473104 |
| C27 | 1 | 22nF | Film capacitor, 5%, 100V | Vishay MKT1813223104 |
| C28 | 1 | 22nF | Film capacitor, 5%, 100V | Vishay MKT1813223104 |
| C30 | 1 | 33nF | Film capacitor, 5%, 100V | Vishay MKT1813333104 |
| C31 | 1 | 10nF | Film capacitor, 5%, 100V | Vishay MKT1813103104 |
| R1 | 1 | 430Ω | Metal film resistor, 1/4W, 1% | Vishay MRS25 |
| J_IN | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_OUT | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_CUT_SEL_SND | 1 | 6-pos | Screw terminal 5.08mm | Phoenix 1757025 |
| J_CUT_SEL_RET | 1 | 6-pos | Screw terminal 5.08mm | Phoenix 1757025 |
| J_CUT_LVL | 1 | 3-pos | Screw terminal 5.08mm | Phoenix 1757022 |
| J_GND | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |

## Assembly Notes
1. Install screw terminals first
2. Install resistor R1 (provides attenuation pad)
3. Install capacitors in order (C18-C31)
4. Verify all solder joints carefully
5. Label selector terminals clearly

## Testing Procedure
1. Visual inspection of all solder joints
2. Continuity test: Verify correct routing between selector positions
3. Resistance test: Verify R1 value, check for shorts
4. Capacitance test: Verify capacitor values if possible
5. Integration test: Connect to High Boost output and verify signal flow
6. Frequency response test: Verify attenuation at selected frequencies

## Integration
- Connects between: High Boost → **High Cut** → Output Stage
- External connections required:
  - Frequency selector switch (rotary, 6+ positions)
  - Cut level potentiometer

## Notes on High Cut Design
The high cut section uses a resistive pad (R1 = 430Ω) to load the network. This resistor is critical for proper operation of the frequency-selective attenuation. The multiple capacitors with similar values (e.g., three 47nF caps) may be used in parallel or series configurations depending on the selected frequency.

## Revision History
- v1.0: Initial design extracted from monolithic schematic
