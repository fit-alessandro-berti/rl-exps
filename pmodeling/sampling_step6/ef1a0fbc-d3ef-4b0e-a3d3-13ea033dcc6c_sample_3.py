import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

milk_sourcing = Transition(label='Milk Sourcing')
farm_selection = Transition(label='Farm Selection')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
starter_culture = Transition(label='Starter Culture')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculate = Transition(label='Mold Inoculate')
aging_control = Transition(label='Aging Control')
flavor_tasting = Transition(label='Flavor Tasting')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
inventory_audit = Transition(label='Inventory Audit')
order_fulfill = Transition(label='Order Fulfill')
retail_shipping = Transition(label='Retail Shipping')

root = StrictPartialOrder(nodes=[
    milk_sourcing,
    farm_selection,
    quality_testing,
    milk_pasteurize,
    starter_culture,
    coagulation,
    curd_cutting,
    whey_draining,
    mold_inoculate,
    aging_control,
    flavor_tasting,
    packaging_design,
    label_approval,
    inventory_audit,
    order_fulfill,
    retail_shipping
])

# Since the process is simple, there are no explicit dependencies to be added.
# If there were dependencies, they would be added here like:
# root.order.add_edge(...)

print(root)