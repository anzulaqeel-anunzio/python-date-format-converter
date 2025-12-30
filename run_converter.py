# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from converter.core import DateConverter

def main():
    parser = argparse.ArgumentParser(description="Date Format Converter")
    parser.add_argument("date", help="Input date string")
    parser.add_argument("--format", "-f", default="%Y-%m-%d", help="Target format (default: YYYY-MM-DD)")
    parser.add_argument("--list-formats", action="store_true", help="Show common format codes")

    args = parser.parse_args()

    if args.list_formats:
        print("Common Strftime Codes:")
        print("  %Y  Year with century (2024)")
        print("  %m  Month as number (01-12)")
        print("  %b  Month abbreviation (Jan)")
        print("  %d  Day of month (01-31)")
        print("  %H  Hour (00-23)")
        print("  %M  Minute (00-59)")
        print("  %S  Second (00-59)")
        sys.exit(0)

    result, error = DateConverter.convert(args.date, args.format)

    if error:
        print(f"Error: {error}")
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
