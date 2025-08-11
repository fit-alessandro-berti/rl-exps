import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_filing = Transition(label='Permit Filing')
module_build = Transition(label='Module Build')
system_install = Transition(label='System Install')
climate_setup = Transition(label='Climate Setup')
lighting_configure = Transition(label='Lighting Configure')
irrigation_setup = Transition(label='Irrigation Setup')
nutrient_mix = Transition(label='Nutrient Mix')
pest_check = Transition(label='Pest Check')
sensor_calibrate = Transition(label='Sensor Calibrate')
data_integration = Transition(label='Data Integration')
crop_planting = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
yield_analyze = Transition(label='Yield Analyze')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')

# Define silent activities (tau labels)
skip = SilentTransition()

# Define the loop node for the pest check process
pest_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_check, sensor_calibrate])

# Define the XOR node for the nutrient mix process
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the XOR node for the irrigation setup process
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])

# Define the XOR node for the climate setup process
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define the XOR node for the lighting configure process
lighting_configure_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, skip])

# Define the XOR node for the system install process
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])

# Define the XOR node for the design layout process
design_layout_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR node for the site survey process
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])

# Define the XOR node for the permit filing process
permit_filing_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])

# Define the XOR node for the module build process
module_build_xor = OperatorPOWL(operator=Operator.XOR, children=[module_build, skip])

# Define the XOR node for the energy audit process
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])

# Define the XOR node for the yield analyze process
yield_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, skip])

# Define the XOR node for the waste manage process
waste_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the XOR node for the growth monitor process
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

# Define the XOR node for the data integration process
data_integration_xor = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])

# Define the XOR node for the crop planting process
crop_planting_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])

# Define the XOR node for the pest check process
pest_check_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_check, sensor_calibrate])

# Define the XOR node for the nutrient mix process
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the XOR node for the irrigation setup process
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])

# Define the XOR node for the climate setup process
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define the XOR node for the lighting configure process
lighting_configure_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, skip])

# Define the XOR node for the system install process
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])

# Define the XOR node for the design layout process
design_layout_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR node for the site survey process
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])

# Define the XOR node for the permit filing process
permit_filing_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])

# Define the XOR node for the module build process
module_build_xor = OperatorPOWL(operator=Operator.XOR, children=[module_build, skip])

# Define the XOR node for the energy audit process
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])

# Define the XOR node for the yield analyze process
yield_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, skip])

# Define the XOR node for the waste manage process
waste_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the XOR node for the growth monitor process
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

# Define the XOR node for the data integration process
data_integration_xor = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])

# Define the XOR node for the crop planting process
crop_planting_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])

# Define the XOR node for the pest check process
pest_check_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_check, sensor_calibrate])

# Define the XOR node for the nutrient mix process
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the XOR node for the irrigation setup process
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])

# Define the XOR node for the climate setup process
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define the XOR node for the lighting configure process
lighting_configure_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, skip])

# Define the XOR node for the system install process
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])

# Define the XOR node for the design layout process
design_layout_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR node for the site survey process
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])

# Define the XOR node for the permit filing process
permit_filing_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])

# Define the XOR node for the module build process
module_build_xor = OperatorPOWL(operator=Operator.XOR, children=[module_build, skip])

# Define the XOR node for the energy audit process
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])

# Define the XOR node for the yield analyze process
yield_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, skip])

# Define the XOR node for the waste manage process
waste_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the XOR node for the growth monitor process
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

# Define the XOR node for the data integration process
data_integration_xor = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])

# Define the XOR node for the crop planting process
crop_planting_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])

# Define the XOR node for the pest check process
pest_check_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_check, sensor_calibrate])

# Define the XOR node for the nutrient mix process
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the XOR node for the irrigation setup process
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])

# Define the XOR node for the climate setup process
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define the XOR node for the lighting configure process
lighting_configure_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, skip])

# Define the XOR node for the system install process
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])

# Define the XOR node for the design layout process
design_layout_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR node for the site survey process
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])

# Define the XOR node for the permit filing process
permit_filing_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])

# Define the XOR node for the module build process
module_build_xor = OperatorPOWL(operator=Operator.XOR, children=[module_build, skip])

# Define the XOR node for the energy audit process
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])

# Define the XOR node for the yield analyze process
yield_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, skip])

# Define the XOR node for the waste manage process
waste_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the XOR node for the growth monitor process
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

# Define the XOR node for the data integration process
data_integration_xor = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])

# Define the XOR node for the crop planting process
crop_planting_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])

# Define the XOR node for the pest check process
pest_check_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_check, sensor_calibrate])

# Define the XOR node for the nutrient mix process
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the XOR node for the irrigation setup process
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])

# Define the XOR node for the climate setup process
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define the XOR node for the lighting configure process
lighting_configure_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, skip])

# Define the XOR node for the system install process
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])

# Define the XOR node for the design layout process
design_layout_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR node for the site survey process
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])

# Define the XOR node for the permit filing process
permit_filing_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])

# Define the XOR node for the module build process
module_build_xor = OperatorPOWL(operator=Operator.XOR, children=[module_build, skip])

# Define the XOR node for the energy audit process
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])

# Define the XOR node for the yield analyze process
yield_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, skip])

# Define the XOR node for the waste manage process
waste_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the XOR node for the growth monitor process
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

# Define the XOR node for the data integration process
data_integration_xor = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])

# Define the XOR node for the crop planting process
crop_planting_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])

# Define the XOR node for the pest check process
pest_check_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_check, sensor_calibrate])

# Define the XOR node for the nutrient mix process
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the XOR node for the irrigation setup process
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])

# Define the XOR node for the climate setup process
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define the XOR node for the lighting configure process
lighting_configure_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, skip])

# Define the XOR node for the system install process
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])

# Define the XOR node for the design layout process
design_layout_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR node for the site survey process
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])

# Define the XOR node for the permit filing process
permit_filing_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])

# Define the XOR node for the module build process
module_build_xor = OperatorPOWL(operator=Operator.XOR, children=[module_build, skip])

# Define the XOR node for the energy audit process
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])

# Define the XOR node for the yield analyze process
yield_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, skip])

# Define the XOR node for the waste manage process
waste_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the XOR node for the growth monitor process
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

# Define the XOR node for the data integration process
data_integration_xor = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])

# Define the XOR node for the crop planting process
crop_planting_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])

# Define the XOR node for the pest check process
pest_check_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_check, sensor_calibrate])

# Define the XOR node for the nutrient mix process
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the XOR node for the irrigation setup process
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])

# Define the XOR node for the climate setup process
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define the XOR node for the lighting configure process
lighting_configure_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, skip])

# Define the XOR node for the system install process
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])

# Define the XOR node for the design layout process
design_layout_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR node for the site survey process
site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])

# Define the XOR node for the permit filing process
permit_filing_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])

# Define the XOR node for the module build process
module_build_xor = OperatorPOWL(operator=Operator.XOR, children=[module_build, skip])

# Define the XOR node for the energy audit process
energy_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])

# Define the XOR node for the yield analyze process
yield_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, skip])

# Define the XOR node for the waste manage process
waste_manage_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

# Define the XOR node for the growth monitor process
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])

# Define the XOR node for the data integration process
data_integration_xor = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])

# Define the XOR node for the crop planting process
crop_planting_xor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, skip])

# Define the XOR node for the pest check process
pest_check_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_check, sensor_calibrate])

# Define the XOR node for the nutrient mix process
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])

# Define the XOR node for the irrigation setup process
irrigation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])

# Define the XOR node for the climate setup process
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define the XOR node for the lighting configure process
lighting_configure_xor = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, skip])

# Define the XOR node for the system install process
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])

# Define the XOR node for the design layout process
design_layout_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR node for the site survey process
site_survey_xor = OperatorPOWL(operator=Operator