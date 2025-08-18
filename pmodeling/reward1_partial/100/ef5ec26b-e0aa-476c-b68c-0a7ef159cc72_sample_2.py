import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define XOR for resource allocation and crop planning
xor_resource_crop = OperatorPOWL(operator=Operator.XOR, children=[resource_plan, crop_selection])

# Define loop for tech setup and irrigation check
loop_tech_irrigation = OperatorPOWL(operator=Operator.LOOP, children=[tech_setup, irrigation_check])

# Define XOR for data collection and growth monitoring
xor_data_growth = OperatorPOWL(operator=Operator.XOR, children=[data_collection, growth_monitoring])

# Define XOR for conflict mediation and workshop preparation
xor_conflict_workshop = OperatorPOWL(operator=Operator.XOR, children=[conflict_mediate, workshop_prep])

# Define XOR for market forecasting and yield analysis
xor_market_yield = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, yield_analysis])

# Define XOR for sustainability audit and community feedback
xor_sustainability_feedback = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, community_feedback])

# Define XOR for equipment maintenance and waste management
xor_maintain_waste = OperatorPOWL(operator=Operator.XOR, children=[equipment_maintain, waste_manage])

# Define strict partial order with all activities and dependencies
root = StrictPartialOrder(nodes=[
    site_survey, 
    soil_testing, 
    stakeholder_meet, 
    xor_resource_crop, 
    xor_tech_irrigation, 
    xor_data_growth, 
    xor_conflict_workshop, 
    xor_market_yield, 
    xor_sustainability_feedback, 
    xor_maintain_waste
])

# Add dependencies between activities
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(soil_testing, xor_resource_crop)
root.order.add_edge(stakeholder_meet, xor_resource_crop)
root.order.add_edge(xor_resource_crop, xor_tech_irrigation)
root.order.add_edge(xor_resource_crop, xor_data_growth)
root.order.add_edge(xor_resource_crop, xor_conflict_workshop)
root.order.add_edge(xor_resource_crop, xor_market_yield)
root.order.add_edge(xor_resource_crop, xor_sustainability_feedback)
root.order.add_edge(xor_resource_crop, xor_maintain_waste)
root.order.add_edge(xor_tech_irrigation, xor_data_growth)
root.order.add_edge(xor_tech_irrigation, xor_conflict_workshop)
root.order.add_edge(xor_tech_irrigation, xor_market_yield)
root.order.add_edge(xor_tech_irrigation, xor_sustainability_feedback)
root.order.add_edge(xor_tech_irrigation, xor_maintain_waste)
root.order.add_edge(xor_data_growth, xor_conflict_workshop)
root.order.add_edge(xor_data_growth, xor_market_yield)
root.order.add_edge(xor_data_growth, xor_sustainability_feedback)
root.order.add_edge(xor_data_growth, xor_maintain_waste)
root.order.add_edge(xor_conflict_workshop, xor_market_yield)
root.order.add_edge(xor_conflict_workshop, xor_sustainability_feedback)
root.order.add_edge(xor_conflict_workshop, xor_maintain_waste)
root.order.add_edge(xor_market_yield, xor_sustainability_feedback)
root.order.add_edge(xor_market_yield, xor_maintain_waste)
root.order.add_edge(xor_sustainability_feedback, xor_maintain_waste)