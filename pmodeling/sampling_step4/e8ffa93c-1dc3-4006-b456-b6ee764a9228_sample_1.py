import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
env_analysis = Transition(label='Env Analysis')
structure_build = Transition(label='Structure Build')
hydroponics_fit = Transition(label='Hydroponics Fit')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
energy_audit = Transition(label='Energy Audit')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')
supply_sync = Transition(label='Supply Sync')
data_review = Transition(label='Data Review')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    env_analysis,
    structure_build,
    hydroponics_fit,
    nutrient_mix,
    climate_setup,
    energy_audit,
    crop_select,
    pest_control,
    growth_monitor,
    harvest_plan,
    waste_recycle,
    community_meet,
    supply_sync,
    data_review
])

# Define dependencies between activities
root.order.add_edge(site_survey, env_analysis)
root.order.add_edge(env_analysis, structure_build)
root.order.add_edge(structure_build, hydroponics_fit)
root.order.add_edge(hydroponics_fit, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, energy_audit)
root.order.add_edge(energy_audit, crop_select)
root.order.add_edge(crop_select, pest_control)
root.order.add_edge(pest_control, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(waste_recycle, community_meet)
root.order.add_edge(community_meet, supply_sync)
root.order.add_edge(supply_sync, data_review)

# Print the final POWL model
print(root)