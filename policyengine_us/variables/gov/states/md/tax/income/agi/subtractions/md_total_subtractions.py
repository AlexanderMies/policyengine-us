from policyengine_us.model_api import *


class md_total_subtractions(Variable):
    value_type = float
    entity = TaxUnit
    label = "MD total subtractions from AGI"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MD

    def formula(tax_unit, period, parameters):
        subtractions = parameters(
            period
        ).gov.states.md.tax.income.agi.subtractions.sources
        return add(tax_unit, period, subtractions)
