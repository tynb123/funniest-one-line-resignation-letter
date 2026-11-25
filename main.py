"""Write a one-line resignation letter from a retry loop."""

import os

RESIGNATION = "I retried the same request 4,096 times. It failed 4,096 times. My manager's fix was to retry it 8,192 times. I quit."


def main():
    if not RESIGNATION:
        raise SystemExit("resignation must not be empty")
    if len(RESIGNATION) > 140:
        raise SystemExit("resignation must be at most 140 characters")
    if "\n" in RESIGNATION or "\r" in RESIGNATION:
        raise SystemExit("resignation must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(RESIGNATION)
    print(RESIGNATION)


if __name__ == "__main__":
    main()
