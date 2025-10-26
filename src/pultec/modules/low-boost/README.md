# Low Boost Module - Pultec Three-Band EQ

## Overview
The Low Boost module provides frequency-selective boost in the low frequency range, typically covering 20Hz, 30Hz, 60Hz, and 100Hz. This is a passive LC network that enhances low-frequency content using inductors and capacitors.

## Circuit Description
The low boost section uses a capacitor and inductor network to create frequency-selective boost. Different capacitor values are selected via a rotary switch to target specific frequencies, while inductors (hand-wound, externally connected) provide the resonant boost characteristic.

## Components

### Capacitors (Film, Non-Polarized)
- C1: 18nF
- C2: 10nF
- C3: 4.7nF
- C4: 3.3nF
- C5: 2.2nF
- C4a2: 1nF (alternate position)
- C5a2: 1.5nF (alternate position)
- C6: 1.8nF
- C7: 1nF
- C34: 1nF
- C35: 1nF

### Resistors
- R2: 56kΩ, 1/4W, 1%

### Connectors (Screw Terminals)
- J_IN: Signal input from previous stage
- J_OUT: Signal output to next stage
- J_BOOST_SEL_SND: Low boost frequency selector send
- J_BOOST_SEL_RET: Low boost frequency selector return
- J_CUT_SEL_SND: Low cut selector send (interface)
- J_BOOST_LVL: Low boost level control connection
- J_INDUCTOR: Inductor connection terminals (multiple positions for different frequencies)
- J_GND: Ground connection

### Controls
- Boost Level: Variable control (external potentiometer)
- Frequency Selector: Rotary switch (external)

### External Components (Not on PCB)
- Inductors: Hand-wound, values TBD based on frequency selection
  - 20Hz: TBD mH
  - 30Hz: TBD mH
  - 60Hz: TBD mH
  - 100Hz: TBD mH

## Interface Specifications

### Input
- Impedance: Matches previous stage output
- Connection: 2-position screw terminal (Signal, Ground)

### Output
- Impedance: Feeds into High Boost module
- Connection: 2-position screw terminal (Signal, Ground)

### Control Connections
- Frequency Selector Send: 6-position screw terminal
- Frequency Selector Return: 6-position screw terminal
- Level Control: 3-position screw terminal
- Inductor Connections: Multiple 2-position terminals (one per frequency)

## PCB Specifications
- Board Size: TBD (larger due to component count)
- Layer Count: 2-layer
- Mounting: 4x mounting holes, M3 size
- Connector Type: Screw terminals throughout

## Bill of Materials

| Ref | Qty | Value | Description | Suggested P/N |
|-----|-----|-------|-------------|---------------|
| C1 | 1 | 18nF | Film capacitor, 5%, 100V | Vishay MKT1813183104 |
| C2 | 1 | 10nF | Film capacitor, 5%, 100V | Vishay MKT1813103104 |
| C3 | 1 | 4.7nF | Film capacitor, 5%, 100V | Vishay MKT1813472104 |
| C4 | 1 | 3.3nF | Film capacitor, 5%, 100V | Vishay MKT1813332104 |
| C5 | 1 | 2.2nF | Film capacitor, 5%, 100V | Vishay MKT1813222104 |
| C4a2 | 1 | 1nF | Film capacitor, 5%, 100V | Vishay MKT1813102104 |
| C5a2 | 1 | 1.5nF | Film capacitor, 5%, 100V | Vishay MKT1813152104 |
| C6 | 1 | 1.8nF | Film capacitor, 5%, 100V | Vishay MKT1813182104 |
| C7 | 1 | 1nF | Film capacitor, 5%, 100V | Vishay MKT1813102104 |
| C34 | 1 | 1nF | Film capacitor, 5%, 100V | Vishay MKT1813102104 |
| C35 | 1 | 1nF | Film capacitor, 5%, 100V | Vishay MKT1813102104 |
| R2 | 1 | 56kΩ | Metal film resistor, 1/4W, 1% | Vishay MRS25 |
| J_IN | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_OUT | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_BOOST_SEL_SND | 1 | 6-pos | Screw terminal 5.08mm | Phoenix 1757025 |
| J_BOOST_SEL_RET | 1 | 6-pos | Screw terminal 5.08mm | Phoenix 1757025 |
| J_CUT_SEL_SND | 1 | 3-pos | Screw terminal 5.08mm | Phoenix 1757022 |
| J_BOOST_LVL | 1 | 3-pos | Screw terminal 5.08mm | Phoenix 1757022 |
| J_IND_20HZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_30HZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_60HZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_100HZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_GND | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |

## Assembly Notes
1. Install screw terminals first (many on this board)
2. Install resistor R2
3. Install capacitors in order (C1-C7, C34, C35, C4a2, C5a2)
4. Verify all solder joints carefully
5. Label inductor terminals clearly (20Hz, 30Hz, 60Hz, 100Hz)

## Testing Procedure
1. Visual inspection of all solder joints
2. Continuity test: Verify correct routing between selector positions
3. Resistance test: Verify R2 value, check for shorts
4. Capacitance test: Verify capacitor values if possible
5. Integration test: Connect external inductors and verify frequency response

## Inductor Specifications
The inductors for this module must be hand-wound to the following specifications:
- Core type: TBD (powdered iron or ferrite)
- Wire gauge: TBD
- Inductance values: TBD (calculated for target frequencies)
- DC resistance: Low as possible
- Test procedure: Measure with LCR meter

## Integration
- Connects between: Low Cut → **Low Boost** → High Boost
- External connections required:
  - Frequency selector switch (6-position rotary)
  - Boost level potentiometer
  - 4x hand-wound inductors (20Hz, 30Hz, 60Hz, 100Hz)

## Revision History
- v1.0: Initial design extracted from monolithic schematic
