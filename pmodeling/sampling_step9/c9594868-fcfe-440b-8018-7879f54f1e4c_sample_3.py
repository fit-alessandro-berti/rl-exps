import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent activities
skip = SilentTransition()

# Define the loop nodes
soil_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_prep, skip])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, skip])
water_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing, skip])

# Define the exclusive choice nodes
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, load_test])
permit_review_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_review, soil_prep_loop])
material_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, sensor_install])
crop_select_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_select, water_testing_loop])
pest_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control_loop, feedback_collect])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey_xor, permit_review_xor, material_sourcing_xor, crop_select_xor, pest_control_xor, growth_monitor, harvest_plan, market_launch])
root.order.add_edge(site_survey_xor, permit_review_xor)
root.order.add_edge(permit_review_xor, material_sourcing_xor)
root.order.add_edge(material_sourcing_xor, crop_select_xor)
root.order.add_edge(crop_select_xor, pest_control_xor)
root.order.add_edge(pest_control_xor, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, market_launch)