from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

# Para poder hacer `import web`, `import model`, etc.
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from web import create_app  # noqa: E402

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5002)  
