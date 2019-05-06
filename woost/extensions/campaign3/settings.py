"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail import schema
from cocktail.translations import translations
from woost.models import add_setting

translations.load_bundle("woost.extensions.campaign3.settings")

add_setting(
    schema.String(
        "x_campaign3_api_key"
    )
)

add_setting(
    schema.String(
        "x_campaign3_client_id"
    )
)

