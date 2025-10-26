# High Boost Module - Pultec Three-Band EQ

## Overview
The High Boost module provides frequency-selective boost in the high frequency range, typically covering 3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, and 16kHz. This is a passive LC network with bandwidth (Q) control, providing the classic Pultec high-frequency enhancement.

## Circuit Description
The high boost section uses a capacitor and inductor network to create frequency-selective boost with adjustable bandwidth. Different capacitor values are selected via a rotary switch to target specific frequencies, while inductors (hand-wound, externally connected) provide the resonant boost characteristic. The Q control allows adjustment of the boost bandwidth.

## Components

### Capacitors (Film, Non-Polarized)
- C14: 4.7nF
- C15: 4.7nF
- C16: 3.3nF
- C17: 1nF
- C2a2: 470pF
- C29: 15nF
- C32: 10nF
- C33: 2.2nF

### Resistors
- R3: 4.7kΩ, 1/4W, 1%

### Connectors (Screw Terminals)
- J_IN: Signal input from previous stage
- J_OUT: Signal output to next stage
- J_BOOST_SEL_SND: High boost frequency selector send
- J_BOOST_SEL_RET: High boost frequency selector return
- J_BOOST_LVL: High boost level control connection
- J_BOOST_L_SND: High boost level send
- J_BOOST_Q: High boost bandwidth (Q) control connection
- J_INDUCTOR: Inductor connection terminals (multiple positions for different frequencies)
- J_GND: Ground connection

### Controls
- Boost Level: Variable control (external potentiometer)
- Bandwidth (Q): Variable control (external potentiometer)
- Frequency Selector: Rotary switch (external)

### External Components (Not on PCB)
- Inductors: Hand-wound, values TBD based on frequency selection
  - 3kHz: TBD mH
  - 4kHz: TBD mH
  - 5kHz: TBD mH
  - 8kHz: TBD mH
  - 10kHz: TBD mH
  - 12kHz: TBD mH
  - 16kHz: TBD mH

## Interface Specifications

### Input
- Impedance: Matches Low Boost module output
- Connection: 2-position screw terminal (Signal, Ground)

### Output
- Impedance: Feeds into High Cut module
- Connection: 2-position screw terminal (Signal, Ground)

### Control Connections
- Frequency Selector Send: 6-position screw terminal
- Frequency Selector Return: 6-position screw terminal
- Level Control: 3-position screw terminal
- Bandwidth (Q) Control: 3-position screw terminal
- Inductor Connections: Multiple 2-position terminals (one per frequency)

## PCB Specifications
- Board Size: TBD (moderate size due to component count)
- Layer Count: 2-layer
- Mounting: 4x mounting holes, M3 size
- Connector Type: Screw terminals throughout

## Bill of Materials

| Ref | Qty | Value | Description | Suggested P/N |
|-----|-----|-------|-------------|---------------|
| C14 | 1 | 4.7nF | Film capacitor, 5%, 100V | Vishay MKT1813472104 |
| C15 | 1 | 4.7nF | Film capacitor, 5%, 100V | Vishay MKT1813472104 |
| C16 | 1 | 3.3nF | Film capacitor, 5%, 100V | Vishay MKT1813332104 |
| C17 | 1 | 1nF | Film capacitor, 5%, 100V | Vishay MKT1813102104 |
| C2a2 | 1 | 470pF | Film capacitor, 5%, 100V | Vishay MKT1813471104 |
| C29 | 1 | 15nF | Film capacitor, 5%, 100V | Vishay MKT1813153104 |
| C32 | 1 | 10nF | Film capacitor, 5%, 100V | Vishay MKT1813103104 |
| C33 | 1 | 2.2nF | Film capacitor, 5%, 100V | Vishay MKT1813222104 |
| R3 | 1 | 4.7kΩ | Metal film resistor, 1/4W, 1% | Vishay MRS25 |
| J_IN | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_OUT | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_BOOST_SEL_SND | 1 | 6-pos | Screw terminal 5.08mm | Phoenix 1757025 |
| J_BOOST_SEL_RET | 1 | 6-pos | Screw terminal 5.08mm | Phoenix 1757025 |
| J_BOOST_LVL | 1 | 3-pos | Screw terminal 5.08mm | Phoenix 1757022 |
| J_BOOST_L_SND | 1 | 3-pos | Screw terminal 5.08mm | Phoenix 1757022 |
| J_BOOST_Q | 1 | 3-pos | Screw terminal 5.08mm | Phoenix 1757022 |
| J_IND_3KHZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_4KHZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_5KHZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_8KHZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_10KHZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_12KHZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_IND_16KHZ | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |
| J_GND | 1 | 2-pos | Screw terminal 5.08mm | Phoenix 1757019 |

## Assembly Notes
1. Install screw terminals first (many on this board)
2. Install resistor R3
3. Install capacitors in order (C14-C17, C2a2, C29, C32, C33)
4. Verify all solder joints carefully
5. Label inductor terminals clearly (3kHz through 16kHz)

## Testing Procedure
1. Visual inspection of all solder joints
2. Continuity test: Verify correct routing between selector positions
3. Resistance test: Verify R3 value, check for shorts
4. Capacitance test: Verify capacitor values if possible
5. Integration test: Connect external inductors and verify frequency response
6. Q control test: Verify bandwidth control affects boost width

## Inductor Specifications
The inductors for this module must be hand-wound to the following specifications:
- Core type: TBD (powdered iron or ferrite)
- Wire gauge: TBD (likely smaller than low-frequency inductors)
- Inductance values: TBD (calculated for target frequencies, typically smaller than low-frequency inductors)
- DC resistance: Low as possible
- Test procedure: Measure with LCR meter

## Integration
- Connects between: Low Boost → **High Boost** → High Cut
- External connections required:
  - Frequency selector switch (rotary, 7+ positions)
  - Boost level potentiometer
  - Bandwidth (Q) control potentiometer
  - 7x hand-wound inductors (3kHz, 4kHz, 5kHz, 8kHz, 10kHz, 12kHz, 16kHz)

## Revision History
- v1.0: Initial design extracted from monolithic schematic
