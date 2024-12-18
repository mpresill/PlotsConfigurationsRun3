import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations)

aliases = {}
aliases = OrderedDict()

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

######### WP for 2018
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'


aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched, 0, 0) * Alt(Lepton_promptgenmatched, 1, 0)',
#    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

##additional variables for VgS
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

###########################################################
################fakes
###########################################################
# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}





############################################################
############# VBS variables for jet pairing
############################################################
#mva_reader_path = '%s/Configurations/VBS_ZV/mva_macros/' % configurations
#models_path = '%s/Configurations/VBS_ZV/Models/All_years_nobtag' % configurations
##models_path = '/eos/user/m/mpresill/www/VBS/Numpy/Alex/'
#models_path_pruned = '%s/Configurations/VBS_ZV/Models/pruned_nobtag' % configurations
#
#aliases['vbs_category'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations 
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('vbs_category','2018',models_path,models_path_pruned, False)
#}
#
#aliases['vbs_jet_0'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('vbs_jet_0','2018', models_path,models_path_pruned, False)
#}
#
#aliases['vbs_jet_1'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('vbs_jet_1','2018', models_path,models_path_pruned, False)
#}
#
#aliases['v_jet_0'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('v_jet_0','2018', models_path,models_path_pruned, False)
#}
#
#aliases['v_jet_1'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('v_jet_1','2018', models_path,models_path_pruned, False)
#}
#
#
#aliases['mjj_max'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('mjj_max','2018', models_path,models_path_pruned, False)
#}
#
#aliases['detajj_mjjmax'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#	],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('detajj_mjjmax','2018', models_path,models_path_pruned, False)
#}
#
#aliases['dphijj_mjjmax'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('dphijj_mjjmax','2018', models_path,models_path_pruned, False)
#}
#
#aliases['Vjet_mass'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#	'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('Vjet_mass','2018', models_path,models_path_pruned, False)
#}
#
#aliases['njet30'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#        'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('njet30','2018', models_path, models_path_pruned,False)
#}
#
#aliases['nbtag'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#        'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('nbtag','2018', models_path,models_path_pruned, False)
#}
#
#aliases['Zleppt'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#        'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('Zleppt','2018', models_path,models_path_pruned, False)
#}
#
#aliases['Vpt'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#        'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('Vpt','2018', models_path,models_path_pruned, False)
#}
# 
#aliases['V_jet_mass'] = {
#    'expr': 'Vjet_mass'
#}
#
### new variable for EFT:
#aliases['mZV'] = {
#    'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#        'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_dnn_FJ',
#    'args': ('mZV','2018', models_path,models_path_pruned, False)
#}



############################################################
############################################################

## PostProcessing did not create (anti)topGenPt for ST samples with _ext1
#lastcopy = (1 << 13)
#
#aliases['isTTbar'] = {
#    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
#    'samples': ['top']
#}
#
#aliases['isSingleTop'] = {
#    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
#    'samples': ['top']
#}
##added 20.11
#aliases['topGenPtOTF'] = {
#    'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#    'samples': ['top']
#}
##added 20.11
#aliases['antitopGenPtOTF'] = {
#    'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#    'samples': ['top']
#}
#
#
#aliases['Top_pTrw'] = {
#	    # New Top PAG added 20.11
#    'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPtOTF - 8.90557e-08*topGenPtOTF*topGenPtOTF) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPtOTF - 8.90557e-08*antitopGenPtOTF*antitopGenPtOTF))) + (topGenPtOTF * antitopGenPtOTF <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5
# #'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + isSingleTop',
#    'samples': ['top']
#}



# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

############################################################
############ b tag (DeepCSV)
############################################################
# B tagging 2018:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X 
#loose 0.1241
#tight 0.7527
#
#aliases['bVeto'] = {
#    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0)'
#}
#
#aliases['bReq'] = {
#    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 1)'
#}
#
#aliases['bReqTight'] = {
#    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.7527) >= 1)'
#}
#
#aliases['bVetoSF'] = {
#    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
#    'samples': mc
#}
#
#aliases['bReqSF'] = {
#    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
#    'samples': mc
#}
#
#aliases['btagSF'] = {
#    'expr': 'bVeto*bVetoSF + bReq *bReqSF',
#    'samples': mc
#}
#
#
#
#for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
#
#    for targ in ['bVeto', 'bReq']:
#        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)
#
#        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)
#
#    aliases['btagSF%sup' % shift] = {
#        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
#        'samples': mc
#    }
#
#    aliases['btagSF%sdown' % shift] = {
#        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
#        'samples': mc
#    }
#
##########################################################################################
###### DY pt reweigthing: what is the source of this correctin? EW/QCD NLO? not sure
##########################################################################################
#
#aliases['nCleanGenJet'] = {
#    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' % os.getenv('CMSSW_BASE')],
#    'class': 'CountGenJet',
#    'samples': mc
#}

##### DY Z pT reweighting: Ref: https://indico.cern.ch/event/904982/contributions/3970035/attachments/2084859/3502366/Latino_20.08.05.pdf 
#aliases['getGenZpt_OTF'] = {
#    'linesToAdd':['.L %s/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+' % os.getenv('CMSSW_BASE')],
#    'class': 'getGenZpt',
#    'samples': ['DY']
#}
#handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew30.py' % os.getenv('CMSSW_BASE'),'r')
#exec(handle)
#handle.close()
#aliases['DY_NLO_pTllrw'] = {
#    'expr': '('+DYrew['2018']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
#    'samples': ['DY']
#}
#aliases['DY_LO_pTllrw'] = {
#    'expr': '('+DYrew['2018']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
#    'samples': ['DY']
#}


###########################################################################################
# PU jet Id SF
###########################################################################################
aliases['Jet_PUIDSF'] = { 
          'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose)))',
          'samples': mc
          }
aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_up)))',
  'samples': mc
}
aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_down)))',
  'samples': mc
}
# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut','Jet_PUIDSF', 'btagSF' ]),
    'samples': mc
}
# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}

##unmorphed bVeto and bReq DNN
##DNN full and pruned with morphed qgl
#morphing_file = configurations + '/Configurations/VBS_ZV/qgl_18/Remorphing/morphing_functions_comb.root'
#do_morph = "11111111"
#m_gluon_loweta_pt0 = "_loweta_pt0_gluon"
#m_gluon_loweta_pt1 = "_loweta_pt1_gluon"
#m_gluon_higheta_pt0 = "_higheta_pt0_gluon"
#m_gluon_higheta_pt1 = "_higheta_pt1_gluon"
#m_quark_loweta_pt0 = "_loweta_pt0_quark"
#m_quark_loweta_pt1 = "_loweta_pt1_quark"
#m_quark_higheta_pt0 = "_higheta_pt0_quark"
#m_quark_higheta_pt1 = "_higheta_pt1_quark"
#
#models_path_pruned_bVeto = '%s/Configurations/VBS_ZV/Models/Sep22/2018_bVeto_pruned' % configurations
#models_path_pruned_bReq = '%s/Configurations/VBS_ZV/Models/Sep22/2018_bReq_pruned' % configurations
#
#aliases['DNNoutput_pruned_bVeto'] = {
#     'linesToAdd': [
#        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
#        'gSystem->Load("libDNNEvaluator.so")',
#        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_morphed_FJ.cc+' % configurations
#    ],
#    'class': 'jets_cat_qgl_FJ',
#    'args': ('dnn_output_pruned_bVeto','2018', models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#
#aliases['DNNoutput_pruned_bReq'] = {
#    'class': 'jets_cat_qgl_FJ',
#    'args': ('dnn_output_pruned_bReq','2018', models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#
#
#
################
#aliases['vbs_0_qglmorphed_res'] = {
#   'class': 'jets_cat_qgl_FJ',
#    'args': ('vbs_0_qglmorphed_res','2018',models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#aliases['vbs_1_qglmorphed_res'] =  {
#'class': 'jets_cat_qgl_FJ',
#    'args': ('vbs_1_qglmorphed_res','2018',models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#
#aliases['vjet_0_qglmorphed_res'] = {
#'class': 'jets_cat_qgl_FJ',
#    'args': ('vjet_0_qglmorphed_res','2018',models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#aliases['vjet_1_qglmorphed_res'] = {
#'class': 'jets_cat_qgl_FJ',
#    'args': ('vjet_1_qglmorphed_res','2018',models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#
#aliases['vbs_0_qgl_res'] =  {
#'class': 'jets_cat_qgl_FJ',
#    'args': ('vbs_0_qgl_res','2018',models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#
#aliases['vbs_1_qgl_res'] =  {
#'class': 'jets_cat_qgl_FJ',
#    'args': ('vbs_1_qgl_res','2018',models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#
#aliases['vjet_0_qgl_res'] = {
#'class': 'jets_cat_qgl_FJ',
#    'args': ('vjet_0_qgl_res','2018',models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#aliases['vjet_1_qgl_res'] = {
#'class': 'jets_cat_qgl_FJ',
#    'args': ('vjet_1_qgl_res','2018',models_path_pruned_bVeto, models_path_pruned_bReq,False,morphing_file, do_morph, m_gluon_loweta_pt0, m_gluon_loweta_pt1, m_gluon_higheta_pt0, m_gluon_higheta_pt1,m_quark_loweta_pt0, m_quark_loweta_pt1, m_quark_higheta_pt0, m_quark_higheta_pt1)
#}
#
############################################
####   new DY 2D fitting Nov 2021
############################################
#aliases['bin1_R'] = {
#    'expr': 'Zleppt <= 75 && CleanJet_pt[vbs_jet_1] <=40'
#}
#aliases['bin2_R'] = {
#    'expr': 'Zleppt <= 75 && CleanJet_pt[vbs_jet_1] > 40  && CleanJet_pt[vbs_jet_1] <=70'
#}
#aliases['bin3_R'] = {
#    'expr': 'Zleppt <= 75 && CleanJet_pt[vbs_jet_1] > 70  && CleanJet_pt[vbs_jet_1] <=150'
#}
#aliases['bin4_R'] = {
#    'expr': 'Zleppt > 75 && Zleppt <=130 && CleanJet_pt[vbs_jet_1] <= 70'
#}
#aliases['bin5_R'] = {
#    'expr': 'Zleppt > 75 && Zleppt <=130 && CleanJet_pt[vbs_jet_1] > 70  && CleanJet_pt[vbs_jet_1] <=150'
#}
#
#aliases['bin6_R'] = {
#    'expr': 'Zleppt > 130 && Zleppt <=230 && CleanJet_pt[vbs_jet_1] <= 70'
#}
#aliases['bin7_R'] = {
#    'expr': 'Zleppt > 130 && Zleppt <=230 && CleanJet_pt[vbs_jet_1] > 70  && CleanJet_pt[vbs_jet_1] <=150'
#}
#aliases['bin8_R'] = {
#    'expr': 'Zleppt <=230 && CleanJet_pt[vbs_jet_1] > 150  && CleanJet_pt[vbs_jet_1] <= 250'
#}
#aliases['bin9_R'] = {
#    'expr': 'Zleppt >230 && Zleppt <=450 && CleanJet_pt[vbs_jet_1] < 150 '
#}
#aliases['bin10_R'] = {
#    'expr': 'Zleppt >450'
#}
#aliases['bin11_R'] = {
#    'expr': ' CleanJet_pt[vbs_jet_1] >250 && Zleppt <=450'
#}
#aliases['bin12_R'] = {
#    'expr': 'Zleppt >230 && Zleppt <=450 && CleanJet_pt[vbs_jet_1] >150 && CleanJet_pt[vbs_jet_1] <= 250'
#}
#
#aliases['fit_2D_bin_Resolved'] = {
#    'expr': '(vbs_category==1)*( \
#            1*(  bin1_R ) +\
#            2*(  bin2_R ) +\
#            3*(  bin3_R ) +\
#            4*(  bin4_R ) +\
#            5*(  bin5_R ) +\
#            6*(  bin6_R ) +\
#            7*(  bin7_R ) + (8)*(  bin8_R ) + 9*(  bin9_R ) + 10*( bin10_R  ) + 11*( bin11_R  ) + 12*( bin12_R  )) + (vbs_category==0)*(-1)'
#}
#
#aliases['fit_Z_bin_Boosted'] = {
#        'expr' : '(vbs_category == 0)*(\
#                 1*(Zleppt > 0 && Zleppt <=75     )+\
#                 2*(Zleppt > 75 && Zleppt <=150   )+\
#                 3*(Zleppt > 150 && Zleppt <=250  )+\
#                 4*(Zleppt > 250 && Zleppt <=400  )+\
#                 5*(Zleppt > 400                  )\
#                 ) + (vbs_category == 1) * (-1)' ,
#}
#
#
#
