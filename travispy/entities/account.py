from ._entity import Entity



#===================================================================================================
# Account
#===================================================================================================
class Account(Entity):

    __slots__ = [
        'name',
        'login',
        'type',
        'repos_count',
        'subscribed',
    ]