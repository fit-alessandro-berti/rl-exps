import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing    = Transition(label='Milk Sourcing')
supplier_audit   = Transition(label='Supplier Audit')
culture_prep     = Transition(label='Culture Prep')
milk_testing     = Transition(label='Milk Testing')
fermentation_st  = Transition(label='Fermentation Start')
ph_monitoring    = Transition(label='pH Monitoring')
curd_cutting     = Transition(label='Curd Cutting')
mold_inoculation = Transition(label='Mold Inoculation')
aging_setup      = Transition(label='Aging Setup')
humidity_ctrl    = Transition(label='Humidity Control')
texture_check    = Transition(label='Texture Check')
flavor_profiling = Transition(label='Flavor Profiling')
batch_labeling   = Transition(label='Batch Labeling')
packaging        = Transition(label='Packaging')
distribution     = Transition(label='Distribution')
feedback_review  = Transition(label='Feedback Review')
sustainability_audit = Transition(label='Sustainability Audit')

# Loop for continuous monitoring and quality checks
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ph_monitoring, texture_check, flavor_profiling]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    supplier_audit,
    culture_prep,
    milk_testing,
    fermentation_st,
    monitor_loop,
    curd_cutting,
    mold_inoculation,
    aging_setup,
    humidity_ctrl,
    batch_labeling,
    packaging,
    distribution,
    feedback_review,
    sustainability_audit
])

# Define the control‐flow dependencies
root.order.add_edge(milk_sourcing, supplier_audit)
root.order.add_edge(supplier_audit, culture_prep)
root.order.add_edge(culture_prep, milk_testing)
root.order.add_edge(milk_testing, fermentation_st)
root.order.add_edge(fermentation_st, monitor_loop)
root.order.add_edge(monitor_loop, curd_cutting)
root.order.add_edge(curd_cutting, mold_inoculation)
root.order.add_edge(mold_inoculation, aging_setup)
root.order.add_edge(aging_setup, humidity_ctrl)
root.order.add_edge(humidity_ctrl, batch_labeling)
root.order.add_edge(batch_labeling, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, feedback_review)
root.order.add_edge(feedback_review, sustainability_audit)

# Final node for completeness
root.order.add_edge(sustainability_audit, pm4py.objects.powl.obj.SILENT)

print(root)