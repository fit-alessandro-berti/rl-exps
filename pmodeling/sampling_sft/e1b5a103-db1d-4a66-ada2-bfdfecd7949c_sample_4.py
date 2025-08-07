import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
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
distribution_plan= Transition(label='Distribution Plan')
data_collection  = Transition(label='Data Collection')
cycle_feedback   = Transition(label='Cycle Feedback')

# Loop for continuous monitoring, pest control, and data collection
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, pest_control, data_collection])

# Build the partial order representing the overall process
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_check,
    climate_setup,
    hydroponics_install,
    nutrient_mix,
    seed_select,
    light_schedule,
    irrigation_plan,
    monitor_loop,
    robotic_harvest,
    clean_packaging,
    distribution_plan,
    cycle_feedback
])

# Sequence edges
root.order.add_edge(site_analysis,    structure_check)
root.order.add_edge(structure_check,  climate_setup)
root.order.add_edge(climate_setup,    hydroponics_install)
root.order.add_edge(hydroponics_install, nutrient_mix)
root.order.add_edge(nutrient_mix,     seed_select)
root.order.add_edge(seed_select,      light_schedule)
root.order.add_edge(light_schedule,   irrigation_plan)
root.order.add_edge(irrigation_plan,  monitor_loop)
root.order.add_edge(monitor_loop,     robotic_harvest)
root.order.add_edge(robotic_harvest,  clean_packaging)
root.order.add_edge(clean_packaging,  distribution_plan)
root.order.add_edge(distribution_plan, cycle_feedback)