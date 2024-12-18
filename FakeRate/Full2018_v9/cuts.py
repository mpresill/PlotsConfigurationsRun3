jet_pt_thresholds = [10, 15, 20, 25, 30, 35, 40, 45]

# cuts
cuts = {}

preselections = 'nLepton > 0'

# Prompt rate selections
cuts['Zpeak_PR_loose'] = {
    'expr'       : 'nLepton>1 && Lepton_pt[0]>25 && LepWPCut1l && Lepton_pt[1]>10 && mll>76 && mll<106 && PuppiMET_pt<20',
    'categories' : {
        'ele'  : 'Lepton_pdgId[0]*Lepton_pdgId[1] == -121',
        'muon' : 'Lepton_pdgId[0]*Lepton_pdgId[1] == -169',
    }
}

# Prompt rate selections
cuts['Zpeak_PR_tight'] = {
    'expr'       : 'nLepton>1 && Lepton_pt[0]>25 && Lepton_pt[1]>10 && LepWPCut2l && mll>76 && mll<106 && PuppiMET_pt<20',
    'categories' : {
        'ele'  : 'Lepton_pdgId[0]*Lepton_pdgId[1] == -121',
        'muon' : 'Lepton_pdgId[0]*Lepton_pdgId[1] == -169',
    }
}


for jet_pt_threshold in jet_pt_thresholds:

    # print(f"Jet pT threshold = {jet_pt_threshold}")

    # print(f"Cuts: {cuts}")
    
    ##########################
    # Loose leptons selections
    ##########################
    
    # QCD region
    cuts[f'QCD_loose_jet_pt_{jet_pt_threshold}'] = {
        'expr'    : f'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && drlj_{jet_pt_threshold} > 1',
        'categories' : {
            'ele'  : 'abs(Lepton_pdgId[0]) == 11',
            'muon' : 'abs(Lepton_pdgId[0]) == 13',
        }
    }
    # 'expr'    : f'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && Alt(CleanJet_pt,0,0) > {jet_pt_threshold} && abs(CleanJet_eta[0]) < 2.5 && dRl1j1 > 1',

    # Z-peak
    cuts[f'Zpeak_loose_jet_pt_{jet_pt_threshold}'] = {
        'expr'       : f'nLepton > 1 && PuppiMET_pt < 20 && mll > 60 && mll < 120',
        'categories' : {
            'ele'  : 'Lepton_pdgId[0]*Lepton_pdgId[1] == -121',
            'muon' : 'Lepton_pdgId[0]*Lepton_pdgId[1] == -169',
        }
    }
    # 'expr'       : f'nLepton > 1 && PuppiMET_pt < 20 && mll > 60 && mll < 120 && Alt(CleanJet_pt,0,0) > {jet_pt_threshold}',

    # WJets region
    cuts[f'WJets_loose_jet_pt_{jet_pt_threshold}'] = {
        'expr'       : f'nLepton == 1 && mtw1 > 20 && PuppiMET_pt < 20 && drlj_{jet_pt_threshold} > 1',
        'categories' : {
            'ele'  : 'abs(Lepton_pdgId[0]) == 11',
            'muon' : 'abs(Lepton_pdgId[0]) == 13',
        }
    }
    # 'expr'       : f'nLepton == 1 && mtw1 > 20 && PuppiMET_pt < 20 && nCleanJet > 0 && abs(CleanJet_eta[0]) < 2.5 && dRl1j1 > 1 && Alt(CleanJet_pt,0,0) > {jet_pt_threshold}',

    
    # # Top region
    # cuts[f'Top_loose_{jet_pt_threshold}'] = {
    #     'expr'    :f 'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && nCleanJet > 0 && bReq && abs(CleanJet_eta[0]) < 2.4 &&  Alt(CleanJet_pt,0,0) > {jet_pt_threshold}',
    #     'categories' : {
    #            'ele_jet_pt'  : 'abs(Lepton_pdgId[0]) == 11',
    #            'muon_jet_pt' : 'abs(Lepton_pdgId[0]) == 13',
    #     }
    # }

    ##########################
    # Tight leptons selections
    ##########################

    # QCD region
    cuts[f'QCD_tight_jet_pt_{jet_pt_threshold}'] = {
        'expr'    : f'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && drlj_{jet_pt_threshold} > 1 && LepWPCut1l',
        'categories' : {
            'ele'  : 'abs(Lepton_pdgId[0]) == 11',
            'muon' : 'abs(Lepton_pdgId[0]) == 13',
        }
    }
    # 'expr'    : f'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && Alt(CleanJet_pt,0,0) > {jet_pt_threshold} && abs(CleanJet_eta[0]) < 2.5 && dRl1j1 > 1 && LepWPCut1l',

    # Z-peak
    cuts[f'Zpeak_tight_jet_pt_{jet_pt_threshold}'] = {
        'expr'    : f'nLepton > 1 && PuppiMET_pt < 20 && mll > 60 && mll < 120 && LepWPCut1l',
        'categories' : {
            'ele'  : 'Lepton_pdgId[0]*Lepton_pdgId[1] == -121',
            'muon' : 'Lepton_pdgId[0]*Lepton_pdgId[1] == -169',
        }
    }
    # 'expr'    : f'nLepton > 1 && PuppiMET_pt < 20 && mll > 60 && mll < 120 && Alt(CleanJet_pt,0,0) > {jet_pt_threshold} && LepWPCut1l',

    # WJets region
    cuts[f'WJets_tight_jet_pt_{jet_pt_threshold}'] = {
        'expr'    : f'nLepton == 1 && mtw1 > 20 && PuppiMET_pt < 20 && drlj_{jet_pt_threshold} > 1 && LepWPCut1l',
        'categories' : {
            'ele'  : 'abs(Lepton_pdgId[0]) == 11',
            'muon' : 'abs(Lepton_pdgId[0]) == 13',
        }
    }
    # 'expr'    : f'nLepton == 1 && mtw1 > 20 && PuppiMET_pt < 20 && nCleanJet > 0 && abs(CleanJet_eta[0]) < 2.5 && dRl1j1 > 1 && Alt(CleanJet_pt,0,0) > {jet_pt_threshold} && LepWPCut1l',

    
    # # Top region
    # cuts[f'Top_tight_{jet_pt_threshold}'] = {
    #     'expr'    : f'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && nCleanJet > 0 && bReq && abs(CleanJet_eta[0]) < 2.4 && Alt(CleanJet_pt,0,0) > {jet_pt_threshold} && LepWPCut1l',
    #     'categories' : {
    #         'ele_jet_pt'  : 'abs(Lepton_pdgId[0]) == 11',
    #         'muon_jet_pt' : 'abs(Lepton_pdgId[0]) == 13',
    #     }
    # }

    
    
# ##########################
# # Loose leptons selections
# ##########################

# # QCD region
# cuts['QCDCR_loose'] = {
#     'expr'    : 'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && nCleanJet > 0 && abs(CleanJet_eta[0]) < 2.4 && dRl1j1 > 1',
#     'categories' : {
#         'ele_high_pt_0j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet',
#         'ele_high_pt_1j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',
#         'ele_high_pt_2j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'ele_low_pt_0j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet',
#         'ele_low_pt_1j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',
#         'ele_low_pt_2j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'muon_high_pt_0j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && zeroJet',
#         'muon_high_pt_1j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && oneJet',
#         'muon_high_pt_2j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && multiJet',
#         'muon_low_pt_0j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && zeroJet', 
#         'muon_low_pt_1j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && oneJet',  
#         'muon_low_pt_2j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && multiJet',
#     }
# }

# # Z-peak
# cuts['ZpeakCR_loose'] = {
#     'expr'    : 'nLepton > 1 && PuppiMET_pt < 20 && mll > 60 && mll < 120',
#     'categories' : {
#         'ele_high_pt_0j'  : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
#         'ele_high_pt_1j'  : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
#         'ele_high_pt_2j'  : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'ele_low_pt_0j'   : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
#         'ele_low_pt_1j'   : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
#         'ele_low_pt_2j'   : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'muon_high_pt_0j' : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && zeroJet', 
#         'muon_high_pt_1j' : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && oneJet',  
#         'muon_high_pt_2j' : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && multiJet',
#         'muon_low_pt_0j'  : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && zeroJet', 
#         'muon_low_pt_1j'  : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && oneJet',  
#         'muon_low_pt_2j'  : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && multiJet',
#     }
# }

# # # Top region
# # cuts['TopCR_loose'] = {
# #     'expr'    : 'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && nCleanJet > 0 && bReq && abs(CleanJet_eta[0]) < 2.4',
# #     'categories' : {
# #         'ele_high_pt_0j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
# #         'ele_high_pt_1j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
# #         'ele_high_pt_2j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
# #         'ele_low_pt_0j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
# #         'ele_low_pt_1j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
# #         'ele_low_pt_2j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
# #         'muon_high_pt_0j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && zeroJet', 
# #         'muon_high_pt_1j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && oneJet',  
# #         'muon_high_pt_2j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && multiJet',
# #         'muon_low_pt_0j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && zeroJet', 
# #         'muon_low_pt_1j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && oneJet',  
# #         'muon_low_pt_2j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && multiJet',
# #     }
# # }

# # WJets region
# cuts['WJetsCR_loose'] = {
#     'expr'    : 'nLepton == 1 && mtw1 > 20 && PuppiMET_pt < 20 && nCleanJet > 0 && abs(CleanJet_eta[0]) < 2.4 && dRl1j1 > 1',
#     'categories' : {
#         'ele_high_pt_0j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
#         'ele_high_pt_1j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
#         'ele_high_pt_2j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'ele_low_pt_0j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
#         'ele_low_pt_1j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
#         'ele_low_pt_2j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'muon_high_pt_0j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && zeroJet', 
#         'muon_high_pt_1j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && oneJet',  
#         'muon_high_pt_2j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && multiJet',
#         'muon_low_pt_0j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && zeroJet', 
#         'muon_low_pt_1j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && oneJet',  
#         'muon_low_pt_2j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && multiJet',
#     }
# }

# ##########################
# # Tight leptons selections
# ##########################

# # QCD region
# cuts['QCDCR_tight'] = {
#     'expr'    : 'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && nCleanJet > 0 && abs(CleanJet_eta[0]) < 2.4 && dRl1j1 > 1 && LepWPCut1l',
#     'categories' : {
#         'ele_high_pt_0j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet',
#         'ele_high_pt_1j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',
#         'ele_high_pt_2j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'ele_low_pt_0j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet',
#         'ele_low_pt_1j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',
#         'ele_low_pt_2j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'muon_high_pt_0j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && zeroJet',
#         'muon_high_pt_1j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && oneJet',
#         'muon_high_pt_2j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && multiJet',
#         'muon_low_pt_0j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && zeroJet', 
#         'muon_low_pt_1j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && oneJet',  
#         'muon_low_pt_2j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && multiJet',
#     }
# }

# # Z-peak
# cuts['ZpeakCR_tight'] = {
#     'expr'    : 'nLepton > 1 && PuppiMET_pt < 20 && mll > 60 && mll < 120 && LepWPCut2l',
#     'categories' : {
#         'ele_high_pt_0j'  : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
#         'ele_high_pt_1j'  : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
#         'ele_high_pt_2j'  : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'ele_low_pt_0j'   : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
#         'ele_low_pt_1j'   : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
#         'ele_low_pt_2j'   : 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'muon_high_pt_0j' : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && zeroJet', 
#         'muon_high_pt_1j' : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && oneJet',  
#         'muon_high_pt_2j' : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && multiJet',
#         'muon_low_pt_0j'  : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && zeroJet', 
#         'muon_low_pt_1j'  : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && oneJet',  
#         'muon_low_pt_2j'  : 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && multiJet',
#     }
# }

# # # Top region
# # cuts['TopCR_tight'] = {
# #     'expr'    : 'nLepton == 1 && mtw1 < 20 && PuppiMET_pt < 20 && nCleanJet > 0 && bReq && abs(CleanJet_eta[0]) < 2.4 && LepWPCut1l',
# #     'categories' : {
# #         'ele_high_pt_0j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
# #         'ele_high_pt_1j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
# #         'ele_high_pt_2j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
# #         'ele_low_pt_0j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
# #         'ele_low_pt_1j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
# #         'ele_low_pt_2j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
# #         'muon_high_pt_0j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && zeroJet', 
# #         'muon_high_pt_1j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && oneJet',  
# #         'muon_high_pt_2j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && multiJet',
# #         'muon_low_pt_0j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && zeroJet', 
# #         'muon_low_pt_1j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && oneJet',  
# #         'muon_low_pt_2j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && multiJet',
# #     }
# # }

# # WJets region
# cuts['WJetsCR_tight'] = {
#     'expr'    : 'nLepton == 1 && mtw1 > 20 && PuppiMET_pt < 20 && nCleanJet > 0 && abs(CleanJet_eta[0]) < 2.4 && dRl1j1 > 1 && LepWPCut1l',
#     'categories' : {
#         'ele_high_pt_0j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
#         'ele_high_pt_1j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
#         'ele_high_pt_2j'  : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] > 25  && HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'ele_low_pt_0j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && zeroJet', 
#         'ele_low_pt_1j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && oneJet',  
#         'ele_low_pt_2j'   : 'abs(Lepton_pdgId[0]) == 11 && Lepton_pt[0] <= 25 && HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30 > 0.5 && multiJet',
#         'muon_high_pt_0j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && zeroJet', 
#         'muon_high_pt_1j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && oneJet',  
#         'muon_high_pt_2j' : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] > 20  && HLT_Mu17_TrkIsoVVL > 0.5 && multiJet',
#         'muon_low_pt_0j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && zeroJet', 
#         'muon_low_pt_1j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && oneJet',  
#         'muon_low_pt_2j'  : 'abs(Lepton_pdgId[0]) == 13 && Lepton_pt[0] <= 20 && HLT_Mu8_TrkIsoVVL  > 0.5 && multiJet',
#     }
# }
