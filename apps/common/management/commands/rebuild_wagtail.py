from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from wagtail.models import Page, Site, Collection
from apps.home.models import PageAcceuil  # Ajustez selon votre modèle réel

class Command(BaseCommand):
    help = "Reconstruit entièrement la structure de base de Wagtail"

    @transaction.atomic
    def handle(self, *args, **options):
        # 1. Vérifier l'état actuel
        self.stdout.write(self.style.WARNING("État actuel:"))
        page_count = Page.objects.count()
        site_count = Site.objects.count()
        collection_count = Collection.objects.count()
        self.stdout.write(f"Pages: {page_count}, Sites: {site_count}, Collections: {collection_count}")

        # 2. Supprimer toutes les pages existantes
        if page_count > 0:
            self.stdout.write(self.style.WARNING("Suppression de toutes les pages existantes..."))
            # Désactiver temporairement les contraintes pour permettre une suppression propre
            Page.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Pages supprimées."))

        # 3. Supprimer tous les sites
        if site_count > 0:
            self.stdout.write(self.style.WARNING("Suppression de tous les sites..."))
            Site.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Sites supprimés."))

        # 4. Supprimer toutes les collections
        if collection_count > 0:
            self.stdout.write(self.style.WARNING("Suppression de toutes les collections..."))
            Collection.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Collections supprimées."))

        # 5. Créer la page racine
        self.stdout.write(self.style.WARNING("Création de la page racine..."))
        root = Page.objects.create(
            title="Root",
            slug="root",
            content_type_id=ContentType.objects.get_for_model(Page).id,
            path="0001",
            depth=1,
            numchild=0,
            url_path="/",
        )
        self.stdout.write(self.style.SUCCESS(f"Page racine créée avec ID={root.id}"))

        # 6. Créer la page d'accueil
        try:
            self.stdout.write(self.style.WARNING("Création de la page d'accueil..."))
            page_accueil_content_type = ContentType.objects.get_for_model(PageAcceuil)

            # Créer la page d'accueil
            homepage = PageAcceuil.objects.create(
                title="Accueil",
                slug="home",
                content_type_id=page_accueil_content_type.id,
                path="00010001",
                depth=2,
                numchild=0,
                url_path="/home/",
                # Ajoutez ici d'autres champs requis par votre modèle
            )

            # Mettre à jour la relation parent-enfant
            root.numchild = 1
            root.save()

            self.stdout.write(self.style.SUCCESS(f"Page d'accueil créée avec ID={homepage.id}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erreur lors de la création de la page d'accueil: {str(e)}"))
            # Si la page d'accueil échoue, créer une page générique à la place
            try:
                homepage = Page.objects.create(
                    title="Accueil",
                    slug="home",
                    content_type_id=ContentType.objects.get_for_model(Page).id,
                    path="00010001",
                    depth=2,
                    numchild=0,
                    url_path="/home/",
                )
                root.numchild = 1
                root.save()
                self.stdout.write(self.style.SUCCESS(f"Page d'accueil générique créée avec ID={homepage.id}"))
            except Exception as e2:
                self.stdout.write(self.style.ERROR(f"Erreur lors de la création de la page générique: {str(e2)}"))
                return

        # 7. Créer le site par défaut
        self.stdout.write(self.style.WARNING("Création du site par défaut..."))
        site = Site.objects.create(
            hostname="127.0.0.1",
            port=8000,
            is_default_site=True,
            root_page=homepage,
            site_name="MJC Mauguio-Carnon"
        )
        self.stdout.write(self.style.SUCCESS(f"Site créé avec ID={site.id}"))

        # 8. Créer la collection racine
        self.stdout.write(self.style.WARNING("Création de la collection racine..."))
        root_collection = Collection.add_root(name="Root")
        self.stdout.write(self.style.SUCCESS(f"Collection racine créée avec ID={root_collection.id}"))

        # 9. Vérifier la structure finale
        self.stdout.write(self.style.WARNING("Structure finale:"))
        page_count = Page.objects.count()
        site_count = Site.objects.count()
        collection_count = Collection.objects.count()
        self.stdout.write(f"Pages: {page_count}, Sites: {site_count}, Collections: {collection_count}")

        self.stdout.write(self.style.SUCCESS("Reconstruction de la structure Wagtail terminée avec succès!"))