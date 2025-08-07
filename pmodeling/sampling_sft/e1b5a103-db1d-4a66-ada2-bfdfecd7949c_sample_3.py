import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis   = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
climate_setup   = Transition(label='Climate Setup')
hydro_install   = Transition(label='Hydroponics Install')
nutrient_mix    = Transition(label='Nutrient Mix')
seed_select     = Transition(label='Seed Select')
light_schedule  = Transition(label='Light Schedule')
irrigation_plan = Transition(label='Irrigation Plan')
health_monitor  = Transition(label='Health Monitor')
pest_control    = Transition(label='Pest Control')
robotic_harvest = Transition(label='Robotic Harvest')
clean_pack      = Transition(label='Clean Packaging')
distribution    = Transition(label='Distribution Plan')
data_collect    = Transition(label='Data Collection')
cycle_feedback  = Transition(label='Cycle Feedback')

# Loop body: Health Monitor -> Pest Control
loop_body = StrictPartialOrder(nodes=[health_monitor, pest_control])
# Loop: Data Collection, then either exit or execute Loop Body then Data Collection again
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collect, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis, structure_check, climate_setup,
    hydro_install, nutrient_mix, seed_select,
    light_schedule, irrigation_plan,
    loop, robotic_harvest, clean_pack, distribution
])

# Define the control-flow dependencies
root.order.add_edge(site_analysis,    structure_check)
root.order.add_edge(structure_check,  climate_setup)
root.order.add_edge(climate_setup,    hydro_install)
root.order.add_edge(hydro_install,    nutrient_mix)
root.order.add_edge(nutrient_mix,     seed_select)
root.order.add_edge(seed_select,      light_schedule)
root.order.add_edge(seed_select,      irrigation_plan)
root.order.add_edge(light_schedule,   loop)
root.order.add_edge(irrigation_plan,  loop)
root.order.add_edge(loop,             robotic_harvest)
root.order.add_edge(loop,             clean_pack)
root.order.add_edge(loop,             distribution)