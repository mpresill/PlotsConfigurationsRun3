# variables

variables = {}
#variables['pTWW'] =  {'fold': 0, 'range': (50, 0, 300), 'name': 'pTWW', 'xaxis': 'pTWW'}
   
variables['testtree'] = {
  'tree' : {
       'Lepton_pt1' : 'Lepton_pt[0]',
       'Lepton_pt2' : 'Lepton_pt[1]',
       'Lepton_phi1' : 'Lepton_phi[0]',
       'Lepton_phi2' : 'Lepton_phi[1]',
       'Lepton_eta1' : 'Lepton_eta[0]',
       'Lepton_eta2' : 'Lepton_eta[1]',
       'mll' : 'mll',
       'ptll' : 'ptll',
       'dphill' : 'dphill',
       'drll' : 'drll',
       'detall' : 'detall',
       'mth' : 'mth',
       'mTi' : 'mTi',
       'mtw1' : 'mtw1',
       'mtw2' : 'mtw2',
       'mR' : 'mR',
       'mT2' : 'mT2',
       'ht' : 'ht',
       'projpfmet' : 'projpfmet',
       'projtkmet' : 'projtkmet',
       'dphiltkmet' : 'dphiltkmet',
       'mpmet' : 'mpmet',
       'pTWW' : 'pTWW',
       'mindetajl' : 'mindetajl',
       'dphilljet' : 'dphilljet',
       'dphillmet' : 'dphillmet',
       'dphilmet' : 'dphilmet',
       'dphilmet1' : 'dphilmet1',
       'dphilmet2' : 'dphilmet2',
       'dphilep1jet1' : 'dphilep1jet1',
       'dphilep2jet1' : 'dphilep2jet1',
       'PuppiMET_pt' : 'PuppiMET_pt',
       'PuppiMET_phi' : 'PuppiMET_phi',
       'CleanJet_pt1' :  'Alt(CleanJet_pt,0,0)',
       'CleanJet_pt2' :  'Alt(CleanJet_pt,1,0)',
       'CleanJet_phi1' : 'Alt(CleanJet_phi,0,0)',
       'CleanJet_phi2' : 'Alt(CleanJet_phi,1,0)',
       'CleanJet_eta1' : 'Alt(CleanJet_eta,0,0)',
       'CleanJet_eta2' : 'Alt(CleanJet_eta,1,0)',
       'mjj' : 'mjj',
       'detajj' : 'detajj',
       'dphijj' : 'dphijj',
   },
  'cuts' : ['hww2l2v_13TeV_incl']
}