import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
t_milk_sourcing = Transition(label='Milk Sourcing')
t_farm_selection = Transition(label='Farm Selection')
t_quality_testing = Transition(label='Quality Testing')
t_milk_pasturize = Transition(label='Milk Pasteurize')
t_starter_culture = Transition(label='Starter Culture')
t_coagulation = Transition(label='Coagulation')
t_curd_cutting = Transition(label='Curd Cutting')
t_whey_draining = Transition(label='Whey Draining')
t_mold_inoculate = Transition(label='Mold Inoculate')
t_aging_control = Transition(label='Aging Control')
t_flavor_tasting = Transition(label='Flavor Tasting')
t_inventory_audit = Transition(label='Inventory Audit')
t_order_fulfill = Transition(label='Order Fulfill')
t_retail_shipping = Transition(label='Retail Shipping')
t_packaging_design = Transition(label='Packaging Design')
t_label_approval = Transition(label='Label Approval')

# Loop for seasonal adjustments
# A: Inventory Audit
# B: Milk Sourcing -> Farm Selection -> Quality Testing -> Milk Pasteurize -> Starter Culture -> Coagulation -> Curd Cutting -> Whey Draining -> Mold Inoculate -> Aging Control -> Flavor Tasting
seasonal_seq = StrictPartialOrder(nodes=[
    t_inventory_audit,
    t_milk_sourcing, t_farm_selection, t_quality_testing,
    t_milk_pasturize, t_starter_culture, t_coagulation,
    t_curd_cutting, t_whey_draining, t_mold_inoculate,
    t_aging_control, t_flavor_tasting
])
seasonal_seq.order.add_edge(t_inventory_audit, t_milk_sourcing)
seasonal_seq.order.add_edge(t_milk_sourcing, t_farm_selection)
seasonal_seq.order.add_edge(t_farm_selection, t_quality_testing)
seasonal_seq.order.add_edge(t_quality_testing, t_milk_pasturize)
seasonal_seq.order.add_edge(t_milk_pasturize, t_starter_culture)
seasonal_seq.order.add_edge(t_starter_culture, t_coagulation)
seasonal_seq.order.add_edge(t_coagulation, t_curd_cutting)
seasonal_seq.order.add_edge(t_curd_cutting, t_whey_draining)
seasonal_seq.order.add_edge(t_whey_draining, t_mold_inoculate)
seasonal_seq.order.add_edge(t_mold_inoculate, t_aging_control)
seasonal_seq.order.add_edge(t_aging_control, t_flavor_tasting)

# Loop: repeat Inventory Audit followed by the seasonal sequence until exit
seasonal_loop = OperatorPOWL(operator=Operator.LOOP, children=[t_inventory_audit, seasonal_seq])

# Packaging and labeling
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')

# Fulfillment and shipping
order_fulfill = Transition(label='Order Fulfill')
retail_shipping = Transition(label='Retail Shipping')

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    seasonal_loop,
    packaging_design, label_approval,
    order_fulfill, retail_shipping
])
root.order.add_edge(seasonal_loop, packaging_design)
root.order.add_edge(packaging_design, label_approval)
root.order.add_edge(label_approval, order_fulfill)
root.order.add_edge(order_fulfill, retail_shipping)

print(root)