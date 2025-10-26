# Claude Agent SDK - Specialized Agents for Circuit Design

This directory contains specialized Claude Code agents designed for electronics and PCB design work, specifically optimized for the Pultec-style three-band EQ project.

## Available Agents

### 1. circuit-design-specialist
**Use when**: Analyzing circuits, calculating component values, designing filter networks

**Capabilities**:
- Passive filter design (RC, LC networks)
- Audio circuit analysis and validation
- Component value calculations for specific frequency responses
- Pultec-style EQ topology expertise
- Impedance matching and signal flow analysis

**Example invocations**:
```
"Use the circuit-design-specialist to calculate the required inductance for a 60Hz boost with a 220nF capacitor"

"Ask the circuit-design-specialist to analyze the low-boost section and verify the frequency response"

"Have the circuit-design-specialist validate the impedance matching between modules"
```

### 2. pcb-layout-engineer
**Use when**: Designing PCB layouts, optimizing component placement, routing audio signals

**Capabilities**:
- PCB layout design for low-noise audio circuits
- Component placement optimization
- Ground plane design and star grounding implementation
- Audio-specific routing best practices
- Design rule management for manufacturability

**Example invocations**:
```
"Use the pcb-layout-engineer to create a layout for the low-cut module"

"Ask the pcb-layout-engineer to optimize the ground plane strategy for minimal noise"

"Have the pcb-layout-engineer review the component placement for signal flow"
```

### 3. inductor-design-specialist
**Use when**: Designing hand-wound inductors, calculating inductor specifications, selecting cores

**Capabilities**:
- Inductance calculations for LC resonance
- Core material selection (air, powdered iron, ferrite, steel)
- Wire gauge selection and DCR calculations
- Q factor optimization
- Winding instructions and specifications
- Test procedures for inductors

**Example invocations**:
```
"Use the inductor-design-specialist to design a 60Hz boost inductor for use with a 220nF capacitor"

"Ask the inductor-design-specialist to specify cores and wire for all low-boost section inductors"

"Have the inductor-design-specialist calculate the expected Q factor for the high-boost inductors"
```

### 4. kicad-expert
**Use when**: Working with KiCAD software, creating schematics, generating Gerbers

**Capabilities**:
- KiCAD schematic creation and editing
- PCB layout in KiCAD
- Custom symbol and footprint creation
- Gerber file generation for manufacturing
- Library management
- KiCAD Python scripting

**Example invocations**:
```
"Use the kicad-expert to create a schematic for the low-cut module from the component list"

"Ask the kicad-expert to generate Gerber files for PCB fabrication"

"Have the kicad-expert create a custom footprint for Phoenix Contact 1757 screw terminals"
```

### 5. bom-and-sourcing
**Use when**: Creating BOMs, sourcing components, finding part numbers, pricing analysis

**Capabilities**:
- Complete BOM generation from schematics
- Component sourcing from Mouser, Digikey, etc.
- Exact manufacturer part number research
- Availability checking and pricing analysis
- Alternative component suggestions
- Cost optimization and quantity breaks

**Example invocations**:
```
"Use the bom-and-sourcing agent to verify current pricing for all module components"

"Ask bom-and-sourcing to create a consolidated purchase order for all four modules"

"Have bom-and-sourcing find alternatives for any out-of-stock components"
```

## How to Use These Agents

### In Claude Code CLI
When working in the Claude Code environment, you can invoke these agents using the Task tool:

```
"I need to design inductors for the low boost section. Use the inductor-design-specialist agent."
```

Claude Code will automatically:
1. Recognize the agent request
2. Load the appropriate agent with its specialized knowledge
3. Execute the task using the agent's expertise
4. Return the results to you

### Agent Collaboration
Agents can work together on complex tasks:

```
"First use circuit-design-specialist to calculate inductor values,
then use inductor-design-specialist to design the actual windings,
then use bom-and-sourcing to source the wire and cores"
```

### Programmatic Usage (TypeScript SDK)
```typescript
import { query } from '@anthropic-ai/claude-agent-sdk';

const result = await query({
  prompt: "Design a 60Hz boost inductor with 220nF capacitor",
  options: {
    agents: {
      'inductor-design-specialist': {
        description: "Designs inductors for audio applications",
        // ... loaded from .claude/agents/inductor-design-specialist.md
      }
    }
  }
});
```

## Agent Tool Access

Each agent has specific tools they can use:

| Agent | Read | Write | Edit | Grep | Glob | Bash | WebFetch | WebSearch |
|-------|------|-------|------|------|------|------|----------|-----------|
| circuit-design-specialist | ✓ | | | ✓ | ✓ | | ✓ | ✓ |
| pcb-layout-engineer | ✓ | ✓ | | ✓ | ✓ | ✓ | | |
| inductor-design-specialist | ✓ | | | ✓ | ✓ | ✓ | ✓ | ✓ |
| kicad-expert | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| bom-and-sourcing | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ |

This tool scoping ensures each agent has exactly what it needs while maintaining security and focus.

## Model Selection

All agents use `model: sonnet` by default, providing:
- Fast response times
- Cost-effective operation
- Sufficient capability for specialized tasks
- Consistent behavior across agents

You can override the model in your invocation if needed:
```typescript
options: {
  agents: {
    'circuit-design-specialist': {
      model: 'opus', // Use more powerful model for complex calculations
      // ...
    }
  }
}
```

## Best Practices

### When to Use Which Agent

**Circuit Design Phase**:
1. Start with `circuit-design-specialist` for topology and calculations
2. Use `inductor-design-specialist` for passive component specifications
3. Consult `bom-and-sourcing` for component availability

**PCB Design Phase**:
1. `kicad-expert` creates the schematic
2. `circuit-design-specialist` validates the design
3. `pcb-layout-engineer` creates the layout
4. `kicad-expert` generates manufacturing files

**Procurement Phase**:
1. `bom-and-sourcing` creates complete BOM
2. `bom-and-sourcing` finds part numbers and pricing
3. `inductor-design-specialist` specifies custom components

### Agent Chaining
Complex workflows benefit from agent chaining:

```
User: "Design the complete low-boost module from scratch"

Claude Code orchestration:
1. circuit-design-specialist: Validate circuit topology
2. inductor-design-specialist: Design 4 inductors
3. kicad-expert: Create schematic
4. pcb-layout-engineer: Design PCB layout
5. kicad-expert: Generate Gerbers
6. bom-and-sourcing: Create complete BOM with pricing
```

### Parallel Agent Execution
For independent tasks, agents can work in parallel:

```
"Run in parallel:
- inductor-design-specialist: Design low-boost inductors
- bom-and-sourcing: Source capacitors for all modules
- circuit-design-specialist: Validate high-cut frequency response"
```

## Customizing Agents

You can modify these agents by editing their markdown files:

1. **Add project-specific context**: Include references to your specific designs
2. **Adjust tool access**: Add or remove tools in the YAML frontmatter
3. **Refine behavior**: Update the system prompt for different working styles
4. **Change model**: Switch between sonnet, opus, haiku as needed

## Project-Specific Context

All agents are pre-loaded with knowledge about:
- The modular Pultec three-band EQ architecture
- Location of schematics and documentation
- Component specifications and requirements
- Ian Thompson-Bell's reference documentation
- Modular design philosophy using screw terminals

## Troubleshooting

**Agent not found**: Ensure the `.md` file is in `.claude/agents/` directory

**Permission errors**: Check that the agent has the required tools in its YAML frontmatter

**Unexpected behavior**: Review the agent's system prompt in the `.md` file

**Context issues**: Make sure project files are accessible to the agent's allowed tools

## Contributing

To add new agents for this project:

1. Create a new `.md` file in `.claude/agents/`
2. Add YAML frontmatter with name, description, tools, model
3. Write a detailed system prompt explaining the agent's expertise
4. Update this README with the new agent's capabilities
5. Test the agent with example invocations

## Version History

- v1.0 (2025-10-25): Initial agent set for Pultec EQ project
  - circuit-design-specialist
  - pcb-layout-engineer
  - inductor-design-specialist
  - kicad-expert
  - bom-and-sourcing
