import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
regulation_check = Transition(label='Regulation Check')
design_modules = Transition(label='Design Modules')
install_hydroponics = Transition(label='Install Hydroponics')
integrate_sensors = Transition(label='Integrate Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
program_climate = Transition(label='Program Climate')
select_crops = Transition(label='Select Crops')
optimize_lighting = Transition(label='Optimize Lighting')
train_staff = Transition(label='Train Staff')
plan_harvest = Transition(label='Plan Harvest')
recycle_waste = Transition(label='Recycle Waste')
analyze_demand = Transition(label='Analyze Demand')
plan_logistics = Transition(label='Plan Logistics')
monitor_systems = Transition(label='Monitor Systems')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, design_modules])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[install_hydroponics, integrate_sensors])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[calibrate_nutrients, program_climate])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[select_crops, optimize_lighting])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[train_staff, plan_harvest])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[recycle_waste, analyze_demand])
loop_7 = OperatorPOWL(operator=Operator.LOOP, children=[plan_logistics, monitor_systems])

# Define exclusive choice nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_1])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_2])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_3])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_4])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_5])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_6])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_7])

# Create root node
root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7])
root.order.add_edge(xor_1, loop_1)
root.order.add_edge(xor_2, loop_2)
root.order.add_edge(xor_3, loop_3)
root.order.add_edge(xor_4, loop_4)
root.order.add_edge(xor_5, loop_5)
root.order.add_edge(xor_6, loop_6)
root.order.add_edge(xor_7, loop_7)

# Save the final result in the variable 'root'