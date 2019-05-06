#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.events import when
from cocktail.translations import translations
from woost.admin.sections import Folder, CRUD, Settings
from woost.admin.sections.contentsection import ContentSection
from woost.extensions.campaign3.campaignmonitorlist import CampaignMonitorList

translations.load_bundle("woost.extensions.campaign3.admin.sections")


class Campaign3Section(Folder):

    icon_uri = (
        "woost.extensions.campaign3.admin.ui://"
        "images/campaignmonitor.svg"
    )

    def _fill(self):
        self.append(CRUD("lists", model = CampaignMonitorList))
        self.append(Campaign3Settings("settings"))


class Campaign3Settings(Settings):

    icon_uri = (
        "woost.extensions.campaign3.admin.ui://"
        "images/campaignmonitor.svg"
    )

    members = [
        "x_campaign3_api_key",
        "x_campaign3_client_id"
    ]


@when(ContentSection.declared)
def fill(e):
    e.source.append(Campaign3Section("campaign3"))

