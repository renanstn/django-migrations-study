# django-migrations-study

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)

Repositório utilizado para estudar migração de dados utilizando o Django

## Situação

Aqui fiz um app, onde inicialmente eu tinha uma model `Book`, e nessa mesma model ficavam as seguintes informações sobre um livro:

- Id
- Título
- Páginas
- Autor

Nessa situação fictícia, vou separar os **autores** em uma model separada, e utilizarei as migrations do Django para isso.

Ao final do processo, a model `Book` deve conter os campos:

- Id
- Título
- Páginas
- Autor (ForeignKey)

E a model `Author` deve conter:

- Id
- Nome

## Passo a passo

Nessa simulação, iniciei o app salvando vários livros em uma model única, onde na mesma eu armazeno o Título do livro, quantidade de páginas, e o autor do mesmo.

A model `Book` foi declarada assim:

```py
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    pages = models.IntegerField()
    author = models.CharField(max_length=255)
```

O primeiro passo, foi criar a model `Author`:

```py
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
```

Segundo passo, adicionar na model `Book`, o campo do tipo ForeignKey que fará o vínculo do livro com o autor. Importante manter inicialmente este campo com `default=None` e `null=True,`:

```py
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    pages = models.IntegerField()
    author = models.CharField(max_length=255)
    author_foreign_key = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
```
