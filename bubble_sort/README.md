Os alunos sentaram desordenadamente em uma fileira de carteiras. Você decide ordenar esses alunos por ordem crescente de altura.

Como poderiamos resolver?

Uma opção possível é começar do primeiro aluno e **comparar** com o aluno da cadeira seguinte.
**Se** ele for maior, você **troca** os alunos de lugar.

**Repete até** chegar na ultima carteira. Dessa forma o aluno maior vai ficar na ultima posicao.

Depois você vai de novo no primeiro aluno e vai comparando até o penultimo aluno (lembra que o ultimo já foi considerado o maior?)
Segue esse ciclo até ordenar todos os alunos.

Exemplo de resultado:

```
[5, 4, 3, 2, 1]
[4, 5, 3, 2, 1]
[4, 3, 5, 2, 1]
[4, 3, 2, 5, 1]
[4, 3, 2, 1, 5]
[3, 4, 2, 1, 5]
[3, 2, 4, 1, 5]
[3, 2, 1, 4, 5]
[2, 3, 1, 4, 5]
[2, 1, 3, 4, 5]
```