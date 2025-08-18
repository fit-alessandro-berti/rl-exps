from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the partial order graph
root = StrictPartialOrder(
    nodes=[site_survey, permit_review, design_layout, material_sourcing, irrigation_setup, sensor_install, structural_test, recruit_farmers, trial_planting, pest_control, soilless_prep, system_calibrate, data_monitor, harvest_plan, community_outreach],
    order=[
        (site_survey, permit_review),
        (permit_review, design_layout),
        (design_layout, material_sourcing),
        (material_sourcing, irrigation_setup),
        (irrigation_setup, sensor_install),
        (sensor_install, structural_test),
        (structural_test, recruit_farmers),
        (recruit_farmers, trial_planting),
        (trial_planting, pest_control),
        (pest_control, soilless_prep),
        (soilless_prep, system_calibrate),
        (system_calibrate, data_monitor),
        (data_monitor, harvest_plan),
        (harvest_plan, community_outreach)
    ]
)

print(root)