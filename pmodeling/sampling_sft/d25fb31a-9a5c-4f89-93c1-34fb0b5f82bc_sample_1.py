import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
assess = Transition(label='Assess Structure')
analyze = Transition(label='Analyze Environment')
design = Transition(label='Design Modules')
procure = Transition(label='Procure Materials')
install = Transition(label='Install Irrigation')
set_sensors = Transition(label='Set Sensors')
select = Transition(label='Select Seeds')
schedule = Transition(label='Schedule Planting')
monitor = Transition(label='Monitor Growth')
collect = Transition(label='Collect Data')
manage = Transition(label='Manage Pests')
harvest = Transition(label='Harvest Crops')
coordinate = Transition(label='Coordinate Sales')
compost = Transition(label='Compost Waste')
review = Transition(label='Review Feedback')

# Loop for continuous monitoring
loop = OperatorPOWL(operator=Operator.LOOP, children=[collect, manage])

# Build the partial order
root = StrictPartialOrder(nodes=[
    assess, analyze, design, procure, install, set_sensors,
    select, schedule, loop, harvest, coordinate, compost, review
])

# Define the control-flow dependencies
root.order.add_edge(assess, analyze)
root.order.add_edge(analyze, design)
root.order.add_edge(design, procure)
root.order.add_edge(procure, install)
root.order.add_edge(install, set_sensors)
root.order.add_edge(set_sensors, select)
root.order.add_edge(select, schedule)
root.order.add_edge(schedule, loop)
root.order.add_edge(loop, harvest)
root.order.add_edge(harvest, coordinate)
root.order.add_edge(coordinate, compost)
root.order.add_edge(compost, review)