from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
soil_sample = Transition(label='Soil Sample')
water_test = Transition(label='Water Test')
crop_selection = Transition(label='Crop Selection')
material_order = Transition(label='Material Order')
planter_setup = Transition(label='Planter Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
solar_setup = Transition(label='Solar Setup')
data_integration = Transition(label='Data Integration')
community_meet = Transition(label='Community Meet')
training_session = Transition(label='Training Session')
yield_monitor = Transition(label='Yield Monitor')
adjust_plan = Transition(label='Adjust Plan')

# Define the process
root = StrictPartialOrder(
    nodes=[
        site_survey,
        structure_check,
        soil_sample,
        water_test,
        crop_selection,
        material_order,
        planter_setup,
        irrigation_install,
        sensor_deploy,
        solar_setup,
        data_integration,
        community_meet,
        training_session,
        yield_monitor,
        adjust_plan
    ],
    order=[
        (site_survey, structure_check),
        (site_survey, soil_sample),
        (site_survey, water_test),
        (site_survey, crop_selection),
        (site_survey, material_order),
        (site_survey, planter_setup),
        (site_survey, irrigation_install),
        (site_survey, sensor_deploy),
        (site_survey, solar_setup),
        (site_survey, data_integration),
        (site_survey, community_meet),
        (site_survey, training_session),
        (site_survey, yield_monitor),
        (site_survey, adjust_plan),
        (structure_check, soil_sample),
        (structure_check, water_test),
        (structure_check, crop_selection),
        (structure_check, material_order),
        (structure_check, planter_setup),
        (structure_check, irrigation_install),
        (structure_check, sensor_deploy),
        (structure_check, solar_setup),
        (structure_check, data_integration),
        (structure_check, community_meet),
        (structure_check, training_session),
        (structure_check, yield_monitor),
        (structure_check, adjust_plan),
        (soil_sample, water_test),
        (soil_sample, crop_selection),
        (soil_sample, material_order),
        (soil_sample, planter_setup),
        (soil_sample, irrigation_install),
        (soil_sample, sensor_deploy),
        (soil_sample, solar_setup),
        (soil_sample, data_integration),
        (soil_sample, community_meet),
        (soil_sample, training_session),
        (soil_sample, yield_monitor),
        (soil_sample, adjust_plan),
        (water_test, crop_selection),
        (water_test, material_order),
        (water_test, planter_setup),
        (water_test, irrigation_install),
        (water_test, sensor_deploy),
        (water_test, solar_setup),
        (water_test, data_integration),
        (water_test, community_meet),
        (water_test, training_session),
        (water_test, yield_monitor),
        (water_test, adjust_plan),
        (crop_selection, material_order),
        (crop_selection, planter_setup),
        (crop_selection, irrigation_install),
        (crop_selection, sensor_deploy),
        (crop_selection, solar_setup),
        (crop_selection, data_integration),
        (crop_selection, community_meet),
        (crop_selection, training_session),
        (crop_selection, yield_monitor),
        (crop_selection, adjust_plan),
        (material_order, planter_setup),
        (material_order, irrigation_install),
        (material_order, sensor_deploy),
        (material_order, solar_setup),
        (material_order, data_integration),
        (material_order, community_meet),
        (material_order, training_session),
        (material_order, yield_monitor),
        (material_order, adjust_plan),
        (planter_setup, irrigation_install),
        (planter_setup, sensor_deploy),
        (planter_setup, solar_setup),
        (planter_setup, data_integration),
        (planter_setup, community_meet),
        (planter_setup, training_session),
        (planter_setup, yield_monitor),
        (planter_setup, adjust_plan),
        (irrigation_install, sensor_deploy),
        (irrigation_install, solar_setup),
        (irrigation_install, data_integration),
        (irrigation_install, community_meet),
        (irrigation_install, training_session),
        (irrigation_install, yield_monitor),
        (irrigation_install, adjust_plan),
        (sensor_deploy, solar_setup),
        (sensor_deploy, data_integration),
        (sensor_deploy, community_meet),
        (sensor_deploy, training_session),
        (sensor_deploy, yield_monitor),
        (sensor_deploy, adjust_plan),
        (solar_setup, data_integration),
        (solar_setup, community_meet),
        (solar_setup, training_session),
        (solar_setup, yield_monitor),
        (solar_setup, adjust_plan),
        (data_integration, community_meet),
        (data_integration, training_session),
        (data_integration, yield_monitor),
        (data_integration, adjust_plan),
        (community_meet, training_session),
        (community_meet, yield_monitor),
        (community_meet, adjust_plan),
        (training_session, yield_monitor),
        (training_session, adjust_plan),
        (yield_monitor, adjust_plan)
    ]
)

# Print the root model
print(root)