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

Agora o momento principal: Eu crio uma migration vazia, com o comando:

```
python manage.py makemigrations core --empty
```

Isso nos da uma migration vazia com o seguinte templade:

```py
# Generated by Django 4.0.1 on 2022-01-06 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_book_author_foreign_key'),
    ]

    operations = [
    ]
```

Renomeei essa migration para `0004_separate_authors_from_books.py`

É aqui que vou escrever a lógica da migração dos dados

Talvez você precise alterar o "dono" do arquivo para poder editá-lo, caso seja necessário, utilize o comando:

```
sudo chown $USER 0004_separate_authors_from_books.py
```

A migration com a lógica completa de separação dos dados ficou assim:

```py
from django.db import migrations


class Migration(migrations.Migration):

    def create_authors_from_books(apps, schema_editor):
        model_book = apps.get_model("core", "Book")
        model_author = apps.get_model("core", "Author")

        books = model_book.objects.all()

        for book in books:
            author, _ = model_author.objects.get_or_create(
                name=book.author
            )
            book.author_foreign_key = author
            book.save()

    def reverse_create_authors_from_books(apps, schema_editor):
        model_book = apps.get_model("core", "Book")
        model_author = apps.get_model("core", "Author")

        books = model_book.objects.all()

        for book in books:
            book.author_foreign_key = None
            book.save()

        model_author.objects.all().delete()

    dependencies = [
        ('core', '0003_book_author_foreign_key'),
    ]

    operations = [
        migrations.RunPython(
            create_authors_from_books, reverse_create_authors_from_books
        )
    ]
```

TODO: Explicar melhor os métodos criados aqui.

