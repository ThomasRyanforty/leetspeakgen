#!/usr/bin/env python3
import argparse
from itertools import product

# Map of characters to their leetspeak substitutions
LEET_MAP = {
    'a': '@', 'A': '@',
    'o': '0', 'O': '0',
    'e': '3', 'E': '3',
    'i': '1', 'I': '1',
    's': '$', 'S': '$'
}

def generate_variants(word):
    """
    Return a set of all variants of `word` where each character in LEET_MAP
    can be replaced by its leetspeak equivalent, in all possible combinations.
    """
    # Find positions that can be substituted
    indices = [i for i, c in enumerate(word) if c in LEET_MAP]
    if not indices:
        return {word}

    # Build choice tuples: at each index, (original, leet)
    choices = [(word[i], LEET_MAP[word[i]]) for i in indices]
    variants = set()

    # product(*) yields every combination of picks from each tuple
    for combo in product(*choices):
        chars = list(word)
        for idx, new_char in zip(indices, combo):
            chars[idx] = new_char
        variants.add(''.join(chars))

    return variants

def main():
    parser = argparse.ArgumentParser(
        description="Generate all leetspeak variants for a wordlist."
    )
    parser.add_argument(
        '-l','--list',
        dest='input_file',
        required=True,
        help='Path to the input wordlist file'
    )
    parser.add_argument(
        '-o','--output',
        dest='output_file',
        required=True,
        help='Path to write the leetspeak-variant wordlist'
    )
    args = parser.parse_args()

    seen = set()
    with open(args.input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
         open(args.output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            word = line.strip()
            if not word or word in seen:
                continue
            for v in generate_variants(word):
                if v not in seen:
                    outfile.write(v + '\n')
                    seen.add(v)

if __name__ == '__main__':
    main()
