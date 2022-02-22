import base64
import hashlib
import re

from django.core.exceptions import ValidationError
from django.db import models


def validate_gtm_id(gtm_id: str) -> None:
    gtm_id = gtm_id.upper().strip()
    if not re.match(r"^GTM-[A-Z0-9]{1,7}$", gtm_id):
        raise ValidationError(
            "Неверный идентификатор контейнера GTM. "
            'Он должен быть вида "GTM-XXXXXXX".'
        )


class DemoLanding(models.Model):
    gtm_id = models.CharField(
        max_length=15,
        verbose_name="ID контейнера GTM",
        db_index=True,
        validators=[validate_gtm_id],
    )
    hashcode = models.SlugField(
        max_length=8,
        verbose_name="Хэш-код",
        unique=True,
        db_index=True,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk}_{self.hashcode}"

    class Meta:
        verbose_name = "демо-лендинг"
        verbose_name_plural = "демо-лендинги"

    def save(self, *args, **kwargs):
        self.gtm_id = self.gtm_id.upper().strip()
        self.hashcode = self._get_hashcode()
        super().save(*args, **kwargs)

    def _get_hashcode(self) -> str:
        """Получи хэш лендинга."""
        fields_for_hash = [self.gtm_id]
        prehash = hashlib.md5("".join(fields_for_hash).encode()).hexdigest()
        return base64.b64encode(prehash.encode("ascii")).decode("utf-8").lower()[:8]
