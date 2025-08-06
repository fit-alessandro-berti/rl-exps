import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition
skip = SilentTransition()

# Define the loops and XOR nodes
loop_structure_mod = OperatorPOWL(operator=Operator.LOOP, children=[impact_study, design_plan])
xor_hydroponics_setup = OperatorPOWL(operator=Operator.XOR, children=[structure_mod, skip])
xor_crop_select = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_setup, skip])
xor_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[crop_select, skip])
xor_pest_control = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
xor_staff_train = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, skip])
xor_logistics_plan = OperatorPOWL(operator=Operator.XOR, children=[packaging_dev, skip])
xor_community_engage = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, skip])
xor_sustainability_check = OperatorPOWL(operator=Operator.XOR, children=[community_engage, skip])

# Define the root model
root = StrictPartialOrder(nodes=[
    loop_structure_mod,
    xor_hydroponics_setup,
    xor_crop_select,
    xor_nutrient_mix,
    xor_pest_control,
    xor_staff_train,
    xor_logistics_plan,
    xor_community_engage,
    xor_sustainability_check
])

# Define the order dependencies
root.order.add_edge(loop_structure_mod, xor_hydroponics_setup)
root.order.add_edge(xor_hydroponics_setup, xor_crop_select)
root.order.add_edge(xor_crop_select, xor_nutrient_mix)
root.order.add_edge(xor_nutrient_mix, xor_pest_control)
root.order.add_edge(xor_pest_control, xor_staff_train)
root.order.add_edge(xor_staff_train, xor_logistics_plan)
root.order.add_edge(xor_logistics_plan, xor_community_engage)
root.order.add_edge(xor_community_engage, xor_sustainability_check)

# Return the root model
return root