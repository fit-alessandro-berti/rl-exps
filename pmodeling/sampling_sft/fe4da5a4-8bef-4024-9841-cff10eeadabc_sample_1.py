import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
permit    = Transition(label='Permit Securing')
structure = Transition(label='Structure Check')
soil      = Transition(label='Soil Testing')
water     = Transition(label='Water Analysis')
material  = Transition(label='Material Sourcing')
planter   = Transition(label='Planter Setup')
sensor    = Transition(label='Sensor Install')
irrigation= Transition(label='Irrigation Setup')
vendor    = Transition(label='Vendor Liaison')
training  = Transition(label='Staff Training')
pest      = Transition(label='Pest Control')
marketing = Transition(label='Produce Marketing')
rotation  = Transition(label='Crop Rotation')
health    = Transition(label='Health Audit')
waste     = Transition(label='Waste Composting')

# Build the partial order
root = StrictPartialOrder(nodes=[
    permit, structure, soil, water, material,
    planter, sensor, irrigation, vendor,
    training, pest, marketing, rotation,
    health, waste
])

# Sequential dependencies
root.order.add_edge(permit,    structure)
root.order.add_edge(structure, soil)
root.order.add_edge(structure, water)
root.order.add_edge(soil,      material)
root.order.add_edge(water,     material)
root.order.add_edge(material,  planter)
root.order.add_edge(planter,   sensor)
root.order.add_edge(sensor,    irrigation)
root.order.add_edge(irrigation, vendor)
root.order.add_edge(vendor,    training)

# After training, parallel pest & marketing
root.order.add_edge(training, pest)
root.order.add_edge(training, marketing)

# Crop rotation and health audit after pest & marketing
root.order.add_edge(pest,      rotation)
root.order.add_edge(pest,      health)
root.order.add_edge(marketing, rotation)
root.order.add_edge(marketing, health)

# Waste composting after rotation & health
root.order.add_edge(rotation, waste)
root.order.add_edge(health,   waste)