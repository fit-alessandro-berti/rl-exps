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
fermentation     = Transition(label='Fermentation Start')
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
sustainability   = Transition(label='Sustainability Audit')

# Loop for continuous microbial testing and pH monitoring
microbial_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[milk_testing, ph_monitoring]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    supplier_audit,
    culture_prep,
    fermentation,
    microbial_loop,
    curd_cutting,
    mold_inoculation,
    aging_setup,
    humidity_ctrl,
    texture_check,
    flavor_profiling,
    batch_labeling,
    packaging,
    distribution,
    feedback_review,
    sustainability
])

# Define the control‐flow dependencies
root.order.add_edge(milk_sourcing, supplier_audit)
root.order.add_edge(supplier_audit, culture_prep)
root.order.add_edge(culture_prep, fermentation)
root.order.add_edge(fermentation, microbial_loop)
root.order.add_edge(microbial_loop, curd_cutting)
root.order.add_edge(curd_cutting, mold_inoculation)
root.order.add_edge(mold_inoculation, aging_setup)
root.order.add_edge(aging_setup, humidity_ctrl)
root.order.add_edge(humidity_ctrl, texture_check)
root.order.add_edge(texture_check, flavor_profiling)
root.order.add_edge(flavor_profiling, batch_labeling)
root.order.add_edge(batch_labeling, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, feedback_review)
root.order.add_edge(feedback_review, sustainability)