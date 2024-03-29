"""

.. moduleauthor:: Jordi Fernández <jordi.fernandez@whads.com>
"""
from cocktail import schema
from cocktail.translations import translations
from cocktail.urls import URL
from woost.models import Item, Page, get_setting
from createsend import CreateSend, List


class CampaignMonitorList(Item):

    members_order = [
        "title",
        "list_id",
        "confirmation_page",
        "confirmation_success_page",
        "unsubscribe_page",
    ]

    title = schema.String(
        required = True,
        descriptive = True,
        spellcheck = True
    )

    list_id = schema.String(
        required = True,
        unique = True,
        text_search = False
    )

    confirmation_page = schema.Reference(
        type = Page,
        related_end = schema.Collection()
    )

    confirmation_success_page = schema.Reference(
        type = Page,
        related_end = schema.Collection()
    )

    unsubscribe_page = schema.Reference(
        type = Page,
        related_end = schema.Collection()
    )

    def update(self):
        list = List(
            {"api_key": get_setting("x_campaign3_api_key")},
            self.list_id
        )
        details = list.details()

        if self.confirmation_success_page:
            confirmation_success_page = \
                self.confirmation_success_page.get_uri(host = "!")
        else:
            confirmation_success_page = None

        if self.unsubscribe_page:
            unsubscribe_page = (
                self.unsubscribe_page.get_uri(host = "!")
                .merge(URL(query = {"email": "[email]"}))
            )
        else:
            unsubscribe_page = None

        list.update(
            details.Title,
            unsubscribe_page,
            details.ConfirmedOptIn,
            confirmation_success_page,
            unsubscribe_setting=details.UnsubscribeSetting
        )

