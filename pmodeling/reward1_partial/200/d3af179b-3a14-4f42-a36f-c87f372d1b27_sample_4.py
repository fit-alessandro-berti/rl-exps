import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
led_tuning = Transition(label='LED Tuning')
seed_automation = Transition(label='Seed Automation')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
yield_forecast = Transition(label='Yield Forecast')
energy_audit = Transition(label='Energy Audit')
waste_system = Transition(label='Waste System')
community_meet = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
crop_packing = Transition(label='Crop Packing')
logistics_plan = Transition(label='Logistics Plan')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[
    site_survey,
    design_modules,
    climate_setup,
    nutrient_mix,
    led_tuning,
    seed_automation,
    growth_monitor,
    pest_control,
    yield_forecast,
    energy_audit,
    waste_system,
    community_meet,
    compliance_check,
    crop_packing,
    logistics_plan
])

root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, skip)