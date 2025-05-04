#%%
#import met_brewer
#
#pal = met_brewer.met_brew(name="Demuth", n=12, brew_type="continuous")
#pal

# "#591c19", 
# "#9b332b", 
# "#b64f32",
# "#d39a2d",
# "#f7c267",
# "#b9b9b8",
# "#8b8b99",
# "#5d6174",
# "#41485f",
# "#262d42"
#%%
#print(met_brewer.export(name = "Demuth"))

#%%

standard = {
    "first"               : "#3c435a",
    "first_light"         : "#9da1ac",
    "plan_target"         : "#ac452f",
    "plan_target_low"     : "#ac452f",
    "plan_target_high"    : "#dda53d",
    "plan_target_belfort" : "#2b614e",
    "plan_linear"         : "#ac452f",
    "plan_linear_low"     : "#ac452f",
    "plan_linear_high"    : "#dda53d",
    "plan_log"            : "#c37130",
    "trend1"              : "#bfbab1",
    "trend2"              : "#9898a1",
    "ar_main"             : "#d39a2d",
    "ar_main_inter"       : "#53586c",
    "ar_background"       : "rgba(211,154,45,0.25)",
    "ar_background2"      : "rgba(191, 186, 177, 0.5)",
    "second"              : "#2A6A89",
    "third"               : "#0094A4",
    "fourth"              : "#18BCA0",
    "fifth"               : "#8BE087",
    "misc"                : "#262d42",
    "pv_sonstige"         : "rgba(191, 186, 177, 0.25)",
    "pv_util"             : "rgba(252, 186, 3,   1)",
    "pv_util_fill"        : "rgba(253, 220, 129, 1)",
    "pv_util_trend"       : "rgba(255, 248, 230, 1)",
    "pv_util_trend_fill"  : "rgba(254, 234, 178, 1)",
    }

#color_standard = {
#    'first'         : '#262d42',
#    'first_light'   : '#8f2f28',
#    'second'        : '#ac452f',
#    'plan_target'   : '#c37130',
#    'plan_linear'   : '#dda53d',
#    'plan_log'      : '#f1c16e',
#    'trend1'        : '#bfbab1',
#    'trend2'        : '#9898a1',
#    'ar_main'       : '#727485',
#    'ar_main_inter' : '#53586c',
#    'ar_background' : '#3c435a',
#    'misc'          : '#262d42'
#    }

colors_gradient = {
    1:  "#F9FDE3",
    2:  "#F7F8B4",
    3:  "#F3E886",
    4:  "#EDCD5A",
    5:  "#E5A82E",
    6:  "#C5791B",
    7:  "#974E17",
    8:  "#692D11",
    9:  "#3D150B",
    10: "#110403"
}


#%% DIW inspired

standard2 = {
    "first"         : "#13c0b0",
    "first_light"   : "#8f2f28",
    "second"        : "#ac452f",
    "plan_target"   : "#9b332b",
    "plan_linear"   : "#9b332b",
#    "plan_linear"   : "#dda53d",
    "plan_log"      : "#f1c16e",
    "trend1"        : "#bfbab1",
    "trend2"        : "#9898a1",
#   "ar_main"       : "#727485",
    "ar_main"       : "#d39a2d",
    "ar_main_inter" : "#53586c",
#   "ar_background" : "#3c435a",
    "ar_background" : "rgba(211, 154, 45, 0.25)",
    "misc"          : "#262d42"
    }


diw = {
    'first'         : 'rgba(0,120,107,1)',
    'first_light'   : 'rgba(0,120,107,0.5)',
    'second'        : 'rgba(111,200,182,1)',
    'plan_target'   : 'rgba(105,70,135,1)',
    'plan_linear'   : 'rgba(105,70,135,1)',
    'plan_log'      : 'rgba(25,90,150,0.75)',
    'trend1'        : 'rgba(94,124,143,1)',
    'trend2'        : 'rgba(23,38,36,1)',
    'ar_main'       : 'rgba(236,102,8,1)',
    'ar_main_inter' : 'rgba(236,102,8,1)',
    'ar_background' : 'rgba(236,102,8,0.25)',
    'third'         : 'rgba(110,183,75,1)',
    'fourth'        : 'rgba(105,75,54,1)',
    'fifth'         : 'rgba(174,57,63,1)',
    }


#colors for technologies
tech = {
    'pv'                : '#FFC94D', # Sunflower Yellow
    'wind_onshore'      : '#7BA5C8', #cornflower blue
    'wind_offshore'     : '#8E9AA5', # Slate Blue
    'lignite'           : '#C2877B', # Rusty Brown
    'nuclear'           : '#ed9178', # Coral / Light Yellow #ed9178 #FCD9A0
    'hydro'             : '#5EAAA8', #Teal
    'conventional_misc' : '#591c19', #Dark Red
    'renewable_misc'    : '#AAB593', #Dusty Green
    'biomass'           : '#9FC68E', #Olive Green
    'hard_coal'         : '#3c435a', #Dark Blue
    'pump_storage'      : '#A9D9C7', #aqua
    'gas'               : '#b9b9b8' #Grey
    }


#Colors for price figures (fading out from dark to light)
prices = {
    'first' :"#c73f38", #dark red (for the cureent year)
    'second':"#3c435a", #dark blue (for the past year)
    'third' :"#47506b", #blue
    'fourth':"#5c678a", #light blue
    'fifth' :"#7580a3", #light blue
    'sixth' :"#949cb8", #light blue
    'further':"#b3b8cc", #light grey blue (for all further years)
    'single_price' : '#3c435a', #dark blue for price figures with only one trace color 
    'years_fading' : ["#c73f38","#3c435a", "#47506b", "#5c678a", "#7580a3", "#949cb8", "#b3b8cc"],
    'years_fading_blue' : ["#2A6A89","#3c435a", "#47506b", "#5c678a", "#7580a3", "#949cb8", "#b3b8cc"],
    'proc_net_dist' : "#3c435a", #dark blue used in hh_electricity_prices
    'proc_dist'     : "#355d7e", #blue used in hh_electricity_prices
    'net'           : '#7BA5C8', #cornflower blue used in hh_electricity_prices
    'conc'          : '#9e3215', #dark red used in hh_electricity_prices
    'eeg'           : '#4d773c', #dark green used in hh_electricity_prices
    'other'         : '#9FC68E', #Olive Green used in hh_electricity_prices
    'tax'           : '#ed9178', #coral used in hh_electricity_prices
    'vat'           : '#e2481d' #red used in hh_electricity_prices
    }
    

#Colors for Mobility/vehicles
emobility = {
    'diesel'        : '#262d42', #dark blue 
    'petrol'        : '#5d6174', #dark grey
    'diesel_petrol' : '#262d42', #dark blue
    'gas'           : '#b9b9b8', #grey
    'hydrogen'      : '#2A6A89', #light blue
    'bev'           : '#41B3A2', #Olivgrün Dunkel 
    'phev'          : '#D6C0B3', 
    'hev'           : '#AB886D', #apricot 
    'hybrid_nodiff' : '#493628', # pale gold 
    'fuel_cell'     : '#7fa5b8', #teal (PV Figure) 
    'other'         : '#b3b8cc', #grey
    'first'         : "#3c435a", #used as fill color for legislative period i.e.
    'line'          : "#ac452f", #used as line color for i.e. trends,
    'black'         : "#000000"
    }

pv_deepdive = {
    #pal: palette for different categories
    "pal" : [ 
    "#5EAAA8",  # Teal
    "#E87352",  # Warm Coral
    "#AAB593",  # Dusty Green
    "#FDBA8F",  # Apricot
    "#FFC94D",  # Sunflower Yellow
    "#A9D9C7",  # Aqua
    "#F7D394",  # Pale Gold
    "#FCD9A0",  # Light Amber
    "#9FC68E",  # Moss Green
    "#E3AE8A",  # Terra Cotta
    "#FFB16D",  # Melon
    "#8E9AA5",  # Slate Blue
    "#C2877B",  # Rusty Brown
    "#E7998C",  # Coral Pink
    "#7BA5C8",  # Cornflower Blue
    "#D5C2C3",  # Rose Taupe
    ],
    "Balkon": "#FDBA8F",
    "Bauliche_Anlagen1": "#5EAAA8", #3c6a90
    "Bauliche_Anlagen2" : "#7BA5C8", #alternative color for pv on buildings #E87352
    "Freifläche": "#AAB593", #9FC68E #598844
    "Andere": "#FCD9A0",
    "gradient_red" : ["#fcede8","#f0a78e","#e2481d"],
    "colorscale_red" : ["#fcede8","#f0a38e","#e2481d"], #colorscale based on warm coral
    "first" : "#3c435a",
    "second" : "#2A6A89",
    "terra_cotta" : "#E3AE8A",
    "red" : "#ac452f",
    "dark_blue" : "#3c6a90",
    "dark_green" : "#598844",
    "legislation_period" : "#3c435a"
    }
