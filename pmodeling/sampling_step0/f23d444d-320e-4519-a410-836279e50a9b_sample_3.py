import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the transitions
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
module_build = Transition(label='Module Build')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_plan = Transition(label='Planting Plan')
irrigation_setup = Transition(label='Irrigation Setup')
climate_control = Transition(label='Climate Control')
lighting_adjust = Transition(label='Lighting Adjust')
pest_monitor = Transition(label='Pest Monitor')
waste_cycle = Transition(label='Waste Cycle')
data_capture = Transition(label='Data Capture')
yield_forecast = Transition(label='Yield Forecast')
regulation_check = Transition(label='Regulation Check')
community_meet = Transition(label='Community Meet')
harvest_prep = Transition(label='Harvest Prep')
market_link = Transition(label='Market Link')
# Define the silent transitions
skip = SilentTransition()
# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, skip])
# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[module_build, system_design])
# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor])
# Add the edges
root.order.add_edge(loop, xor)
# Print the POWL model
print(root)