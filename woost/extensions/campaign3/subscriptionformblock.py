"""

.. moduleauthor:: Jordi Fernández <jordi.fernandez@whads.com>
"""
from cocktail import schema
from woost.extensions.blocks.block import Block
from .campaignmonitorlist import CampaignMonitorList


class SubscriptionFormBlock(Block):

    instantiable = True
    type_group = "blocks.forms"

    members_order = ["subscriber_model", "lists"]

    default_controller = (
        "woost.extensions.campaign3."
        "subscriptioncontroller.SubscriptionController"
    )

    subscriber_model = schema.String(
        required = True,
        default = "woost.extensions.campaign3.subscriber.Subscriber",
        text_search = False,
        member_group = "content"
    )

    lists = schema.Collection(
        items = schema.Reference(type = CampaignMonitorList),
        min = 1,
        member_group = "content",
        listed_by_default = False
    )

