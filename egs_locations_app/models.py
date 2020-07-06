from django.db import models


# Pve Factions that appear in the game
class Faction(models.Model):
    name = models.CharField(max_length=120, primary_key=True, help_text='Faction Name')


# Star system containing playfields
class System(models.Model):
    name = models.CharField(max_length=120, primary_key=True, help_text='Name of the system')
    territory = models.ForeignKey(Faction, default=None, blank=True, null=True, on_delete=models.CASCADE, help_text='Faction territory the system belongs to')

    def __str__(self):
        return self.name


# Possible Sizes of Playfields
class PlayfieldSize(models.Model):
    name = models.CharField(max_length=120, primary_key=True, help_text='Name of the playfield size')


# Playfield in a star system
class Playfield(models.Model):
    name = models.CharField(max_length=120, primary_key=True, help_text='Name of the playfield')
    system = models.ForeignKey(System, on_delete=models.CASCADE, help_text='System to which the playfield belongs')
    pvp = models.BooleanField(help_text='Pvp or Pve');
    size = models.ForeignKey(PlayfieldSize, default=None, blank=True, null=True, on_delete=models.CASCADE, help_text='Size of the playfield or NULL if orbit')
    gravity = models.FloatField(help_text='Gravity on the playfield')
    specialNotes = models.CharField(default=None, blank=True, null=True, max_length=1024, help_text='Anything particularly groovy about this playfield')

    def __str__(self):
        return self.name


# POI
class POI(models.Model):
    name = models.CharField(max_length=120, primary_key=True, help_text='Name of the POI')
    countWhiteContainers = models.IntegerField(default=None, blank=True, null=True, help_text='The number of white containers in this POI is >= this number')
    countYellowContainers = models.IntegerField(default=None, blank=True, null=True, help_text='The number of yellow containers in this POI is >= this number')
    countRedContainers = models.IntegerField(default=None, blank=True, null=True, help_text='The number of red containers in this POI is >= this number')
    countBrownContainers = models.IntegerField(default=None, blank=True, null=True, help_text='The number of brown containers in this POI is >= this number')
    countPurpleContainers = models.IntegerField(default=None, blank=True, null=True, help_text='The number of purple containers in this POI is >= this number')
    countBlackContainers = models.IntegerField(default=None, blank=True, null=True, help_text='The number of brown containers in this POI is >= this number')

    def __str__(self):
        return self.name


# Playfield POI count
# Number of a particular POIs belonging to a particular faction, that appear on a particular play field
class PlayfieldPOICount(models.Model):
    id = models.AutoField(primary_key=True)
    playfield = models.ForeignKey(Playfield, on_delete=models.CASCADE, help_text='Playfield on which the POI appears')
    poi = models.ForeignKey(POI, on_delete=models.CASCADE, help_text='Name of the POI')
    owner = models.ForeignKey(Faction, on_delete=models.CASCADE, help_text='Faction that owns the POI')
    count = models.IntegerField(help_text='The number of instances of this particular POI that appear on this particular playfield is >= this number')

    def __str__(self):
        return self.id


# Resources that appear in the game
class Resource(models.Model):
    name = models.CharField(max_length=120, primary_key=True, help_text='Name of the resource')


# Size of a resource deposit or "asteroid"
class DepositSize(models.Model):
    name = models.CharField(max_length=120, primary_key=True, help_text='Describes the size in which a resource could appear')


# Playfield deposit or asteroid count
# Number of a particular resource and size appearances on a particular playfield
class PlayfieldResourceCount(models.Model):
    id = models.AutoField(primary_key=True)
    playfield = models.ForeignKey(Playfield, on_delete=models.CASCADE, help_text='Name of the playfield the resource appears on')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, help_text='Name of the resource')
    size = models.ForeignKey(DepositSize, on_delete=models.CASCADE, help_text='Describes the size in which the resource appears')
    count = models.IntegerField(help_text='The number of instances of this particular resource and size combination on the particular playfield is >= this number')