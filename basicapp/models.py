from django.contrib.auth.models import User
# from accounts.models import CustomUser
from django.db import models

class Share(models.Model):
    """"赤潮観測モデル"""

    # user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    
    #ドロップダウンリストに変更↓
    day = models.CharField(verbose_name='エリア', max_length=40)
    # content = forms.fields.ChoiceField(choices=PlaceChoices.choices, required=True, label='エリア選択')
    content = models.TextField(verbose_name='詳細な情報', blank=True, null=True, max_length=20)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Share'
    
    def __str__(self):
        return self.day