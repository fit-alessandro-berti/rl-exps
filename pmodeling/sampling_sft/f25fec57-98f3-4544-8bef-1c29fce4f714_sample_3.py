import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey       = Transition(label='Site Survey')
permit_filing     = Transition(label='Permit Filing')
structure_design  = Transition(label='Structure Design')
system_install    = Transition(label='System Install')
hydroponic_setup  = Transition(label='Hydroponic Setup')
climate_config    = Transition(label='Climate Config')
ai_integration    = Transition(label='AI Integration')
nutrient_sourcing = Transition(label='Nutrient Sourcing')
waste_planning    = Transition(label='Waste Planning')
staff_training    = Transition(label='Staff Training')
crop_seeding      = Transition(label='Crop Seeding')
growth_monitoring = Transition(label='Growth Monitoring')
quality_testing   = Transition(label='Quality Testing')
harvest_scheduling= Transition(label='Harvest Scheduling')
distribution_plan = Transition(label='Distribution Plan')
data_analysis     = Transition(label='Data Analysis')

# Define the main production cycle as a partial order
cycle = StrictPartialOrder(
    nodes=[
        crop_seeding, growth_monitoring, quality_testing, harvest_scheduling,
        distribution_plan, data_analysis
    ]
)
# Define the control-flow dependencies within one cycle
cycle.order.add_edge(crop_seeding, growth_monitoring)
cycle.order.add_edge(growth_monitoring, quality_testing)
cycle.order.add_edge(quality_testing, harvest_scheduling)
cycle.order.add_edge(harvest_scheduling, distribution_plan)
cycle.order.add_edge(distribution_plan, data_analysis)

# Define the overall process as a loop: do the cycle, then optionally repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle, cycle]
)