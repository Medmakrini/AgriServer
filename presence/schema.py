from graphene_django import DjangoObjectType
import graphene
from worker.models import Worker
from .models import PresenceDate


class PresenceType(DjangoObjectType):
    class Meta:
        model = PresenceDate


class AddPresence(graphene.Mutation):
    presenceDate = graphene.Field(PresenceType)

    class Arguments: 
        date=graphene.DateTime()
        hoursofWork=graphene.String()
        worker_id=graphene.String()
        

    def mutate(self, info,date,hoursofWork,worker_id):
        f = PresenceDate(date=date,hoursofWork=hoursofWork,worker_id=worker_id)
        o = Worker.objects.get(id=worker_id)
        f.presenceDate=o
        f.save()
        return AddPresence(presenceDate=f)
 
