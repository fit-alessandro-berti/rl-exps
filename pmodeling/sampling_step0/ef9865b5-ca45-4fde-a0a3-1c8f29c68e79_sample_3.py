import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define silent transitions
skip = SilentTransition()

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for system calibrate and loop pest control
xor_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.XOR, children=[system_calibrate, loop_pest_control])

# Define XOR for system calibrate and loop pest control
xor_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.XOR, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data_monitor, community_outreach])

# Define loop for system calibrate and loop pest control
loop_system_calibrate_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[system_calibrate, loop_pest_control])

# Define loop for soilless prep and data monitor
loop_soilless_prep_data_monitor = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[soilless_prep, data_monitor])

# Define loop for structural test
loop_structural = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[structural_test])

# Define XOR for trial planting and soilless prep
xor_trial_planting_soilless = OperatorPOWL(operator=OperatorPOWL.XOR, children=[trial_planting, soilless_prep])

# Define loop for pest control
loop_pest_control = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[pest_control])

# Define XOR for data monitor and community outreach
xor_data_monitor_community = OperatorPOWL(operator=OperatorPOWL.XOR, children=[data