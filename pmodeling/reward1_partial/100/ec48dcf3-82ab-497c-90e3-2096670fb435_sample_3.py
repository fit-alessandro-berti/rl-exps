import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the urban vertical farm process
root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='Structure Build'),
        Transition(label='System Install'),
        Transition(label='Climate Setup'),
        Transition(label='Nutrient Prep'),
        Transition(label='Seed Germinate'),
        Transition(label='Planting Phase'),
        Transition(label='Sensor Deploy'),
        Transition(label='Pest Control'),
        Transition(label='Water Monitor'),
        Transition(label='Data Analyze'),
        Transition(label='Staff Train'),
        Transition(label='Yield Forecast'),
        Transition(label='Community Meet')
    ],
    order={
        ('Site Survey', 'Design Layout'): True,
        ('Design Layout', 'Structure Build'): True,
        ('Structure Build', 'System Install'): True,
        ('System Install', 'Climate Setup'): True,
        ('Climate Setup', 'Nutrient Prep'): True,
        ('Nutrient Prep', 'Seed Germinate'): True,
        ('Seed Germinate', 'Planting Phase'): True,
        ('Planting Phase', 'Sensor Deploy'): True,
        ('Sensor Deploy', 'Pest Control'): True,
        ('Pest Control', 'Water Monitor'): True,
        ('Water Monitor', 'Data Analyze'): True,
        ('Data Analyze', 'Staff Train'): True,
        ('Staff Train', 'Yield Forecast'): True,
        ('Yield Forecast', 'Community Meet'): True
    }
)