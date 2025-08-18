import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their respective labels
site_survey = Transition(label='Site Survey')
design_plan = Transition(label='Design Plan')
permit_acquire = Transition(label='Permit Acquire')
structural_retrofit = Transition(label='Structural Retrofit')
system_install = Transition(label='System Install')
lighting_setup = Transition(label='Lighting Setup')
sensor_deploy = Transition(label='Sensor Deploy')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_prep = Transition(label='Nutrient Prep')
staff_training = Transition(label='Staff Training')
data_monitor = Transition(label='Data Monitor')
yield_analyze = Transition(label='Yield Analyze')
compliance_check = Transition(label='Compliance Check')
community_meet = Transition(label='Community Meet')
market_launch = Transition(label='Market Launch')
logistics_plan = Transition(label='Logistics Plan')

# Define the exclusive choice (XOR) operator for activities related to compliance and community engagement
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, community_meet])

# Define the loop (PO) for data monitoring and yield analysis
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, yield_analyze])

# Define the root POWL model with all the defined transitions and operators
root = StrictPartialOrder(
    nodes=[site_survey, design_plan, permit_acquire, structural_retrofit, system_install, lighting_setup, sensor_deploy,
           seed_sourcing, nutrient_prep, staff_training, loop_monitor, xor_compliance, market_launch, logistics_plan],
    order={
        site_survey: [design_plan],
        design_plan: [permit_acquire],
        permit_acquire: [structural_retrofit],
        structural_retrofit: [system_install],
        system_install: [lighting_setup],
        lighting_setup: [sensor_deploy],
        sensor_deploy: [seed_sourcing],
        seed_sourcing: [nutrient_prep],
        nutrient_prep: [staff_training],
        staff_training: [data_monitor],
        data_monitor: [yield_analyze],
        yield_analyze: [compliance_check, community_meet],
        compliance_check: [market_launch],
        community_meet: [market_launch],
        market_launch: [logistics_plan]
    }
)