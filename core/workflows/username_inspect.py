from core.adapters import get_username_adapters

def inspect_username(username: str):
    adapters = get_username_adapters()
    for adapter in adapters:
        name = adapter.__class__.__name__
        print(f"[+] Running {name}…")
        results = adapter.run(username) or []
        if results:
            for r in results:
                print(f"    [*] {r['url']} (via {r['tool']})")
        else:
            print("    (no results)")
