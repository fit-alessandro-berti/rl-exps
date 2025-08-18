import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    supplier_audit,
    culture_prep,
    milk_testing,
    fermentation_start,
    pH_monitoring,
    curd_cutting,
    mold_inoculation,
    aging_setup,
    humidity_control,
    texture_check,
    flavor_profiling,
    batch_labeling,
    packaging,
    distribution,
    feedback_review,
    sustainability_audit
])

# Define the dependencies
root.order.add_edge(milk_sourcing, supplier_audit)
root.order.add_edge(supplier_audit, culture_prep)
root.order.add_edge(culture_prep, milk_testing)
root.order.add_edge(milk_testing, fermentation_start)
root.order.add_edge(fermentation_start, pH_monitoring)
root.order.add_edge(pH_monitoring, curd_cutting)
root.order.add_edge(curd_cutting, mold_inoculation)
root.order.add_edge(mold_inoculation, aging_setup)
root.order.add_edge(aging_setup, humidity_control)
root.order.add_edge(humidity_control, texture_check)
root.order.add_edge(texture_check, flavor_profiling)
root.order.add_edge(flavor_profiling, batch_labeling)
root.order.add_edge(batch_labeling, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, feedback_review)
root.order.add_edge(feedback_review, sustainability_audit)

# Print the root
print(root)