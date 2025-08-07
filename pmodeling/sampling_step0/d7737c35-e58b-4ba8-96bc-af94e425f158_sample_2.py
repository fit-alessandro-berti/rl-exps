import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions (if any)
skip = SilentTransition()

# Define the loops
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_start, pH_monitoring, curd_cutting, mold_inoculation])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control, texture_check, flavor_profiling])

# Define the exclusive choice (xor) for the feedback and sustainability audits
feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, sustainability_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[
    fermentation_loop, aging_loop, feedback_xor, milk_sourcing, supplier_audit, culture_prep, milk_testing, batch_labeling, packaging, distribution
])

# Define the partial order edges
root.order.add_edge(fermentation_loop, aging_loop)
root.order.add_edge(fermentation_loop, feedback_xor)
root.order.add_edge(aging_loop, feedback_xor)
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_testing)
root.order.add_edge(milk_testing, batch_labeling)
root.order.add_edge(batch_labeling, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(aging_loop, feedback_xor)

print(root)