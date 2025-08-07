import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
permit_filing    = Transition(label='Permit Filing')
structure_design = Transition(label='Structure Design')
system_install   = Transition(label='System Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_config   = Transition(label='Climate Config')
ai_integration   = Transition(label='AI Integration')
nutrient_sourcing= Transition(label='Nutrient Sourcing')
waste_planning   = Transition(label='Waste Planning')
staff_training   = Transition(label='Staff Training')
crop_seeding     = Transition(label='Crop Seeding')
growth_monitor   = Transition(label='Growth Monitoring')
quality_testing  = Transition(label='Quality Testing')
harvest_sched    = Transition(label='Harvest Scheduling')
distribution_pl  = Transition(label='Distribution Plan')
data_analysis    = Transition(label='Data Analysis')

# Define the monitoring loop: Growth Monitoring -> Quality Testing, repeated until exit
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, quality_testing]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    structure_design,
    system_install,
    hydroponic_setup,
    climate_config,
    ai_integration,
    nutrient_sourcing,
    waste_planning,
    staff_training,
    crop_seeding,
    monitor_loop,
    harvest_sched,
    distribution_pl,
    data_analysis
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,     permit_filing)
root.order.add_edge(permit_filing,   structure_design)
root.order.add_edge(structure_design,system_install)
root.order.add_edge(system_install,  hydroponic_setup)
root.order.add_edge(hydroponic_setup,climate_config)
root.order.add_edge(climate_config,  ai_integration)
root.order.add_edge(ai_integration,  nutrient_sourcing)
root.order.add_edge(nutrient_sourcing,waste_planning)
root.order.add_edge(waste_planning,  staff_training)
root.order.add_edge(staff_training,  crop_seeding)
root.order.add_edge(crop_seeding,    monitor_loop)
root.order.add_edge(monitor_loop,    harvest_sched)
root.order.add_edge(harvest_sched,   distribution_pl)
root.order.add_edge(distribution_pl, data_analysis)