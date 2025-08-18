import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_review,
    impact_study,
    design_plan,
    structure_mod,
    hydroponics_setup,
    crop_select,
    nutrient_mix,
    pest_control,
    sensor_install,
    staff_train,
    compliance_audit,
    packaging_dev,
    logistics_plan,
    community_engage,
    sustainability_check
])

# Define the dependencies
root.order.add_edge(site_review, impact_study)
root.order.add_edge(impact_study, design_plan)
root.order.add_edge(design_plan, structure_mod)
root.order.add_edge(structure_mod, hydroponics_setup)
root.order.add_edge(hydroponics_setup, crop_select)
root.order.add_edge(crop_select, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_control)
root.order.add_edge(pest_control, sensor_install)
root.order.add_edge(sensor_install, staff_train)
root.order.add_edge(staff_train, compliance_audit)
root.order.add_edge(compliance_audit, packaging_dev)
root.order.add_edge(packaging_dev, logistics_plan)
root.order.add_edge(logistics_plan, community_engage)
root.order.add_edge(community_engage, sustainability_check)

# Print the root
print(root)