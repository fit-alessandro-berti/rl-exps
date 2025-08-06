import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
source_materials = Transition(label='Source Materials')
install_framework = Transition(label='Install Framework')
setup_irrigation = Transition(label='Setup Irrigation')
integrate_sensors = Transition(label='Integrate Sensors')
configure_ai = Transition(label='Configure AI')
select_crops = Transition(label='Select Crops')
calibrate_climate = Transition(label='Calibrate Climate')
plant_seeds = Transition(label='Plant Seeds')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
recycle_waste = Transition(label='Recycle Waste')
engage_community = Transition(label='Engage Community')
ensure_compliance = Transition(label='Ensure Compliance')
distribute_produce = Transition(label='Distribute Produce')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[calibrate_climate, manage_pests, recycle_waste])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[plant_seeds, monitor_growth])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[distribute_produce])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[select_crops, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[configure_ai, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[integrate_sensors, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[install_framework, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[setup_irrigation, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[design_modules, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[source_materials, skip])

# Define the root
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, loop1, loop2, loop3])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop1)
root.order.add_edge(xor5, loop2)
root.order.add_edge(xor6, loop3)
root.order.add_edge(xor7, loop1)
root.order.add_edge(xor8, loop2)

print(root)