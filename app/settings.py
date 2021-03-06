import os
from pathlib import Path

ROOT = Path(__file__).parent.parent.resolve()

# Server configuration

PORT = int(os.environ.get("PORT", 5000))
WORKERS = int(os.environ.get("WEB_CONCURRENCY", 1))

if "DOMAIN" in os.environ:  # staging / production
    SERVER_NAME = os.environ["DOMAIN"]
    RELEASE_STAGE = "staging" if "staging" in SERVER_NAME else "production"
elif "HEROKU_APP_NAME" in os.environ:  # review apps
    SERVER_NAME = os.environ["HEROKU_APP_NAME"] + ".herokuapp.com"
    RELEASE_STAGE = "review"
else:  # localhost
    SERVER_NAME = f"localhost:{PORT}"
    RELEASE_STAGE = "local"


DEPLOYED = RELEASE_STAGE != "local"
BUGSNAG_API_KEY = os.getenv("BUGSNAG_API_KEY")
DEBUG = bool(os.environ.get("DEBUG", False))

# Fonts

FONTS_DIRECTORY = ROOT / "fonts"
FONT_THIN = FONTS_DIRECTORY / "TitilliumWeb-SemiBold.ttf"
FONT_THICK = FONTS_DIRECTORY / "TitilliumWeb-Black.ttf"

# Image rendering

IMAGES_DIRECTORY = ROOT / "images"
DEFAULT_EXT = "png"
DEFAULT_STYLE = "default"
DEFAULT_SIZE = (600, 600)

# Test images

TEST_IMAGES_DIRECTORY = ROOT / "app" / "tests" / "images"
TEST_IMAGES = [
    (
        "iw",
        ["tests code", "in production"],
    ),
    (
        "fry",
        ["a", "b"],
    ),
    (
        "fry",
        ["short line", "longer line of text than the short one"],
    ),
    (
        "fry",
        ["longer line of text than the short one", "short line"],
    ),
    (
        "sparta",
        ["", "this is a wide image!"],
    ),
    (
        "ski",
        [
            "if you try to put a bunch more text than can possibly fit on a meme",
            "you're gonna have a bad time",
        ],
    ),
    (
        "ds",
        ["Push this button.", "Push that button.", "can't decide which is worse"],
    ),
    (
        "spongebob",
        ["You: Stop talking like that", "Me: Stop talking like that"],
    ),
]
