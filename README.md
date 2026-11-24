# Tiny Chess Engine v3

[![Competition](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01) [![Rank](https://make.fun/badge/tiny-chess-01/abilyusa/tiny-chess-01-entry-v3/rank.svg)](https://make.fun/bounty/tiny-chess-01) [![Reward](https://make.fun/badge/tiny-chess-01/abilyusa/tiny-chess-01-entry-v3/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A fast 0x88 chess engine in 4 KB of Python: incremental tapered evaluation
(material + piece-square tables, updated on make/unmake), incremental Zobrist
hashing, alpha-beta with null-move pruning, late-move reductions, futility
pruning, killer/history move ordering and a transposition table. Searches to
a fixed node budget (never a clock), so replays are deterministic.

`main.py` is the packed entrypoint (see `source.py`, packed with
`makefun compress`). It plays the house gauntlet through the env at
`MAKEFUN_ENV_URL`.
