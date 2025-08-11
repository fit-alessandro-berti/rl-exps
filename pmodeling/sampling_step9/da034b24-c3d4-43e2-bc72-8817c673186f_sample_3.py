import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
permit_check = Transition(label='Permit Check')
hive_setup = Transition(label='Hive Setup')
community_meet = Transition(label='Community Meet')
hive_monitor = Transition(label='Hive Monitor')
pest_control = Transition(label='Pest Control')
honey_harvest = Transition(label='Honey Harvest')
data_logging = Transition(label='Data Logging')
workshop_plan = Transition(label='Workshop Plan')
supply_order = Transition(label='Supply Order')
volunteer_coord = Transition(label='Volunteer Coord')
regulation_review = Transition(label='Regulation Review')
pollination_map = Transition(label='Pollination Map')
apiary_audit = Transition(label='Apiary Audit')
feedback_gather = Transition(label='Feedback Gather')
waste_manage = Transition(label='Waste Manage')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_check])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[hive_setup, community_meet])

# Define choice nodes
choice_1 = OperatorPOWL(operator=Operator.XOR, children=[hive_monitor, skip])
choice_2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
choice_3 = OperatorPOWL(operator=Operator.XOR, children=[honey_harvest, skip])
choice_4 = OperatorPOWL(operator=Operator.XOR, children=[data_logging, skip])
choice_5 = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, skip])
choice_6 = OperatorPOWL(operator=Operator.XOR, children=[supply_order, skip])
choice_7 = OperatorPOWL(operator=Operator.XOR, children=[volunteer_coord, skip])
choice_8 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, skip])
choice_9 = OperatorPOWL(operator=Operator.XOR, children=[pollination_map, skip])
choice_10 = OperatorPOWL(operator=Operator.XOR, children=[apiary_audit, skip])
choice_11 = OperatorPOWL(operator=Operator.XOR, children=[feedback_gather, skip])
choice_12 = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define root
root = StrictPartialOrder(nodes=[loop_1, loop_2, choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8, choice_9, choice_10, choice_11, choice_12])

# Add dependencies
root.order.add_edge(loop_1, choice_1)
root.order.add_edge(loop_1, choice_2)
root.order.add_edge(loop_1, choice_3)
root.order.add_edge(loop_1, choice_4)
root.order.add_edge(loop_1, choice_5)
root.order.add_edge(loop_1, choice_6)
root.order.add_edge(loop_1, choice_7)
root.order.add_edge(loop_1, choice_8)
root.order.add_edge(loop_1, choice_9)
root.order.add_edge(loop_1, choice_10)
root.order.add_edge(loop_1, choice_11)
root.order.add_edge(loop_1, choice_12)
root.order.add_edge(loop_2, choice_1)
root.order.add_edge(loop_2, choice_2)
root.order.add_edge(loop_2, choice_3)
root.order.add_edge(loop_2, choice_4)
root.order.add_edge(loop_2, choice_5)
root.order.add_edge(loop_2, choice_6)
root.order.add_edge(loop_2, choice_7)
root.order.add_edge(loop_2, choice_8)
root.order.add_edge(loop_2, choice_9)
root.order.add_edge(loop_2, choice_10)
root.order.add_edge(loop_2, choice_11)
root.order.add_edge(loop_2, choice_12)

# Print the result
print(root)