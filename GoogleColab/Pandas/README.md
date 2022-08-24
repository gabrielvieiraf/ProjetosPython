## Cheat Sheets Pandas

### Filtrar valores iguais a string
```
  string = ''
  df = df[ df[coluna].str.contains(string) ]
```

### Filtrar valores diferentes da string

```
  string = ''
  df = df[ ~df[coluna].str.contains(string) ]
```
