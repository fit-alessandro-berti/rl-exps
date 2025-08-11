import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
climate_setup = Transition(label='Climate Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_mix = Transition(label='Nutrient Mix')
seed_select = Transition(label='Seed Select')
light_schedule = Transition(label='Light Schedule')
irrigation_plan = Transition(label='Irrigation Plan')
health_monitor = Transition(label='Health Monitor')
pest_control = Transition(label='Pest Control')
robotic_harvest = Transition(label='Robotic Harvest')
clean_packaging = Transition(label='Clean Packaging')
distribution_plan = Transition(label='Distribution Plan')
data_collection = Transition(label='Data Collection')
cycle_feedback = Transition(label='Cycle Feedback')

# Define silent transitions
skip = SilentTransition()

# Define loop for hydroponics install and nutrient mix
loop_hydroponics = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_install, nutrient_mix])
loop_hydroponics.order.add_edge(hydroponics_install, nutrient_mix)

# Define exclusive choice for light schedule and irrigation plan
xor_light_irrigation = OperatorPOWL(operator=Operator.XOR, children=[light_schedule, irrigation_plan])

# Define exclusive choice for pest control and health monitor
xor_pest_health = OperatorPOWL(operator=Operator.XOR, children=[pest_control, health_monitor])

# Define exclusive choice for robotic harvest and clean packaging
xor_harvest_clean = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, clean_packaging])

# Define exclusive choice for distribution plan and data collection
xor_plan_collection = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, data_collection])

# Define exclusive choice for cycle feedback and site analysis
xor_feedback_site = OperatorPOWL(operator=Operator.XOR, children=[cycle_feedback, site_analysis])

# Define the root node
root = StrictPartialOrder(nodes=[loop_hydroponics, xor_light_irrigation, xor_pest_health, xor_harvest_clean, xor_plan_collection, xor_feedback_site])
root.order.add_edge(loop_hydroponics, xor_light_irrigation)
root.order.add_edge(loop_hydroponics, xor_pest_health)
root.order.add_edge(loop_hydroponics, xor_harvest_clean)
root.order.add_edge(loop_hydroponics, xor_plan_collection)
root.order.add_edge(loop_hydroponics, xor_feedback_site)

# Save the final result in the variable 'root'