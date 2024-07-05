# variables

# 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
    
variables = {}

variables['events'] = {
    'name'  : '1',      
    'range' : (1,0,2),  
    'xaxis' : 'events', 
    'fold'  : 3
}

variables['mjj']  = {   'name': 'mjj',            #   variable name    
                        'range' : (30,500,3500),    #   variable range
                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        'fold' :3,
                        }

#variables['mjj']  = {   'name': 'mjj_max',            #   variable name    
#                        'range' : (30,500,3500),    #   variable range
#                        'xaxis' : 'm_{jj} [GeV]',  #   x axis name
#                        'fold' :3,
#                        }