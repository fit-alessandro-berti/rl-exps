import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
supplier_audit = Transition(label='Supplier Audit')
culture_prep = Transition(label='Culture Prep')
milk_testing = Transition(label='Milk Testing')
fermentation_start = Transition(label='Fermentation Start')
pH_monitoring = Transition(label='pH Monitoring')
curd_cutting = Transition(label='Curd Cutting')
mold_inoculation = Transition(label='Mold Inoculation')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
texture_check = Transition(label='Texture Check')
flavor_profiling = Transition(label='Flavor Profiling')
batch_labeling = Transition(label='Batch Labeling')
packaging = Transition(label='Packaging')
distribution = Transition(label='Distribution')
feedback_review = Transition(label='Feedback Review')
sustainability_audit = Transition(label='Sustainability Audit')

# Define silent activities
skip = SilentTransition()

# Define loops
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, supplier_audit, culture_prep, milk_testing, fermentation_start, pH_monitoring, curd_cutting, mold_inoculation, aging_setup, humidity_control, texture_check, flavor_profiling, batch_labeling, packaging, distribution, feedback_review, sustainability_audit])

# Define XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, skip])

# Define root
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, aging_loop)

print(root)