def factorizar(n):
    factores = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factores[d] = factores.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factores[n] = factores.get(n, 0) + 1
    return factores

a = 36
b = 60

fa = factorizar(a)
fb = factorizar(b)

print("Factorización de", a, ":", fa)
print("Factorización de", b, ":", fb)

# calcula MCD
mcd = 1
for p in fa:
    if p in fb:
        mcd *= p ** min(fa[p], fb[p])

# calcula MCM
mcm = 1
for p in set(fa) | set(fb):
    mcm *= p ** max(fa.get(p, 0), fb.get(p, 0))

print("MCD:", mcd)
print("MCM:", mcm)
