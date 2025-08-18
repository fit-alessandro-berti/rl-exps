import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Env Analysis'),
    Transition(label='Modular Build'),
    Transition(label='Hydroponic Setup'),
    Transition(label='Seed Select'),
    Transition(label='Nutrient Prep'),
    Transition(label='Climate Calibrate'),
    Transition(label='Sensor Install'),
    Transition(label='AI Integration'),
    Transition(label='Crop Monitor'),
    Transition(label='Growth Adjust'),
    Transition(label='Harvest Sort'),
    Transition(label='Packaging'),
    Transition(label='Distribution Plan'),
    Transition(label='Sustain Audit'),
    Transition(label='Energy Optimize')
])

# Define dependencies
root.order.add_edge('Site Survey', 'Env Analysis')
root.order.add_edge('Env Analysis', 'Modular Build')
root.order.add_edge('Modular Build', 'Hydroponic Setup')
root.order.add_edge('Hydroponic Setup', 'Seed Select')
root.order.add_edge('Seed Select', 'Nutrient Prep')
root.order.add_edge('Nutrient Prep', 'Climate Calibrate')
root.order.add_edge('Climate Calibrate', 'Sensor Install')
root.order.add_edge('Sensor Install', 'AI Integration')
root.order.add_edge('AI Integration', 'Crop Monitor')
root.order.add_edge('Crop Monitor', 'Growth Adjust')
root.order.add_edge('Growth Adjust', 'Harvest Sort')
root.order.add_edge('Harvest Sort', 'Packaging')
root.order.add_edge('Packaging', 'Distribution Plan')
root.order.add_edge('Distribution Plan', 'Sustain Audit')
root.order.add_edge('Sustain Audit', 'Energy Optimize')

print(root)