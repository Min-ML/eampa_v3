


class pf_potential:

  def update(p):    
    # Store
    g.pfdata['params']['current'][:] = p[:]
  
    # Update potential
    a = 0
    for fn in range(len(g.pot_functions['functions'])): 
      if(g.pot_functions['functions'][fn]['fit_type'] == 1):     # NODE SPLINE    
        ###NEED TO REDO MAYBE??###
      
        # Calc b
        b = a + g.pot_functions['functions'][fn]['fit_size']          
        # LOAD ORIGINAL
        g.pot_functions['functions'][fn]['points'] = numpy.copy(g.pot_functions['functions'][fn]['points_original'])        
        # VARY SPLINE
        potential.vary_tabulated_points(fn, p[a:b])
        # Update a
        a = b        
      elif(g.pot_functions['functions'][fn]['fit_type'] == 2):   # ANALYTIC  
        b = a + g.pot_functions['functions'][fn]['fit_size'] 
        # Make Analytic Points
        g.pot_functions['functions'][fn]['a_params'][:] = p[a:b]
        potential.make_analytic_points_inner(fn)
        a = b    
      
    # Rescale density functions 0.0 to 1.0  
    if(g.fit['rescale_density']):
      rescale_density.run()    
    
    # Update efs and bp modules
    potential.efs_add_potentials()     # Load potentials
    potential.bp_add_potentials()      # Load potentials