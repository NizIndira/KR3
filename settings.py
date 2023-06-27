from pathlib import Path

CURRENT_PATH = Path(__file__).resolve().parent
PATH_WITH_FIXTURES = Path.joinpath(CURRENT_PATH, 'src', 'operations.json' )