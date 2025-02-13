# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'
        unique_together = (('user', 'email'),)


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CommunityAd(models.Model):
    id = models.BigAutoField(primary_key=True)
    ad_type = models.CharField(max_length=10)
    image = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_posted = models.DateTimeField()
    contact_info = models.CharField(max_length=255)
    approved = models.BooleanField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'community_ad'


class CommunityAnnouncement(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    date_posted = models.DateTimeField()
    contact_info = models.CharField(max_length=255)
    approved = models.BooleanField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_announcement'


class CommunityComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    object_id = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_comment'


class CommunityReaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    emoji = models.CharField(max_length=2)
    announcement = models.ForeignKey(CommunityAnnouncement, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'community_reaction'
        unique_together = (('user', 'announcement', 'emoji'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class ExerciseScheduleExerciseschedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    notes = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    horse = models.ForeignKey('HorsesHorseprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exercise_schedule_exerciseschedule'


class ExerciseScheduleExercisescheduleitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    exercise_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    schedule = models.ForeignKey(ExerciseScheduleExerciseschedule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exercise_schedule_exercisescheduleitem'


class FeedingManagementFeedingchart(models.Model):
    id = models.BigAutoField(primary_key=True)
    breakfast_feed = models.CharField(max_length=200, blank=True, null=True)
    breakfast_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lunch_feed = models.CharField(max_length=200, blank=True, null=True)
    lunch_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dinner_feed = models.CharField(max_length=200, blank=True, null=True)
    dinner_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hay = models.CharField(max_length=200, blank=True, null=True)
    hay_quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    supplements = models.CharField(max_length=200, blank=True, null=True)
    medicines = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField()
    horse = models.OneToOneField('HorsesHorseprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeding_management_feedingchart'


class FeedingManagementFeedingchartApprovedUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedingchart = models.ForeignKey(FeedingManagementFeedingchart, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeding_management_feedingchart_approved_users'
        unique_together = (('feedingchart', 'user'),)


class HorsesHorseprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    image = models.CharField(max_length=100, blank=True, null=True)
    barn_manager = models.ForeignKey(AuthUser, models.DO_NOTHING)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='horseshorseprofile_owner_set')
    rider = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='horseshorseprofile_rider_set')

    class Meta:
        managed = False
        db_table = 'horses_horseprofile'


class HorsesHorseprofileStaff(models.Model):
    id = models.BigAutoField(primary_key=True)
    horseprofile = models.ForeignKey(HorsesHorseprofile, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'horses_horseprofile_staff'
        unique_together = (('horseprofile', 'user'),)


class HorsesProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    bio = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50)
    horse_id = models.BigIntegerField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'horses_profile'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=200)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    provider_id = models.CharField(max_length=200)
    settings = models.JSONField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class UsersHorse(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users_horse'


class UsersProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=20)
    contact = models.CharField(max_length=100)
    notes = models.TextField()
    is_approved = models.BooleanField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_profile'
