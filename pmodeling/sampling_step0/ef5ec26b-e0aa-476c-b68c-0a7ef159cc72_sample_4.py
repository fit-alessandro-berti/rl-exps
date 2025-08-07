import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop and choice operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, growth_monitoring])
xor = OperatorPOWL(operator=Operator.XOR, children=[conflict_mediate, workshop_prep])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, yield_analysis])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, community_feedback])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[equipment_maintain, waste_manage])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, soil_testing, stakeholder_meet, resource_plan, crop_selection, volunteer_sign_up, tech_setup, irrigation_check, loop, xor, xor2, xor3, xor4])
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(soil_testing, stakeholder_meet)
root.order.add_edge(stakeholder_meet, resource_plan)
root.order.add_edge(resource_plan, crop_selection)
root.order.add_edge(crop_selection, volunteer_sign_up)
root.order.add_edge(volunteer_sign_up, tech_setup)
root.order.add_edge(tech_setup, irrigation_check)
root.order.add_edge(irrigation_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)

print(root)