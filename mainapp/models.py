# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TBlockSetting(models.Model):
    block_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    block_size = models.IntegerField(blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_block_setting'


class TFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    file_type = models.CharField(max_length=1, blank=True, null=True)
    fille_name = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    file_size = models.FloatField(blank=True, null=True)
    parent_file_id = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file'


class TGroom(models.Model):
    groom_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    friend_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_groom'


class THistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    message = models.ForeignKey('TMessage', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    see_time = models.DateTimeField(blank=True, null=True)
    see_cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_history'


class TImageLinks(models.Model):
    link_id = models.AutoField(primary_key=True)
    water = models.ForeignKey('TWater', models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey(TFile, models.DO_NOTHING, blank=True, null=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    expires = models.IntegerField(blank=True, null=True)
    create_time = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_image_links'


class TMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    link_url = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_message'


class TShare(models.Model):
    share_id = models.AutoField(primary_key=True)
    file = models.ForeignKey(TFile, models.DO_NOTHING, blank=True, null=True)
    friend_id = models.IntegerField(blank=True, null=True)
    expires = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_share'


class TSysMenu(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    ord = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_menu'


class TSysRole(models.Model):
    name = models.CharField(unique=True, max_length=20)
    code = models.CharField(unique=True, max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_role'


class TSysRoleMenu(models.Model):
    role_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_role_menu'


class TSysUser(models.Model):
    username = models.CharField(unique=True, max_length=20)
    auth_string = models.CharField(max_length=32)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    @property
    def role(self):
        return TSysRole.objects.get(pk=self.role_id)

    class Meta:
        managed = False
        db_table = 't_sys_user'


class TUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    head = models.CharField(max_length=50, blank=True, null=True)
    label = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TWater(models.Model):
    water_id = models.AutoField(primary_key=True)
    water_text = models.CharField(max_length=50, blank=True, null=True)
    water_pos = models.IntegerField(blank=True, null=True)
    font_size = models.IntegerField(blank=True, null=True)
    font_name = models.CharField(max_length=20, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_water'
