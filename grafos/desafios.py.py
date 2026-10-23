# desafios 5 e 7 - grafos
# aluno: rafael ramos magalhaes
# fiz a resolucao no papel e depois usei esse codigo pra conferir

# desafio 5
G = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [3, 1]}
H = {"a": ["c", "d"], "b": ["c", "d"], "c": ["a", "b"], "d": ["b", "a"]}

print("ordem de G =", len(G), "| tamanho de G =", sum(len(x) for x in G.values()) // 2)
print("ordem de H =", len(H), "| tamanho de H =", sum(len(x) for x in H.values()) // 2)
print("sequencia de G:", sorted(len(x) for x in G.values()))
print("sequencia de H:", sorted(len(x) for x in H.values()))

# minha correspondencia (diferente da obvia, comecei pelo c)
mapa = {1: "c", 2: "b", 3: "d", 4: "a"}

tudo_certo = True
for v in G:
    for viz in G[v]:
        if mapa[viz] not in H[mapa[v]]:
            tudo_certo = False
            print("problema em", v, viz)
print("a correspondencia preserva as adjacencias?", tudo_certo)

# desafio 7
# comecei pelo H (grau 6) e fui descendo
lista = "HB HC HD HE HF HG FG FA FD GD GE CE".split()
grau = {letra: 0 for letra in "ABCDEFGH"}
for aresta in lista:
    grau[aresta[0]] += 1
    grau[aresta[1]] += 1

print()
for letra in grau:
    print(letra, "=", grau[letra])
print("sequencia obtida:", sorted(grau.values()))
print("soma dos graus =", sum(grau.values()), "e arestas =", len(lista))
print("bate com 2 x arestas?", sum(grau.values()) == 2 * len(lista))
