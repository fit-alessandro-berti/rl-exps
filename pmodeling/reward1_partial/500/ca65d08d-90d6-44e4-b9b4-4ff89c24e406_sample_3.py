import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_build = Transition(label='System Build')
install_sensors = Transition(label='Install Sensors')
select_crops = Transition(label='Select Crops')
setup_lighting = Transition(label='Setup Lighting')
configure_climate = Transition(label='Configure Climate')
nutrient_mix = Transition(label='Nutrient Mix')
automate_watering = Transition(label='Automate Watering')
test_systems = Transition(label='Test Systems')
train_staff = Transition(label='Train Staff')
waste_plan = Transition(label='Waste Plan')
market_link = Transition(label='Market Link')
data_monitor = Transition(label='Data Monitor')
optimize_yield = Transition(label='Optimize Yield')

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[system_build, install_sensors])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[select_crops, setup_lighting])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[configure_climate, nutrient_mix])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[automate_watering, test_systems])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[train_staff, waste_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[market_link, data_monitor])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[optimize_yield, xor6])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor6)