from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Create the root node as a strict partial order
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

# Add dependencies if any are needed
# For example, if site_review must be completed before impact_study:
root.order.add_edge(site_review, impact_study)

# Continue adding dependencies as needed

# The final POWL model is defined by 'root'