from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions (activities) with exact names
site_survey = Transition(label='Site Survey')
climate_check = Transition(label='Climate Check')
soil_testing = Transition(label='Soil Testing')
media_select = Transition(label='Media Select')
design_layout = Transition(label='Design Layout')
hydro_setup = Transition(label='Hydro Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
regulation_review = Transition(label='Regulation Review')
permit_apply = Transition(label='Permit Apply')
stakeholder_meet = Transition(label='Stakeholder Meet')
community_train = Transition(label='Community Train')
plant_seed = Transition(label='Plant Seed')
monitor_growth = Transition(label='Monitor Growth')
adjust_controls = Transition(label='Adjust Controls')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
feedback_loop = Transition(label='Feedback Loop')

# Define partial order model
root = StrictPartialOrder(
    nodes=[
        site_survey, climate_check, soil_testing, media_select, design_layout, 
        hydro_setup, nutrient_mix, sensor_install, regulation_review, permit_apply, 
        stakeholder_meet, community_train, plant_seed, monitor_growth, adjust_controls, 
        harvest_plan, waste_recycle, feedback_loop
    ],
    order={
        site_survey: [climate_check], climate_check: [soil_testing], soil_testing: [media_select], media_select: [design_layout], 
        design_layout: [hydro_setup], hydro_setup: [nutrient_mix], nutrient_mix: [sensor_install], sensor_install: [regulation_review], 
        regulation_review: [permit_apply], permit_apply: [stakeholder_meet], stakeholder_meet: [community_train], community_train: [plant_seed], 
        plant_seed: [monitor_growth], monitor_growth: [adjust_controls], adjust_controls: [harvest_plan], harvest_plan: [waste_recycle], 
        waste_recycle: [feedback_loop]
    }
)

print(root)