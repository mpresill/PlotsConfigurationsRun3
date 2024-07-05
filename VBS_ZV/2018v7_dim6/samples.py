# flake8: noqa E266
import os,glob
#redirector = "root://eoscms.cern.ch//"
#redirector = "root://cms-xrd-global.cern.ch//"
#redirector = ""

################################################
################# SKIMS ########################
################################################ 
mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
dataReco = 'Run2018_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'
fakeReco = 'Run2018_102X_nAODv7_Full2018v7'
fakeSteps = 'DATAl1loose2018v7__l2loose__fakeW'
dataSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7'


##############################################
###### Tree base directory for the site ######
##############################################

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
DirectorySMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

limitFiles  = -1

def makeMCDirectory(var=''):
    return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory   = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

samples = {}

from mkShapesRDF.lib.search_files import SearchFiles
s = SearchFiles()

useXROOTD = True
redirector = 'root://eoscms.cern.ch/'

def nanoGetSampleFiles(path, name):
    _files = s.searchFiles(path, name, redirector=redirector)
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return [(name, _files)]

def CombineBaseW(samples, proc, samplelist):
    _filtFiles = list(filter(lambda k: k[0] in samplelist, samples[proc]['name']))
    _files = list(map(lambda k: k[1], _filtFiles))
    _l = list(map(lambda k: len(k), _files))
    leastFiles = _files[_l.index(min(_l))]
    dfSmall = ROOT.RDataFrame('Runs', leastFiles)
    s = dfSmall.Sum('genEventSumw').GetValue()
    f = ROOT.TFile.Open(leastFiles[0])
    t = f.Get('Events')
    t.GetEntry(1)
    xs = t.baseW * s

    __files = []
    for f in _files:
        __files += f
    df = ROOT.RDataFrame('Runs', __files)
    s = df.Sum('genEventSumw').GetValue()
    newbaseW = str(xs / s)
    weight = newbaseW + '/baseW'

    for iSample in samplelist:
        addSampleWeight(samples, proc, iSample, weight)

def addSampleWeight(samples, sampleName, sampleNameType, weight):
    obj = list(filter(lambda k: k[0] == sampleNameType, samples[sampleName]['name']))[0]
    samples[sampleName]['name'] = list(filter(lambda k: k[0] != sampleNameType, samples[sampleName]['name']))
    if len(obj) > 2:
        samples[sampleName]['name'].append((obj[0], obj[1], obj[2] + '*(' + weight + ')'))
    else:
        samples[sampleName]['name'].append((obj[0], obj[1], '(' + weight + ')' ))



################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
           }

#########################################
############ MC COMMON ##################
#########################################
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'



#######################################
#############  SIGNALS  ###############
#######################################
#######       EFT weights       #######
### cW
sm = '( LHEReweightingWeight[0] )'
quadReweight_cW = '( 0.5* (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0]))'
LinReweight_cW = '( 0.5* (1/(0.2)) * ( LHEReweightingWeight[2] - LHEReweightingWeight[1] ))'
LinQuadReweight_cW = '(' + quadReweight_cW + '+' + LinReweight_cW + ')'
smLinQuadReweight_cW = '(' + sm + '+' + quadReweight_cW + '+' + LinReweight_cW + ')'
 #************ EFT samples ************#
  #*******************#      sm from reweighting
samples['sm'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
} 
addSampleWeight(samples,'sm','ZTo2E_ZTo2J_SMEFT',                                              sm)
addSampleWeight(samples,'sm','ZTo2Mu_ZTo2J_SMEFT',                                             sm)
addSampleWeight(samples,'sm','ZTo2Tau_ZTo2J_SMEFT',                                            sm)
addSampleWeight(samples,'sm','WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm)
addSampleWeight(samples,'sm','WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm)
 #*******************#      sm+linear+quadratic
samples['sm_lin_quad_cW'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
} 
addSampleWeight(samples,'sm_lin_quad_cW','ZTo2E_ZTo2J_SMEFT',                                              smLinQuadReweight_cW)
addSampleWeight(samples,'sm_lin_quad_cW','ZTo2Mu_ZTo2J_SMEFT',                                             smLinQuadReweight_cW)
addSampleWeight(samples,'sm_lin_quad_cW','ZTo2Tau_ZTo2J_SMEFT',                                            smLinQuadReweight_cW)
addSampleWeight(samples,'sm_lin_quad_cW','WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cW)
addSampleWeight(samples,'sm_lin_quad_cW','WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cW)
 #*******************#      quadratic only
samples['quad_cW'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
} 
addSampleWeight(samples,'quad_cW','ZTo2E_ZTo2J_SMEFT',                                              quadReweight_cW)
addSampleWeight(samples,'quad_cW','ZTo2Mu_ZTo2J_SMEFT',                                             quadReweight_cW)
addSampleWeight(samples,'quad_cW','ZTo2Tau_ZTo2J_SMEFT',                                            quadReweight_cW)
addSampleWeight(samples,'quad_cW','WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cW)
addSampleWeight(samples,'quad_cW','WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cW)
 #**********************************************************************************#      
