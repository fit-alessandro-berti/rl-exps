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

# Define the process
root = StrictPartialOrder(nodes=[
    site_survey, permit_check, hive_setup, community_meet, hive_monitor, pest_control, honey_harvest, data_logging,
    workshop_plan, supply_order, volunteer_coord, regulation_review, pollination_map, apiary_audit, feedback_gather,
    waste_manage
])

# Define the dependencies
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(permit_check, hive_setup)
root.order.add_edge(hive_setup, community_meet)
root.order.add_edge(community_meet, hive_monitor)
root.order.add_edge(hive_monitor, pest_control)
root.order.add_edge(pest_control, honey_harvest)
root.order.add_edge(honey_harvest, data_logging)
root.order.add_edge(data_logging, workshop_plan)
root.order.add_edge(workshop_plan, supply_order)
root.order.add_edge(supply_order, volunteer_coord)
root.order.add_edge(volunteer_coord, regulation_review)
root.order.add_edge(regulation_review, pollination_map)
root.order.add_edge(pollination_map, apiary_audit)
root.order.add_edge(apiary_audit, feedback_gather)
root.order.add_edge(feedback_gather, waste_manage)

print(root)