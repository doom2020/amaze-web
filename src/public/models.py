from django.db import models


class CommentInfo(models.Model):
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    update_user_account = models.CharField(verbose_name='更新人', blank=True, null=True, max_length=20)
    comment = models.CharField(verbose_name='备注', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'comment_info'


class UserInfo(CommentInfo):
    user_name = models.CharField(verbose_name='用户名', max_length=20)
    user_password = models.CharField(verbose_name='用户密码', max_length=100)
    user_phone = models.CharField(verbose_name='手机号', max_length=10)
    user_email = models.EmailField(verbose_name='邮箱', max_length=10)
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)

    class Meta:
        db_table = 'user_info'


class SysMenu(CommentInfo):
    pass


class Rule(CommentInfo):
    pass


class RuleUser(CommentInfo):
    pass


class Permission(CommentInfo):
    pass

