import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
permit = Transition(label='Permit Securing')
structure = Transition(label='Structure Check')
soil = Transition(label='Soil Testing')
water = Transition(label='Water Analysis')
material = Transition(label='Material Sourcing')
planter = Transition(label='Planter Setup')
sensor = Transition(label='Sensor Install')
irrigation = Transition(label='Irrigation Setup')
vendor = Transition(label='Vendor Liaison')
staff = Transition(label='Staff Training')
pest = Transition(label='Pest Control')
produce = Transition(label='Produce Marketing')
rotation = Transition(label='Crop Rotation')
health = Transition(label='Health Audit')
waste = Transition(label='Waste Composting')

# Define the loop for seasonal crop rotation:
# A = Crop Rotation, B = Pest Control
crop_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[rotation, pest]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    permit, structure, soil, water,
    material, planter, sensor, irrigation,
    vendor, staff, pest, produce, crop_loop,
    health, waste
])

# Define the control-flow dependencies
root.order.add_edge(permit, structure)
root.order.add_edge(structure, soil)
root.order.add_edge(structure, water)
root.order.add_edge(soil, material)
root.order.add_edge(water, material)
root.order.add_edge(material, planter)
root.order.add_edge(material, sensor)
root.order.add_edge(material, irrigation)
root.order.add_edge(planter, vendor)
root.order.add_edge(sensor, vendor)
root.order.add_edge(irrigation, vendor)
root.order.add_edge(vendor, staff)
root.order.add_edge(staff, pest)
root.order.add_edge(pest, produce)
root.order.add_edge(produce, crop_loop)
root.order.add_edge(crop_loop, pest)  # Loop continues after Pest Control
root.order.add_edge(produce, health)
root.order.add_edge(health, waste)