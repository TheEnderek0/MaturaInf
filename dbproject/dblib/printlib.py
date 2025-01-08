
def printa(msg: str, lvl:int=0) -> None:

    if lvl == 0:
        print(f"[INFO] {msg}")
    elif lvl == 1:
        print(f"[WARN] {msg}")
    elif lvl >= 2:
        print(f"[ERR] {msg}")
