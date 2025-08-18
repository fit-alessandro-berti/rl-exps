from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
sourcing = Transition(label='Colony Sourcing')
hive_design = Transition(label='Hive Design')
site_survey = Transition(label='Site Survey')
prep = Transition(label='Installation Prep')
setup = Transition(label='Hive Setup')
sensor_install = Transition(label='Sensor Install')
monitor = Transition(label='Health Monitor')
pest_control = Transition(label='Pest Control')
harvest = Transition(label='Honey Harvest')
wax_processing = Transition(label='Wax Processing')
packaging = Transition(label='Product Packaging')
order_dispatch = Transition(label='Order Dispatch')
workshop_setup = Transition(label='Workshop Setup')
community_outreach = Transition(label='Community Outreach')
regulation_check = Transition(label='Regulation Check')
data_analysis = Transition(label='Data Analysis')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[
    sourcing,
    hive_design,
    site_survey,
    prep,
    setup,
    sensor_install,
    monitor,
    pest_control,
    harvest,
    wax_processing,
    packaging,
    order_dispatch,
    workshop_setup,
    community_outreach,
    regulation_check,
    data_analysis,
    maintenance_plan
])

# Define the dependencies
root.order.add_edge(sourcing, hive_design)
root.order.add_edge(hive_design, site_survey)
root.order.add_edge(site_survey, prep)
root.order.add_edge(prep, setup)
root.order.add_edge(setup, sensor_install)
root.order.add_edge(sensor_install, monitor)
root.order.add_edge(monitor, pest_control)
root.order.add_edge(pest_control, harvest)
root.order.add_edge(harvest, wax_processing)
root.order.add_edge(wax_processing, packaging)
root.order.add_edge(packaging, order_dispatch)
root.order.add_edge(order_dispatch, workshop_setup)
root.order.add_edge(workshop_setup, community_outreach)
root.order.add_edge(community_outreach, regulation_check)
root.order.add_edge(regulation_check, data_analysis)
root.order.add_edge(data_analysis, maintenance_plan)

print(root)