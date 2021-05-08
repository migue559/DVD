from graphene_django import DjangoObjectType
import graphene

class ConnectionBase(graphene.relay.Connection):
    total_count = graphene.Int()
    class Meta:
        abstract = True
    def resolve_total_count(self, info, **kwargs):
        return self.iterable.count()

###############################################
class BaseNode(DjangoObjectType):
    class Meta:
        abstract = True
    @classmethod
    def sortBy(cls, queryset, info):
        try:
            for argument in info.field_asts[0].arguments:
                if argument.name.value == 'sort':
                    return queryset.order_by(argument.value.value)
        except:
            pass
        return queryset
    @classmethod
    def get_queryset(cls, queryset, info):
        return cls.sortBy(queryset, info)
