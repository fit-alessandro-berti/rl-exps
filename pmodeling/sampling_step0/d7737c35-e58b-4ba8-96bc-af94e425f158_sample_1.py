import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[pH_monitoring, curd_cutting, mold_inoculation, texture_check, flavor_profiling])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control, texture_check, flavor_profiling])
supplier_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, supplier_audit])
culture_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[culture_prep, skip])
milk_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip])
fermentation_choice = OperatorPOWL(operator=Operator.XOR, children=[fermentation_start, skip])
aging_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, skip])
packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging, skip])
distribution_choice = OperatorPOWL(operator=Operator.XOR, children=[distribution, skip])
feedback_review_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])
sustainability_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[supplier_audit_choice, culture_prep_choice, milk_testing_choice, fermentation_choice, aging_choice, packaging_choice, distribution_choice, feedback_review_choice, sustainability_audit_choice])

# Define dependencies
root.order.add_edge(supplier_audit_choice, culture_prep_choice)
root.order.add_edge(culture_prep_choice, milk_testing_choice)
root.order.add_edge(milk_testing_choice, fermentation_choice)
root.order.add_edge(fermentation_choice, fermentation_loop)
root.order.add_edge(fermentation_loop, aging_choice)
root.order.add_edge(aging_choice, aging_loop)
root.order.add_edge(aging_loop, packaging_choice)
root.order.add_edge(packaging_choice, distribution_choice)
root.order.add_edge(distribution_choice, feedback_review_choice)
root.order.add_edge(feedback_review_choice, sustainability_audit_choice)
root.order.add_edge(sustainability_audit_choice, root)

print(root)