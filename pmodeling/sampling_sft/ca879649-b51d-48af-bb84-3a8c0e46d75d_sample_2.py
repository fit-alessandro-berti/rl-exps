import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk = Transition(label='Milk Sourcing')
quality = Transition(label='Quality Testing')
batch = Transition(label='Batch Selection')
curd = Transition(label='Curd Preparation')
press = Transition(label='Pressing Cheese')
aging = Transition(label='Aging Control')
flavor = Transition(label='Flavor Profiling')
pack = Transition(label='Packaging Prep')
climate = Transition(label='Climate Packing')
license = Transition(label='Export Licensing')
customs = Transition(label='Customs Filing')
freight = Transition(label='Freight Booking')
cold = Transition(label='Cold Storage')
tracking = Transition(label='Transport Tracking')
retail = Transition(label='Retail Delivery')
feedback = Transition(label='Feedback Collection')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for aging control: do aging, then either exit or do profiling and repeat aging
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging, flavor])

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk, quality, batch,
    curd, press, loop_aging,
    pack, climate,
    license, customs, freight,
    cold, tracking, retail, feedback
])

# Define the control-flow edges
root.order.add_edge(milk, quality)
root.order.add_edge(quality, batch)
root.order.add_edge(batch, curd)
root.order.add_edge(curd, press)
root.order.add_edge(press, loop_aging)
root.order.add_edge(loop_aging, pack)
root.order.add_edge(pack, climate)
root.order.add_edge(climate, license)
root.order.add_edge(license, customs)
root.order.add_edge(customs, freight)
root.order.add_edge(freight, cold)
root.order.add_edge(cold, tracking)
root.order.add_edge(tracking, retail)
root.order.add_edge(retail, feedback)

print(root)