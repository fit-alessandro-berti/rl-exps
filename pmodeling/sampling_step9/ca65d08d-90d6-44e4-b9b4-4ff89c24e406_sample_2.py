import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities (tau labels)
skip = SilentTransition()

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, system_build, install_sensors, select_crops, setup_lighting, configure_climate, nutrient_mix, automate_watering])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[test_systems, train_staff, waste_plan, market_link, data_monitor])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)

# Print the root of the POWL model
print(root)