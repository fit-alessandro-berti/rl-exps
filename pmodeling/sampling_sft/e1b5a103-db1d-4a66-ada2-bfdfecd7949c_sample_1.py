import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_analysis    = Transition(label='Site Analysis')
structure_check  = Transition(label='Structure Check')
climate_setup    = Transition(label='Climate Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_select      = Transition(label='Seed Select')
light_schedule   = Transition(label='Light Schedule')
irrigation_plan  = Transition(label='Irrigation Plan')
health_monitor   = Transition(label='Health Monitor')
pest_control     = Transition(label='Pest Control')
robotic_harvest  = Transition(label='Robotic Harvest')
clean_packaging  = Transition(label='Clean Packaging')
distribution_plan = Transition(label='Distribution Plan')
data_collection  = Transition(label='Data Collection')
cycle_feedback   = Transition(label='Cycle Feedback')

# Define the loop body (monitoring and pest control, then data collection and feedback)
loop_body = StrictPartialOrder(nodes=[health_monitor, pest_control, data_collection, cycle_feedback])

# Build the loop: do the body, then optionally do the body again
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_check,
    climate_setup,
    hydroponics_install,
    nutrient_mix,
    seed_select,
    light_schedule,
    irrigation_plan,
    loop,
    robotic_harvest,
    clean_packaging,
    distribution_plan
])

# Add the control-flow edges
root.order.add_edge(site_analysis,    structure_check)
root.order.add_edge(structure_check,  climate_setup)
root.order.add_edge(climate_setup,    hydroponics_install)
root.order.add_edge(hydroponics_install, nutrient_mix)
root.order.add_edge(nutrient_mix,     seed_select)
root.order.add_edge(seed_select,      light_schedule)
root.order.add_edge(light_schedule,   irrigation_plan)
root.order.add_edge(irrigation_plan,  loop)
root.order.add_edge(loop,             robotic_harvest)
root.order.add_edge(robotic_harvest,  clean_packaging)
root.order.add_edge(clean_packaging,  distribution_plan)