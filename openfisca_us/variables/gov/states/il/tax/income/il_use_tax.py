from openfisca_us.model_api import *


class il_use_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "IL use tax"
    unit = USD
    definition_period = YEAR
    reference = ""

    def formula(tax_unit, period, parameters):
        agi = tax_unit("federal_agi", period)
        p = parameters(period).openfisca_us.gov.states.il.tax.income.use_tax
        return p.amount.calc(agi) + p.rate.calc(agi)
