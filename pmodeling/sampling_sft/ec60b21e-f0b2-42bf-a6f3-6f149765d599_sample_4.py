import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey    = Transition(label='Site Survey')
modular_design = Transition(label='Modular Design')
system_build   = Transition(label='System Build')
env_control    = Transition(label='Env Control')
nutrient_mix   = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_setup = Transition(label='Planting Setup')
growth_monitor = Transition(label='Growth Monitor')
data_capture   = Transition(label='Data Capture')
pest_control   = Transition(label='Pest Control')
water_cycle    = Transition(label='Water Cycle')
yield_forecast = Transition(label='Yield Forecast')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')
supply_sync    = Transition(label='Supply Sync')
waste_reuse    = Transition(label='Waste Reuse')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    modular_design,
    system_build,
    env_control,
    nutrient_mix,
    seed_selection,
    planting_setup,
    growth_monitor,
    data_capture,
    pest_control,
    water_cycle,
    yield_forecast,
    stakeholder_meet,
    compliance_check,
    supply_sync,
    waste_reuse
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(modular_design, system_build)
root.order.add_edge(system_build, env_control)
root.order.add_edge(system_build, nutrient_mix)
root.order.add_edge(system_build, seed_selection)
root.order.add_edge(env_control, growth_monitor)
root.order.add_edge(nutrient_mix, growth_monitor)
root.order.add_edge(seed_selection, planting_setup)
root.order.add_edge(planting_setup, growth_monitor)
root.order.add_edge(growth_monitor, data_capture)
root.order.add_edge(data_capture, pest_control)
root.order.add_edge(data_capture, water_cycle)
root.order.add_edge(pest_control, yield_forecast)
root.order.add_edge(water_cycle, yield_forecast)
root.order.add_edge(yield_forecast, stakeholder_meet)
root.order.add_edge(stakeholder_meet, compliance_check)
root.order.add_edge(compliance_check, supply_sync)
root.order.add_edge(compliance_check, waste_reuse)