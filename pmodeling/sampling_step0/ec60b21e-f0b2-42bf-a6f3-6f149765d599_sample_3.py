import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define transitions for each activity
site_survey = Transition(label='Site Survey')
modular_design = Transition(label='Modular Design')
system_build = Transition(label='System Build')
env_control = Transition(label='Env Control')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_setup = Transition(label='Planting Setup')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
water_cycle = Transition(label='Water Cycle')
data_capture = Transition(label='Data Capture')
yield_forecast = Transition(label='Yield Forecast')
waste_reuse = Transition(label='Waste Reuse')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')
supply_sync = Transition(label='Supply Sync')

# Define silent transitions
skip = SilentTransition()

# Define the loop for modular design and system build
loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_design, system_build])

# Define exclusive choices for nutrient mix and planting setup
xor1 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, planting_setup])

# Define exclusive choices for pest control and water cycle
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, water_cycle])

# Define exclusive choices for data capture and yield forecast
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_capture, yield_forecast])

# Define exclusive choices for waste reuse and compliance check
xor4 = OperatorPOWL(operator=Operator.XOR, children=[waste_reuse, compliance_check])

# Define exclusive choices for stakeholder meet and supply sync
xor5 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, supply_sync])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)