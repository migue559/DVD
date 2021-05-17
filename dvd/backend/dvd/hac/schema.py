from dvd.core.schemabase import ConnectionBase, BaseNode
from graphene_subscriptions.events import UPDATED
from dvd.hac.models import HiveCatalogue
from graphene_django.filter import DjangoFilterConnectionField
import graphene


print("HOLA")

########################################################################################
########################################################################################
class HiveCatalogueNode(BaseNode):
    class Meta:
        model = HiveCatalogue
        interfaces = [graphene.relay.Node]
        connection_class = ConnectionBase
        filter_fields = {
            'name': ['icontains'],
        }
    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_anonymous:
            return queryset.filter(isPublic=True)
        return HiveCatalogue().getUserCatalogues(info.context.user, queryset)

#################################################################
#########   QUERYS   ############################################
#################################################################
class Query(object):
    hiveCatalogueID = graphene.relay.Node.Field(HiveCatalogueNode)
    hiveCatalogueQuery = DjangoFilterConnectionField(HiveCatalogueNode)
    #################################################################
    hiveSchemaID = graphene.JSONString(
        id = graphene.ID(required=True, description = "ID del catálogo")
    )
    def resolve_hiveSchemaID(self, info, id):
        # HiveCatalogue().getPermission(info.context.user)
        return HiveCatalogue().getSchema(id)
    #################################################################
    hiveGetDataID = graphene.JSONString(
        id=graphene.ID(required=True, description = "ID del catálogo")
    )
    def resolve_hiveGetDataID(self, info, id):
        # HiveCatalogue().getPermission(info.context.user)
        return HiveCatalogue().getData(id)


#################################################################
#########    SUBSCRIPTIONS    ###################################
#################################################################
class Subscription(graphene.ObjectType):
    hiveCatalogueSubscription = graphene.Field(HiveCatalogueNode, id=graphene.ID())
    def resolve_hiveCatalogueSubscription(root, info, id):
        return root.filter(
            lambda event:
                event.operation == UPDATED and
                isinstance(event.instance, HiveCatalogue) and
                event.instance.pk == HiveCatalogue().get64Id(id)
        ).map(lambda event: event.instance)
