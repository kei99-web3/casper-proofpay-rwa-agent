from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "media"
BUILD = MEDIA / "_final_video_build"
DRAFT = MEDIA / "casper-proofpay-demo-draft.mp4"
FINAL = MEDIA / "casper-proofpay-demo-final.mp4"

FFMPEG = os.environ.get("FFMPEG_BIN", "ffmpeg")

PACKAGE_HASH = "b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2"
CONTRACT_HASH = "f56cf425f3a10ed7f3e9e2622b64ca2f2a0609c9446b1cb79ea2b58167293c61"
INSTALL_HASH = "930222bfc49b84b775e9c5b008651432e7614025624df410aac993efcafd4d3d"
RECEIPT_HASH = "2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994"
RECEIPT_URL = f"https://testnet.cspr.live/deploy/{RECEIPT_HASH}"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


TITLE = font(56, True)
SUBTITLE = font(29, False)
BODY = font(26, False)
MONO = font(22, False)
SMALL = font(19, False)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, width: int) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        words = raw.split(" ")
        line = ""
        for word in words:
            test = word if not line else f"{line} {word}"
            if draw.textbbox((0, 0), test, font=fnt)[2] <= width:
                line = test
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


def short_hash(value: str) -> str:
    return f"{value[:12]}...{value[-12:]}"


def draw_slide(path: Path, title: str, subtitle: str, blocks: list[tuple[str, str]]) -> None:
    img = Image.new("RGB", (1280, 720), "#f6f7fb")
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 0, 1280, 92), fill="#151a35")
    draw.rectangle((0, 92, 1280, 100), fill="#d71920")
    draw.text((52, 22), "Casper ProofPay", fill="#ffffff", font=SUBTITLE)
    draw.text((52, 128), title, fill="#172033", font=TITLE)
    draw.text((54, 198), subtitle, fill="#4d5a68", font=SUBTITLE)

    y = 270
    for label, value in blocks:
        draw.rounded_rectangle((54, y, 1226, y + 92), radius=10, fill="#ffffff", outline="#dfe3ee", width=2)
        draw.text((82, y + 17), label, fill="#172033", font=BODY)
        value_font = MONO if len(value) > 42 else BODY
        for i, line in enumerate(wrap(draw, value, value_font, 950)):
            draw.text((315, y + 17 + i * 28), line, fill="#1028c7", font=value_font)
        y += 110

    draw.text((54, 680), "Synthetic data demo. Private keys and raw revenue data are not included in this repo.", fill="#667085", font=SMALL)
    img.save(path)


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    if not DRAFT.exists():
        raise SystemExit(f"Draft video missing: {DRAFT}")
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir(parents=True)

    slides = [
        (
            "Testnet evidence first",
            "The receipt-producing component is live on Casper Testnet.",
            [
                ("Contract package", short_hash(PACKAGE_HASH)),
                ("Contract hash", short_hash(CONTRACT_HASH)),
                ("Install deploy", short_hash(INSTALL_HASH)),
            ],
        ),
        (
            "record_proof_receipt executed",
            "The deterministic proof payload was recorded on-chain.",
            [
                ("Entry point", "record_proof_receipt"),
                ("Receipt deploy", short_hash(RECEIPT_HASH)),
                ("Explorer", RECEIPT_URL),
            ],
        ),
        (
            "Agent revenue proof flow",
            "A finance agent pays for a proof, verifies revenue quality, then checks the Casper receipt.",
            [
                ("Proof id", "proof-e9889ea33e5d"),
                ("Quality score", "96 / 100"),
                ("Next", "Local walkthrough follows"),
            ],
        ),
    ]

    frame_paths = []
    for index, slide in enumerate(slides, start=1):
        frame = BUILD / f"slide_{index:02d}.png"
        draw_slide(frame, *slide)
        frame_paths.append(frame)

    concat_txt = BUILD / "slides.txt"
    with concat_txt.open("w", encoding="utf-8") as f:
        for frame in frame_paths:
            f.write(f"file '{frame.as_posix()}'\n")
            f.write("duration 5\n")
        f.write(f"file '{frame_paths[-1].as_posix()}'\n")

    intro = BUILD / "intro.mp4"
    run([
        FFMPEG,
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat_txt),
        "-r",
        "30",
        "-pix_fmt",
        "yuv420p",
        str(intro),
    ])
    run([
        FFMPEG,
        "-y",
        "-i",
        str(intro),
        "-i",
        str(DRAFT),
        "-filter_complex",
        "[0:v][1:v]concat=n=2:v=1:a=0[v]",
        "-map",
        "[v]",
        "-r",
        "30",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(FINAL),
    ])
    print(FINAL)


if __name__ == "__main__":
    main()
