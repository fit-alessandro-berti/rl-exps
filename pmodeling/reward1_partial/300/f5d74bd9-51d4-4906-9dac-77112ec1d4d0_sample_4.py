import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_review = Transition(label='Site Review')
impact_study = Transition(label='Impact Study')
design_plan = Transition(label='Design Plan')
structure_mod = Transition(label='Structure Mod')
hydroponics_setup = Transition(label='Hydroponics Setup')
crop_select = Transition(label='Crop Select')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
sensor_install = Transition(label='Sensor Install')
staff_train = Transition(label='Staff Train')
compliance_audit = Transition(label='Compliance Audit')
packaging_dev = Transition(label='Packaging Dev')
logistics_plan = Transition(label='Logistics Plan')
community_engage = Transition(label='Community Engage')
sustainability_check = Transition(label='Sustainability Check')

# Define partial order nodes
loop_structure_mod = OperatorPOWL(operator=Operator.LOOP, children=[structure_mod, impact_study])
loop_hydroponics_setup = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_setup, sensor_install])
loop_crop_select = OperatorPOWL(operator=Operator.LOOP, children=[crop_select, nutrient_mix, pest_control])
xor_logistics_plan = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, community_engage])

# Define the root partial order
root = StrictPartialOrder(nodes=[loop_structure_mod, loop_hydroponics_setup, loop_crop_select, xor_logistics_plan])
root.order.add_edge(loop_structure_mod, loop_hydroponics_setup)
root.order.add_edge(loop_hydroponics_setup, loop_crop_select)
root.order.add_edge(loop_crop_select, xor_logistics_plan)

# Print the root partial order
print(root)