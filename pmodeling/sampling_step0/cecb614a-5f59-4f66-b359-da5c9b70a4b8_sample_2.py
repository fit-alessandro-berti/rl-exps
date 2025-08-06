from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice (XOR) for resource logistics and community engagement
xor_resource = OperatorPOWL(operator=Operator.XOR, children=[supplier_outreach, community_meet])
xor_community = OperatorPOWL(operator=Operator.XOR, children=[community_meet, market_launch])

# Define loop for pest monitoring and nutrient testing
loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, nutrient_testing])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, load_testing, crop_selection, soil_prep, irrigation_setup, permits_acquire, xor_resource, xor_community, loop_monitoring, staff_training, waste_sorting, harvest_planning, yield_tracking])
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(load_testing, crop_selection)
root.order.add_edge(crop_selection, soil_prep)
root.order.add_edge(soil_prep, irrigation_setup)
root.order.add_edge(irrigation_setup, permits_acquire)
root.order.add_edge(permits_acquire, xor_resource)
root.order.add_edge(xor_resource, xor_community)
root.order.add_edge(xor_community, loop_monitoring)
root.order.add_edge(loop_monitoring, staff_training)
root.order.add_edge(staff_training, waste_sorting)
root.order.add_edge(waste_sorting, harvest_planning)
root.order.add_edge(harvest_planning, market_launch)
root.order.add_edge(market_launch, yield_tracking)

print(root)