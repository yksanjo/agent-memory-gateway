from datetime import datetime, timezone


def main() -> None:
    print("agent-memory-gateway initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
