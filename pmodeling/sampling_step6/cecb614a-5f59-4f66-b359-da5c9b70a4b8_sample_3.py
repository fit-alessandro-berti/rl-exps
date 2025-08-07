import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_testing, crop_selection, soil_prep, irrigation_setup,
    permits_acquire, supplier_outreach, planting_seedlings, pest_monitoring,
    nutrient_testing, waste_sorting, staff_training, community_meet,
    harvest_planning, market_launch, yield_tracking
])

# Define the dependencies (partial order relationships)
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(site_survey, crop_selection)
root.order.add_edge(site_survey, soil_prep)
root.order.add_edge(site_survey, irrigation_setup)
root.order.add_edge(site_survey, permits_acquire)
root.order.add_edge(site_survey, supplier_outreach)
root.order.add_edge(site_survey, planting_seedlings)
root.order.add_edge(site_survey, pest_monitoring)
root.order.add_edge(site_survey, nutrient_testing)
root.order.add_edge(site_survey, waste_sorting)
root.order.add_edge(site_survey, staff_training)
root.order.add_edge(site_survey, community_meet)
root.order.add_edge(site_survey, harvest_planning)
root.order.add_edge(site_survey, market_launch)
root.order.add_edge(site_survey, yield_tracking)

# Now 'root' contains the POWL model for the urban rooftop farm process