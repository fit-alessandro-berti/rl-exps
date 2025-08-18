from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
install_sensors = Transition(label='Install Sensors')
calibrate_climate = Transition(label='Calibrate Climate')
select_seeds = Transition(label='Select Seeds')
optimize_nutrients = Transition(label='Optimize Nutrients')
deploy_robots = Transition(label='Deploy Robots')
monitor_growth = Transition(label='Monitor Growth')
detect_pests = Transition(label='Detect Pests')
analyze_data = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
customize_pack = Transition(label='Customize Pack')
recycle_waste = Transition(label='Recycle Waste')
audit_energy = Transition(label='Audit Energy')
align_demand = Transition(label='Align Demand')

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_modules])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[install_sensors, calibrate_climate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[select_seeds, optimize_nutrients])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[deploy_robots, monitor_growth])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[detect_pests, analyze_data])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, customize_pack])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, audit_energy])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[align_demand, audit_energy])

# Define partial order
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)