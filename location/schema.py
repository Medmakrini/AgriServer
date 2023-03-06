from graphene_django import DjangoObjectType
import graphene
from farm.models import Farm
from .models import Location


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class CreateLocation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        farm_id=graphene.String()
        longitude=graphene.Float()
        latitude=graphene.Float()

    def mutate(self, info, farm_id, longitude,latitude):
        f = Location(longitude=longitude,latitude=latitude ,farm_id=farm_id )
        o = Farm.objects.get(id=farm_id)
        f.location=o
        f.save()
        return CreateLocation(location=f)


