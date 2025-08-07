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
conflict_meditate = Transition(label='Conflict Mediate')
workshop_prep = Transition(label='Workshop Prep')
market_forecast = Transition(label='Market Forecast')
yield_analysis = Transition(label='Yield Analysis')
sustainability_audit = Transition(label='Sustainability Audit')
community_feedback = Transition(label='Community Feedback')
equipment_maintain = Transition(label='Equipment Maintain')
waste_manage = Transition(label='Waste Manage')

# Define the root Partial Order
root = StrictPartialOrder(nodes=[
    site_survey,
    soil_testing,
    stakeholder_meet,
    resource_plan,
    crop_selection,
    volunteer_sign_up,
    tech_setup,
    irrigation_check,
    data_collection,
    growth_monitoring,
    conflict_meditate,
    workshop_prep,
    market_forecast,
    yield_analysis,
    sustainability_audit,
    community_feedback,
    equipment_maintain,
    waste_manage
])

# Define the dependencies (if any)
# In this example, there are no explicit dependencies defined in the problem statement,
# so we don't need to add any edges to the 'root' object.

# The 'root' variable now contains the POWL model for the process
print(root)