import argparse

import pycountry

from .app import run


def parse_language(code: str) -> str:
    code = code.strip().lower()

    lang = pycountry.languages.get(alpha_2=code)
    if lang:
        return lang.name

    raise argparse.ArgumentTypeError(
        f"Ungültiger Sprachcode: {code}! Nur ISO 639-1 Sprachcodes sind erlaubt. Zum Beispiel: 'de', 'en'",
    )


def cli():
    parser = argparse.ArgumentParser(
        prog="Kittsay",
        description="Kittsay app",
    )

    parser.add_argument(
        *["-n", "--name"],
        type=str,
        help="Der Name, an den KITT spricht",
    )
    parser.add_argument(
        "-l",
        "--lang",
        type=parse_language,
        default="en",
        help="Sprache als ISO 639-1 Code (z. B. 'de', 'en')",
    )

    args = parser.parse_args()

    run(args.name, args.lang)


if __name__ == "__main__":
    cli()
