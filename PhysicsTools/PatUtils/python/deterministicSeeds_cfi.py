# -*- coding: utf-8 -*-

import FWCore.ParameterSet.Config as cms


# empty input collections mean that no seeds are produced for that objects

deterministicSeeds = cms.EDProducer("DeterministicSeedProducer",
    produceCollections = cms.bool(True),
    produceValueMaps   = cms.bool(False),
    electronCollection = cms.InputTag(""),
    electronSeedFactor = cms.int32(1),
    muonCollection     = cms.InputTag(""),
    muonSeedFactor     = cms.int32(1),
    tauCollection      = cms.InputTag(""),
    tauSeedFactor      = cms.int32(1),
    photonCollection   = cms.InputTag(""),
    photonSeedFactor   = cms.int32(1),
    jetCollection      = cms.InputTag(""),
    jetSeedFactor      = cms.int32(1),
    METCollection      = cms.InputTag(""),
    METSeedFactor      = cms.int32(1),
    seedUserInt        = cms.string("deterministicSeed"),
    debug              = cms.untracked.bool(False)
)

