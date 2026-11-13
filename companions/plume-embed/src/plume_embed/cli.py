"""Command line entry point for Plume Embed."""

import argparse
import json

from .index import EmbeddingIndex


def main() -> None:
    parser = argparse.ArgumentParser(prog="plume-embed")
    parser.add_argument("--dim", type=int, required=True)
    parser.add_argument("--input", required=True, help="JSONL file of {key, vector}")
    parser.add_argument("--query", required=True, help="JSON file with one vector")
    args = parser.parse_args()

    index = EmbeddingIndex(dim=args.dim)
    with open(args.input, "r", encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            index.add(row["key"], row["vector"])

    with open(args.query, "r", encoding="utf-8") as handle:
        query = json.load(handle)

    for key, score in index.search(query, k=5):
        print(f"{key}\t{score:.4f}")


if __name__ == "__main__":
    main()
