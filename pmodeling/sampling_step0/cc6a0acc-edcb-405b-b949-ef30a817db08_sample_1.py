from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
water_check = Transition(label='Water Check')
design_plan = Transition(label='Design Plan')
bed_setup = Transition(label='Bed Setup')
irrigation_install = Transition(label='Irrigation Install')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
planting_phase = Transition(label='Planting Phase')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_prep = Transition(label='Harvest Prep')
community_meet = Transition(label='Community Meet')
waste_manage = Transition(label='Waste Manage')
yield_report = Transition(label='Yield Report')

# Define the silent transition for the 'skip' activity
skip = SilentTransition()

# Define the loop node for the 'Bed Setup' and 'Irrigation Install' activities
loop = OperatorPOWL(operator=Operator.LOOP, children=[bed_setup, irrigation_install])
root = StrictPartialOrder(nodes=[site_survey, load_test, soil_sample, water_check, design_plan, loop, planting_phase, pest_control, growth_monitor, harvest_prep, community_meet, waste_manage, yield_report])
root.order.add_edge(loop, planting_phase)
root.order.add_edge(loop, pest_control)
root.order.add_edge(loop, growth_monitor)
root.order.add_edge(loop, harvest_prep)
root.order.add_edge(loop, community_meet)
root.order.add_edge(loop, waste_manage)
root.order.add_edge(loop, yield_report)

print(root)