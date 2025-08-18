from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loop nodes
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_check, hive_setup, community_meet])
hive_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[hive_monitor, pest_control, honey_harvest, data_logging])
workshop_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[workshop_plan, supply_order, volunteer_coord])
regulation_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_review, pollination_map, apiary_audit, feedback_gather, waste_manage])

# Define exclusive choice nodes
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey_loop, regulation_review_loop])
hive_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[hive_monitor_loop, workshop_plan_loop])
site_survey_xor2 = OperatorPOWL(operator=Operator.XOR, children=[site_survey_xor, hive_monitor_xor])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_survey_xor2])
root.order.add_edge(site_survey_xor, hive_monitor_xor)
root.order.add_edge(regulation_review_loop, workshop_plan_loop)

root