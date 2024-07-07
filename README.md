

# Assembly Re-alignment Experiment

## Overview
This project aims to measure the effectiveness of a linear sweep disassembler in handling randomly chosen misaligned offsets in 32 and 64-bit executable code. The experiment determines how often the disassembler realigns or encounters an invalid instruction when starting from these incorrect offsets.

## Project Structure
- `main.py`: Main script to run the disassembly experiment and save results to a CSV file.
- `visualize.py`: Script to generate plots and display statistics from the CSV file.
- `requirements.txt`: List of dependencies required to run the project.
- `executables/`: Directory where the executable files to be analyzed should be placed.
- `disassembly_results.csv`: Output CSV file containing the disassembly results.
- `forensics.pdf`: Detailed report of the experiment.

## Requirements
- Python 3.6 or higher
- Required Python packages (listed in `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place the executable files you want to analyze in the `executables/` directory.

2. Run the main script to perform the disassembly tests and collect results:
   ```bash
   python3 main.py
   ```

3. Run the visualization script to generate plots and display statistics:
   ```bash
   python3 visualize.py
   ```

4. Check the `forensics.pdf` file for a detailed report of the experiment.

## Results
The generated plots provide insights into the distribution of valid instructions before encountering an invalid instruction. Summary statistics are printed to the console.

## References
- Capstone disassembly framework: [http://www.capstone-engine.org/](http://www.capstone-engine.org/)
- GitHub repository for executables: [https://github.com/bormaa/Benign-NET](https://github.com/bormaa/Benign-NET)

## Authors
- Mohamed Aziz Sghaier
- Mohamed Radhi Halila
```
