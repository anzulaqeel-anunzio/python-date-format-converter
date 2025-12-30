# Date Format Converter

A CLI tool to reformat date strings. It attempts to automatically detect the input format and converts it to your desired output format.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Auto-Detection**: Supports standard ISO 8601, `YYYY-MM-DD`, `DD/MM/YYYY`, and more.
*   **Custom Output**: Use standard Python `strftime` codes to define the output format.
*   **Zero Dependencies**: Uses standard python `datetime`.

## Usage

```bash
python run_converter.py [date] [options]
```

### Options

*   `--format`, `-f`: Target format string (default: `%Y-%m-%d`).
*   `--list-formats`: Show a cheat sheet of format codes.

### Examples

**1. Basic Conversion**
```bash
python run_converter.py "25/12/2024"
# Output: 2024-12-25
```

**2. Custom Format**
```bash
python run_converter.py "2024-12-25" -f "%d %b, %Y"
# Output: 25 Dec, 2024
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
