import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, supplier_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[culture_prep, milk_testing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[fermentation_start, pH_monitoring])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, mold_inoculation])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, humidity_control])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[texture_check, flavor_profiling])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[batch_labeling, packaging])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[distribution, feedback_review])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, feedback_review])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor8)