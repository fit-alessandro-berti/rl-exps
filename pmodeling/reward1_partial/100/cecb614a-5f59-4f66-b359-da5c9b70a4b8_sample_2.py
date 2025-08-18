from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define activities
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

# Create operators
xor = OperatorPOWL(operator=Operator.XOR, children=[soil_prep, irrigation_setup])
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, nutrient_testing, waste_sorting, staff_training])
community = OperatorPOWL(operator=Operator.XOR, children=[community_meet, market_launch])
yield_tracking_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_tracking])

# Define the root Partial Order
root = StrictPartialOrder(nodes=[site_survey, load_testing, crop_selection, xor, loop, community, yield_tracking_loop])
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(site_survey, crop_selection)
root.order.add_edge(load_testing, xor)
root.order.add_edge(crop_selection, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, community)
root.order.add_edge(community, yield_tracking_loop)
root.order.add_edge(yield_tracking_loop, yield_tracking)

# Print the root for verification
print(root)