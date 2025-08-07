import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_acquire = Transition(label='Permit Acquire')
modular_build = Transition(label='Modular Build')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
sensor_install = Transition(label='Sensor Install')
growth_monitor = Transition(label='Growth Monitor')
waste_process = Transition(label='Waste Process')
data_analysis = Transition(label='Data Analysis')
staff_train = Transition(label='Staff Train')
community_link = Transition(label='Community Link')
yield_report = Transition(label='Yield Report')

# Define the partial order process
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permit_acquire,
    modular_build,
    climate_setup,
    nutrient_mix,
    seed_automation,
    pest_control,
    energy_audit,
    sensor_install,
    growth_monitor,
    waste_process,
    data_analysis,
    staff_train,
    community_link,
    yield_report
])

# Since there are no dependencies defined in the description, the partial order is straightforward and no edges are added.

# The 'root' variable now contains the POWL model for the urban vertical farm process.