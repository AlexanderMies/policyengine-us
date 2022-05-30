from openfisca_us.model_api import *


class is_ssi_ineligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Is an SSI-ineligible child"
    definition_period = YEAR

    def formula(person, period, parameters):
        return ~person("is_ssi_aged_blind_disabled", period) & person(
            "is_child", period
        )
