import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
soil_testing = Transition(label='Soil Testing')
stakeholder_meet = Transition(label='Stakeholder Meet')
resource_plan = Transition(label='Resource Plan')
crop_selection = Transition(label='Crop Selection')
volunteer_sign_up = Transition(label='Volunteer Sign-up')
tech_setup = Transition(label='Tech Setup')
irrigation_check = Transition(label='Irrigation Check')
data_collection = Transition(label='Data Collection')
growth_monitoring = Transition(label='Growth Monitoring')
conflict_mediate = Transition(label='Conflict Mediate')
workshop_prep = Transition(label='Workshop Prep')
market_forecast = Transition(label='Market Forecast')
yield_analysis = Transition(label='Yield Analysis')
sustainability_audit = Transition(label='Sustainability Audit')
community_feedback = Transition(label='Community Feedback')
equipment_maintain = Transition(label='Equipment Maintain')
waste_manage = Transition(label='Waste Manage')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, soil_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet, resource_plan])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, volunteer_sign_up])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[tech_setup, irrigation_check])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, growth_monitoring])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[conflict_mediate, workshop_prep])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[market_forecast, yield_analysis])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit, community_feedback])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[equipment_maintain, waste_manage])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop8, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[loop9, skip])

# Define root
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)

# Print the root
print(root)