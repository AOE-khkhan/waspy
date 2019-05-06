from __future__ import division, print_function
import pickle
from waspy.all_read_cases import load_all_cases, print_results, plot_thicknesses, plot_lifts, plot_tc, plot_twist, folders


read_OM_db = False

if read_OM_db:
    data = load_all_cases()
    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)
else:
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)

thickness_labels = {
    'baseline' : (0.5, 0.008),
    'viscous' : (0.0481, 0.0055),
    'wave_drag' : (-0.03, 0.0097),
    'struct_weight' : (0.0919, 0.0120),
    'fuel_weight' : (0.317, 0.0100),
    'engine_mass' : (0.19, 0.0113),
    'engine_thrust' : (-0.03, 0.0093),
}

print_results(data)
plot_thicknesses(data, folders, live_plot=False, annotate_data=thickness_labels)

anchor = 0.8
spacing = 0.06
lift_labels = {
    'baseline' : (0.1, anchor + 0.0),
    'viscous' : (0.1, anchor - 5 * spacing),
    'wave_drag' : (0.1, anchor - 4 * spacing),
    'struct_weight' : (0.1, anchor + spacing),
    'fuel_weight' : (0.1, anchor - 3 * spacing),
    'engine_mass' : (0.1, anchor - 2 * spacing),
    'engine_thrust' : (0.1, anchor - spacing),
    'elliptical' : (0.6, 1.1),
}

plot_lifts(data, folders, live_plot=False, annotate_data=lift_labels)

tc_labels = {
    'baseline' : (0.8, 0.12),
    'viscous' : (0.0576, 0.16),
    'wave_drag' : (0.0576, 0.12),
    'struct_weight' : (0.17, 0.1233),
    'fuel_weight' : (0.55, 0.126),
    'engine_mass' : (0.8, 0.12),
    'engine_thrust' : (0.8, 0.12),
}

plot_tc(data, folders, live_plot=False, annotate_data=tc_labels)

twist_labels = {
    'baseline' : (0.8, 4.),
    'viscous' : (0.0576, 4.),
    'wave_drag' : (0.0576, 4.),
    'struct_weight' : (0.17, 4.3),
    'fuel_weight' : (0.55, 4.),
    'engine_mass' : (0.8, 4.),
    'engine_thrust' : (0.8, 4.),
}

plot_twist(data, folders, live_plot=False, annotate_data=twist_labels)
