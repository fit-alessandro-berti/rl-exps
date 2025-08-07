import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
farm = Transition(label='Farm Selection')
milk = Transition(label='Milk Testing')
batch = Transition(label='Batch Pasteurize')
culture = Transition(label='Culture Add')
curd = Transition(label='Curd Cut')
whey = Transition(label='Whey Drain')
mold = Transition(label='Mold Inoculate')
press = Transition(label='Press Form')
salt = Transition(label='Salt Rub')
aging = Transition(label='Aging Monitor')
flavor = Transition(label='Flavor Adjust')
pack = Transition(label='Packaging Design')
label = Transition(label='Label Approval')
order = Transition(label='Order Processing')
cold = Transition(label='Cold Storage')
delivery = Transition(label='Delivery Schedule')
retail = Transition(label='Retail Setup')
feedback = Transition(label='Feedback Collect')

# Loop for seasonal flavor adjustments
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging, flavor])

# Build the partial order
root = StrictPartialOrder(nodes=[
    farm, milk, batch, culture, curd, whey, mold, press, salt,
    loop,
    pack, label, order,
    cold, delivery, retail, feedback
])

# Define the control-flow dependencies
root.order.add_edge(farm, milk)
root.order.add_edge(milk, batch)
root.order.add_edge(batch, culture)
root.order.add_edge(culture, curd)
root.order.add_edge(curd, whey)
root.order.add_edge(whey, mold)
root.order.add_edge(mold, press)
root.order.add_edge(press, salt)
root.order.add_edge(salt, loop)
root.order.add_edge(loop, pack)
root.order.add_edge(pack, label)
root.order.add_edge(label, order)
root.order.add_edge(order, cold)
root.order.add_edge(cold, delivery)
root.order.add_edge(delivery, retail)
root.order.add_edge(retail, feedback)

# Final dependencies for the loop body
root.order.add_edge(loop, aging)
root.order.add_edge(loop, flavor)