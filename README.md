A simple Python3 script to generate **all** leetspeak variants of a given wordlist. 

Using leetspeakgen.py to pre-generate all leetspeak variants.

For example, if your wordlist contains `password`, LeetSpeakGen will produce:
- `password`
- `p@ssword`
- `passw0rd`
- `p@ssw0rd`
- `p@$w0rd`
- `p@$$w0rd`
- …and so on for every combination of `a→@`, `o→0`, `e→3`, `i→1`, `s→$`.

---

Generally, if you want combinatoric coverage (e.g., all permutations of substitutions), you'll need to either:

a) Write many variants of the rule

  or

b) Use external tools to pre-process the wordlist (e.g., rsmangler, mentalist, crunch, or a Python script).

This is that Python script...

---

## 🚀 Features

- Reads any plaintext password list.
- Emits **all** combinations of common leetspeak substitutions:
  - `a ↔ @`
  - `o ↔ 0`
  - `e ↔ 3`
  - `i ↔ 1`
  - `s ↔ $`
- Deduplicates variants so output is unique.
- Zero external dependencies beyond Python3’s standard library.

---

## 📋 Prerequisites

- **Python 3.6+** installed on your system.
- (Optional) UNIX-like shell (bash, zsh, etc.) or Windows WSL2.

---

## ⚙️ Installation

**Clone your GitHub repo** (or download `leetspeakgen.py` directly):

```
git clone https://github.com/ThomasRyanforty/leetspeakgen.git
cd leetspeakgen
chmod +x leetspeakgen.py
```

---

## 💡 Usage

```
./leetspeakgen.py -l <input-wordlist> -o <output-wordlist>
```

- `l, --list` Path to your original password list.
- `o, --output` Path for the generated leetspeak variants.

---

## Examples

Generate leet variants for passwords-cewl.txt

```
./leetspeakgen.py -l passwords-cewl.txt -o passwords-cewl-leetspeak.txt
```
