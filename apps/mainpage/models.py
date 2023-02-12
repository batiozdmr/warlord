from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.mixins import AuditMixin
from apps.common.oneTextField import OneTextField


class TelegramBot(AuditMixin):
    username = models.CharField(max_length=200, null=True, verbose_name=_('Kullanıcı Adı'))
    first_name = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Ad'))
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Soyad'))
    user_id = models.IntegerField(blank=True, null=True, verbose_name=_('Kullanıcı ID'))
    and_date = models.DateTimeField(blank=True, null=True, verbose_name=_('Gruptan Atılma Zamanı'))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Bot'
        verbose_name_plural = 'Bor'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
