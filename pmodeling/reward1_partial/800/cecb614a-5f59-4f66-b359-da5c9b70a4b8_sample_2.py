import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_testing])
crop_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection, soil_prep, irrigation_setup])
permits_acquire_loop = OperatorPOWL(operator=Operator.LOOP, children=[permits_acquire, supplier_outreach])
pest_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, nutrient_testing])
waste_sorting_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_sorting, staff_training])
community_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, harvest_planning])
market_launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_launch, yield_tracking])

root = StrictPartialOrder(nodes=[site_survey_loop, crop_selection_loop, permits_acquire_loop, pest_monitoring_loop, waste_sorting_loop, community_meet_loop, market_launch_loop])
root.order.add_edge(site_survey_loop, crop_selection_loop)
root.order.add_edge(crop_selection_loop, permits_acquire_loop)
root.order.add_edge(permits_acquire_loop, pest_monitoring_loop)
root.order.add_edge(pest_monitoring_loop, waste_sorting_loop)
root.order.add_edge(waste_sorting_loop, community_meet_loop)
root.order.add_edge(community_meet_loop, market_launch_loop)