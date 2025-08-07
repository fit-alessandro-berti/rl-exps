import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_survey, permit_check, hive_setup, community_meet, hive_monitor, pest_control, honey_harvest, data_logging, workshop_plan, supply_order, volunteer_coord, regulation_review, pollination_map, apiary_audit, feedback_gather, waste_manage])

# Optionally, you can add dependencies between nodes if needed
# For example, if site survey must be done before hive setup:
# root.order.add_edge(site_survey, hive_setup)

# If you want to save the result in a variable, you can assign it to 'root'
print("POWL model for urban beekeeping process defined and saved in 'root'.")