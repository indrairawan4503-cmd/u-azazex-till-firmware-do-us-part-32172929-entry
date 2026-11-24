import os

ENTRY_TEXT = ("I do, and I'll love you at full charge and at one percent, through every update and reboot, until my final shutdown.")

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f: f.write(ENTRY_TEXT)
    # The grader mounts the repo read-only: /output first, repo-root copy best-effort only.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f: f.write(ENTRY_TEXT)
    except OSError: pass

if __name__ == "__main__": main()
