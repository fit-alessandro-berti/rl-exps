import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_assess = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
permit_obtain = Transition(label='Permit Obtain')
material_source = Transition(label='Material Source')
soil_prepare = Transition(label='Soil Prepare')
waterproof_roof = Transition(label='Waterproof Roof')
irrigation_setup = Transition(label='Irrigation Setup')
bed_assemble = Transition(label='Bed Assemble')
crop_plan = Transition(label='Crop Plan')
pest_monitor = Transition(label='Pest Monitor')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
harvest_schedule = Transition(label='Harvest Schedule')
community_train = Transition(label='Community Train')
yield_record = Transition(label='Yield Record')
impact_review = Transition(label='Impact Review')

# Define the loop and choice nodes
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[soil_prepare, waterproof_roof, irrigation_setup, bed_assemble, crop_plan, nutrient_calibrate])
xor_node = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, community_train, yield_record, impact_review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_node, xor_node])
root.order.add_edge(loop_node, xor_node)

# Return the root
return root