from graphene_django import DjangoObjectType
import graphene
from farm.models import Farm
from .models import Worker


class WorkerType(DjangoObjectType):
    class Meta:
        model = Worker


class CreateWorker(graphene.Mutation):
    worker = graphene.Field(WorkerType)

    class Arguments: 
        firstName=graphene.String()
        secondName=graphene.String()
        code=graphene.String()
        startWork=graphene.DateTime()
        farm_id=graphene.String()
        workField=graphene.String()
        

    def mutate(self, info,startWork,code,farm_id, secondName,firstName,workField):
        f = Worker(firstName=firstName,code=code,startWork=startWork, secondName=secondName,farm_id=farm_id,workField=workField)
        o = Farm.objects.get(id=farm_id)
        f.worker=o
        f.save()
        return CreateWorker(worker=f)

################>>>>>>>>>> UpdateWorker

class UpdateWorker(graphene.Mutation):
    worker = graphene.Field(WorkerType)

    class Arguments:
        id = graphene.ID()
        firstName=graphene.String()
        secondName=graphene.String()
        code=graphene.String()
        workField=graphene.String()

     
    def mutate(self, info, id, secondName, firstName ,code,workField):
        c = Worker.objects.get(id=id)
        c.secondName = secondName
        c.firstName = firstName
        c.code = code
        c.workField=workField
        c.save()

        return UpdateWorker(worker=c)


################>>>>>>>>>> deletWorker

class DeletWorker(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info, **kwargs):
        obj = Worker.objects.get(pk=kwargs["id"])
        obj.delete()
        return DeletWorker(ok=True)
