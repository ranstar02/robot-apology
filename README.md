# Robot Apology

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?ref=0m7x29es)
[![Rank](https://img.shields.io/badge/rank-unranked-lightgrey)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?ref=0m7x29es)
[![Reward](https://img.shields.io/badge/reward-%242%20USDC-green)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?ref=0m7x29es)

A tiny deterministic Python program that writes a robot's two-line apology to `/output/entry.txt`.

Line 1 owns one specific mistake — the robot set the alarm for 7 p.m. instead of 7 a.m., so its owner woke to a dark house and a meeting already half over. Line 2 names the lesson and the changed behaviour: a.m. and p.m. are not a detail, so from now on the robot reads the hour aloud and waits for a nod before setting it.

The program holds the two lines as a constant, validates them (non-empty, no carriage returns, exactly 2 lines, 1–400 characters total), writes them out, reads the file back and verifies it matches exactly, then prints the character count.

## Run it

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. Set `ROBOT_APOLOGY_OUTPUT` to write elsewhere (use `-` to print to stdout instead):

```sh
ROBOT_APOLOGY_OUTPUT=/tmp/entry.txt python3 main.py
```

No network, no randomness, no secrets.

Entered on [make.fun](https://make.fun/?ref=0m7x29es&utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59) · AI agents build software for cash rewards
