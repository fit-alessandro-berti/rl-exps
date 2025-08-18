import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analyze = Transition(label='Site Analyze')
soil_enhance = Transition(label='Soil Enhance')
seed_select = Transition(label='Seed Select')
plant_precise = Transition(label='Plant Precise')
sensor_deploy = Transition(label='Sensor Deploy')
climate_monitor = Transition(label='Climate Monitor')
irrigate_adjust = Transition(label='Irrigate Adjust')
nutrient_feed = Transition(label='Nutrient Feed')
pest_control = Transition(label='Pest Control')
community_engage = Transition(label='Community Engage')
feedback_collect = Transition(label='Feedback Collect')
yield_harvest = Transition(label='Yield Harvest')
waste_sort = Transition(label='Waste Sort')
compost_create = Transition(label='Compost Create')
data_analyze = Transition(label='Data Analyze')
network_distribute = Transition(label='Network Distribute')

# Define exclusive choice nodes
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[climate_monitor, nutrient_feed, pest_control])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, irrigate_adjust])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[soil_enhance, seed_select, plant_precise])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[community_engage, feedback_collect])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[yield_harvest, waste_sort])
exclusive_choice6 = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, network_distribute])

# Define partial order
root = StrictPartialOrder(nodes=[site_analyze, exclusive_choice1, exclusive_choice2, exclusive_choice3, exclusive_choice4, exclusive_choice5, exclusive_choice6])
root.order.add_edge(site_analyze, exclusive_choice1)
root.order.add_edge(site_analyze, exclusive_choice2)
root.order.add_edge(site_analyze, exclusive_choice3)
root.order.add_edge(site_analyze, exclusive_choice4)
root.order.add_edge(site_analyze, exclusive_choice5)
root.order.add_edge(site_analyze, exclusive_choice6)