import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk = Transition(label='Milk Sourcing')
quality = Transition(label='Quality Testing')
starter = Transition(label='Starter Prep')
curd = Transition(label='Curd Cutting')
whey = Transition(label='Whey Draining')
press = Transition(label='Molding Press')
fermentation = Transition(label='Fermentation Control')
aging = Transition(label='Aging Setup')
humidity = Transition(label='Humidity Check')
packaging = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
inventory = Transition(label='Inventory Audit')
order = Transition(label='Order Scheduling')
delivery = Transition(label='Market Delivery')
feedback = Transition(label='Feedback Review')
compliance = Transition(label='Compliance Check')
marketing = Transition(label='Marketing Sync')

# Silent transition for loop exit
skip = SilentTransition()

# Loop: do Humidity Check then either exit or do Compliance Check and repeat
humidity_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[humidity, compliance]
)

# Exclusive choice: do either Marketing Sync or Feedback Review
marketing_xor = OperatorPOWL(
    operator=Operator.XOR,
    children=[marketing, feedback]
)

# Main partial order
root = StrictPartialOrder(nodes=[
    milk, quality, starter, curd, whey, press,
    fermentation, aging, humidity_loop,
    packaging, label_approval, inventory,
    order, delivery,
    marketing_xor, compliance
])

# Sequential flow: Milk Sourcing -> Quality Testing -> Starter Prep -> Curd Cutting -> Whey Draining -> Molding Press
root.order.add_edge(milk, quality)
root.order.add_edge(quality, starter)
root.order.add_edge(starter, curd)
root.order.add_edge(curd, whey)
root.order.add_edge(whey, press)

# Parallel fermentation control and aging setup
root.order.add_edge(fermentation, aging)
root.order.add_edge(fermentation, humidity_loop)

# Packaging and label approval must happen after aging
root.order.add_edge(aging, packaging)
root.order.add_edge(aging, label_approval)

# Inventory audit must happen after packaging and label approval
root.order.add_edge(packaging, inventory)
root.order.add_edge(label_approval, inventory)

# Order scheduling must happen after inventory audit
root.order.add_edge(inventory, order)

# Market delivery must happen after order scheduling
root.order.add_edge(order, delivery)

# Marketing or feedback can happen concurrently after delivery
root.order.add_edge(delivery, marketing_xor)

# Compliance check must happen after marketing or feedback
root.order.add_edge(marketing_xor, compliance)

# End of the process
root.order.add_edge(compliance, skip)