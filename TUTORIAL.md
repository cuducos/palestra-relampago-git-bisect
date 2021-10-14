Inicie o `git bisect`:

```console
$ git bisect start
```

Diga a ele qual _commit_ **você tem certeza que está ruim** (o :lady_beetle:  está presente). Nesse exemplo, é o _commit_ atual, mais novo, por isso podemos omitir o _hash_:
```console
$ git bisect bad
```
Diga a ele qual _commit_ **você tem certeza que está bom** (o :lady_beetle:  **não** está presente):

```console
$ git bisect good fc4653b
```

Execute um `git bisect` com um comando que vai falhar no **primeiro** _commit_ ruim, ou seja, na primeira vez que o :lady_beetle: se manifestar:

```console
$ git bisect run python -c "from calculadora import divisão; assert divisão(5, 2) == 2.5"
```

**Bingo :tada:** O `git bisect` achou o _commit_ que causou o :lady_beetle::

```console
866187492fbeccd7de73cd8a60f1f55b1ab0f489 is the first bad commit
```
