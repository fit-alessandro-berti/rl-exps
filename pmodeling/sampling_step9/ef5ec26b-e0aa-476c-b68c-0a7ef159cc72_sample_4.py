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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
loop_soil_testing = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing])
loop_stakeholder_meet = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet])
loop_resource_plan = OperatorPOWL(operator=Operator.LOOP, children=[resource_plan])
loop_crop_selection = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection])
loop_volunteer_sign_up = OperatorPOWL(operator=Operator.LOOP, children=[volunteer_sign_up])
loop_tech_setup = OperatorPOWL(operator=Operator.LOOP, children=[tech_setup])
loop_irrigation_check = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_check])
loop_data_collection = OperatorPOWL(operator=Operator.LOOP, children=[data_collection])
loop_growth_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring])
loop_conflict_mediate = OperatorPOWL(operator=Operator.LOOP, children=[conflict_mediate])
loop_workshop_prep = OperatorPOWL(operator=Operator.LOOP, children=[workshop_prep])
loop_market_forecast = OperatorPOWL(operator=Operator.LOOP, children=[market_forecast])
loop_yield_analysis = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis])
loop_sustainability_audit = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit])
loop_community_feedback = OperatorPOWL(operator=Operator.LOOP, children=[community_feedback])
loop_equipment_maintain = OperatorPOWL(operator=Operator.LOOP, children=[equipment_maintain])
loop_waste_manage = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage])

# Define exclusive choices
xor_stakeholder_meet = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
xor_resource_plan = OperatorPOWL(operator=Operator.XOR, children=[resource_plan, skip])
xor_crop_selection = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, skip])
xor_volunteer_sign_up = OperatorPOWL(operator=Operator.XOR, children=[volunteer_sign_up, skip])
xor_tech_setup = OperatorPOWL(operator=Operator.XOR, children=[tech_setup, skip])
xor_irrigation_check = OperatorPOWL(operator=Operator.XOR, children=[irrigation_check, skip])
xor_data_collection = OperatorPOWL(operator=Operator.XOR, children=[data_collection, skip])
xor_growth_monitoring = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, skip])
xor_conflict_mediate = OperatorPOWL(operator=Operator.XOR, children=[conflict_mediate, skip])
xor_workshop_prep = OperatorPOWL(operator=Operator.XOR, children=[workshop_prep, skip])
xor_market_forecast = OperatorPOWL(operator=Operator.XOR, children=[market_forecast, skip])
xor_yield_analysis = OperatorPOWL(operator=Operator.XOR, children=[yield_analysis, skip])
xor_sustainability_audit = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, skip])
xor_community_feedback = OperatorPOWL(operator=Operator.XOR, children=[community_feedback, skip])
xor_equipment_maintain = OperatorPOWL(operator=Operator.XOR, children=[equipment_maintain, skip])
xor_waste_manage = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    loop_site_survey,
    loop_soil_testing,
    loop_stakeholder_meet,
    loop_resource_plan,
    loop_crop_selection,
    loop_volunteer_sign_up,
    loop_tech_setup,
    loop_irrigation_check,
    loop_data_collection,
    loop_growth_monitoring,
    loop_conflict_mediate,
    loop_workshop_prep,
    loop_market_forecast,
    loop_yield_analysis,
    loop_sustainability_audit,
    loop_community_feedback,
    loop_equipment_maintain,
    loop_waste_manage,
    xor_stakeholder_meet,
    xor_resource_plan,
    xor_crop_selection,
    xor_volunteer_sign_up,
    xor_tech_setup,
    xor_irrigation_check,
    xor_data_collection,
    xor_growth_monitoring,
    xor_conflict_mediate,
    xor_workshop_prep,
    xor_market_forecast,
    xor_yield_analysis,
    xor_sustainability_audit,
    xor_community_feedback,
    xor_equipment_maintain,
    xor_waste_manage
])

# Define the order of dependencies
root.order.add_edge(loop_site_survey, xor_stakeholder_meet)
root.order.add_edge(loop_soil_testing, xor_resource_plan)
root.order.add_edge(loop_stakeholder_meet, xor_crop_selection)
root.order.add_edge(loop_resource_plan, xor_volunteer_sign_up)
root.order.add_edge(loop_crop_selection, xor_tech_setup)
root.order.add_edge(loop_volunteer_sign_up, xor_irrigation_check)
root.order.add_edge(loop_tech_setup, xor_data_collection)
root.order.add_edge(loop_irrigation_check, xor_growth_monitoring)
root.order.add_edge(loop_data_collection, xor_conflict_mediate)
root.order.add_edge(loop_growth_monitoring, xor_workshop_prep)
root.order.add_edge(loop_conflict_mediate, xor_market_forecast)
root.order.add_edge(loop_workshop_prep, xor_yield_analysis)
root.order.add_edge(loop_market_forecast, xor_sustainability_audit)
root.order.add_edge(loop_yield_analysis, xor_community_feedback)
root.order.add_edge(loop_sustainability_audit, xor_equipment_maintain)
root.order.add_edge(loop_community_feedback, xor_waste_manage)