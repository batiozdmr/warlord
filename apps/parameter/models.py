from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext as _
from mptt.models import MPTTModel

from ..common.fileUpload.userPath import userDirectoryPath
from ..common.oneTextField import OneTextField


class SiteSettings(OneTextField):
    site = models.OneToOneField(Site, related_name="settings", on_delete=models.CASCADE, verbose_name='Site')
    copyright = RichTextUploadingField(default="", blank=True, verbose_name=_('copyright'))
    logo = models.ImageField(upload_to=userDirectoryPath, null=True, verbose_name=_('Logo'), blank=True)
    favicon = models.ImageField(upload_to=userDirectoryPath, null=True, verbose_name=_('Fav İcon'), blank=True)

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url

    @property
    def favicon_url(self):
        if self.favicon and hasattr(self.favicon, 'url'):
            return self.favicon.url

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Site Ayarları'
        verbose_name_plural = 'Site Ayarları'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Icon(OneTextField):
    class Meta:
        verbose_name = 'İcon'
        verbose_name_plural = 'İcon'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class MenuType(OneTextField):

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Menü Tipi'
        verbose_name_plural = 'Menü Tipi'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Menu(MPTTModel):
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE,
                               verbose_name='Üst Menü')
    menu_type = models.ForeignKey(MenuType, blank=True, on_delete=models.PROTECT, null=True,
                                  verbose_name='Menü Tipi')
    icon = models.ForeignKey(Icon, blank=True, on_delete=models.PROTECT, null=True, verbose_name='İcon')
    name = models.CharField(max_length=250, verbose_name='Başlık')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name="Link")
    alignment = models.IntegerField(null=True, blank=True, verbose_name='Sıralama')
    groupList = models.ManyToManyField(Group, blank=True, verbose_name="Grup")

    def __str__(self):
        if self.menu_type:
            return str(self.name) + " | " + str(self.menu_type.text)
        else:
            return str(self.name)

    class Meta:
        verbose_name = 'Menü'
        verbose_name_plural = 'Menü'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


# Address
class Country(models.Model):
    text = models.CharField(max_length=200, null=True, verbose_name=_('Başlık'))
    rewrite = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Kısaltması'))
    area_code = models.IntegerField(blank=True, null=True, verbose_name=_('Alan Kodu'))
    alignment = models.IntegerField(null=True, blank=True, verbose_name=_('Sıralama'))

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('text',)
        verbose_name = _('Ülke')
        verbose_name_plural = _('Ülke')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Province(models.Model):
    text = models.CharField(max_length=200, null=True, verbose_name=_('Başlık'))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_('Ülke'))
    code = models.CharField(max_length=15, null=True, verbose_name=_('İl Kodu'))

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('text',)
        verbose_name = _('İl')
        verbose_name_plural = _('İl')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class District(OneTextField):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('İl'))

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('text',)
        verbose_name = _('İlçe')
        verbose_name_plural = _('İlçe')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
