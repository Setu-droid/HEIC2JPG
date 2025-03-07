# HEIC to JPG Bulk Converter

## Overview

This Python script provides a robust solution for bulk conversion of HEIC (High Efficiency Image Format) files to JPG format, specifically optimized for macOS environments. It preserves directory structures, supports parallel processing, and offers configurable quality settings.

## Features

- Bulk conversion of HEIC files to JPG
- Preserves original directory structure
- Parallel processing for improved performance
- Configurable JPEG quality
- Detailed error handling and reporting
- Progress tracking and summary statistics

## Requirements

- macOS (tested on macOS 11.0+)
- Python 3.6+
- Pillow
- pillow-heif
- libheif (system dependency)

## Installation

1. Install the required system dependency:
brew install libheif


2. Install Python dependencies:
pip install pillow pillow-heif


3. Clone this repository or download the script:
git clone https://github.com/yourusername/heic-to-jpg-converter.git
cd heic-to-jpg-converter


## Usage

Basic usage:
python heic2jpg.py -i <input_directory> -o <output_directory>


Advanced usage with all options:
python heic2jpg.py -i <input_directory> -o <output_directory> -j <num_workers> -q <jpeg_quality>


### Parameters

| Option | Long Option | Description | Default |
|--------|-------------|-------------|---------|
| `-i`   | `--input`   | Input directory containing HEIC files | Required |
| `-o`   | `--output`  | Output directory for JPG files | Required |
| `-j`   | `--jobs`    | Number of parallel workers | 4 |
| `-q`   | `--quality` | JPEG quality (1-100) | 90 |

## Examples

1. Convert all HEIC files in the Downloads folder to JPG in the Pictures folder:
python heic2jpg.py -i ~/Downloads -o ~/Pictures

python heic2jpg.py -i ~/Photos/HEIC -o ~/Photos/JPG -j 8 -q 95


## Error Handling

The script provides detailed error reporting for each file:
- Successfully converted files are marked with [✓]
- Failed conversions are marked with [✗] and include error details
- A summary of successes and failures is provided at the end of the conversion process

## Performance

Conversion speed depends on your hardware, the number of workers, and the size/complexity of the HEIC files. On a modern Mac, you can expect to process several files per second.

## Limitations

- The script is optimized for macOS and may require modifications for other operating systems
- Very large HEIC files may require additional memory allocation

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/heic-to-jpg-converter/issues) if you want to contribute.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Pillow](https://python-pillow.org/) - Python Imaging Library
- [pillow-heif](https://github.com/bigcat88/pillow_heif) - HEIF plugin for Pillow


