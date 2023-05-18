import graphene
from graphene_django import DjangoObjectType
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
import graphql_jwt

from django.contrib.auth.hashers import make_password

from farm.models import Farm as FarmModel
from worker.models import Worker as WorkerModel
from machine.models import Machine as MachineModel
from presence.models import PresenceDate as PresenceDateModel
from location.models import Location as LocationModel
from todoapp.models import TodoList as  TodoListModel
from users.models import ExtendUser


from farm.schema import (
    FarmType,
    CreateFarm,
    UpdateFarm ,
    DeletFarm
)
from worker.schema import (
    WorkerType,
    CreateWorker,
    UpdateWorker,DeletWorker
)
from machine.schema import (
    MachineType,
    CreateMachine,
    UpdateMachine
)
from presence.schema import (
    PresenceType,
    AddPresence,
)

from location.schema import (
    LocationType,
    CreateLocation,
)

from todoapp.schema import(
    TodoType,
    CreateTodo,
    UpdateTodo,
    Delettodo,
    TodoDone
)


class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   resend_activation_email = mutations.ResendActivationEmail.Field()
   send_password_reset_email = mutations.SendPasswordResetEmail.Field()
   password_reset = mutations.PasswordReset.Field()
   password_change = mutations.PasswordChange.Field()
   verify_token = graphql_jwt.Verify.Field()
   refresh_token = graphql_jwt.Refresh.Field()
   revoke_token = graphql_jwt.Revoke.Field()


class DeletUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info, **kwargs):
        obj = ExtendUser.objects.get(pk=kwargs["id"])
        obj.delete()
        return DeletUser(ok=True)


class VerifyUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info, **kwargs):
        obj = ExtendUser.objects.get(pk=kwargs["id"])
        obj.status.verified=True
        obj.is_active=True
        obj.status.save()
        obj.save()

        return VerifyUser(ok=True)



class VerifyAuth(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        phone = graphene.String()

    def mutate(cls, info, phone):
        obj = ExtendUser.objects.get(phone=phone)
        obj.status.verified=True
        obj.is_active=True
        obj.status.save()
        obj.save()

        return VerifyAuth(ok=True)


class ChangePass(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        phone = graphene.String()
        password = graphene.String()

    def mutate(cls, info, phone,password):
        obj = ExtendUser.objects.get(phone=phone)
        encryptedpassword=make_password(password)
        obj.password=encryptedpassword
        obj.save()
        return ChangePass(ok=True)
        
class IsUserExist(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        phone = graphene.String()

    def mutate(cls, info, phone):
        try:
            obj = ExtendUser.objects.get(phone=phone)
            return IsUserExist(ok=True)
        except:
            raise Exception("This phone number already used")



class BlockUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info, **kwargs):
        obj = ExtendUser.objects.get(pk=kwargs["id"])
        obj.status.verified=False
        obj.is_active=False
        obj.status.save()
        obj.save()
        return BlockUser(ok=True)

class UpdateAccount(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()
        phone=graphene.String()
        firstName=graphene.String()
        lastName=graphene.String()
        email=graphene.String()
    def mutate(cls, info,phone,firstName,lastName,email, **kwargs):
        obj = ExtendUser.objects.get(pk=kwargs["id"])
        obj.phone=phone
        obj.firstName=firstName
        obj.lastName=lastName
        obj.email=email
        obj.save()
        return UpdateAccount(ok=True)


class Query(UserQuery, MeQuery, graphene.ObjectType):
    farms=graphene.List(FarmType)
    workers=graphene.List(WorkerType)
    machines=graphene.List(MachineType)
    presences =graphene.List(PresenceType)
    location =graphene.List(LocationType)
    todoapp=graphene.List(TodoType)

    def resolve_farms(self,info):
        return FarmModel.objects.all()

    def resolve_worker(self,info):
        return WorkerModel.objects.all()

    def resolve_machine(self,info):
        return MachineModel.objects.all()
        
    def resolve_presence(self,info):
        return PresenceDateModel.objects.all()

    def resolve_location(self,info):
        return LocationModel.objects.all()

    def resolve_todoapp(self,info):
        return TodoListModel.objects.all()


class Mutation(AuthMutation, graphene.ObjectType):
    Create_farm = CreateFarm.Field()
    Creat_worker = CreateWorker.Field()
    Create_machine = CreateMachine.Field()
    Creat_todo=CreateTodo.Field()
    Add_presence=AddPresence.Field()
    Creat_location=CreateLocation.Field()


    Update_farm = UpdateFarm.Field()
    Update_todo =UpdateTodo.Field()
    Update_worker = UpdateWorker.Field()
    Update_machine = UpdateMachine.Field()
    Update_Account=UpdateAccount.Field()

    Delet_farm = DeletFarm.Field()
    Delet_todo = Delettodo.Field()
    Delet_Worker=DeletWorker.Field()
    Delet_user=DeletUser.Field()

    Verify_User=VerifyUser.Field()
    Verify_Auth=VerifyAuth.Field()
    Block_user=BlockUser.Field()
    Todo_Done = TodoDone.Field()
    Change_Pass=ChangePass.Field()
    IsUser_Exist=IsUserExist.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)