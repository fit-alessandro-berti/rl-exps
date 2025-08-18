from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
site_audit = Transition(label='Site Audit')
impact_study = Transition(label='Impact Study')
design_modules = Transition(label='Design Modules')
sensor_setup = Transition(label='Sensor Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_test = Transition(label='Nutrient Test')
lighting_config = Transition(label='Lighting Config')
staff_training = Transition(label='Staff Training')
data_collection = Transition(label='Data Collection')
yield_analysis = Transition(label='Yield Analysis')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
feedback_loop = Transition(label='Feedback Loop')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        site_audit,
        impact_study,
        design_modules,
        sensor_setup,
        hydroponics_install,
        nutrient_test,
        lighting_config,
        staff_training,
        data_collection,
        yield_analysis,
        pest_control,
        harvest_plan,
        packaging_prep,
        market_delivery,
        feedback_loop
    ],
    order={
        (site_audit, impact_study): None,
        (impact_study, design_modules): None,
        (design_modules, sensor_setup): None,
        (sensor_setup, hydroponics_install): None,
        (hydroponics_install, nutrient_test): None,
        (nutrient_test, lighting_config): None,
        (lighting_config, staff_training): None,
        (staff_training, data_collection): None,
        (data_collection, yield_analysis): None,
        (yield_analysis, pest_control): None,
        (pest_control, harvest_plan): None,
        (harvest_plan, packaging_prep): None,
        (packaging_prep, market_delivery): None,
        (market_delivery, feedback_loop): None
    }
)

# Optionally, you can add transitions for loops or choices, but in this case, the model is straightforward