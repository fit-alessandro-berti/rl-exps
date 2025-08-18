import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define loops
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[pH_monitoring, curd_cutting, mold_inoculation])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control])

# Define exclusive choices
quality_checkpoints = OperatorPOWL(operator=Operator.XOR, children=[texture_check, flavor_profiling])
consumer_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, sustainability_audit])

# Define partial order
root = StrictPartialOrder(nodes=[milk_sourcing, supplier_audit, culture_prep, milk_testing, fermentation_start, fermentation_loop, aging_setup, aging_loop, batch_labeling, packaging, distribution, quality_checkpoints, consumer_feedback])
root.order.add_edge(milk_sourcing, supplier_audit)
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(milk_sourcing, milk_testing)
root.order.add_edge(culture_prep, fermentation_start)
root.order.add_edge(fermentation_start, pH_monitoring)
root.order.add_edge(pH_monitoring, curd_cutting)
root.order.add_edge(curd_cutting, mold_inoculation)
root.order.add_edge(mold_inoculation, aging_setup)
root.order.add_edge(aging_setup, humidity_control)
root.order.add_edge(humidity_control, batch_labeling)
root.order.add_edge(batch_labeling, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(fermentation_loop, aging_loop)
root.order.add_edge(aging_loop, quality_checkpoints)
root.order.add_edge(quality_checkpoints, consumer_feedback)

print(root)