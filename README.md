# Containment Checker

A formal verification tool for Sequential Function Charts (SFC) that provides automated containment checking, LLM-based code generation, and comprehensive benchmarking capabilities.

## Overview

The Containment Checker is designed to analyze and verify Sequential Function Charts (SFC) - a graphical programming language commonly used in industrial automation and control systems. The tool provides:

- **Formal Verification**: Uses Z3 theorem prover to check containment relationships between SFCs
- **LLM-based Code Generation**: Generates upgraded SFC code using Azure OpenAI
- **Benchmark Suite**: Comprehensive collection of SFC examples for testing and validation
- **Visualization**: Generates DOT/PNG diagrams of SFC structures and Petri nets

## Features

### Core Functionality

1. **SFC to Petri Net Conversion**: Converts Sequential Function Charts to Petri nets for formal analysis
2. **Containment Verification**: Checks if one SFC is contained within another using formal methods
3. **Cut-point Analysis**: Identifies critical control points in SFC execution paths
4. **HTML Reports**: Generates detailed verification reports with visualizations

### Code Generation

- **LLM Integration**: Uses Azure OpenAI to generate upgraded SFC code
- **Template-based Upgrades**: Supports predefined upgrade patterns (factorial, decimal-to-hex conversion)
- **Automated Code Enhancement**: Adds features like loop tracking, error handling, and cleanup mechanisms

### Benchmarking

- **Mathematical Algorithms**: Factorial, Fibonacci, GCD, LCM, prime checking
- **String/Number Operations**: Palindrome check, digit counting, number reversal
- **Control Logic**: OSCAT-compatible industrial control examples
- **Timer Functions**: Delay timers, edge detection, pulse generation

## Installation

### Prerequisites

- Python 3.8 or higher
- Graphviz (for visualization)
- Azure OpenAI API access (for LLM features)

### Required Dependencies

```bash
pip install -r requirements.txt
```

### Environment Setup

1. Create a `.env` file in the project root:
```bash
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
```

2. Install Graphviz for visualization:
```bash
# On macOS
brew install graphviz

# On Ubuntu/Debian
sudo apt-get install graphviz

# On Windows
# Download from https://graphviz.org/download/
```

## Usage

### Basic SFC Verification

```python
from Verifier import SFC, check_pn_containment_html

# Define an SFC
steps = [
    {"name": "Start", "function": "i := 1; fact := 1"},
    {"name": "Check", "function": ""},
    {"name": "Multiply", "function": "fact := fact * i"},
    {"name": "Increment", "function": "i := i + 1"},
    {"name": "End", "function": ""}
]

transitions = [
    {"src": "Start", "tgt": "Check", "guard": "init"},
    {"src": "Check", "tgt": "Multiply", "guard": "i <= n"},
    {"src": "Multiply", "tgt": "Increment", "guard": "True"},
    {"src": "Increment", "tgt": "Check", "guard": "True"},
    {"src": "Check", "tgt": "End", "guard": "i > n"}
]

sfc = SFC(
    steps=steps,
    variables=["i", "fact", "n", "init"],
    transitions=transitions,
    initial_step="Start"
)

# Generate verification report
check_pn_containment_html(sfc1, pn1, sfc2, pn2)
```

### LLM-based Code Generation

```bash
# Generate upgraded SFC code
python LLM_Manager.py SFC_FACT.txt
```

This will:
1. Read the input SFC from the specified file
2. Send it to Azure OpenAI for upgrading
3. Generate an enhanced version with additional features
4. Save the result to a `*_Generated.txt` file

### Running Benchmarks

```python
from Benchmarks import sfc_examples
from Verifier import SFC

# Access predefined benchmark examples
factorial_example = sfc_examples[0]  # Factorial computation
fibonacci_example = sfc_examples[1]  # Fibonacci sequence

# Create SFC instances
sfc = SFC(
    steps=factorial_example["steps"],
    variables=factorial_example["variables"],
    transitions=factorial_example["transitions"],
    initial_step=factorial_example["steps"][0]["name"]
)
```

## Project Structure

```
Containmentchecker/
├── README.md                      # This file
├── requirements.txt              # Python dependencies
├── LLM_Manager.py               # Azure OpenAI integration
├── Verifier.py                  # Core verification engine
├── Benchmarks.py                # Mathematical algorithm examples
├── Benchmark-OSCAT-Name.py      # Industrial control examples
├── BenchMrk-OSCAT.py           # Additional OSCAT benchmarks
├── SFC_FACT.txt                # Factorial SFC example
├── SFC_TLC.txt                 # Traffic light control example
├── SFC-DEC_TO_HEX.txt          # Decimal to hex conversion example
└── PromptForUpgrade.txt        # LLM upgrade prompt template
```

## Key Components

### SFC Class

The core data structure representing Sequential Function Charts:

```python
class SFC:
    def __init__(self, steps, variables, transitions, initial_step):
        self.steps = steps              # List of steps with names and functions
        self.variables = variables      # List of variable names
        self.transitions = transitions  # List of transitions with guards
        self.initial_step = initial_step # Starting step name
```

### Verification Engine

The `Verifier.py` module provides:

- **Petri Net Conversion**: `sfc_to_petrinet(sfc)`
- **Cut-point Analysis**: `find_cut_points(pn)`
- **Path Analysis**: `cutpoint_to_cutpoint_paths_with_conditions()`
- **Z3 Integration**: Formal verification using satisfiability solving
- **HTML Report Generation**: `check_pn_containment_html()`

### LLM Manager

The `LLM_Manager.py` module handles:

- Azure OpenAI API integration
- SFC code generation and upgrades
- Error handling for API failures
- Streaming responses for real-time feedback

## Example SFC Formats

### Factorial Computation

```python
steps = [
    {"name": "Start", "function": "i := 1; fact := 1"},
    {"name": "Check", "function": ""},
    {"name": "Multiply", "function": "fact := fact * i"},
    {"name": "Increment", "function": "i := i + 1"},
    {"name": "End", "function": ""}
]
```

### Traffic Light Control

```python
steps = [
    {"name": "NormalOperation", "function": "GreenLight := True; YellowLight := False; RedLight := False"},
    {"name": "Pedestrian", "function": "GreenLight := False; YellowLight := True; RedLight := False"},
    {"name": "Emergency", "function": "GreenLight := False; YellowLight := False; RedLight := True"}
]
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built using the Z3 theorem prover for formal verification
- Integrates with Azure OpenAI for intelligent code generation
- Inspired by industrial automation and control system requirements
- Supports OSCAT (Open Source Community for Automation Technology) standards

## Support

For questions, bug reports, or feature requests, please open an issue in the repository.