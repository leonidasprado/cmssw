# -*- coding: utf-8 -*-

import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing("python")
options.setDefault("inputFiles", "root://xrootd-cms.infn.it//store/mc/RunIIFall17MiniAOD/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/00000/3C91F22D-C30A-E811-AC84-02163E019C27.root")
options.setDefault("outputFile", "output.root")
options.setDefault("maxEvents", 10)
options.parseArguments()

process = cms.Process("TEST")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.deterministicSeeds = cms.EDProducer("DeterministicSeedProducer",
    produceCollections = cms.bool(True),
    produceValueMaps   = cms.bool(True),
    electronCollection = cms.InputTag("slimmedElectrons"),
    electronSeedFactor = cms.int32(1),
    muonCollection     = cms.InputTag("slimmedMuons"),
    muonSeedFactor     = cms.int32(1),
    tauCollection      = cms.InputTag("slimmedTaus"),
    tauSeedFactor      = cms.int32(1),
    photonCollection   = cms.InputTag("slimmedPhotons"),
    photonSeedFactor   = cms.int32(1),
    jetCollection      = cms.InputTag("slimmedJets"),
    jetSeedFactor      = cms.int32(1),
    METCollection      = cms.InputTag("slimmedMETs"),
    METSeedFactor      = cms.int32(1),
    seedUserInt        = cms.string("deterministicSeed"),
    debug              = cms.untracked.bool(True)
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outputFile)
)

process.p = cms.Path(process.deterministicSeeds)
process.e = cms.EndPath(process.out)

