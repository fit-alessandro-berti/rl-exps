import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
permit = Transition(label='Permit Securing')
structure = Transition(label='Structure Check')
soil = Transition(label='Soil Testing')
water = Transition(label='Water Analysis')
material = Transition(label='Material Sourcing')
planter = Transition(label='Planter Setup')
sensor = Transition(label='Sensor Install')
irrigation = Transition(label='Irrigation Setup')
vendor = Transition(label='Vendor Liaison')
training = Transition(label='Staff Training')
pest = Transition(label='Pest Control')
marketing = Transition(label='Produce Marketing')
rotation = Transition(label='Crop Rotation')
health = Transition(label='Health Audit')
waste = Transition(label='Waste Composting')

# Loop for ongoing monitoring and maintenance
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[health, waste]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    permit, structure, soil, water, material,
    planter, sensor, irrigation, vendor,
    training, pest, marketing, rotation,
    monitoring_loop
])

# Sequence of initial setup
root.order.add_edge(permit, structure)
root.order.add_edge(structure, soil)
root.order.add_edge(soil, water)
root.order.add_edge(water, material)
root.order.add_edge(material, planter)
root.order.add_edge(planter, sensor)
root.order.add_edge(sensor, irrigation)
root.order.add_edge(irrigation, vendor)
root.order.add_edge(vendor, training)

# Parallelize pest control and produce marketing
root.order.add_edge(training, pest)
root.order.add_edge(training, marketing)

# Add crop rotation after marketing
root.order.add_edge(marketing, rotation)

# Loop for ongoing health and waste management
root.order.add_edge(marketing, monitoring_loop)
root.order.add_edge(rotation, monitoring_loop)