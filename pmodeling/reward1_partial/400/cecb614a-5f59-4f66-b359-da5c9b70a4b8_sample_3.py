import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[permits_acquire, supplier_outreach])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_monitoring, nutrient_testing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, staff_training])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[community_meet, market_launch])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[harvest_planning, yield_tracking])
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_testing, crop_selection, soil_prep, irrigation_setup])

# Define the root node
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)