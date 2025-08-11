import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
site_survey = Transition(label='Site Survey')
load_testing = Transition(label='Load Testing')
crop_selection = Transition(label='Crop Selection')
soil_prep = Transition(label='Soil Prep')
irrigation_setup = Transition(label='Irrigation Setup')
permits_acquire = Transition(label='Permits Acquire')
supplier_outreach = Transition(label='Supplier Outreach')
planting_seedlings = Transition(label='Planting Seedlings')
pest_monitoring = Transition(label='Pest Monitoring')
nutrient_testing = Transition(label='Nutrient Testing')
waste_sorting = Transition(label='Waste Sorting')
staff_training = Transition(label='Staff Training')
community_meet = Transition(label='Community Meet')
harvest_planning = Transition(label='Harvest Planning')
market_launch = Transition(label='Market Launch')
yield_tracking = Transition(label='Yield Tracking')

# Define the silent transitions
skip = SilentTransition()

# Define the loops
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_testing])
loop_culture_management = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, nutrient_testing])
loop_community_engagement = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, staff_training])

# Define the exclusive choices
xor_risk_assessment = OperatorPOWL(operator=Operator.XOR, children=[permits_acquire, skip])
xor_market_strategies = OperatorPOWL(operator=Operator.XOR, children=[market_launch, skip])

# Define the root
root = StrictPartialOrder(nodes=[loop_site_survey, loop_culture_management, loop_community_engagement, xor_risk_assessment, xor_market_strategies])
root.order.add_edge(loop_site_survey, loop_culture_management)
root.order.add_edge(loop_culture_management, loop_community_engagement)
root.order.add_edge(loop_community_engagement, xor_risk_assessment)
root.order.add_edge(xor_risk_assessment, xor_market_strategies)

print(root)