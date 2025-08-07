import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
structure_reinforce = Transition(label='Structure Reinforce')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_install  = Transition(label='Climate Install')
ai_integration   = Transition(label='AI Integration')
seed_sourcing    = Transition(label='Seed Sourcing')
nutrient_prep    = Transition(label='Nutrient Prep')
system_testing   = Transition(label='System Testing')
staff_training   = Transition(label='Staff Training')
crop_planting    = Transition(label='Crop Planting')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
harvest_schedule = Transition(label='Harvest Schedule')
quality_check    = Transition(label='Quality Check')
market_dispatch  = Transition(label='Market Dispatch')
waste_recycle    = Transition(label='Waste Recycle')
data_analysis    = Transition(label='Data Analysis')

# Build the loop body: Pest Control -> Growth Monitor -> Pest Control
loop_body = StrictPartialOrder(nodes=[pest_control, growth_monitor])
loop_body.order.add_edge(pest_control, growth_monitor)

# Define the loop: do Crop Planting, then either exit or do the loop body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting, loop_body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_reinforce,
    hydroponic_setup,
    climate_install,
    ai_integration,
    seed_sourcing,
    nutrient_prep,
    system_testing,
    staff_training,
    loop,
    quality_check,
    market_dispatch,
    waste_recycle,
    data_analysis
])

# Define the control-flow edges
root.order.add_edge(site_survey,    structure_reinforce)
root.order.add_edge(structure_reinforce, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_install)
root.order.add_edge(climate_install, ai_integration)
root.order.add_edge(ai_integration, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(nutrient_prep, system_testing)
root.order.add_edge(system_testing, staff_training)
root.order.add_edge(staff_training, loop)
root.order.add_edge(loop, quality_check)
root.order.add_edge(quality_check, market_dispatch)
root.order.add_edge(market_dispatch, waste_recycle)
root.order.add_edge(waste_recycle, data_analysis)