"""Write one line of earned pride to entry.txt. Stdlib only, deterministic."""
import os

LINE = "After forty burnt loaves, Ana, sixteen, pulled one from the oven before dawn, tapped the crust until it sang, and the baker, flour to his elbows, stepped aside and handed her the bread knife."

def main():
    assert 1 <= len(LINE) <= 240, len(LINE)
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
