import graphene
import dvd.core.schema


class Query(
        dvd.core.schema.Query,
        graphene.ObjectType,
    ):
    pass

class Mutation(
        dvd.core.schema.Mutation,    
        graphene.ObjectType
    ):
    pass

class Subscription(        
        graphene.ObjectType
    ):
    pass

schema = graphene.Schema(
    query=Query
    ,mutation=Mutation
    #,subscription=Subscription
)

