from graphene_django import DjangoObjectType
import graphene
from users.models import ExtendUser
from .models import Farm
from graphene.types.generic import GenericScalar


class FarmType(DjangoObjectType):
    class Meta:
        model = Farm

################>>>>>>>>>> CreateFarm

class CreateFarm(graphene.Mutation):
    farm = graphene.Field(FarmType)

    class Arguments:
        owner_id=graphene.String()
        name=graphene.String()
        description = graphene.String()
        culture = graphene.String()
        work =GenericScalar()
        token=graphene.String()

    def mutate(self, info, owner_id, description,name,culture,work,token):
        f = Farm(name=name, description=description ,owner_id=owner_id,culture=culture,work=work,token=token)
        o = ExtendUser.objects.get(id=owner_id )
        f.farm=o
        f.save()
        return CreateFarm(farm=f)


################>>>>>>>>>> UpdateFarm

class UpdateFarm(graphene.Mutation):
    farm = graphene.Field(FarmType)

    class Arguments:
        id = graphene.ID()
        name=graphene.String()
        description = graphene.String()
        culture = graphene.String()
        work =GenericScalar()
        token=graphene.String()



    def mutate(self, info, id, name, description,culture,work,token):
        c = Farm.objects.get(id=id)
        c.name = name
        c.description = description
        c.culture = culture
        c.work=work
        c.token=token
        c.save()

        return UpdateFarm(farm=c)

################>>>>>>>>>> deletFarm

class DeletFarm(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info, **kwargs):
        obj = Farm.objects.get(pk=kwargs["id"])
        obj.delete()
        return DeletFarm(ok=True)

