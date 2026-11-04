"""Generate a QR code for each resource list.

Run from the repo root:
    uv run --no-project --python 3.12 --with 'qrcode[pil]' --with zxing-cpp python scripts/make_qr.py
"""
from pathlib import Path

import qrcode
import zxingcpp
from PIL import Image

REPO = "https://github.com/Every-Flavor-Robotics/learn-modern-making"
TARGETS = {
    "all": REPO,
    "design": f"{REPO}/blob/main/resources/design.md",
    "features": f"{REPO}/blob/main/resources/features.md",
    "printing": f"{REPO}/blob/main/resources/printing.md",
    "tolerancing": f"{REPO}/blob/main/resources/tolerancing.md",
    "onshape": f"{REPO}/blob/main/resources/onshape.md",
    "llms": f"{REPO}/blob/main/resources/llms.md",
}

out = Path("qr")
out.mkdir(exist_ok=True)
for name, url in TARGETS.items():
    code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=4)
    code.add_data(url)
    code.make(fit=True)
    path = out / f"{name}.png"
    code.make_image(fill_color="black", back_color="white").save(path)

    results = zxingcpp.read_barcodes(Image.open(path).convert("L"))
    decoded = results[0].text if results else ""
    if decoded != url:
        raise SystemExit(f"{path} decoded to {decoded!r}, expected {url}")
    print(f"ok v{code.version} {path} -> {url}")
