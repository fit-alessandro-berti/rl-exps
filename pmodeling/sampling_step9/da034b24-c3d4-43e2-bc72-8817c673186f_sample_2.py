import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for hive setup
xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, skip])

# Define the loop for site survey
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_check])

# Define the loop for hive monitor
loop_hive_monitor = OperatorPOWL(operator=Operator.LOOP, children=[hive_monitor, pest_control])

# Define the loop for data logging
loop_data_logging = OperatorPOWL(operator=Operator.LOOP, children=[data_logging, supply_order])

# Define the loop for volunteer coordination
loop_volunteer_coord = OperatorPOWL(operator=Operator.LOOP, children=[volunteer_coord, regulation_review])

# Define the loop for feedback gathering
loop_feedback_gather = OperatorPOWL(operator=Operator.LOOP, children=[feedback_gather, waste_manage])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_site_survey, loop_hive_monitor, loop_data_logging, loop_volunteer_coord, loop_feedback_gather, workshop_plan, pollination_map, apiary_audit, community_meet, honey_harvest])
root.order.add_edge(loop_site_survey, loop_hive_monitor)
root.order.add_edge(loop_site_survey, loop_data_logging)
root.order.add_edge(loop_site_survey, loop_volunteer_coord)
root.order.add_edge(loop_site_survey, loop_feedback_gather)
root.order.add_edge(loop_hive_monitor, loop_data_logging)
root.order.add_edge(loop_hive_monitor, loop_volunteer_coord)
root.order.add_edge(loop_hive_monitor, loop_feedback_gather)
root.order.add_edge(loop_data_logging, loop_volunteer_coord)
root.order.add_edge(loop_data_logging, loop_feedback_gather)
root.order.add_edge(loop_volunteer_coord, loop_feedback_gather)