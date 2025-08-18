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

# Define loop for pest monitoring and nutrient testing
pest_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, nutrient_testing])

# Define XOR for supplier outreach and waste sorting
xor = OperatorPOWL(operator=Operator.XOR, children=[supplier_outreach, waste_sorting])

# Define XOR for community meet and market launch
market_launch_xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet, market_launch])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, load_testing, crop_selection, soil_prep, irrigation_setup, permits_acquire, pest_monitoring_loop, xor, staff_training, harvest_planning, market_launch_xor, yield_tracking])
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(load_testing, crop_selection)
root.order.add_edge(crop_selection, soil_prep)
root.order.add_edge(soil_prep, irrigation_setup)
root.order.add_edge(irrigation_setup, permits_acquire)
root.order.add_edge(permits_acquire, pest_monitoring_loop)
root.order.add_edge(pest_monitoring_loop, xor)
root.order.add_edge(xor, staff_training)
root.order.add_edge(staff_training, harvest_planning)
root.order.add_edge(harvest_planning, market_launch_xor)
root.order.add_edge(market_launch_xor, yield_tracking)