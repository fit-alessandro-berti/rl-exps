import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the loop node (PO=(nodes={...}, order={...}))
loop = OperatorPOWL(operator=Operator.LOOP, children=[site_review, impact_study, design_plan, structure_mod, hydroponics_setup, crop_select, nutrient_mix, pest_control, sensor_install, staff_train, compliance_audit, packaging_dev, logistics_plan, community_engage, sustainability_check])

# Define the exclusive choice node (X(A, B))
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)