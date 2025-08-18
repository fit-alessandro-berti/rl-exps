from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_check = Transition(label='Environment Check')
planting_setup = Transition(label='Planting Setup')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
automated_harvest = Transition(label='Automated Harvest')
quality_inspect = Transition(label='Quality Inspect')
packaging_prep = Transition(label='Packaging Prep')
order_fulfill = Transition(label='Order Fulfill')
local_delivery = Transition(label='Local Delivery')
waste_collect = Transition(label='Waste Collect')
biomass_process = Transition(label='Biomass Process')
compost_create = Transition(label='Compost Create')
energy_recover = Transition(label='Energy Recover')
regulation_review = Transition(label='Regulation Review')
community_engage = Transition(label='Community Engage')

# Define the control-flow operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, environment_check])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[planting_setup, growth_monitoring])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, automated_harvest])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, packaging_prep])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[order_fulfill, local_delivery])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[waste_collect, biomass_process])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[compost_create, energy_recover])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, community_engage])

# Define the partial order structure
root = StrictPartialOrder(nodes=[seed_selection, choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8])
root.order.add_edge(seed_selection, choice1)
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)

print(root)