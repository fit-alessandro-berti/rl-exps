import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
soil_prep = Transition(label='Soil Prep')
hydroponic_setup = Transition(label='Hydroponic Setup')
community_meet = Transition(label='Community Meet')
crop_select = Transition(label='Crop Select')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
market_launch = Transition(label='Market Launch')
feedback_collect = Transition(label='Feedback Collect')

# Define loops and choices
site_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_test, permit_review])
soil_hydroponic_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_prep, hydroponic_setup])
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install])
water_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
growth_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor])
harvest_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan])
market_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_launch])
feedback_collect_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect])

# Define the root node
root = StrictPartialOrder(nodes=[site_loop, soil_hydroponic_loop, community_loop, sensor_loop, water_testing_loop, pest_control_loop, growth_monitor_loop, harvest_plan_loop, market_loop, feedback_collect_loop])
root.order.add_edge(site_loop, soil_hydroponic_loop)
root.order.add_edge(soil_hydroponic_loop, community_loop)
root.order.add_edge(community_loop, sensor_loop)
root.order.add_edge(sensor_loop, water_testing_loop)
root.order.add_edge(water_testing_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, growth_monitor_loop)
root.order.add_edge(growth_monitor_loop, harvest_plan_loop)
root.order.add_edge(harvest_plan_loop, market_loop)
root.order.add_edge(market_loop, feedback_collect_loop)