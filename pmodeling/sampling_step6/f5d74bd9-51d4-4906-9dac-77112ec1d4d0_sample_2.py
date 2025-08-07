from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names as given
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

# Define the root partial order with all the activities
root = StrictPartialOrder(nodes=[site_review, impact_study, design_plan, structure_mod, hydroponics_setup, crop_select, nutrient_mix, pest_control, sensor_install, staff_train, compliance_audit, packaging_dev, logistics_plan, community_engage, sustainability_check])

# Optionally, you can define dependencies between activities if needed.
# For example, if the hydroponics setup depends on the design plan:
# root.order.add_edge(design_plan, hydroponics_setup)

# Now, 'root' contains the complete POWL model for the process.