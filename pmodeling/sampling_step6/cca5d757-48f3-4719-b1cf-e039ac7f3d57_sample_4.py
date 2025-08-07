import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
site_assess = Transition(label='Site Assess')
load_testing = Transition(label='Load Testing')
climate_study = Transition(label='Climate Study')
medium_prep = Transition(label='Medium Prep')
bed_install = Transition(label='Bed Install')
irrigation_setup = Transition(label='Irrigation Setup')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
monitor_deploy = Transition(label='Monitor Deploy')
waste_cycle = Transition(label='Waste Cycle')
yield_forecast = Transition(label='Yield Forecast')
market_link = Transition(label='Market Link')
workshop_plan = Transition(label='Workshop Plan')
tech_integrate = Transition(label='Tech Integrate')

# Define the partial order workflow
root = StrictPartialOrder(nodes=[
    site_assess,
    load_testing,
    climate_study,
    medium_prep,
    bed_install,
    irrigation_setup,
    crop_select,
    pest_control,
    community_meet,
    monitor_deploy,
    waste_cycle,
    yield_forecast,
    market_link,
    workshop_plan,
    tech_integrate
])

# Define the order dependencies (if any)
# In this case, there are no explicit dependencies mentioned in the problem statement, so we leave the order empty
# root.order = set()

print(root)