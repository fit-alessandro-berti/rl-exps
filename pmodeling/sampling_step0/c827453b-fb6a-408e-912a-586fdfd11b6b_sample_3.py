import pm4py

# Define the POWL model structure
root = pm4py.objects.powl.obj.StrictPartialOrder(
    nodes=[pm4py.objects.powl.obj.Transition(label='Sensor Setup'),
           pm4py.objects.powl.obj.Transition(label='Data Capture'),
           pm4py.objects.powl.obj.Transition(label='Nutrient Mix'),
           pm4py.objects.powl.obj.Transition(label='Crop Rotate'),
           pm4py.objects.powl.obj.Transition(label='Waste Collect'),
           pm4py.objects.powl.obj.Transition(label='Compost Process'),
           pm4py.objects.powl.obj.Transition(label='Drone Dispatch'),
           pm4py.objects.powl.obj.Transition(label='Pest Control'),
           pm4py.objects.powl.obj.Transition(label='Pollination Run'),
           pm4py.objects.powl.obj.Transition(label='Volunteer Assign'),
           pm4py.objects.powl.obj.Transition(label='Feedback Gather'),
           pm4py.objects.powl.obj.Transition(label='Model Update'),
           pm4py.objects.powl.obj.Transition(label='Yield Forecast'),
           pm4py.objects.powl.obj.Transition(label='Water Adjust'),
           pm4py.objects.powl.obj.Transition(label='Report Generate'),
           pm4py.objects.powl.obj.Transition(label='Resource Audit'),
           pm4py.objects.powl.obj.Transition(label='Schedule Sync')],

    order={})

# Define the dependencies between activities
root.order.add_edge(root.nodes[0], root.nodes[1])  # Sensor Setup -> Data Capture
root.order.add_edge(root.nodes[1], root.nodes[2])  # Data Capture -> Nutrient Mix
root.order.add_edge(root.nodes[2], root.nodes[3])  # Nutrient Mix -> Crop Rotate
root.order.add_edge(root.nodes[3], root.nodes[4])  # Crop Rotate -> Waste Collect
root.order.add_edge(root.nodes[4], root.nodes[5])  # Waste Collect -> Compost Process
root.order.add_edge(root.nodes[5], root.nodes[6])  # Compost Process -> Drone Dispatch
root.order.add_edge(root.nodes[6], root.nodes[7])  # Drone Dispatch -> Pest Control
root.order.add_edge(root.nodes[7], root.nodes[8])  # Pest Control -> Pollination Run
root.order.add_edge(root.nodes[8], root.nodes[9])  # Pollination Run -> Volunteer Assign
root.order.add_edge(root.nodes[9], root.nodes[10]) # Volunteer Assign -> Feedback Gather
root.order.add_edge(root.nodes[10], root.nodes[11])# Feedback Gather -> Model Update
root.order.add_edge(root.nodes[11], root.nodes[12])# Model Update -> Yield Forecast
root.order.add_edge(root.nodes[12], root.nodes[13])# Yield Forecast -> Water Adjust
root.order.add_edge(root.nodes[13], root.nodes[14])# Water Adjust -> Report Generate
root.order.add_edge(root.nodes[14], root.nodes[15])# Report Generate -> Resource Audit
root.order.add_edge(root.nodes[15], root.nodes[16])# Resource Audit -> Schedule Sync

# Print the POWL model
print(root)