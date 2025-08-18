import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
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

# Define the loop for site survey and permit check
site_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_check])

# Define the XOR for hive setup and community meet
hive_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[hive_setup, community_meet])

# Define the loop for hive monitor, pest control, and honey harvest
monitor_control_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[hive_monitor, pest_control, honey_harvest])

# Define the XOR for data logging and workshop plan
data_logging_xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, workshop_plan])

# Define the loop for supply order, volunteer coordination, and regulation review
supply_volunteer_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_order, volunteer_coord, regulation_review])

# Define the loop for pollination map, apiary audit, feedback gather, and waste manage
pollination_audit_gather_waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[pollination_map, apiary_audit, feedback_gather, waste_manage])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[site_check_loop, hive_setup_xor, monitor_control_harvest_loop, data_logging_xor, supply_volunteer_review_loop, pollination_audit_gather_waste_loop])

# Define the dependencies between nodes
root.order.add_edge(site_check_loop, hive_setup_xor)
root.order.add_edge(hive_setup_xor, monitor_control_harvest_loop)
root.order.add_edge(monitor_control_harvest_loop, data_logging_xor)
root.order.add_edge(data_logging_xor, supply_volunteer_review_loop)
root.order.add_edge(supply_volunteer_review_loop, pollination_audit_gather_waste_loop)

# Print the root
print(root)