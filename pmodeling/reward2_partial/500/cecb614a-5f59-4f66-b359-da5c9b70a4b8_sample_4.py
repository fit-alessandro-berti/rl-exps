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

# Define partial order structure
root = StrictPartialOrder(nodes=[
    site_survey, load_testing, crop_selection, soil_prep, irrigation_setup, permits_acquire, supplier_outreach,
    planting_seedlings, pest_monitoring, nutrient_testing, waste_sorting, staff_training, community_meet,
    harvest_planning, market_launch, yield_tracking
])

# Define dependencies between activities
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(load_testing, crop_selection)
root.order.add_edge(crop_selection, soil_prep)
root.order.add_edge(soil_prep, irrigation_setup)
root.order.add_edge(irrigation_setup, permits_acquire)
root.order.add_edge(permits_acquire, supplier_outreach)
root.order.add_edge(supplier_outreach, planting_seedlings)
root.order.add_edge(planting_seedlings, pest_monitoring)
root.order.add_edge(pest_monitoring, nutrient_testing)
root.order.add_edge(nutrient_testing, waste_sorting)
root.order.add_edge(waste_sorting, staff_training)
root.order.add_edge(staff_training, community_meet)
root.order.add_edge(community_meet, harvest_planning)
root.order.add_edge(harvest_planning, market_launch)
root.order.add_edge(market_launch, yield_tracking)

# Print the final root model
print(root)