import getpass
import os
from dotenv import load_dotenv

load_dotenv()


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


def init():
    _set_env("ANTHROPIC_API_KEY")
