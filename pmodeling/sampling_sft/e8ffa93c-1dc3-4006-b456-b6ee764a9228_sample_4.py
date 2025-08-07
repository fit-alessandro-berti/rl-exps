import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
env_analysis   = Transition(label='Env Analysis')
structure_build= Transition(label='Structure Build')
hydro_fit      = Transition(label='Hydroponics Fit')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_setup  = Transition(label='Climate Setup')
energy_audit   = Transition(label='Energy Audit')
crop_select    = Transition(label='Crop Select')
pest_control   = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan   = Transition(label='Harvest Plan')
waste_recycle  = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')
supply_sync    = Transition(label='Supply Sync')
data_review    = Transition(label='Data Review')

# Loop for continuous monitoring and adjustments
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, data_review])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, env_analysis,
    structure_build, hydro_fit, nutrient_mix, climate_setup, energy_audit,
    crop_select, pest_control,
    monitor_loop,
    harvest_plan, waste_recycle, community_meet, supply_sync
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,    env_analysis)
root.order.add_edge(env_analysis,   structure_build)
root.order.add_edge(structure_build, hydro_fit)
root.order.add_edge(structure_build, nutrient_mix)
root.order.add_edge(structure_build, climate_setup)
root.order.add_edge(structure_build, energy_audit)
root.order.add_edge(hydro_fit,       crop_select)
root.order.add_edge(nutrient_mix,    crop_select)
root.order.add_edge(climate_setup,   crop_select)
root.order.add_edge(energy_audit,    crop_select)
root.order.add_edge(crop_select,     pest_control)
root.order.add_edge(pest_control,    monitor_loop)
root.order.add_edge(monitor_loop,    harvest_plan)
root.order.add_edge(harvest_plan,    waste_recycle)
root.order.add_edge(harvest_plan,    community_meet)
root.order.add_edge(harvest_plan,    supply_sync)