import json,os,random,sys
from urllib.request import urlopen, Request
V = [0, 100, 320, 330, 500, 900, 0]
Y = [0, 0, 1, 1, 2, 4, 0]
MT = 30000
IG = 30001
NB = 215000
PST_P = [0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,0,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0]
PST_N = [-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50]
PST_B = [-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20]
PST_R = [0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0]
PST_Q = [-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20]
PST_K = [-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20]
PST_KE = [-50,-40,-30,-20,-20,-30,-40,-50,-30,-20,-10,0,0,-10,-20,-30,-30,-10,20,30,30,20,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,20,30,30,20,-10,-30,-30,-30,0,0,0,0,-30,-30,-50,-30,-30,-30,-30,-30,-30,-50]
PS = [None, PST_P, PST_N, PST_B, PST_R, PST_Q, PST_K]
VM = [[0] * 128 for _ in range(15)]
VE = [[0] * 128 for _ in range(15)]
for _p in range(1, 7):
    for _r in range(8):
        for _f in range(8):
            _sq = _r * 16 + _f
            _v = PS[_p][(7 - _r) * 8 + _f]
            _w = PST_KE[(7 - _r) * 8 + _f] if _p == 6 else _v
            VM[_p][_sq] = V[_p] + _v
            VE[_p][_sq] = V[_p] + _w
            VM[_p + 8][_sq ^ 0x70] = -VM[_p][_sq]
            VE[_p + 8][_sq ^ 0x70] = -VE[_p][_sq]
_rg = random.Random(12345)
Z = [[_rg.getrandbits(64) for _ in range(128)] for _ in range(15)]
ZS = _rg.getrandbits(64)
ZC = [_rg.getrandbits(64) for _ in range(16)]
ZE = [_rg.getrandbits(64) for _ in range(8)]
KN = [[] for _ in range(128)]
KG = [[] for _ in range(128)]
RY = [[] for _ in range(128)]
for _s in range(128):
    if _s & 0x88:
        continue
    for _d in (-33, -31, -18, -14, 14, 18, 31, 33):
        _t = _s + _d
        if 0 <= _t < 128 and not (_t & 0x88):
            KN[_s].append(_t)
    for _d in (-17, -16, -15, -1, 1, 15, 16, 17):
        _t = _s + _d
        if 0 <= _t < 128 and not (_t & 0x88):
            KG[_s].append(_t)
    for _d in (-17, -15, 15, 17, -16, -1, 1, 16):
        _ry = []
        _t = _s + _d
        while 0 <= _t < 128 and not (_t & 0x88):
            _ry.append(_t)
            _t += _d
        RY[_s].append(_ry)
S6 = [_s for _s in range(128) if not (_s & 0x88)]
CB = [0] * 128
CB[0] = 2
CB[7] = 1
CB[112] = 8
CB[119] = 4
CM = {"K": 1, "Q": 2, "k": 4, "q": 8}
bd = [0] * 128
sd = 0
cs = 0
ep = -1
mg = 0
eg = 0
ph = 0
hh = 0
kg = [0, 0]
nd = 0
TT = {}
def su(fen):
    global sd, cs, ep, mg, eg, ph, hh
    for i in range(128):
        bd[i] = 0
    p = fen.split()
    mg = eg = ph = hh = 0
    for r8, row in enumerate(p[0].split("/")):
        r = 7 - r8
        f = 0
        for c in row:
            if c.isdigit():
                f += int(c)
            else:
                sq = r * 16 + f
                pc = "PNBRQK".find(c.upper()) + 1
                if c.islower():
                    pc += 8
                bd[sq] = pc
                mg += VM[pc][sq]
                eg += VE[pc][sq]
                ph += Y[pc & 7]
                hh ^= Z[pc][sq]
                if (pc & 7) == 6:
                    kg[(pc & 8) >> 3] = sq
                f += 1
    sd = 0 if p[1] == "w" else 8
    if sd:
        hh ^= ZS
    cs = 0
    for c in p[2]:
        cs |= CM.get(c, 0)
    hh ^= ZC[cs]
    ep = -1
    if len(p) > 3 and p[3] != "-":
        ep = (ord(p[3][0]) - 97) + (int(p[3][1]) - 1) * 16
        hh ^= ZE[ep & 7]

def at(sq, by):
    b = bd
    if by == 0:
        for t in (sq - 15, sq - 17):
            if 0 <= t < 128 and not (t & 0x88) and b[t] == 1:
                return 1
    else:
        for t in (sq + 15, sq + 17):
            if 0 <= t < 128 and not (t & 0x88) and b[t] == 9:
                return 1
    for t in KN[sq]:
        q = b[t]
        if q and (q & 8) == by and (q & 7) == 2:
            return 1
    for t in KG[sq]:
        q = b[t]
        if q and (q & 8) == by and (q & 7) == 6:
            return 1
    for i in range(8):
        for t in RY[sq][i]:
            q = b[t]
            if q:
                if (q & 8) == by and (q & 7) in ((3, 5) if i < 4 else (4, 5)):
                    return 1
                break
    return 0


def gn(c):
    M = []
    S = []
    b = bd
    s = sd
    o = s ^ 8
    def a(to):
        q = b[to]
        if q:
            if (q & 8) == o:
                M.append(sq | (to << 7) | (q << 14))
                S.append(10000 + 10 * V[q & 7] - V[t] // 16)
            return 1
        if not c:
            M.append(sq | (to << 7))
            S.append(0)
        return 0
    for sq in S6:
        p = b[sq]
        if not p or (p & 8) != s:
            continue
        t = p & 7
        if t == 1:
            d = 16 if s == 0 else -16
            r = sq >> 4
            pr = (r == 6 and s == 0) or (r == 1 and s == 8)
            to = sq + d
            if not b[to]:
                if pr:
                    for w in (5, 4, 3, 2):
                        M.append(sq | (to << 7) | (w << 18))
                        S.append(9000 + V[w])
                elif not c:
                    M.append(sq | (to << 7))
                    S.append(0)
                    if (r == 1 and s == 0) or (r == 6 and s == 8):
                        if not b[sq + 2 * d]:
                            M.append(sq | ((sq + 2 * d) << 7))
                            S.append(0)
            for dd in (d - 1, d + 1):
                to = sq + dd
                if to < 0 or to > 127 or (to & 0x88):
                    continue
                q = b[to]
                if q and (q & 8) == o:
                    if pr:
                        for w in (5, 4, 3, 2):
                            M.append(sq | (to << 7) | (q << 14) | (w << 18))
                            S.append(19000 + 10 * V[q & 7] + V[w])
                    else:
                        M.append(sq | (to << 7) | (q << 14))
                        S.append(10000 + 10 * V[q & 7] - 6)
                elif to == ep:
                    M.append(sq | (to << 7) | ((9 if s == 0 else 1) << 14))
                    S.append(10000 + 10 * V[1] - 6)
        elif t == 2 or t == 6:
            for to in (KN[sq] if t == 2 else KG[sq]):
                a(to)
            if t == 6 and not c:
                ks = kg[s >> 3]
                rk = 4 if s == 0 else 12
                cr = (1, 2) if s == 0 else (4, 8)
                if (cs & cr[0] and not b[ks + 1] and not b[ks + 2] and b[ks + 3] == rk
                        and not at(ks, o) and not at(ks + 1, o) and not at(ks + 2, o)):
                    M.append(ks | ((ks + 2) << 7))
                    S.append(0)
                if (cs & cr[1] and not b[ks - 1] and not b[ks - 2] and not b[ks - 3]
                        and b[ks - 4] == rk and not at(ks, o)
                        and not at(ks - 1, o) and not at(ks - 2, o)):
                    M.append(ks | ((ks - 2) << 7))
                    S.append(0)
        else:
            for i in range(8):
                if t == 3 and i > 3:
                    continue
                if t == 4 and i < 4:
                    continue
                for to in RY[sq][i]:
                    if a(to):
                        break
    return M, S

def mk(mv):
    global sd, cs, ep, mg, eg, ph, hh
    frm = mv & 127
    to = (mv >> 7) & 127
    cap = (mv >> 14) & 15
    pro = (mv >> 18) & 7
    pc = bd[frm]
    oc, oe, om, og, op, oh = cs, ep, mg, eg, ph, hh
    hh ^= ZC[cs]
    if ep >= 0:
        hh ^= ZE[ep & 7]
    bd[frm] = 0
    hh ^= Z[pc][frm]
    mg -= VM[pc][frm]
    eg -= VE[pc][frm]
    csq = to
    if cap:
        if (pc & 7) == 1 and bd[to] == 0:
            csq = to - 16 if sd == 0 else to + 16
        cpc = bd[csq]
        bd[csq] = 0
        hh ^= Z[cpc][csq]
        mg -= VM[cpc][csq]
        eg -= VE[cpc][csq]
        ph -= Y[cpc & 7]
        cs &= ~CB[csq]
    npc = (pro + sd) if pro else pc
    bd[to] = npc
    hh ^= Z[npc][to]
    mg += VM[npc][to]
    eg += VE[npc][to]
    if pro:
        ph += Y[pro]
    if (pc & 7) == 6:
        kg[sd >> 3] = to
        cs &= ~(3 if sd == 0 else 12)
        if to - frm == 2 or frm - to == 2:
            rf, rt = (frm + 3, frm + 1) if to - frm == 2 else (frm - 4, frm - 1)
            rp = bd[rf]
            bd[rf] = 0
            bd[rt] = rp
            hh ^= Z[rp][rf] ^ Z[rp][rt]
            mg += VM[rp][rt] - VM[rp][rf]
            eg += VE[rp][rt] - VE[rp][rf]
    elif (pc & 7) == 4:
        cs &= ~CB[frm]
    ep = -1
    if (pc & 7) == 1 and (to - frm == 32 or frm - to == 32):
        ep = (frm + to) // 2
        hh ^= ZE[ep & 7]
    hh ^= ZC[cs]
    hh ^= ZS
    sd ^= 8
    return (mv, cap, csq, oc, oe, om, og, op, oh)


def um(st):
    global sd, cs, ep, mg, eg, ph, hh
    mv, cap, csq, cs, ep, mg, eg, ph, hh = st
    sd ^= 8
    frm = mv & 127
    to = (mv >> 7) & 127
    pro = (mv >> 18) & 7
    npc = bd[to]
    bd[to] = 0
    pc = (1 + sd) if pro else npc
    bd[frm] = pc
    if (npc & 7) == 6:
        kg[sd >> 3] = frm
        if to - frm == 2:
            bd[frm + 3] = bd[frm + 1]
            bd[frm + 1] = 0
        elif frm - to == 2:
            bd[frm - 4] = bd[frm - 1]
            bd[frm - 1] = 0
    if cap:
        bd[csq] = cap


def mn():
    global sd, ep, hh
    st = (ep, hh)
    if ep >= 0:
        hh ^= ZE[ep & 7]
    ep = -1
    hh ^= ZS
    sd ^= 8
    return st


def un(st):
    global sd, ep, hh
    ep, hh = st
    sd ^= 8


def ev():
    s = (mg * ph + eg * (24 - ph)) // 24
    return s if sd == 0 else -s

KL = [[0, 0] for _ in range(256)]
HS = [[0] * 128 for _ in range(128)]


def qs(a, be, pl):
    global nd
    nd += 1
    if nd > NB:
        return ev()
    ik = at(kg[sd >> 3], sd ^ 8)
    if ik:
        M, S = gn(0)
    else:
        st = ev()
        if st >= be:
            return be
        if st > a:
            a = st
        M, S = gn(1)
    n = len(M)
    lg = 0
    for i in range(n):
        bi = max(range(i, n), key=S.__getitem__)
        if bi != i:
            M[i], M[bi] = M[bi], M[i]
            S[i], S[bi] = S[bi], S[i]
        mv = M[i]
        cp = (mv >> 14) & 15
        if not ik and not ((mv >> 18) & 7) and st + V[cp & 7] + 200 < a:
            continue
        u = mk(mv)
        if at(kg[(sd ^ 8) >> 3], sd):
            um(u)
            continue
        lg = 1
        v = -qs(-be, -a, pl + 1)
        um(u)
        if v >= be:
            return be
        if v > a:
            a = v
    if ik and not lg:
        return -MT + pl
    return a


def sr(a, be, d, pl, nu=1):
    global nd
    nd += 1
    if nd > NB:
        return ev()
    if d <= 0:
        return qs(a, be, pl)
    ao = a
    if pl:
        if a < -MT + pl:
            a = -MT + pl
        if be > MT - pl:
            be = MT - pl
        if a >= be:
            return a
    e = TT.get(hh)
    tm = 0
    if e:
        tm = e[3]
        if e[0] >= d:
            v = e[1]
            if e[2] == 0:
                return v
            if e[2] == 1 and v >= be:
                return v
            if e[2] == 2 and v <= a:
                return v
    ik = at(kg[sd >> 3], sd ^ 8)
    if ik:
        d += 1
    x = ev()
    if nu and d >= 3 and not ik and ph >= 2 and be < MT - 100 and x >= be:
        u = mn()
        v = -sr(-be, -be + 1, d - 3, pl + 1, 0)
        un(u)
        if v >= be:
            return be
    fu = d == 1 and not ik and x + 200 < a
    M, S = gn(0)
    n = len(M)
    for i in range(n):
        mv = M[i]
        if mv == tm:
            S[i] = 20000
        elif not ((mv >> 14) & 15) and not ((mv >> 18) & 7):
            if mv == KL[pl][0]:
                S[i] = 9000
            elif mv == KL[pl][1]:
                S[i] = 8000
            else:
                S[i] = HS[mv & 127][(mv >> 7) & 127]
    bs = -IG
    bm = 0
    lg = 0
    al = a
    for i in range(n):
        bi = max(range(i, n), key=S.__getitem__)
        if bi != i:
            M[i], M[bi] = M[bi], M[i]
            S[i], S[bi] = S[bi], S[i]
        mv = M[i]
        cp = (mv >> 14) & 15
        pr = (mv >> 18) & 7
        if fu and not cp and not pr:
            continue
        u = mk(mv)
        if at(kg[(sd ^ 8) >> 3], sd):
            um(u)
            continue
        lg += 1
        if lg == 1 or d < 3 or cp or pr or ik:
            v = -sr(-be, -al, d - 1, pl + 1)
        else:
            v = -sr(-be, -al, d - 2, pl + 1)
            if v > al:
                v = -sr(-be, -al, d - 1, pl + 1)
        um(u)
        if v > bs:
            bs = v
            bm = mv
        if v > al:
            al = v
            if al >= be:
                if not cp and not pr:
                    if KL[pl][0] != mv:
                        KL[pl][1] = KL[pl][0]
                        KL[pl][0] = mv
                    h2 = HS[mv & 127][(mv >> 7) & 127] + d * d
                    HS[mv & 127][(mv >> 7) & 127] = h2 if h2 < 7000 else 7000
                break
    if lg == 0:
        return -MT + pl if ik else 0
    fl = 1 if bs >= be else (2 if bs <= ao else 0)
    if len(TT) > (1 << 20):
        TT.clear()
    if nd <= NB: TT[hh] = (d, fl, bs, bm)
    return bs

def rs(d):
    M, S = gn(0)
    e = TT.get(hh)
    if e:
        for i in range(len(M)):
            if M[i] == e[3]:
                S[i] = 20000
    bs = -IG
    bm = 0
    a = -IG
    n = len(M)
    for i in range(n):
        bi = max(range(i, n), key=S.__getitem__)
        if bi != i:
            M[i], M[bi] = M[bi], M[i]
            S[i], S[bi] = S[bi], S[i]
        mv = M[i]
        u = mk(mv)
        if at(kg[(sd ^ 8) >> 3], sd):
            um(u)
            continue
        v = -sr(-IG, -a, d - 1, 1)
        um(u)
        if v > bs:
            bs = v
            bm = mv
        if v > a:
            a = v
    return bm, bs


def th():
    global nd
    nd = 0
    M, S = gn(0)
    lg = []
    for mv in M:
        u = mk(mv)
        if not at(kg[(sd ^ 8) >> 3], sd):
            lg.append(mv)
        um(u)
    if not lg:
        return 0
    if len(lg) == 1:
        return lg[0]
    bm = lg[0]
    for d in range(1, 65):
        mv, v = rs(d)
        if nd < NB and mv:
            bm = mv
        if v >= MT - 100:
            break
        if nd >= NB:
            break
    return bm


U = os.environ.get("MAKEFUN_ENV_URL", "")


def po(p, d):
    try:
        return json.load(urlopen(Request(U + p, data=json.dumps(d).encode(),
                                        headers={"content-type": "application/json"})))
    except Exception as e:
        sys.exit(str(e))


def uc(m):
    f = m & 127
    t = (m >> 7) & 127
    s = "abcdefgh"[f & 7] + str((f >> 4) + 1) + "abcdefgh"[t & 7] + str((t >> 4) + 1)
    pr = (m >> 18) & 7
    return s + "nbrq"[pr - 2] if pr else s


if __name__ == "__main__":
    if not U:
        sys.exit("MAKEFUN_ENV_URL is not set")
    while True:
        g = po("/game", {})
        if g["status"] == "done":
            break
        while g["status"] == "your_move":
            su(g["fen"])
            mv = th()
            if not mv:
                g = po("/resign", {"game": g["game"]})
                break
            u = uc(mv)
            if u not in g["legal_moves"]:
                u = g["legal_moves"][0]
            g = po("/move", {"game": g["game"], "move": u})
        print(g["game"], g["outcome"], g["reason"], file=sys.stderr)
