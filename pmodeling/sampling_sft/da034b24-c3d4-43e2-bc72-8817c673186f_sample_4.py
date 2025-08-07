import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
permit_check     = Transition(label='Permit Check')
hive_setup       = Transition(label='Hive Setup')
community_meet   = Transition(label='Community Meet')
volunteer_coord  = Transition(label='Volunteer Coord')
hive_monitor     = Transition(label='Hive Monitor')
pest_control     = Transition(label='Pest Control')
honey_harvest    = Transition(label='Honey Harvest')
data_logging     = Transition(label='Data Logging')
regulation_review= Transition(label='Regulation Review')
workshop_plan    = Transition(label='Workshop Plan')
supply_order     = Transition(label='Supply Order')
feedback_gather  = Transition(label='Feedback Gather')
pollination_map  = Transition(label='Pollination Map')
apiary_audit     = Transition(label='Apiary Audit')
waste_manage     = Transition(label='Waste Manage')

# Define the monitoring loop: Hive Monitor, then optionally Pest Control and Honey Harvest
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[hive_monitor,
              X(pest_control, honey_harvest)
              ]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_check, hive_setup, community_meet, volunteer_coord,
    monitor_loop,
    regulation_review, data_logging,
    supply_order, workshop_plan, feedback_gather,
    pollination_map, apiary_audit, waste_manage
])

# Define the order dependencies
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(permit_check, hive_setup)
root.order.add_edge(hive_setup, community_meet)
root.order.add_edge(community_meet, volunteer_coord)
root.order.add_edge(volunteer_coord, monitor_loop)

# Monitoring loop can happen concurrently with other activities
root.order.add_edge(monitor_loop, regulation_review)
root.order.add_edge(monitor_loop, data_logging)

# After monitoring, supply and workshop planning can proceed
root.order.add_edge(monitor_loop, supply_order)
root.order.add_edge(monitor_loop, workshop_plan)

# After supply and workshop, gather feedback and map pollination
root.order.add_edge(supply_order, feedback_gather)
root.order.add_edge(workshop_plan, feedback_gather)
root.order.add_edge(feedback_gather, pollination_map)

# After mapping pollination, do the audit and waste management
root.order.add_edge(pollination_map, apiary_audit)
root.order.add_edge(pollination_map, waste_manage)