
# Colrfx

Colrfx is a Python script that allows users to retrieve color information based on color names, hex values, or RGB values. It utilizes a `colors.json` file to store color data and provides functionalities to convert and match colors.

## Installation

Clone the repository using pip:

```bash
pip install git+https://github.com/abrarishere/colrfx.git
```

## Usage

After installation, you can use `colrfx` in your terminal to interact with the script. Follow the prompts to input a color in one of the supported formats:

```bash
colrfx
```

### Supported Color Input Formats

- **Color Name**: Enter a recognized color name (e.g., "red", "blue").
- **Hex Value**: Prefix with "#" (e.g., "#FF0000").
- **RGB Value**: Enclose in parentheses and separate values with commas (e.g., "(255, 0, 0)").

### Example Usage

```bash
Enter a color name, hex value, or RGB value: #00FF00
```

## Functionality

The script validates the input and determines the type of color provided. It then searches for matches in the `colors.json` file:

- **Hex Colors**: Converts short hex values to full hex and matches against stored data.
- **RGB Colors**: Matches RGB values and displays corresponding hex values.
- **Color Names**: Matches against predefined color names and displays associated hex and RGB values.

If an exact match isn't found, the script attempts to find similar colors based on input criteria.

### Dependencies

- `json`: For reading color data from `colors.json`.
- `os`: For file path operations.
- `input`: For user input handling.
