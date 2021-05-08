import graphene
import graphql_jwt
import datetime



#################################################################
#########   QUERYS   ############################################
#################################################################
class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")    
    #userQuery = DjangoFilterConnectionField(UserNode)

#################################################################
#########    MUTATIONS   ########################################
#################################################################
class Mutation( graphene.ObjectType):    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

#################################################################
#########    SUBSCRIPTIONS    ###################################
#################################################################
class Subscription(graphene.ObjectType):    
    hello = graphene.String()
    def resolve_hello(root, info):
        return Observable.interval(1000).map(lambda i: datetime.datetime.now())
    ###########################################    