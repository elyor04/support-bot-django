from django.db import models


class User(models.Model):
    Id = models.BigAutoField(primary_key=True)

    TgId = models.BigIntegerField(null=True, blank=True)
    TgName = models.CharField(max_length=200, null=True, blank=True)

    PhoneNumber = models.CharField(max_length=50, null=True, blank=True, unique=True)
    Name = models.CharField(max_length=200, null=True, blank=True)

    TaskCount = models.IntegerField(default=0, null=True, blank=True)
    Role = models.CharField(max_length=50, null=True, blank=True)

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Users"

    def __repr__(self):
        return f"User(Id={self.Id}, TgName='{self.TgName}')"


class Task(models.Model):
    Id = models.BigAutoField(primary_key=True)

    RequestDate = models.DateTimeField(null=True, blank=True)
    Company = models.CharField(max_length=200, null=True, blank=True)

    Author = models.CharField(max_length=200, null=True, blank=True)
    Message = models.TextField(null=True, blank=True)

    Worker = models.CharField(max_length=200, null=True, blank=True)

    StartDate = models.DateTimeField(null=True, blank=True)
    EndDate = models.DateTimeField(null=True, blank=True)

    IsReassigned = models.CharField(max_length=10, null=True, blank=True)
    Confirmation = models.CharField(max_length=10, null=True, blank=True)

    GroupId = models.BigIntegerField(null=True, blank=True)
    MessageId = models.BigIntegerField(null=True, blank=True)

    AuthorId = models.BigIntegerField(null=True, blank=True)
    WorkerId = models.BigIntegerField(null=True, blank=True)

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Tasks"

    def __repr__(self):
        return f"Task(Id={self.Id}, Company='{self.Company}')"


class TaskReassign(models.Model):
    Id = models.BigAutoField(primary_key=True)
    TaskId = models.BigIntegerField(null=True, blank=True)

    Appointer = models.CharField(max_length=200, null=True, blank=True)
    Executor = models.CharField(max_length=200, null=True, blank=True)

    Hours = models.FloatField(null=True, blank=True)

    StartDate = models.DateTimeField(null=True, blank=True)
    EndDate = models.DateTimeField(null=True, blank=True)

    IsDone = models.CharField(max_length=10, null=True, blank=True)

    AppointerId = models.BigIntegerField(null=True, blank=True)
    ExecutorId = models.BigIntegerField(null=True, blank=True)

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TaskReassigns"

    def __repr__(self):
        return f"TaskReassign(Id={self.Id}, TaskId={self.TaskId})"
