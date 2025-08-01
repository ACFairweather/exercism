"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    return (temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = ((voltage * current) / theoretical_max_power) * 100
    output = ''
    if efficiency >= 80:
        output = 'green'
    elif efficiency >= 60:
        output = 'orange'
    elif efficiency >= 30:
        output = 'red'
    else:
        output = 'black'
    return output

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    temp_by_neutron_flux = temperature * neutrons_produced_per_second
    output = ''
    if (temp_by_neutron_flux < (threshold * 0.9)):
        output = 'LOW'
    elif (temp_by_neutron_flux >= (threshold * 0.9) and temp_by_neutron_flux <= (threshold * 1.1)):
        output = 'NORMAL'
    else:
        output = 'DANGER'
    return output