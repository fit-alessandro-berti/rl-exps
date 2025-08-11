import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, regulation_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[design_modules, install_hydroponics])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[integrate_sensors, calibrate_nutrients])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[program_climate, select_crops])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[optimize_lighting, train_staff])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[plan_harvest, recycle_waste])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[analyze_demand, plan_logistics])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[monitor_systems])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop8, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)