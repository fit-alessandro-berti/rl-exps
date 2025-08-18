import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Site Review and Impact Study
site_review_impact = OperatorPOWL(operator=Operator.XOR, children=[site_review, impact_study])

# Design Plan and Structure Mod
design_plan_structure_mod = OperatorPOWL(operator=Operator.XOR, children=[design_plan, structure_mod])

# Hydroponics Setup and Crop Select
hydroponics_setup_crop_select = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_setup, crop_select])

# Nutrient Mix and Pest Control
nutrient_mix_pest_control = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, pest_control])

# Sensor Install and Staff Train
sensor_install_staff_train = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, staff_train])

# Compliance Audit and Packaging Dev
compliance_audit_packaging_dev = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, packaging_dev])

# Logistics Plan and Community Engage
logistics_plan_community_engage = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, community_engage])

# Sustainability Check
sustainability_check = Transition(label='Sustainability Check')

# Loop: Sustainability Check
sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_check])

# Root node: Site Review, Impact Study, Design Plan, Structure Mod, Hydroponics Setup, Crop Select, Nutrient Mix, Pest Control, Sensor Install, Staff Train, Compliance Audit, Packaging Dev, Logistics Plan, Community Engage, Sustainability Check
root = StrictPartialOrder(nodes=[site_review_impact, design_plan_structure_mod, hydroponics_setup_crop_select, nutrient_mix_pest_control, sensor_install_staff_train, compliance_audit_packaging_dev, logistics_plan_community_engage, sustainability_loop])

# Add edges
root.order.add_edge(site_review_impact, design_plan_structure_mod)
root.order.add_edge(design_plan_structure_mod, hydroponics_setup_crop_select)
root.order.add_edge(hydroponics_setup_crop_select, nutrient_mix_pest_control)
root.order.add_edge(nutrient_mix_pest_control, sensor_install_staff_train)
root.order.add_edge(sensor_install_staff_train, compliance_audit_packaging_dev)
root.order.add_edge(compliance_audit_packaging_dev, logistics_plan_community_engage)
root.order.add_edge(logistics_plan_community_engage, sustainability_loop)

print(root)