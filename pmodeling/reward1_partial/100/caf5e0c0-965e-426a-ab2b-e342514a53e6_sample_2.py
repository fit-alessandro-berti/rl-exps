from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
climate_sim = Transition(label='Climate Sim')
seed_select = Transition(label='Seed Select')
module_setup = Transition(label='Module Setup')
nutrient_mix = Transition(label='Nutrient Mix')
water_cycle = Transition(label='Water Cycle')
energy_link = Transition(label='Energy Link')
sensor_install = Transition(label='Sensor Install')
pest_detect = Transition(label='Pest Detect')
growth_scan = Transition(label='Growth Scan')
data_sync = Transition(label='Data Sync')
community_meet = Transition(label='Community Meet')
reg_compliance = Transition(label='Reg Compliance')
system_test = Transition(label='System Test')
maintenance_plan = Transition(label='Maintenance Plan')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define sub-processes and their relationships
climate_sim_process = OperatorPOWL(operator=Operator.XOR, children=[climate_sim, skip])
module_setup_process = OperatorPOWL(operator=Operator.XOR, children=[module_setup, skip])
nutrient_mix_process = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
water_cycle_process = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, skip])
energy_link_process = OperatorPOWL(operator=Operator.XOR, children=[energy_link, skip])
sensor_install_process = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
pest_detect_process = OperatorPOWL(operator=Operator.XOR, children=[pest_detect, skip])
growth_scan_process = OperatorPOWL(operator=Operator.XOR, children=[growth_scan, skip])
data_sync_process = OperatorPOWL(operator=Operator.XOR, children=[data_sync, skip])
community_meet_process = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
reg_compliance_process = OperatorPOWL(operator=Operator.XOR, children=[reg_compliance, skip])
system_test_process = OperatorPOWL(operator=Operator.XOR, children=[system_test, skip])
maintenance_plan_process = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, skip])

# Define main process
root = StrictPartialOrder(
    nodes=[
        site_survey,
        system_design,
        climate_sim_process,
        module_setup_process,
        nutrient_mix_process,
        water_cycle_process,
        energy_link_process,
        sensor_install_process,
        pest_detect_process,
        growth_scan_process,
        data_sync_process,
        community_meet_process,
        reg_compliance_process,
        system_test_process,
        maintenance_plan_process
    ],
    order=[
        (site_survey, system_design),
        (system_design, climate_sim_process),
        (system_design, module_setup_process),
        (system_design, nutrient_mix_process),
        (system_design, water_cycle_process),
        (system_design, energy_link_process),
        (system_design, sensor_install_process),
        (system_design, pest_detect_process),
        (system_design, growth_scan_process),
        (system_design, data_sync_process),
        (system_design, community_meet_process),
        (system_design, reg_compliance_process),
        (system_design, system_test_process),
        (system_design, maintenance_plan_process),
        (climate_sim_process, module_setup_process),
        (module_setup_process, nutrient_mix_process),
        (module_setup_process, water_cycle_process),
        (module_setup_process, energy_link_process),
        (module_setup_process, sensor_install_process),
        (module_setup_process, pest_detect_process),
        (module_setup_process, growth_scan_process),
        (module_setup_process, data_sync_process),
        (module_setup_process, community_meet_process),
        (module_setup_process, reg_compliance_process),
        (module_setup_process, system_test_process),
        (module_setup_process, maintenance_plan_process),
        (nutrient_mix_process, water_cycle_process),
        (nutrient_mix_process, energy_link_process),
        (nutrient_mix_process, sensor_install_process),
        (nutrient_mix_process, pest_detect_process),
        (nutrient_mix_process, growth_scan_process),
        (nutrient_mix_process, data_sync_process),
        (nutrient_mix_process, community_meet_process),
        (nutrient_mix_process, reg_compliance_process),
        (nutrient_mix_process, system_test_process),
        (nutrient_mix_process, maintenance_plan_process),
        (water_cycle_process, energy_link_process),
        (water_cycle_process, sensor_install_process),
        (water_cycle_process, pest_detect_process),
        (water_cycle_process, growth_scan_process),
        (water_cycle_process, data_sync_process),
        (water_cycle_process, community_meet_process),
        (water_cycle_process, reg_compliance_process),
        (water_cycle_process, system_test_process),
        (water_cycle_process, maintenance_plan_process),
        (energy_link_process, sensor_install_process),
        (energy_link_process, pest_detect_process),
        (energy_link_process, growth_scan_process),
        (energy_link_process, data_sync_process),
        (energy_link_process, community_meet_process),
        (energy_link_process, reg_compliance_process),
        (energy_link_process, system_test_process),
        (energy_link_process, maintenance_plan_process),
        (sensor_install_process, pest_detect_process),
        (sensor_install_process, growth_scan_process),
        (sensor_install_process, data_sync_process),
        (sensor_install_process, community_meet_process),
        (sensor_install_process, reg_compliance_process),
        (sensor_install_process, system_test_process),
        (sensor_install_process, maintenance_plan_process),
        (pest_detect_process, growth_scan_process),
        (pest_detect_process, data_sync_process),
        (pest_detect_process, community_meet_process),
        (pest_detect_process, reg_compliance_process),
        (pest_detect_process, system_test_process),
        (pest_detect_process, maintenance_plan_process),
        (growth_scan_process, data_sync_process),
        (growth_scan_process, community_meet_process),
        (growth_scan_process, reg_compliance_process),
        (growth_scan_process, system_test_process),
        (growth_scan_process, maintenance_plan_process),
        (data_sync_process, community_meet_process),
        (data_sync_process, reg_compliance_process),
        (data_sync_process, system_test_process),
        (data_sync_process, maintenance_plan_process),
        (community_meet_process, reg_compliance_process),
        (community_meet_process, system_test_process),
        (community_meet_process, maintenance_plan_process),
        (reg_compliance_process, system_test_process),
        (reg_compliance_process, maintenance_plan_process),
        (system_test_process, maintenance_plan_process)
    ]
)