# cuts

cuts = {}
preselections = '   nLepton == 2 \
            && Lepton_pt[0]>35. \
            && Lepton_pt[1]>20. \
            && mll >76. && mll <106. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && njet >= 2  \
            && mjj > 500 \
            '
        
#preselections = '   nLepton == 2 \
#            && Lepton_pt[0]>35. \
#            && Lepton_pt[1]>20. \
#            && mll >76. && mll <106. \
#            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
#            && nCleanJetNotFat >= 2  \
#            && mjj_max > 500 && detajj_mjjmax > 2.5 \
#            && vbs_category==0 \
#            '


#######################################
#
#   BOOSTED CATEGORY
#   vbs_category = 0 (at least one FJ)
#######################################

cuts['test'] =  'bVeto &&  (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

#cuts['Boosted_topcr']  = 'nCleanFatJet==1 && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'
#
#cuts['Boosted_DYcr_bVeto']  = 'bVeto && nCleanFatJet==1 && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'
#
#cuts['Boosted_DYcr_bTag']  = 'bReq && nCleanFatJet==1 && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'
#
#cuts['Boosted_SR_bVeto']  = 'bVeto && nCleanFatJet==1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Vjet_mass > 65 && Vjet_mass <105'
#
#cuts['Boosted_SR_bTag']  = 'bReq && nCleanFatJet==1 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Vjet_mass > 65 && Vjet_mass <105'


###check if they need it on the form cuts{expr: , categories: ...} like follows
#cuts['hww2l2v_13TeV_WH_SS_noZveto_mm_2j'] = {
#    'expr' : '(Lepton_pdgId[0]*Lepton_pdgId[1] == 13*13) && nLepton==2 && Alt(CleanJet_pt,0,0)>30 && Alt(CleanJet_pt,1,0)>30 && mjj < 100 && mlljj20_whss > 50.',
#    'categories' : {
#        # Sub-leading lepton pT >= 20 GeV
#        'plus_pt2ge20'  : 'Lepton_pdgId[0] == -13 && Lepton_pdgId[1] == -13 && Lepton_pt[1]>=20 && abs(Lepton_eta[0] - Lepton_eta[1])<2.0',
#        'minus_pt2ge20' : 'Lepton_pdgId[0] == +13 && Lepton_pdgId[1] == +13 && Lepton_pt[1]>=20 && abs(Lepton_eta[0] - Lepton_eta[1])<2.0',
#        # Sub-leading lepton pT < 20 GeV
#        'plus_pt2lt20'  : 'Lepton_pdgId[0] == -13 && Lepton_pdgId[1] == -13 && Lepton_pt[1]<20 && abs(Lepton_eta[0] - Lepton_eta[1])<2.0',
#        'minus_pt2lt20' : 'Lepton_pdgId[0] == +13 && Lepton_pdgId[1] == +13 && Lepton_pt[1]<20 && abs(Lepton_eta[0] - Lepton_eta[1])<2.0',
#        # Same-sign CR for fakes: delta-eta(ll) >= 2.0 (Sub-leading lepton pT >= 20 GeV)
#        'SS_CR_plus_pt2ge20'  : 'Lepton_pdgId[0] == -13 && Lepton_pdgId[1] == -13 && Lepton_pt[1]>=20 && abs(Lepton_eta[0] - Lepton_eta[1])>=2.0',
#        'SS_CR_minus_pt2ge20' : 'Lepton_pdgId[0] == +13 && Lepton_pdgId[1] == +13 && Lepton_pt[1]>=20 && abs(Lepton_eta[0] - Lepton_eta[1])>=2.0',
#        # Same-sign CR for fakes: delta-eta(ll) >= 2.0 (Sub-leading lepton pT < 20 GeV)
#        'SS_CR_plus_pt2lt20'  : 'Lepton_pdgId[0] == -13 && Lepton_pdgId[1] == -13 && Lepton_pt[1]<20 && abs(Lepton_eta[0] - Lepton_eta[1])>=2.0',
#        'SS_CR_minus_pt2lt20' : 'Lepton_pdgId[0] == +13 && Lepton_pdgId[1] == +13 && Lepton_pt[1]<20 && abs(Lepton_eta[0] - Lepton_eta[1])>=2.0',
#    }
#}
