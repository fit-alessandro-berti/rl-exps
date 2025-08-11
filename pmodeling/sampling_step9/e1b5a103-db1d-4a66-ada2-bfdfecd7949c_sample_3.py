import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, structure_check, climate_setup, hydroponics_install, nutrient_mix, seed_select, light_schedule, irrigation_plan, health_monitor, pest_control, robotic_harvest, clean_packaging, distribution_plan, data_collection, cycle_feedback])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)