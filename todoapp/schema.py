from graphene_django import DjangoObjectType
import graphene
from users.models import ExtendUser
from .models import TodoList


class TodoType(DjangoObjectType):
    class Meta:
        model = TodoList

################>>>>>>>>>> CreateTodo

class CreateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        user_id=graphene.String()
        name=graphene.String()
        description = graphene.String()
        date=graphene.DateTime()
        isdone=graphene.Boolean()

    def mutate(self, info, user_id, description,name,date):
        f = TodoList(name=name, description=description,date=date ,user_id=user_id ,isdone=False)
        o = ExtendUser.objects.get(id=user_id )
        f.todo=o
        f.save()
        return CreateTodo(todo=f)


################>>>>>>>>>> UpdateTodo

class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        id = graphene.ID()
        name=graphene.String()
        description = graphene.String()
        date=graphene.DateTime()
        isdone=graphene.Boolean()
        
    def mutate(self, info, isdone, description,name,date):
        c = TodoList.objects.get(id=id)
        c.name = name
        c.description = description
        c.date=date
        c.isdone=isdone
        c.save()

        return UpdateTodo(todo=c)
################>>>>>>>>>> todo Done
class TodoDone(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        id = graphene.ID()

    def mutate(self, info ,**kwargs):
        c = TodoList.objects.get(pk=kwargs["id"])
        c.isdone=True
        c.save()

        return TodoDone(todo=c)

################>>>>>>>>>> delettodo

class Delettodo(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info, **kwargs):
        obj = TodoList.objects.get(pk=kwargs["id"])
        obj.delete()
        return Delettodo(ok=True)

