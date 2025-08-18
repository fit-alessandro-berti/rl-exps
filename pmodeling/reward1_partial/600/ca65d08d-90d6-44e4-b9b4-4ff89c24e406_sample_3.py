import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, system_build, install_sensors])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[select_crops, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[setup_lighting, configure_climate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, automate_watering])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[test_systems, train_staff])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, market_link])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[data_monitor, optimize_yield])

root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)

# Add dependencies if needed
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)