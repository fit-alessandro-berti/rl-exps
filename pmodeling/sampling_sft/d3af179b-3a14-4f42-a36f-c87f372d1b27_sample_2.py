import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
climate_setup  = Transition(label='Climate Setup')
nutrient_mix   = Transition(label='Nutrient Mix')
led_tuning     = Transition(label='LED Tuning')
seed_auto      = Transition(label='Seed Automation')
growth_monitor = Transition(label='Growth Monitor')
pest_control   = Transition(label='Pest Control')
yield_forecast = Transition(label='Yield Forecast')
energy_audit   = Transition(label='Energy Audit')
waste_system   = Transition(label='Waste System')
compliance_chk = Transition(label='Compliance Check')
community_meet = Transition(label='Community Meet')
crop_packing   = Transition(label='Crop Packing')
logistics_plan = Transition(label='Logistics Plan')

# Silent transition for loop exit
skip = SilentTransition()

# Loop: repeat Compliance Check -> Community Meet until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_chk, community_meet])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_modules,
    climate_setup,
    nutrient_mix,
    led_tuning,
    seed_auto,
    growth_monitor,
    pest_control,
    yield_forecast,
    energy_audit,
    waste_system,
    loop,
    crop_packing,
    logistics_plan
])

# Define the control-flow order
root.order.add_edge(site_survey,    design_modules)
root.order.add_edge(design_modules, climate_setup)
root.order.add_edge(climate_setup,  nutrient_mix)
root.order.add_edge(nutrient_mix,   led_tuning)
root.order.add_edge(led_tuning,     seed_auto)
root.order.add_edge(seed_auto,      growth_monitor)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control,   yield_forecast)
root.order.add_edge(yield_forecast, energy_audit)
root.order.add_edge(energy_audit,   waste_system)
root.order.add_edge(waste_system,   loop)
root.order.add_edge(loop,           crop_packing)
root.order.add_edge(crop_packing,   logistics_plan)