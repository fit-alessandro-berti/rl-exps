from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define silent transitions
skip = SilentTransition()

# Define loop for environmental assessments
environmental_assessments = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_testing])

# Define XOR for resource logistics and community engagement
resource_logistics = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, soil_prep, irrigation_setup, permits_acquire, supplier_outreach, planting_seedlings, pest_monitoring, nutrient_testing, waste_sorting, staff_training, community_meet, harvest_planning, market_launch, yield_tracking])

# Define root POWL model
root = StrictPartialOrder(nodes=[environmental_assessments, resource_logistics])
root.order.add_edge(environmental_assessments, resource_logistics)