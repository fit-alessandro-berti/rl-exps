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
choice1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[system_build, install_sensors])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[select_crops, setup_lighting])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[configure_climate, nutrient_mix])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[automate_watering, test_systems])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[train_staff, waste_plan])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[market_link, data_monitor])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[optimize_yield, waste_plan])

# Define the partial order
root = StrictPartialOrder(nodes=[choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8])
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)