import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
structural_test = Transition(label='Structural Test')
recruit_farmers = Transition(label='Recruit Farmers')
trial_planting = Transition(label='Trial Planting')
pest_control = Transition(label='Pest Control')
soilless_prep = Transition(label='Soilless Prep')
system_calibrate = Transition(label='System Calibrate')
data_monitor = Transition(label='Data Monitor')
harvest_plan = Transition(label='Harvest Plan')
community_outreach = Transition(label='Community Outreach')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_review,
    design_layout,
    material_sourcing,
    irrigation_setup,
    sensor_install,
    structural_test,
    recruit_farmers,
    trial_planting,
    pest_control,
    soilless_prep,
    system_calibrate,
    data_monitor,
    harvest_plan,
    community_outreach
])

# Add dependencies if any (in this case, all activities are concurrent)
# No dependencies are added explicitly in this example

# The final result is 'root', which represents the complete POWL model of the process.