import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
modular_design  = Transition(label='Modular Design')
system_build    = Transition(label='System Build')
env_control     = Transition(label='Env Control')
seed_selection  = Transition(label='Seed Selection')
nutrient_mix    = Transition(label='Nutrient Mix')
planting_setup  = Transition(label='Planting Setup')
growth_monitor  = Transition(label='Growth Monitor')
pest_control    = Transition(label='Pest Control')
water_cycle     = Transition(label='Water Cycle')
data_capture    = Transition(label='Data Capture')
yield_forecast  = Transition(label='Yield Forecast')
waste_reuse     = Transition(label='Waste Reuse')
stakeholder_meet= Transition(label='Stakeholder Meet')
compliance_check= Transition(label='Compliance Check')
supply_sync     = Transition(label='Supply Sync')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, modular_design, system_build,
    env_control, seed_selection, nutrient_mix, planting_setup,
    growth_monitor, pest_control, water_cycle, data_capture,
    yield_forecast, waste_reuse, stakeholder_meet, compliance_check,
    supply_sync
])

# Sequence: Site Survey -> Modular Design -> System Build -> Env Control
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(modular_design, system_build)
root.order.add_edge(system_build, env_control)

# Parallel: Nutrient Mix & Seed Selection
root.order.add_edge(env_control, nutrient_mix)
root.order.add_edge(env_control, seed_selection)

# After Nutrient Mix & Seed Selection, plant setup
root.order.add_edge(nutrient_mix, planting_setup)
root.order.add_edge(seed_selection, planting_setup)

# After Planting Setup, concurrent growth monitoring, pest control, water cycle
root.order.add_edge(planting_setup, growth_monitor)
root.order.add_edge(planting_setup, pest_control)
root.order.add_edge(planting_setup, water_cycle)

# After Growth Monitor, Data Capture
root.order.add_edge(growth_monitor, data_capture)

# After Data Capture, Yield Forecast, Waste Reuse
root.order.add_edge(data_capture, yield_forecast)
root.order.add_edge(data_capture, waste_reuse)

# After Yield Forecast & Waste Reuse, Stakeholder Meet
root.order.add_edge(yield_forecast, stakeholder_meet)
root.order.add_edge(waste_reuse, stakeholder_meet)

# After Stakeholder Meet, Compliance Check
root.order.add_edge(stakeholder_meet, compliance_check)

# After Compliance Check, Supply Sync
root.order.add_edge(compliance_check, supply_sync)