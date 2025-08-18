from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the transitions (activities)
sourcing = Transition(label='Colony Sourcing')
design = Transition(label='Hive Design')
survey = Transition(label='Site Survey')
prep = Transition(label='Installation Prep')
setup = Transition(label='Hive Setup')
sensor = Transition(label='Sensor Install')
health = Transition(label='Health Monitor')
pest = Transition(label='Pest Control')
harvest = Transition(label='Honey Harvest')
wax = Transition(label='Wax Processing')
packaging = Transition(label='Product Packaging')
dispatch = Transition(label='Order Dispatch')
workshop = Transition(label='Workshop Setup')
outreach = Transition(label='Community Outreach')
regulation = Transition(label='Regulation Check')
data = Transition(label='Data Analysis')
maintenance = Transition(label='Maintenance Plan')

# Define the partial order structure
root.nodes.extend([sourcing, design, survey, prep, setup, sensor, health, pest, harvest, wax, packaging, dispatch, workshop, outreach, regulation, data, maintenance])
root.order.add_edge(sourcing, design)
root.order.add_edge(sourcing, survey)
root.order.add_edge(survey, prep)
root.order.add_edge(prep, setup)
root.order.add_edge(setup, sensor)
root.order.add_edge(sensor, health)
root.order.add_edge(health, pest)
root.order.add_edge(pest, harvest)
root.order.add_edge(harvest, wax)
root.order.add_edge(wax, packaging)
root.order.add_edge(packaging, dispatch)
root.order.add_edge(dispatch, workshop)
root.order.add_edge(workshop, outreach)
root.order.add_edge(outreach, regulation)
root.order.add_edge(regulation, data)
root.order.add_edge(data, maintenance)

# Return the root node
print(root)