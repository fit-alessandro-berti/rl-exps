import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
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

# Define the choice for community engagement and volunteer coordination
xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet, volunteer_coord])

# Define the partial order for the process
root = StrictPartialOrder(nodes=[site_survey, permit_check, hive_setup, loop, xor, data_logging, workshop_plan, supply_order, regulation_review, pollination_map, apiary_audit, feedback_gather, waste_manage])
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(permit_check, hive_setup)
root.order.add_edge(hive_setup, loop)
root.order.add_edge(loop, data_logging)
root.order.add_edge(data_logging, workshop_plan)
root.order.add_edge(workshop_plan, supply_order)
root.order.add_edge(supply_order, regulation_review)
root.order.add_edge(regulation_review, pollination_map)
root.order.add_edge(pollination_map, apiary_audit)
root.order.add_edge(apiary_audit, feedback_gather)
root.order.add_edge(feedback_gather, waste_manage)

# The final result is saved in the variable 'root'