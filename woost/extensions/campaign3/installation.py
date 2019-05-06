"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from woost.models import ExtensionAssets


def install():
    """Creates the assets required by the campaign3 extension."""

    assets = ExtensionAssets("campaign3")

