import pm4py
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

# Define the loop and choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, pest_control, growth_monitor, planting_phase, community_meet, waste_manage])
xor = OperatorPOWL(operator=Operator.XOR, children=[yield_report, site_survey, load_test, soil_sample, water_check, design_plan, bed_setup, irrigation_install, climate_setup])

# Define the root node
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)