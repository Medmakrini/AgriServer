
from graphene_django import DjangoObjectType
import graphene
from farm.models import Farm
from .models import Machine


class MachineType(DjangoObjectType):
    class Meta:
        model = Machine


class CreateMachine(graphene.Mutation):
    machine = graphene.Field(MachineType)

    class Arguments:
        farm_id=graphene.String()
        name=graphene.String()
        description = graphene.String()

    def mutate(self, info, farm_id, description,name):
        f = Machine(name=name, description=description , farm_id=farm_id )
        o = Farm.objects.get(id=farm_id)
        f.machine=o
        f.save()
        return CreateMachine(machine=f)


################>>>>>>>>>> UpdateMachine

class UpdateMachine(graphene.Mutation):
    machine = graphene.Field(MachineType)

    class Arguments:
        id = graphene.ID()
        name=graphene.String()
        description = graphene.String()

    def mutate(self, info, id, name, description):
        c = Machine.objects.get(id=id)
        c.name = name
        c.description = description
        c.save()

        return UpdateMachine(machine=c)


################>>>>>>>>>> deletMachine

class DeletMachine(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info, **kwargs):
        obj = Machine.objects.get(pk=kwargs["id"])
        obj.delete()
        return DeletMachine(ok=True)
