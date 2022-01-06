# Generated by Django 4.0.1 on 2022-01-06 00:09

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