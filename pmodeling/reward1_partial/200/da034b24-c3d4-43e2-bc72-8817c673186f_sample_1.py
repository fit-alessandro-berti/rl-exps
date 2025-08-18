from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
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

# Define the operators (control-flow operators) for the POWL model
# Create a loop for hive monitoring and pest control
loop = OperatorPOWL(operator=Operator.LOOP, children=[hive_monitor, pest_control])

# Create an exclusive choice for data logging and supply order
xor = OperatorPOWL(operator=Operator.XOR, children=[data_logging, supply_order])

# Create a loop for regulation review and volunteer coordination
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[regulation_review, volunteer_coord])

# Create a loop for apiary audit and feedback gather
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[apiary_audit, feedback_gather])

# Create a loop for waste management
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage])

# Create the root node with all the defined transitions and operators
root = StrictPartialOrder(nodes=[site_survey, permit_check, hive_setup, community_meet, loop, xor, loop2, loop3, loop4])

# Add the dependencies between the nodes
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(permit_check, hive_setup)
root.order.add_edge(hive_setup, community_meet)
root.order.add_edge(community_meet, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, site_survey)

print(root)