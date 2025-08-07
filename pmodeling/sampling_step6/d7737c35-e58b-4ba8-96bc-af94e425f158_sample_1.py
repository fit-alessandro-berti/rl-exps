import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
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

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing, supplier_audit, culture_prep, milk_testing, fermentation_start,
    pH_monitoring, curd_cutting, mold_inoculation, aging_setup, humidity_control,
    texture_check, flavor_profiling, batch_labeling, packaging, distribution,
    feedback_review, sustainability_audit
])

# Add dependencies as needed (not specified in the problem statement, but can be added if required)
# For example, if there is a dependency between 'Milk Testing' and 'Culture Prep', you can add it like this:
# root.order.add_edge(milk_testing, culture_prep)

# The root variable now contains the POWL model for the process
print(root)