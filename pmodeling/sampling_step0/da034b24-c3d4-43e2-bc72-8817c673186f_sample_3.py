import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for hive monitoring and pest control
loop = OperatorPOWL(operator=Operator.LOOP, children=[hive_monitor, pest_control])

# Define the exclusive choice for honey harvest and data logging
xor = OperatorPOWL(operator=Operator.XOR, children=[honey_harvest, data_logging])

# Define the exclusive choice for supply order and volunteer coordination
xor2 = OperatorPOWL(operator=Operator.XOR, children=[supply_order, volunteer_coord])

# Define the exclusive choice for regulation review and feedback gather
xor3 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, feedback_gather])

# Define the exclusive choice for waste manage and apiary audit
xor4 = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, apiary_audit])

# Define the exclusive choice for workshop plan and pollination map
xor5 = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, pollination_map])

# Define the root model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

# Save the root model