from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


class Seance(models.Model):
    slug = models.SlugField(_("Slug"), blank=True, null=True)
    titre = models.CharField(_('Titre de la séance'), max_length=75)
    description = models.TextField(
        _('Description de la séance'),
        blank=True,
        null=True
    )
    nb_participants = models.IntegerField(_('Nombre de participants'),default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Seance")
        verbose_name_plural = _("Seances")

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Seance, self).save(*args, **kwargs)
