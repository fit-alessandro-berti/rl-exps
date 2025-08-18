import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (tau)
skip = SilentTransition()

# Define partial orders for different parts of the process
# 1. Initial Setup
initial_setup = StrictPartialOrder(nodes=[site_survey, load_testing, crop_selection, soil_prep, irrigation_setup, permits_acquire, supplier_outreach])
initial_setup.order.add_edge(site_survey, load_testing)
initial_setup.order.add_edge(load_testing, crop_selection)
initial_setup.order.add_edge(crop_selection, soil_prep)
initial_setup.order.add_edge(soil_prep, irrigation_setup)
initial_setup.order.add_edge(irrigation_setup, permits_acquire)
initial_setup.order.add_edge(permits_acquire, supplier_outreach)

# 2. Planting and Monitoring
planting_monitoring = StrictPartialOrder(nodes=[planting_seedlings, pest_monitoring, nutrient_testing])
planting_monitoring.order.add_edge(planting_seedlings, pest_monitoring)
planting_monitoring.order.add_edge(pest_monitoring, nutrient_testing)

# 3. Community Engagement
community_engagement = StrictPartialOrder(nodes=[community_meet, staff_training])
community_engagement.order.add_edge(community_meet, staff_training)

# 4. Waste Sorting and Market Launch
waste_market = StrictPartialOrder(nodes=[waste_sorting, market_launch])
waste_market.order.add_edge(waste_sorting, market_launch)

# 5. Harvest Planning and Yield Tracking
harvest_yield = StrictPartialOrder(nodes=[harvest_planning, yield_tracking])
harvest_yield.order.add_edge(harvest_planning, yield_tracking)

# Define exclusive choice for different steps
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[planting_monitoring, community_engagement, waste_market, harvest_yield])

# Define the final root node with concurrent execution of the exclusive choice and initial setup
root = StrictPartialOrder(nodes=[initial_setup, exclusive_choice])
root.order.add_edge(initial_setup, exclusive_choice)

print(root)