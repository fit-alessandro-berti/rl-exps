from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
permit_filing = Transition(label='Permit Filing')
design_layout = Transition(label='Design Layout')
install_hvac = Transition(label='Install HVAC')
set_lighting = Transition(label='Set Lighting')
build_racks = Transition(label='Build Racks')
install_hydroponics = Transition(label='Install Hydroponics')
configure_sensors = Transition(label='Configure Sensors')
select_crops = Transition(label='Select Crops')
seed_planting = Transition(label='Seed Planting')
monitor_growth = Transition(label='Monitor Growth')
nutrient_mixing = Transition(label='Nutrient Mixing')
staff_training = Transition(label='Staff Training')
market_launch = Transition(label='Market Launch')
waste_recycling = Transition(label='Waste Recycling')
customer_onboarding = Transition(label='Customer Onboarding')

# Define the partial order for the process
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    permit_filing,
    design_layout,
    install_hvac,
    set_lighting,
    build_racks,
    install_hydroponics,
    configure_sensors,
    select_crops,
    seed_planting,
    monitor_growth,
    nutrient_mixing,
    staff_training,
    market_launch,
    waste_recycling,
    customer_onboarding
])

# Add dependencies if needed (for example, 'Site Survey' must be done before 'Structural Audit')
root.order.add_edge(site_survey, structural_audit)

# Now, 'root' contains the POWL model for the urban vertical farming setup process.