# Containment Checker

A formal verification tool for Sequential Function Charts (SFC) with automated containment checking, LLM-based code generation, and comprehensive benchmarking.

## Features

- **Formal Verification**: Uses Z3 theorem prover to check SFC containment relationships
- **LLM Code Generation**: Generates upgraded SFC code using Azure OpenAI
- **SFC to Petri Net Conversion**: Converts SFCs to Petri nets for formal analysis
- **Benchmark Suite**: Mathematical algorithms and industrial control examples
- **Visualization**: Generates DOT/PNG diagrams and HTML reports

## Installation

### Prerequisites
- Python 3.8+
- Graphviz
- Azure OpenAI API access

### Setup
```bash
pip install -r requirements.txt

# Install Graphviz
brew install graphviz  # macOS
sudo apt-get install graphviz  # Ubuntu/Debian
```

### Environment
Create `.env` file:
```bash
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
```

## Usage

### Basic SFC Verification
```python
from Verifier import SFC, check_pn_containment_html

# Define SFC
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

sfc = SFC(steps, ["i", "fact", "n", "init"], transitions, "Start")
check_pn_containment_html(sfc1, pn1, sfc2, pn2)
```

### LLM Code Generation
```bash
python LLM_Manager.py SFC_FACT.txt
```

### Using Benchmarks
```python
from Benchmarks import sfc_examples
factorial_example = sfc_examples[0]  # Factorial computation
fibonacci_example = sfc_examples[1]  # Fibonacci sequence
```

## Project Structure

```
Containmentchecker/
├── Verifier.py                  # Core verification engine
├── LLM_Manager.py               # Azure OpenAI integration
├── Benchmarks.py                # Algorithm examples
├── Benchmark-OSCAT-Name.py      # Industrial control examples
├── SFC_FACT.txt                # Example SFC files
├── SFC_TLC.txt
├── SFC-DEC_TO_HEX.txt
└── PromptForUpgrade.txt        # LLM upgrade template
```

## Key Components

### SFC Class
```python
class SFC:
    def __init__(self, steps, variables, transitions, initial_step):
        # Core SFC representation
```

### Verification Engine (`Verifier.py`)
- Petri Net conversion: `sfc_to_petrinet(sfc)`
- Cut-point analysis: `find_cut_points(pn)`
- Z3 formal verification
- HTML report generation

### LLM Manager (`LLM_Manager.py`)
- Azure OpenAI API integration
- SFC code generation and upgrades
- Error handling and streaming responses

## Examples

### Factorial SFC
```python
steps = [
    {"name": "Start", "function": "i := 1; fact := 1"},
    {"name": "Check", "function": ""},
    {"name": "Multiply", "function": "fact := fact * i"},
    {"name": "End", "function": ""}
]
```

### Traffic Light Control
```python
steps = [
    {"name": "NormalOperation", "function": "GreenLight := True"},
    {"name": "Pedestrian", "function": "YellowLight := True"},
    {"name": "Emergency", "function": "RedLight := True"}
]
```

## License

MIT License

## Support

Open an issue for questions, bug reports, or feature requests.