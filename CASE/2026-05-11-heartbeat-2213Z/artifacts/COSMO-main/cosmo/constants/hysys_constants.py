"""

HYSYS V14 enum list

Extracted from C:\Program Files\AspenTech\Aspen HYSYS V14.0\hysys.tlb

"""


class EmptyValue:
    HEmpty = -32767
    HHidden = -32768


class HColourID:
    hcidRedColour = 0
    hcidGreenColour = 1
    hcidBlueColour = 2
    hcidPurpleColour = 3
    hcidCyanColour = 4
    hcidGreyColour = 5
    hcidBlackColour = 6
    hcidYellowColour = 7
    hcidWhiteColour = 8


class VariableStatus:
    vsCalculated = 0
    vsSpecified = 1
    vsDefaultedValue = 2
    vsSpecifiedOutside = 4
    vsDefaultOutside = 5


class UnitConversionType:
    uctPhase = 0
    uctTemperature = 1
    uctPressure = 2
    uctMolarFlow = 3
    uctMassFlow = 4
    uctVolumeFlow = 5
    uctEnthalpy = 6
    uctDensity = 7
    uctHeatCapacity = 8
    uctEntropy = 9
    uctThermalConductivity = 10
    uctViscosity = 11
    uctSurfaceTension = 12
    uctSpecificGravity = 13
    uctSpecificGravityAir = 14
    uctHeatCapacityMass = 15
    uctMassDensity = 16
    uctUA = 17
    uctSmallVolumeFlow = 18
    uctStdGasFlow = 19
    uctAuctGasFlow = 20
    uctMolarEnthalpy = 21
    uctLength = 22
    uctSmallLength = 23
    uctDeltaTemperature = 24
    uctMolarVolume = 25
    uctHeatCoefficient = 26
    uctLargeEnthalpy = 27
    uctStdDensity = 28
    uctMassEntropy = 29
    uctMassEnthalpy = 30
    uctIdealHTerm_A = 31
    uctIdealHTerm_B = 32
    uctIdealHTerm_C = 33
    uctIdealHTerm_D = 34
    uctIdealHTerm_E = 35
    uctIdealHTerm_F = 36
    uctGibbsTerm_A = 37
    uctGibbsTerm_B = 38
    uctGibbsTerm_C = 39
    uctKinematicViscosity = 40
    uctArea = 41
    uctVolume = 42
    uctVelocity = 43
    uctTime = 44
    uctDeltaPressure = 45
    uctHeatFlux = 46
    uctFouling = 47
    uctCakeLoading = 48
    uctPermeability = 49
    uctMassVelocity = 50
    uctMass = 51
    uctRVS = 52
    uctAreaPerVolume = 53
    uctPressurePerLength = 54
    uctVolumeFlowPerLength = 55
    uctVolumeFlowPerArea = 56
    uctMoles = 57
    uctReactionRate = 58
    uctValveCvMolar = 59
    uctValveCvMass = 60
    uctValveCvVolume = 61
    uctStdVolumeFlow = 62
    uctFrequency = 63
    uctPercent = 64
    uctUnitless = 65
    uctWork = 66
    uctComponentFlow = 67
    uctMassComponentFlow = 68
    uctVolumeComponentFlow = 69
    uctActualVolumeFlow = 70
    uctLowerHeatingValue = 71
    uctMassLowerHeatingValue = 72
    uctHeatOfVapourization = 73
    uctMassHeatOfVapourization = 74
    uctEenthalpyPerLength = 75
    uctBWR_A = 76
    uctBWR_A0 = 77
    uctBWR_B = 78
    uctBWR_B0 = 79
    uctBWR_C = 80
    uctBWR_C0 = 81
    uctBWR_Alpha = 82
    uctPowerPerFlow = 83
    uctPower = 84
    uctMolesPerMass = 85
    uctPerVolume = 86
    uctPerMassVolume = 87
    uctGasOilRatio = 88
    uctOilVolume = 89
    uctSpecificVolume = 90
    uctCompressibility = 91
    uctVolumetricEnthalpyFlow = 92
    uctMassTransferCoefficient = 93
    uctDiffusivity = 94
    uctMassReactionRate = 95
    uctMolarReactionYield = 96
    uctMassReactionYield = 97
    uctMassEnthalpyFlow = 98
    uctHCost = 99
    uctHCostPerTime = 100
    uctHCostPerEnergy = 101
    uctCvDyn = 102
    uctKturbDyn = 103
    uctKlamDyn = 104
    uctSurgeADyn = 105
    uctSurgeBDyn = 106
    uctQopenRate = 107
    uctRotatInertia = 108
    uctFlossFactor = 109
    uctSmallArea = 110
    uctForce = 111
    uctActLiqDensity = 112
    uctElecFlow = 113
    uctEmissions = 114
    uctEnergy = 115
    uctElectricFOE = 116
    uctFOEFactor = 117
    uctFOEFlow = 118
    uctLeadLevel = 119
    uctPerFOE = 120
    uctPerMass = 121
    uctPerMole = 122
    uctPerTime = 123
    uctPerVapVol = 124
    uctSteamRatio = 125
    uctVapVol = 126
    uctVolRatio = 127
    uctVolSpecEner = 128
    uctVolConc = 129
    uctMassConc = 130
    uctMolConc = 131
    uctConcentration = 132
    uctPPMVol = 133
    uctPPMMass = 134
    uctPPMMoles = 135
    uctDeactivtionRate = 136
    uctAcidity = 137
    uctElecPotential = 138
    uctElecConductivity = 139
    uctMolarElecCond = 140
    uctMassMass = 141
    uctVolVol = 142
    uctMolMol = 143
    uctCostPerFOE = 144
    uctCostPerMass = 145
    uctCostPerMole = 146
    uctCostPerVolume = 147
    uctAPIFireEeqnCorr = 148
    uctRadiusGY = 149
    uctDipMoment = 150
    uctDistGasPI = 151
    uctDistLiqPI = 152
    uctGasPI = 153
    uctGasRateCIP = 154
    uctJonesGasA = 155
    uctJonesGasB = 156
    uctJonesLiqA = 157
    uctJonesLiqB = 158
    uctLiqPI = 159
    uctLiqRateRecip = 160
    uctPermeabilityRes = 161
    uctShots = 162
    uctAngle = 163
    uctStdGasDen = 164
    uctFluidPotential = 165
    uctTorque = 166
    uctSURGECDYN = 167
    uctSURGEDDYN = 168
    uctFLOWTOTEMPLINK = 169
    uctTEMPTOFLOWLINK = 170
    uctPERLENGTH = 171
    uctMASSEMISSIONS = 172
    uctWATERCONTENT = 173
    uctFFactor = 174
    uctFs = 175
    uctPerArea = 176
    uctHead = 177
    uctmmLength = 178
    uctSMDELTAP = 179
    uctSMPRESSPERLENGTH = 180
    uctFormationVolumeFactor = 181
    uctDeltaDensity = 182
    uctSmallVelocity = 183
    uctDesignPressure = 184
    uctMechanicalStress = 185
    uctCurrentDensity = 186
    uctElectricalResistance = 187
    uctElectricalResistivity = 188
    uctPowerDensity = 189
    uctElectricFieldStrength = 190
    uctFaradayConstant = 191
    uctAmperage = 192
    uctNullUnit = -1


class UserVarType:
    uvtReal = 1
    uvtText = 3


class StatusLevel:
    slOK = 0
    slMissingOptionalInformation = 1
    slWarning = 2
    slMissingRequiredInformation = 3
    slError = 4


class DataTableAccessMode:
    dtam_NoTransfer = 0
    dtam_Read = 1
    dtam_Write = 2
    dtam_ReadWrite = 3


class HDirectionType:
    hdteHorizontal = 0
    hdteVertical = 1


class HAxisType:
    hatXAxis = 0
    hatYAxis = 1


class HTickType:
    httEvenTick = 0
    httOddTick = 1
    httMinorTick = 2


class HATAlignment:
    hataAlignNW = 0
    hataAlignN = 1
    hataAlignNE = 2
    hataAlignE = 3
    hataAlignSE = 4
    hataAlignS = 5
    hataAlignSW = 6
    hataAlignW = 7
    hataAlignC = 8
    hataAlignBC = 9
    hataAlignBW = 10
    hataAlignBE = 11


class HRTRotation:
    hrtRotate0 = 0
    hrtRotate90 = 1
    hrtRotate180 = 2
    hrtRotate270 = 3


class HLineStypes:
    hlsLineSolid = 0
    hlsLineDotted = 1
    hlsLineDashed = 2
    hlsLineDotdash = 3
    hlsLineFrame = 4
    hlsFinalLineStyle = 5


class HPointSymbols:
    hpsSquare = 0
    hpsDiamond = 1
    hpsCross = 2
    hpsHexagon = 3
    hpsCross2 = 4
    hpsTriangle = 5
    hpsTriangleDown = 6
    hpsSolidSquare = 100
    hpsSolidDiamond = 101
    hpsSolidHexagon = 102
    hpsSolidTriangle = 103
    hpsSolidTriangleDown = 104
    hpsNoSymbol = 1000


class HPlotType:
    hptTwoDimensionalPlot = 0
    hptThreeDimensionalPlot = 1
    hptEquilateralTrianglePlot = 2
    hptNoPlotDefined = 999


class HPlottableType:
    hptUndetermined = 0
    hptXAxis = 1
    hptYAxis = 2
    hptZAxis = 4
    hptDataPlotArea = 8
    hptLegend = 16
    hptTitle = 32


class HMouseEvent:
    hmouseNoMouseEvent = 0
    hmouseMouseMove = 1
    hmouseButtonDownL = 2
    hmouseButtonUpL = 4
    hmouseButtonDblClkL = 8
    hmouseMouseEnter = 16
    hmouseMouseLeave = 32


class HKeyEvent:
    hkeyNoKeyEvent = 0
    hkeyChar = 1


class CommandProtectionType:
    cptAllAccess = 0
    cptWarnAccess = 1
    cptDenyAccess = 2


class ComponentClass:
    cc_Inorganic = 100
    cc_Inorganic_Gas = 110
    cc_Sulphur_Component = 120
    cc_Salt = 130
    cc_Hydrocarbon = 200
    cc_Alkane = 210
    cc_Alkene = 220
    cc_Alkyne = 230
    cc_Cyclo_Alkane = 240
    cc_Cyclo_Alkene = 250
    cc_Cyclo_Alkyne = 260
    cc_Aromatic = 270
    cc_Poly_Aromatic = 280
    cc_Organic_Inorganic = 300
    cc_Mercaptan = 310
    cc_Organic = 400
    cc_Alcohol = 410
    cc_Aliphatic_Alcohol = 411
    cc_Aromatic_Alcohol = 412
    cc_Cyclo_Alcohol = 413
    cc_Poly_Alcohol = 414
    cc_Phenol = 420
    cc_Ketone = 430
    cc_Aldehyde = 440
    cc_Carboxilic_Acid = 450
    cc_Ester = 460
    cc_Anhydride = 470
    cc_Ether = 480
    cc_Epoxide = 481
    cc_Peroxide = 482
    cc_Halogen = 490
    cc_Fluoro_Halogen = 491
    cc_Chloro_Halogen = 492
    cc_Iodo_Halogen = 493
    cc_Bromo_Halogen = 494
    cc_Nitrogen_Component = 500
    cc_Amine = 501
    cc_Imine = 502
    cc_Amide = 503
    cc_Nitrile = 504
    cc_Cyanate = 505
    cc_Silane = 510
    cc_Miscellaneous = 600


class UsingCurve:
    ucNo = 0
    ucYes = 1


class PCBBasisType:
    pcbMolarFlow = 0
    pcbMassFlow = 1
    pcbLiqVolFlow = 2


class PropertyPackageType:
    ppkg_PR = 5891
    ppkg_SRK = 5892
    ppkg_SourPR = 5893
    ppkg_SourSRK = 5894
    ppkg_PRTwu = 5895
    ppkg_SRKTwu = 5896
    ppkg_TSTPR = 5897
    ppkg_GLYCOLPKG = 5898
    ppkg_KabadiDannerSRK = 5905
    ppkg_ZudkevitchJoffeeRK = 5906
    ppkg_PRSV = 5907
    ppkg_GCEOS = 5908
    ppkg_BWRS = 5909
    ppkg_CPA = 5910
    ppkg_SRPKG = 5911
    ppkg_IF97Steam = 5912
    ppkg_Wilson = 5922
    ppkg_Uniquac = 5923
    ppkg_NRTL = 5924
    ppkg_VanLaar = 5925
    ppkg_Margules = 5926
    ppkg_ChienNull = 5936
    ppkg_ChaoSeader = 5953
    ppkg_GraysonStreed = 5954
    ppkg_Antoine = 5969
    ppkg_BraunK10 = 5970
    ppkg_EssoTabular = 5971
    ppkg_ASMESteam = 5985
    ppkg_NBSSteam = 5986
    ppkg_Amine = 6000


class EnthalpyMethodType:
    EnthalpyMethod_EOS = 0
    EnthalpyMethod_LeeKesler = 1


class VapourModelType:
    VapourModel_Ideal = 0
    VapourModel_RK = 1
    VapourModel_Virial = 2
    VapourModel_PR = 3
    VapourModel_SRK = 4


class PhaseType:
    ptVapourPhase = 0
    ptLiquidPhase = 1
    ptLiquid2Phase = 2
    ptCombinedLiquidPhase = 3
    ptSolidPhase = 4
    ptCombinedPhase = 5
    ptPolymerPhase = 6
    ptUnknownPhase = 7


class LiqActivityModels:
    ActivityModel_Henry = 0
    ActivityModel_varLaar = 1
    ActivityModel_Margules = 2
    ActivityModel_NRTL = 3
    ActivityModel_Scatchard = 4
    ActivityModel_RegSoln = 5
    ActivityModel_General = 6


class NRTLFormulation:
    NRTLType1 = 0
    NRTLType2 = 1
    NRTLType3 = 2
    NRTLType4 = 3
    NRTLType5 = 4


class HeatExchangerCurveUse:
    hcuDoesNotUse = 0
    hcuAllPoints = 1
    hcuDewAndBubbleOnly = 2


class AssayD86ConversionType:
    D86_Default1974 = 0
    D86_1988 = 1
    D86_1992 = 3
    D86_Okamoto = 4


class AssayASTM_D2887ConversionType:
    D2887_API1987 = 0
    D2887_API1994Indirect = 1
    D2887_API1994Direct = 2


class lbpFbpBasis:
    ifb_LiquidVolumePercent = -1
    ifb_MolePercent = -2
    ifb_MassPercent = -3


class AssayType:
    at_TBP = 0
    at_D86 = 1
    at_D1160 = 2
    at_D86D1160 = 3
    at_ASTMD2887 = 4
    at_Chromatograph = 5
    at_EFV = 6
    at_BulkPropertiesOnly = 7


class AssayCurveType:
    ac_NotUsed = 0
    ac_Dependent = 1
    ac_Independent = 2


class AssayExtrapolationMethod:
    aem_LeastSquares = 1
    aem_LaGrange = 2
    aem_Probability = 3


class AssayBasis:
    ab_LiquidVolumeFraction = -1
    ab_MoleFraction = -2
    ab_MassFraction = -3


class AssayLightEndsCalculationType:
    alect_IgnoreLightEnds = 0
    alect_AutoCalculateLightEnds = -4
    alect_UserInputLightEnds = -1


class AssayLightEndsCompositionBasis:
    alecb_LiquidVolumeFraction = -1
    alecb_MoleFraction = -2
    alecb_MassFraction = -3
    alecb_MoleFlow = -5
    alecb_MassFlow = -6
    alecb_LiquidVolumeFlow = -7


class AssayViscosityType:
    av_Dynamic = 1
    av_Kinematic = 2


class BlendFlowBasis:
    bfb_LiquidVolume = -1
    bfb_Molar = -2
    bfb_Mass = -3


class BlendCutOptionType:
    bco_AutoCut = 1
    bco_UserRanges = 2
    bco_UserPoints = 3


class BlendOilDistributionTableType:
    bodt_StraightRun = 0
    bodt_CycleOil = 1
    bodt_VacuumOil = 2
    bodt_UserCustom = 3


class MWCorrelation:
    MW_Lee_Kesler = 1
    MW_Riazi_Daubert = 3
    MW_Bergman = 7
    MW_Robinson_Peng = 13
    MW_Hariu_Sage = 14
    MW_Katz_Firoozabadi = 16
    MW_Penn_State = 17
    MW_Aspen = 19
    MW_Katz_Nokay = 21
    MW_Aspen_LwastSq = 22
    MW_Whitson = 28
    MW_Twu1983 = 30
    MW_API1980 = 31


class SGCorrelation:
    SG_Lee_Kesler = 1
    SG_Bergman = 7
    SG_Hariu_Sage = 14
    SG_Yarborough = 15
    SG_Katz_Firoozabadi = 16
    SG_Bergman_PNA = 26


class TcCorrelation:
    Tc_Lee_Kesler = 1
    Tc_Cavett = 2
    Tc_Riazi_Daubert = 3
    Tc_Nokay = 4
    Tc_Roess = 5
    Tc_Edmister = 6
    Tc_Bergman = 7
    Tc_Spencer_Daubert = 8
    Tc_Rowe = 9
    Tc_Standing_Mathews_Roland_Katz = 10
    Tc_Penn_State = 17
    Tc_Mathur = 18
    Tc_Aspen = 19
    Tc_Chen_Hu = 20
    Tc_Eaton_Porter = 23
    Tc_Meissner_Redding = 24
    Tc_Twu1983 = 30


class PcCorrelation:
    Pc_Lee_Kesler = 1
    Pc_Cavett = 2
    Pc_Riazi_Daubert = 3
    Pc_Edmister = 6
    Pc_Bergman = 7
    Pc_Rowe = 9
    Pc_Standing_Mathews_Roland_Katz = 10
    Pc_Lydersen = 11
    Pc_Penn_State = 17
    Pc_Mathur = 18
    Pc_Aspen = 19
    Pc_Twu1983 = 30


class AcentricFacterCorrelation:
    AF_Lee_Kesler = 1
    AF_Edmister = 6
    AF_Bergman = 7
    AF_Robinson_Peng = 13


class IdealEnthalpyCorrelation:
    IH_Lee_Kesler = 1
    IH_Cavett = 2
    IH_Fallon_Watson = 27
    IH_Modified_Lee_Kesler = 29


class UserPropertyMixingBasis:
    UPMB_MoleFraction = 1
    UPMB_MassFraction = 2
    UPMB_LiquidVolumeFraction = 3
    UPMB_MoleFlow = -1
    UPMB_MassFlow = -2
    UPMB_LiquidVolumeFlow = -3


class UserPropertyMixingRule:
    UPMR_Rule1 = 1
    UPMR_Rule2 = 2
    UPMR_Rule3 = 3


class evtVariableType:
    evtVapourFraction = 0
    evtTemperature = 1
    evtPressure = 2
    evtMoleFlow = 3
    evtMassFlow = 4
    evtLiqVolFlow = 5
    evtHeatFlow = 6
    evtMolarDensity = 1001
    evtHeatCapacity = 1000
    evtEntropy = 8
    evtThermalCond = 1007
    evtViscosity = 1008
    evtSurfTension = 1010
    evtSG = 4119
    evtSGAir = 1022
    evtMassCp = 1011
    evtMassDensity = 1012
    evtUA = 1516
    evtSmallVolFlow = 4118
    evtStdGasFlow = 1024
    evtActGasFlow = 1025
    evtMolarEnthalpy = 7
    evtLength = 1505
    evtSmallLength = 4116
    evtDeltaTemp = 1517
    evtMolarVolume = 1013
    evtHtTranCoeff = 1524
    evtLargeHeatFlow = 4117
    evtStandardDensity = 1016
    evtMassEntropy = 1019
    evtMassEnthalpy = 1018
    evtEnthCoeffCA = 4102
    evtEnthCoeffCB = 4103
    evtEnthCoeffCC = 4104
    evtEnthCoeffCD = 4105
    evtEnthCoeffCE = 4106
    evtEnthCoeffCF = 4107
    evtGibbsCoeffCA = 4108
    evtGibbsCoeffCB = 4109
    evtGibbsCoeffCC = 4110
    evtKinematicVisc = 1009
    evtArea = 1508
    evtVolume = 1502
    evtVelocity = 1027
    evtTime = 1520
    evtDeltaPressure = 1503
    evtHeatFlux = 4100
    evtFouling = 4101
    evtCakeLoading = 1527
    evtPermeability = 1528
    evtMassVelocity = 1028
    evtMass = 1029
    evtRhoVSqr = 4111
    evtAreaPerVolume = 4112
    evtPressPerLength = 4113
    evtVFlowPerLength = 4114
    evtVFlowPerArea = 4115
    evtMoles = 1500
    evtReactionRate = 3900
    evtValveCVMole = 3800
    evtValveCVMass = 3801
    evtValveCVVolume = 3802
    evtStdVolFlow = 1023
    evtFrequency = 3701
    evtPercent = 110
    evtUnitless = -32767
    evtWork = 1030
    evtCompMoleFlow = 12
    evtCompMassFlow = 13
    evtCompVolFlow = 14
    evtActVolFlow = 1026
    evtHeatingValue = 1032
    evtMassHeatingValue = 1033
    evtHeatOfVap = 1034
    evtMassHeatOfVap = 1035
    evtEnthalpyPerLength = 4120
    evtBWRA = 5000
    evtBWRA0 = 5001
    evtBWRB = 5002
    evtBWRB0 = 5003
    evtBWRC = 5004
    evtBWRC0 = 5005
    evtBWRAlpha = 5006
    evtPowerPerFlow = 6000
    evtPower = 4121
    evtMolesPerMass = 5010
    evtPerVolume = 5011
    evtPerMassVolume = 5012
    evtGasOilRatio = 4131
    evtOilVolume = 4132
    evtSpecificVolume = 4133
    evtCompressibility = 4130
    evtVolumetricEnthalpyFlow = 5013
    evtMassTransferCoefficient = 93
    evtDiffusivity = 94
    evtMassReactionRate = 95
    evtMolarYieldFromReaction = 96
    evtMassYieldFromReaction = 97
    evtMassEnthalpyFlow = 98
    evtCostIndex = 31000
    evtCostIndexPerTime = 31001
    evtCostIndexPerEnergy = 31002
    evtDynamicsCv = 31003
    evtDynamicsKTurbulent = 31004
    evtDynamicsKLaminar = 31005
    evtSurgeControlParameterA = 31006
    evtSurgeControlParameterB = 31007
    evtQuickOpeningRate = 31008
    evtRotationalInertia = 31009
    evtFrictionPowerLossFactor = 31010
    evtSmallArea = 31011
    evtForce = 31015
    evtActualMassDensity = 32010
    evtElectricalFlow = 32011
    evtEmissions = 32012
    evtEnergyLrg = 31012
    evtElectricalFuelOilFactor = 32013
    evtFuelOilEqvFactor = 32014
    evtFuelOilEqvMassFlowrate = 32015
    evtLeadLevelInGasoline = 32016
    evtReciprocalFOE = 32017
    evtReciprocalMass = 32018
    evtReciprocalMoles = 32019
    evtReciprocalTime = 32020
    evtReciprocalVapourVolume = 32021
    evtSteamRatio = 32000
    evtVapourVolume = 32022
    evtVolumeRatio = 32023
    evtVolumeSpecificEnergy = 32024
    evtVolumeConcentration = 32001
    evtMassConcentration = 32003
    evtMolarConcentration = 32005
    evtConcentration = 32007
    evtVolumeConcentrationPPM = 32002
    evtMassConcentrationPPM = 32004
    evtMolarConcentrationPPM = 32006
    evtDeactivationRate = 32033
    evtAcidity = 32034
    evtElectricPotential = 31017
    evtElectricalConductivity = 31018
    evtMolarElectricalConductivity = 31019


class SolverMode:
    sm_SteadyState = 0
    sm_Dynamic = 1


class IntegratorMode:
    imAutomatic = 0
    imManual = 1


class FlashStatus:
    fsFlashOK = 0
    fsTempNotFound = 1
    fsPressNotFound = 2
    fsVFNotFound = 3
    fsFlashNotPossible = 4
    fsFlashNeeded = 5


class StabilityTestMethod:
    ttNone = 0
    ttTangentPlaneLow = 1
    ttTangentPlaneMed = 2
    ttTangentPlaneHigh = 3
    ttTangentPlaneSpec = 4
    ttProp3 = 5


class FlashType:
    ftTPFlash = 1
    ftPHFlash = 2
    ftPSFlash = 3
    ftPVFlash = 4
    ftTHFlash = 5
    ftTVFlash = 7


class OperationClassification:
    oc_All = 0
    oc_Vessels = 1
    oc_HeatTransfer = 2
    oc_Rotating = 3
    oc_Piping = 4
    oc_SolidsHandling = 5
    oc_Reactor = 6
    oc_Column = 7
    oc_ShortCutColumn = 8
    oc_SubFlowsheet = 9
    oc_Logical = 10


class BPCurveBasis:
    bpcb_LiquidVolumeFraction = -1
    bpcb_MoleFraction = -2
    bpcb_MassFraction = -3


class BPCurvePhase:
    bpcp_Liquid = 1
    bpcp_Vapour = 2


class FlowSpecificType:
    fstNone = 0
    fstUseIfSpecified = 1
    fstUseMolarFlowAlways = 2
    fstUseMassFlowAlways = 3
    fstUseVolumeFlowAlways = 4


class PressureSpecificationType:
    pstNone = 0
    pstUseIfSpecified = 1
    pstUseAlways = 2


class PropertyType:
    gpt_Point = 0
    gpt_Curve = 1
    gpt_Distributed = 2
    gpt_PSD = 3
    gpt_Hydrate = 4


class PropertyVectorGroup:
    pvg_Thermo = 0
    pvg_PropPkg = 1
    pvg_Physical = 2
    pvg_Cold = 3
    pvg_Solid = 4
    pvg_Environ = 5
    pvg_OLI_Component = 7
    pvg_OLI_Ion = 8
    pvg_UserProperty = 9


class BOViscMethodType:
    BOSpecifiedCoefficents = 0
    BOSpecifyTwoOrMorePoints = 1
    BOTwu = 2
    BOBeal = 3
    BOAbbot = 4
    BOBeggsAndRobinson = 5
    BOGlaso = 6
    BONgAndEgbogah = 7
    BOTwuSinglePoint = 8
    BOBealSinglePoint = 9
    BOAbbotSinglePoint = 10
    BOBeggsAndRobinsonSinglePoint = 11
    BOGlasoSinglePoint = 12
    BONgAndEgbogahSinglePoint = 13


class StreamFlowBasis:
    MolarFlow = 0
    MassFlow = 1
    LiqVolFlow = 2
    AbsoluteCost = 3
    AsFuelOil = 4


class XMLOptionFlags:
    opt_SpecsOnly = 1
    opt_UseUserUnitSet = 2
    opt_IncludeAttachments = 4
    opt_SupplyMonikers = 8
    opt_TreatDefaultAsSpecs = 16
    opt_SupplyCalcByInfo = 32
    opt_HandleEmpties = 64
    opt_OverlaySpecs = 128
    opt_FPInteractionData = 256
    opt_IncludeColumnEstimates = 512
    opt_MinCorrelationInfo = 1024
    opt_NoBasisData = 2048
    opt_MinStreamInfo = 4096
    opt_CondenseData = 8192


class VariableRetrivialFlags:
    vars_Standard = 1
    vars_TemperaturePressure = 2
    vars_HeatFlow = 4
    vars_MolarComposition = 8
    vars_MassComposition = 16
    vars_PropertyVector = 32


class DataSource:
    ds_NONE = -1
    ds_EC589 = 0
    ds_US5711 = 1
    ds_USER = 2


class FuelType:
    eu_AviationGasoline = 0
    eu_CrudeOil = 1
    eu_Biodiesel = 2
    eu_Biogas = 3
    eu_Biogasoline = 4
    eu_Biomass = 5
    eu_Bitumen = 6
    eu_BlastFurnaceGas = 7
    eu_CarbonMonoxide = 8
    eu_Charcoal = 9
    eu_CoalAnthracite = 10
    eu_CoalBituminous = 11
    eu_CoalCoking = 12
    eu_CoalTar = 13
    eu_Coke = 14
    eu_CokeOvenGas = 15
    eu_DieselOil = 16
    eu_Ethane = 17
    eu_GasCoke = 18
    eu_GasWorksGas = 19
    eu_Gasoline = 20
    eu_GeneralPetroleumProducts = 21
    eu_JetGasoline = 22
    eu_JetKerosene = 23
    eu_Kerosene = 24
    eu_LandfillGas = 25
    eu_LiquefiedPetroleumGas = 26
    eu_Lubricants = 27
    eu_Methane = 28
    eu_Naphtha = 29
    eu_NaturalGas = 30
    eu_NaturalGasLiquids = 31
    eu_Orimulsion = 32
    eu_OxygenSteelFurnaceGas = 33
    eu_PatentFuel = 34
    eu_Peat = 35
    eu_PetroleumCoke = 36
    eu_RefineryFeedstocks = 37
    eu_RefineryGas = 38
    eu_ResidualFuelOil = 39
    eu_ShaleOil = 40
    eu_SludgeGas = 41
    eu_WasteOil = 42
    eu_Waxes = 43
    eu_WhiteSpiritAndSBP = 44
    eu_Wood = 45
    us_Asphalt = 46
    us_Biogas = 47
    us_CoalAnthracite = 48
    us_CoalBituminous = 49
    us_CoalCoking = 50
    us_CoalCommercial = 51
    us_CoalElectricPower = 52
    us_CoalIndustrial = 53
    us_CoalIgnite = 54
    us_CoalSubBituminous = 55
    us_Coke = 56
    us_CrudeOil = 57
    us_DistillateFuelOil = 58
    us_DiredSewageSludge = 59
    us_Ethane = 60
    us_FossilBasedWaste = 61
    us_GasolineAviation = 62
    us_GasolineMotor = 63
    us_GasolineNatural = 64
    us_ImpregnatedSawdust = 65
    us_Isobutane = 66
    us_JetFuel = 67
    us_Kerosene = 68
    us_LPG = 69
    us_Lubricants = 70
    us_MixedIndustrialWastes = 71
    us_MunicipalSolidWastes = 72
    us_NaphthaSpecial = 73
    us_NaphthaHeavyGreaterThan401F = 74
    us_NaphthaLightLessThan401F = 75
    us_NaturalGas = 76
    us_NornamlButane = 77
    us_PentanesPlus = 78
    us_PetrochemicalFeedstock = 79
    us_PetroleumCoke = 80
    us_Plastics = 81
    us_Propane = 82
    us_ResidualFuelOil = 83
    us_Solvents = 84
    us_Tires = 85
    us_UnfinishedOils = 86
    us_WasteOil = 87
    us_Waxes = 88
    us_Wood = 89


class FlowSheetObjStatusFlag:
    flag_OK = 1
    flag_NotSolved = 2
    flag_Warning = 4
    flag_UnderSpecified = 8
    flag_Error = 16


class ReactionSetSolverMethod:
    rs_RateIteration = 0
    rs_RateIntegration = 1
    rs_AutoSelected = 2
    rs_RBNewton1 = 3
    rs_Unknown = -32767


class ReactionSetTraceLevel:
    rs_NoTrace = 0
    rs_LoTrace = 1
    rs_MedTrace = 2
    rs_HiTrace = 3


class ReactionBasis:
    rbUnknownBasis = -32767
    rbActivityBasis = 1
    rbPartialPressBasis = 2
    rbMolarConcBasis = 3
    rbMassConcBasis = 4
    rbMoleFracBasis = 5
    rbMassFracBasis = 6
    rbMolarityBasis = 7
    rbMolalityBasis = 8


class LnKSource:
    eqrxn_Gibbs = 0
    eqrxn_LnKEquation = 1
    eqrxn_FixedK = 2
    eqrxn_Table = 3
    eqrxn_FixedExtent = 4


class CurvePropertyEQType:
    cpeq_Poly1 = 0
    cpeq_Poly2 = 1
    cpeq_Poly3 = 2
    cpeq_Poly4 = 3
    cpeq_Anto1 = 4
    cpeq_Anto2 = 5
    cpeq_Quot1 = 6
    cpeq_Quot2 = 7
    cpeq_Quot3 = 8
    cpeq_Expo1 = 9
    cpeq_Expo2 = 10
    cpeq_Wtsn1 = 11
    cpeq_DiCp1 = 12
    cpeq_Kfac2 = 13
    cpeq_Kfac4 = 14
    cpeq_Wgnr1 = 15
    cpeq_Mllr1 = 16
    cpeq_DiSV1 = 17
    cpeq_Ppds1 = 18
    cpeq_Ppds2 = 19
    cpeq_Ppds3 = 20
    cpeq_Ppds5 = 21
    cpeq_Ppds6 = 22
    cpeq_Ppds8 = 23
    cpeq_Ppds9 = 24
    cpeq_Ppds10 = 25
    cpeq_Ppds11 = 26
    cpeq_Ppds12 = 27
    cpeq_Ppds14 = 28
    cpeq_Ppds15 = 29
    cpeq_Ppds16 = 30
    cpeq_Ppds17 = 31
    cpeq_Hvclas = 32


class CurvePropertyXShape:
    cps_X = 0
    cps_X_reduced = 1
    cps_XrM = 2
    cps_LogX = 3
    cps_LogXr = 4
    cps_LogXr1 = 5
    cps_LnX = 6
    cps_LnXr = 7
    cps_LnXr1 = 8
    cps_ExpX = 9
    cps_ExpXr = 10
    cps_ExpXr1 = 11
    cps_SinX = 12
    cps_CosX = 13
    cps_TanX = 14
    cps_SinXr = 15
    cps_CosXr = 16
    cps_TanXr = 17
    cps_SinXr1 = 18
    cps_CosXr1 = 19
    cps_TanXr1 = 20
    cps_X1 = 21
    cps_Xr1 = 22
    cps_ScaleX = 23
    cps_XPpds = 24
    cps_XdQ = 25
    cps_XxQ = 26
    cps_LnXQ = 27
    cps_RootQdX = 28


class CurvePropertyYShape:
    cps_Y = 0
    cps_Y_reduced = 1
    cps_YrM = 2
    cps_LogY = 3
    cps_LogYr = 4
    cps_LogYr1 = 5
    cps_LnY = 6
    cps_LnYr = 7
    cps_LnYr1 = 8
    cps_ExpY = 9
    cps_ExpYr = 10
    cps_ExpYr1 = 11
    cps_SinY = 12
    cps_CosY = 13
    cps_TanY = 14
    cps_SinYr = 15
    cps_CosYr = 16
    cps_TanYr = 17
    cps_SinYr1 = 18
    cps_CosYr1 = 19
    cps_TanYr1 = 20
    cps_Y1 = 21
    cps_Yr1 = 22
    cps_ScaleY = 23
    cps_YPpds = 24
    cps_YdQ = 25
    cps_YxQ = 26
    cps_LnYQ = 27
    cps_RootQdY = 28
    cps_ScaleYX = 29
    cps_YdX = 30
    cps_RootXdY = 31


class InputPSDType:
    psdt_UserDefinedDiscrete = 0
    psdt_LogProbability = 1
    psdt_RosinRammler = 2


class InputPSDBasis:
    psdb_InSize = 0
    psdb_UnderSize = 1
    psdb_Oversize = 2


class InputPSDCompositionBasis:
    pscb_MassPercent = 1
    pscb_NumberPercent = 3


class PSD_FitType:
    psdft_AutoFit = 0
    psdft_StandardInterp = 1
    psdft_ProbabilityInterp = 2
    psdft_LogProbabilityFit = 3
    psdft_RosinRammlerFit = 4
    psdft_NoFit = 5


class VesselOrientation:
    vo_Horizontal = 0
    vo_Vertical = 1
    duHorizontal = 0
    duVertical = 1


class VesselMaterialType:
    vmt_CarbonSteel = 1
    vmt_StainlessSteel304 = 2
    vmt_StainlessSteel316 = 3
    vmt_Aluminium = 4
    vmt_UserDefined = 5


class VesselSizingSpecification:
    vss_MaximumVelocity = 0
    vss_Diameter = 1
    vss_LengthOverDiameterRatio = 2
    vss_VapourSpaceHeight = 3
    vss_DemisterThickness = 4
    vss_LiquidResidenceTime = 5
    vss_LiquidSurgeHeight = 6
    vss_LLSD = 7
    vss_DemisterToTop = 8
    vss_NozzleToDemister = 9
    vss_SurgeToNozzle = 10
    vss_TotalHeight = 11


class LevelOrFlowControlType:
    ctLiquidFlow = 0
    ctLevel = 1


class FlowType:
    ftMolar = 3
    ftMass = 4
    ftVolume = 5


class PressureSourceType:
    pstUserSpecified = 0
    pstOtherOperation = 1


class DutyType:
    dtUtility = 0
    dtDirectQ = 1


class DutyLocationType:
    htLiquid = 0
    htVessel = 1


class SeparatorType:
    stSeparator = 0
    stThreePhase = 1
    stTank = 2


class HoldupInitType:
    hitDryStartup = 0
    hitInitFromProducts = 1
    hitInitFromUser = 2


class HeatLossmModelType:
    hlmtNone = 0
    hlmtSimple = 1
    hlmtDetailed = 2


class HeatLossParameterType:
    hlptTemperatureProfile = 0
    hlptConduction = 1
    hlptConvection = 2


class TraySizingInternals:
    tsiSieveTray = 0
    tsiValveTray = 1
    tsiPackedTray = 2
    tsiBubbleCapTray = 3


class TraySizingMode:
    tsmDesign = 0
    tsmRating = 1


class TraySizingDowncomerType:
    tsdtVertical = 1
    tsdtSloped = 2


class TraySizingValveOrificeType:
    tsvotFlat = 1
    tsvotVenturi = 2


class TraySizingValveDesignManual:
    tsvdmGlitsch = 1
    tsvdmKoch = 2
    tsvdmNutter = 3


class TraySizingPackingCorrelationType:
    tspctSLE = 1
    tspctRobbins = 2


class TraySizingHETPCorrelationType:
    tshctIntalox = 0
    tshctNortons = 1
    tshctHands = 2
    tshctFrank = 3
    tshctSpecifiedHETP = 4


class TraySizingDesignLimitType:
    tsdltChannelling = 0
    tsdltFlooding = 1
    tsdltDeltaP = 2
    tsdltSpecdDiameter = 3
    tsdltMinDiameter = 4
    tsdltVaporLoading = 5
    tsdltFlowPathLength = 6
    tsdltDCBackup = 7
    tsdltDCResidenceTime = 8
    tsdltWeirLoading = 9
    tsdltReliefWeir = 10


class TraySizingFloodingCalcMethod:
    tsfcmMinimumCsb = 1
    tsfcmOriginalCsb = 2
    tsfcmFairsModifiedCsb = 3


class TraySizingUseVapourMethod:
    tsuvmAskEachTime = 1
    tsuvmAlwaysYes = 2
    tsuvmAlwaysNo = 3


class TraySizingWeirType:
    tswtStraight = 1
    tswtRelief = 2


class TraySizingCalcStatus:
    tscsIncomplete = 0
    tscsNeedsCalculating = 1
    tscsComplete = 2


class TraySizingActiveFlag:
    tsafOn = 0
    tsafOff = 1


class ControllerMode:
    cmOff = 0
    cmManual = 1
    cmAuto = 2
    cmRamping = 3
    cmCascaded = 4
    cmTuning = 5


class ControllerAction:
    cdReverse = 0
    cdDirect = 1


class ControllerSignals:
    pidPvSignal = 0
    pidOpSignal = 1
    pidSpSignal = 2
    pidDvSignal = 3
    pidRemoteSpSignal = 4


class ControllerAlarmResults:
    pidNormal = 0
    pidLowLowAlarm = 1
    pidLowAlarm = 2
    pidHighAlarm = 3
    pidHighHighAlarm = 4


class ControllerScheduling:
    pidSp = 0
    pidPv = 1


class ControllerManualSpTrack:
    mpidNoTracking = 0
    mpidTrackPv = 1


class ControllerAutoTunerDesignType:
    pidPID = 0
    pidPI = 1


class ControllerLocalSpTrack:
    lpidNoTracking = 0
    lpidTrackRemote = 1


class ControllerRemoteSpUnits:
    pidUsePercent = 0
    pidUsePVUnits = 1


class ControllerPVSamplingFailuremode:
    sfNone = 0
    sfFixedSignal = 1
    sfBias = 2


class ControllerBasisPercentOfPVMode:
    bippvPVUnits = 0
    bippvPercentPVR = 1


class ValveFlowBasis:
    vfbMolarFlow = 3
    vfbMassFlow = 4
    vfbLiquidVolumeFlow = 5
    vfbActualVolumeFlow = 6


class TraySectionType:
    tstStandard = 0
    tstSideStripper = 1
    tstSideRectifier = 2


class TypeOfRecycleStream:
    GenericStream = 0
    MaterialStream = 1
    EnergyStream = 2


class AccelType:
    Wegstein = 0
    Dominant_Eigenvalue = 1


class SimuRecy:
    Simultaneous = 0
    Nested = 1


class Convergence:
    Unconverged = 0
    Converged = 1
    Ignored = 2
    MaxIterations = 3


class PFDItemType:
    pfdAll = -1
    pfdOperation = -2
    pfdStreamLine = -3
    pfdOperationLabel = -4
    pfdTextAnnotation = -5
    pfdOperationTable = -6
    pfdWorkSheetTable = -7
    pfdObject = -8


class PFDItemVisibility:
    pfdVisible = 0
    pfdHidden = 1
    pfdVisibleandHidden = 2


class PFDItemRotion:
    pfdRotateNormal = 0
    pfdRotate90 = 1
    pfdRotate180 = 2
    pfdRotate270 = 3


class PFDItemMirror:
    pfdMirrorNormal = 0
    pfdMirrorX = 4
    pfdMirrorY = 5


class PFDNozzleDirection:
    pfdUp = 1
    pfdDown = 2
    pfdRight = 3
    pfdLeft = 4


class PFDAttachment:
    pfdInletFromMaterialStream = 0
    pfdOutletToMaterialStream = 1
    pfdInletFromStream = 2
    pfdOutletToStream = 3
    pfdMaterialStreamInlet = 4
    pfdMaterialStreamOutlet = 5
    pfdToController = 6
    pfdFromController = 7
    pfdSPFromLogical = 8
    pfdPVToLogical = 9
    pfdCascade = 10
    pfdEnergyStreamInlet = 11
    pfdEnergyStreamOutlet = 12
    pfdInletFromEnergyStream = 13
    pfdOutletToEnergyStream = 14
    pfdAny = 15
    pfdHybridToController = 16
    pfdHybridFromController = 17
    pfdPowerStreamInlet = 18
    pfdPowerStreamOutlet = 19
    pfdInletFromPowerStream = 20
    pfdOutletToPowerStream = 21
    pfdLastAttachType = 22


class SolType:
    SecantMethod = 0
    BroydenMethod = 1
    SimultaneousSolution = 2


class TransferBasisType:
    tb_TemperaturePressure = 0
    tb_VapFracTemperature = 1
    tb_VapFracPressure = 2
    tb_NoneRequired = 3
    tb_UserSpecified = 4
    tb_PressureEnthalpy = 5
    tb_NotSet = 6


class StepType:
    es_EqualEnthalpy = 0
    es_EqualTemp = 1
    es_AutoInterval = 2


class HeatCurvePressureType:
    es_ConstdPdH = 0
    es_ConstdPdUA = 1
    es_ConstdPdA = 2
    es_InletPressure = 3
    es_OutletPressure = 4
    es_DesignCorrelation = 5


class HeatExchangerSpecificationType:
    hex_UnknownExchSpecType = -32767
    hex_TemperatureType = 0
    hex_DeltaTempType = 1
    hex_UAType = 2
    hex_LMTDType = 3
    hex_AreaType = 4
    hex_DutyType = 5
    hex_MinDTType = 6
    hex_FlowType = 7
    hex_FlowRatioType = 8
    hex_DutyRatioType = 9
    hex_LengthType = 10
    hex_SubCoolingType = 11
    hex_SuperHeatingType = 12


class HeatExchangerPass:
    hepError = 8
    hepHeatLeak = 19
    hepHeatLoss = 20


class HeatExchangerStream:
    hesColdInletEquilibrium = 17
    hesHotInletEquilibrium = 18


class HeatExchangerFlowBasis:
    hefbMole = 3
    hefbMass = 4
    hefbLiqVol = 5


class HeatExchangerModel:
    hex_EndPoint = 822
    hex_Weighted = 823
    hex_SimpleRating = 824


class HeatLeakLoss:
    hex_None = 0
    hex_Extremes = 1
    hex_Proportional = 2


class ShellPasses:
    hex_CounterCurrent = 0
    hex_OnePass = 1
    hex_TwoPass = 2
    hex_ThreePass = 3
    hex_FoourPass = 4
    hex_FivePass = 5
    hex_SixPass = 6
    hex_SevenPass = 7


class DynamicModel:
    hex_Basic = 0
    hex_SimpleDetailed = 1
    hex_Detailed = 2


class Orientation:
    hex_Horizontal = 0
    hex_Vertical = 1


class TubeLayout:
    hex_Square = 0
    hex_Triangular = 1


class TemaA:
    ta_A = 65
    ta_B = 66
    ta_C = 67
    ta_D = 68
    ta_N = 78


class TemaB:
    tb_E = 69
    tb_F = 70
    tb_G = 71
    tb_H = 72
    tb_J = 74
    tb_K = 75
    tb_X = 88


class TemaC:
    tc_L = 76
    tc_M = 77
    tc_N = 78
    tc_P = 80
    tc_S = 83
    tc_T = 84
    tc_U = 85
    tc_W = 87


class ShellBaffleType:
    hex_Single = 0
    hex_Double = 1
    hex_Triple = 2
    hex_NTIW = 3
    hex_Grid = 4


class LayoutAngle:
    hex_Thirty = 30
    hex_FortyFive = 45
    hex_Sixty = 60
    hex_Ninety = 90


class RatingMethod:
    lng_EndPoint = 822
    lng_Weighted = 823


class SideType:
    lng_Hot = 0
    lng_Cold = 1
    lng_NotSet = -32767


class ValveType:
    vtLinear = 0
    vtQuickOpening = 1
    vtEqualPercentage = 2


class ValveFailPosition:
    vfpNone = 0
    vfpFailOpen = 1
    vfpFailClosed = 2


class ValveActuatormode:
    vamInstantaneous = 0
    vamFirstOrder = 1
    vamLinear = 2


class ValveCvType:
    cvStandardCv = 0
    cvConductance = 1
    vtMASONEILAN = 1


class ValveManufacturer:
    vtMOKVELD = 2
    vtFISHER = 3
    vtINTROL = 4
    vtVALTEK = 5
    vtCCIDRAG = 6
    vtUniversal = 7
    vtKType = 8


class vtMASONEILANStype:
    DPGLOBE = 1
    SERIES40000 = 2
    SPGLOBE = 3
    CAMFLEXOPEN = 4
    SPLITOPEN = 5
    CAMFLEXCLOSE = 6
    BUTTERFLY = 7
    CONTROL = 8
    SPLITCLOSE = 9
    GLOBECONTOURED = 10
    GLOBECLOSE = 11


class vtMOKVELDStype:
    RZDR = 1
    RZDRES = 2
    RZDRVX = 3
    RZDREVX = 4
    RZDRCX = 5


class vtNTROLStype:
    S10OPEN = 1
    S20OPENCLOSE = 2
    S10CLOSE = 3
    S60A = 4
    S60 = 5
    S10HF = 6
    S20H = 7
    S10HFD = 8
    S20HFD = 9
    S10HFT = 10
    S20HFT = 11


class vtVALTEKStype:
    MARKONEOPEN = 1
    MARKTWOOPEN = 2
    MARKONECLOSE = 3
    MARKTWOCLOSE = 4
    VECTORONE60DEG = 5
    VECTORONE90DEG = 6
    DRAGONTOOTH = 7


class ControllerMPCMode:
    mpcOff = 0
    mpcManual = 1
    mpcAuto = 2


class ControllerMPCAlgorithm:
    mpcUnconstrained = 0
    mpcConstrained = 1


class ControllerMPCSetpointmode:
    mpcSpLocal = 0
    mpcSpRemote = 1


class ControllerMPCCurrentAlarmSignal:
    cmpcPvSignal = 0
    cmpcOpSignal = 1
    cmpcSpSignal = 2
    cmpcDvSignal = 3
    cmpcRemoteSpSignal = 4


class ControllerMPCAlarmSignals:
    mpcPvSignal = 0
    mpcOpSignal = 1
    mpcSpSignal = 2
    mpcDvSignal = 3
    mpcRemoteSpSignal = 4


class ControllerMPCAlarmResults:
    mpcNormal = 0
    mpcLowLowAlarm = 1
    mpcLowAlarm = 2
    mpcHighAlarm = 3
    mpcHighHighAlarm = 4


class ControllerMPCExecutionMode:
    mpcInternal = 0
    mpcExternal = 1


class ControllerMPCManualSpTrack:
    mmpcNoTracking = 0
    mmpcTrackPV = 1


class ControllerMPCLocalSpTrack:
    lmpcNoTracking = 0
    lmpcTrackRemote = 1


class ControllerMPCRemoteSpUnits:
    mpcUsePercent = 0
    mpcUsePVUnits = 1


class DigitalControllerMode:
    dmOff = 0
    dmManual = 1
    dmAuto = 2


class DynType:
    NotSelected = -32767
    Ntu_PT = 0
    Ntu_PH = 1
    Ntu_SinglePhase = 2


class UseCurve:
    No = 0
    Yes = 1


class EffType:
    Adiabatic_Eff = 500
    Polytropic_Eff = 501


class CylinderType:
    cdtSingle_ActingOuterEnd = 0
    cdtSingle_ActingCrankEnd = 1
    cdtDouble_ActingTailRodType = 2
    cdtDouble_ActingNoTailRodType = 3


class PolyMethod:
    SchultzOpt = 0
    HuntingtonOpt = 1
    ReferenceOpt = 2
    OtherOpt = 3


class BalanceRatioType:
    brt_Mole = 0
    brt_Mass = 1
    brt_Volume = 2
    brt_Unknown = -32767


class BalanceOptype:
    botMoleAndHeat = 0
    botMole = 1
    botMass = 2
    botHeat = 3
    botGeneral = 4
    botNotSet = -32767


class ValveControlType:
    vc_MultiStream = 0
    vc_ThreeWay = 1


class LogicExpressionState:
    logic_Complete = 0
    logic_Incomplete = 1
    logic_BadSyntax = 2


class JumpWhen:
    ev_Never = 0
    ev_Always = 1
    ev_True = 2
    ev_Timeout = 3


class EventState:
    evFalse = 0
    evTrue = 1


class WaitFor:
    ev_LogicTrue = 0
    ev_ElapsedTime = 1
    ev_SpecificTime = 2
    ev_StabilizeVariable = 3


class LogicCondition:
    ev_NoLogic = 0
    ev_HasLogic = 1


class SequenceStatus:
    seqIncomplete = 0
    seqInactive = 1
    seqRunning = 2
    seqWaiting = 3
    seqHolding = 4
    seqComplete = 5


class SequenceRunMode:
    seqOneShot = 0
    seqContinuous = 1


class ScheduleState:
    sched_False = 0
    sched_True = 1


class PerformanceSliderSetting:
    FavourCalculationsMax = 1
    FavourCalculations3 = 2
    FavourCalculations2 = 3
    FavourCalculations1 = 4
    AutoLoadBalance = 5
    FavourResponse1 = 6
    FavourResponse2 = 7
    FavourResponse3 = 8
    FavourResponseMax = 9


class AirCoolerConfiguration:
    acOneTubeOnePass = 0
    acTwoTubeOnePass = 1
    acThreeTubeOnePass = 2
    acFourTubeOnePass = 3
    acTwoTubeTwoPass = 4
    acThreeTubeThreePass = 5
    acFourTubeTwoPass = 7
    acFourTubeFourPass = 6


class PressurOptions:
    csUseStreamPressureSpecification = 0
    csEqualizeAllPressures = 1
    csUseLowestFeedPressureForAll = 2


class StreamSpecifications:
    csCalcualteEqualTemperatures = 0
    csUseStreamFlashSpecification = 1


class SplitFractionBasis:
    csMolar = 0
    csMass = 1


class SplitFractionType:
    csFeedFracToProduct = 0
    csFractionInProduct = 1
    csFlowInProduct = 2


class InputType:
    pmUseUtilityData = 0
    pmInputFromDataFile = 1


class DataFileFormat:
    pmRow = 0
    pmColumn = 1


class DataMapping:
    pmInputs = 0
    pmOutputs = 1


class TrainingType:
    pmManipulated = 0
    pmObservable = 1


class TransferBasis:
    scTPFlash = 0
    scPHFlash = 5
    scVFTFlash = 1
    scVFPFlash = 2
    scNoneRequired = 3
    scNoneSet = 6


class SecondOrderFunctionalityType:
    tfLag = 0
    tfSineWave = 1


class PulseBehavior:
    ceLatched = 0
    cePulseOn = 1
    cePulseOff = 2
    ceNA = 3


class LocalSwitch:
    swOff = 0
    swOn = 1
    swAuto = 2


class OperatingMode:
    duFire = 0
    duAlternateFire = 4
    duFireWetted = 1
    duAdiabatic = 2
    duUseSpreadsheet = 3


class HeatLossModel:
    duNone = 0
    duSimple = 1
    duDetailed = 2


class CorrelationConstantSelection:
    duAutoSelect = 1
    duUseSpecified = 0


class FixedOrUpdatedU:
    duUseFixed = 0
    duUseUpdated = 1


class VapourFlowEquation:
    du1Fisher = 0
    du1Relief = 6
    du1Supersonic = 1
    du1Subsonic = 2
    du1Masoneilan = 3
    du1General = 4
    du1NoFlow = 5
    du1UseSpreadsheet = 7


class LiquidFlowEqation:
    du2Fisher = 0
    du2Supersonic = 1
    du2Subsonic = 2
    du2Masoneilan = 3
    du2General = 4
    du2NoFlow = 5
    du2UseSpreadsheet = 6


class CalculateCvOrPressure:
    duCv = 0
    duPressure = 1


class HydrateFormation:
    hfWillForm = 0
    hfWillNotForm = 1
    hfEmpty = 2


class HydrateTypeFormed:
    htTypeI = 0
    htTypeII = 1
    htTypeIandII = 2
    htNoType = 3
    htEmpty = 4
    htIceFormsFirst = 5


class EquilibriumPhase:
    epAssumeFreeWater = 0
    epFreeWaterFound = 1
    epvapourPhase = 2
    epEmpty = 3
    epLiquidPhase = 4


class HydrateModel:
    hmAssumeFreeWater = 0
    hmAsymmetricalModel = 1
    hmSymmetrical = 2
    hmVapourOnlyModel = 3


class HydrateTypeFormedAtStreamPressure:
    spTypeI = 0
    spTypeII = 1
    spTypeIandII = 2
    spNoType = 3
    spEmpty = 4
    spIceFormsFirst = 5


class EquilibriumPhaseAtStreamPressure:
    eppAssumeFreeWater = 0
    eppFreeWaterFound = 1
    eppvapourPhase = 2
    eppEmpty = 3
    eppLiquidPhase = 4


class HydrateTypeFormedAtStreamTemperature:
    stTypeI = 0
    stTypeII = 1
    stTypeIandII = 2
    stNoType = 3
    stEmpty = 4
    stIceFormsFirst = 5


class EquilibriumPhaseAtStreamTemperature:
    eptAssumeFreeWater = 0
    eptFreeWaterFound = 1
    eptvapourPhase = 2
    eptEmpty = 3
    eptLiquidPhase = 4


class CalculationType:
    ctMaxDiameter = 0
    ctPressureDrop = 1


class PipeSchedule:
    psNone = -32767
    psSchedule40 = 0
    psSchedule80 = 80
    psSchedule160 = 160


class Mode1:
    m1State = 0
    m1Incremental = 1


class Mode2:
    m2State = 0
    m2Incremental = 1


class BalanceType:
    btTotalBalance = 0
    btMoleBalance = 1
    btMassBalance = 2
    btHeatBalance = 3
    btVolumeBalance = 5


class CurrentExtensionVersion:
    extnCurrentVersion = 140359


class DynamicPropertyMethod:
    dpmIdealGas = 0
    dpmIdealGasWithActivities = 1
    dpmLocalK = 2


class PhaseTypeModel:
    ptmNotPresent = 0
    ptmLiquid = 1
    ptmVapour = 4


class PhaseOffset:
    poVapour = 0
    poLiquid1 = 1
    poLiquid2 = 2
    poOverall = 3


class PhasePair:
    ppVapourLiquid1 = 1
    ppVapourLiquid2 = 2
    ppLiquid1Liquid2 = 4


class SupercriticalMethod:
    HYSIMMethod = 1
    ReducePressure = 2
    SimpleModelFromPreviousStage = 3


class ColumnInnerLoopType:
    OLEUnknownInnerLoopType = 0
    OLEHysimClassicInnerLoop = 1
    OLENRInnerLoop = 2
    OLEDoglegInnerLoop = 3
    OLEModifiedHysimLoop = 4
    OLEUnknownColumnAlgorithm = 0
    OLERussellInsideOutAlgorithm = 1
    OLEZhimingAlgorithm = 2
    OLENewtonRaphsonSolver = 3


class ColumnAlgorithm:
    caHYSIMInsideOut = 0
    caModifiedHYSIMInsideOut = 1
    caNewtonRaphsonInsideOut = 2
    caSparseContinuationSolver = 5
    caSimulataneousCorrection = 4


class BasisType:
    MoleBasis = 0
    MassBasis = 1
    IdealLiquidVolumeBasis = 2


class ComponentEfficienciesType:
    ComponentEfficiencies = 0
    OverallEfficiencies = 1


class ColumnTraceLevel:
    Low = 1
    Medium = 2
    High = 3


class ReboilerType:
    TwoPhaseReboiler = 0
    ThreePhaseReboiler = 1


class CondenserType:
    PartialCondenser = 0
    TotalCondenser = 1
    ThreePhaseCondenser = 2


class HeatCool:
    Cooling = 0
    Heating = 1


class ProductFlowBasis:
    Molar = 3
    Mass = 4
    Volume = 5


class ReactionProperty:
    rpReactants = 0
    rpStoichiometricCoefficients = 1
    rpMinTemperature = 2
    rpMaxTemperature = 3
    rpReactionBasis = 4
    rpReactionPhase = 5
    rpBaseReactant = 6
    rpBasisConversion = 7
    rpRateConversion = 8


class ExtensionType:
    extPropertyPackage = 0
    extUnitOperation = 1
    extHeatExchangerDesigner = 2
    extKineticReaction = 3


class ExchangerDesignRequiredPressures:
    xdrpNone = 0
    xdrpInlet = 1
    xdrpOutlet = 2
    xdrpInletAndOutlet = 3
    xdrpInletOrOutlet = 4


class KineticRateDerivativeType:
    krdt_drdx = 0
    krdt_drdlnx = 1


class psPipeSegHeatTransfer:
    psHeat_Loss = 0
    psOverall_HTC = 1
    psSegment_HTC = 2
    psEstimate_HTC = 3


class psAmbientTemp:
    psBy_Segment = 0
    psGlobal = 1


class psHTCCorrelation:
    psPetukov = 0
    psDittus = 1
    psSieder = 2
    psProfes = 3
    psHTFS = 4


class psInsulation:
    psIENo_Insulation = -32767
    psIEUser_Specified = 0
    psEvacuated_Annulus = 1
    psUrethane_Foam = 2
    psGlass_Block = 3
    psFiberglass_Block = 4
    psFiber_Blanket = 5
    psFiber_Blanket_Vap_Barr = 6
    psPlastic_Block = 7
    psAsphalt = 8
    psConcrete = 9
    psConcreteInsulated = 10
    psNeoprene = 11
    psPVC_Foam = 12
    psPVCBlock = 13
    psPolyStyreneFoam = 14


class psMedium:
    psAir = 0
    psWater = 1
    psGround = 2


class psGroundType:
    psGTNone = -32767
    psGTUser_Specified = 0
    psGTDryPeat = 1
    psGTWetPeat = 2
    psGTIcyPeat = 3
    psGTDrySand = 4
    psGTMoistSand = 5
    psGTWetSand = 6
    psGTDryClay = 7
    psGTMoistClay = 8
    psGTWetClay = 9
    psGTFrozenClay = 10
    psGTGravel = 11
    psGTSandyGravel = 12
    psGTLimestone = 13
    psGTSandStone = 14
    psGTIce = 15
    psGTColdIce = 16
    psGTLooseSnow = 17
    psGTHardSnow = 18


class psSlugTrans:
    psBendikson = 0
    psSTEUser_Specified = 1


class psHoldup:
    psGregory_et_al = 0
    psHEUser_Specified = 1


class psFrictionFactor:
    psFFESmooth = 0
    psColebrook = 1


class psFrequency:
    psHill_Wood = 0
    psFEUser_Specified = 1


class psHydroDynModeling:
    psZuberFindlay = 2
    psFullGasLiquidModelling = 4


class psHydroDynFunc:
    psAllConfigurationTested = 0
    psDispersed = 1
    psIntermittent = 2
    psStatified = 3


class PropertyBalanceType:
    pbtRegularBalance = 0
    pbtMixerBalance = 1
    pbtTeeBalance = 2


class PetroluemPropertyType:
    pptAcidityProp = 11000
    pptAnilinePointProp = 11001
    pptAromByVolProp = 11002
    pptAromByWtProp = 11003
    pptAsphalteneContentProp = 11004
    pptBasicN2ContentProp = 11005
    pptCToHRatioProp = 11006
    pptCloudPointProp = 11007
    pptConradsonCContentProp = 11008
    pptCopperContentProp = 11009
    pptCuFeContentProp = 11010
    pptFlashPointProp = 11011
    pptFreezePtProp = 11012
    pptMONClearProp = 11013
    pptMONLeadedProp = 11014
    pptNapthenesByVolProp = 11015
    pptNapthenesByWtProp = 11016
    pptNiContentProp = 11017
    pptN2ContentProp = 11018
    pptOlefinsByVolProp = 11019
    pptOlefinsByWtProp = 11020
    pptParaffinsByVolProp = 11021
    pptParaffinsByWtProp = 11022
    pptPourPointProp = 11023
    pptRefractIdxProp = 11024
    pptRVPProp = 11025
    pptRONClearProp = 11026
    pptRONLeadedProp = 11027
    pptSmokePtProp = 11028
    pptSContentProp = 11029
    pptSMercaptanContentProp = 11030
    pptSodiumContentProp = 11031
    pptTVPProp = 11032
    pptVaContentProp = 11033
    pptFeContentProp = 11034
    pptLuminometerNumberProp = 11035
    pptC5Mass = 11036
    pptC5Vol = 11037
    pptViscosity38 = 11038
    pptViscosity50 = 11039
    pptViscosity60 = 11040
    pptWaxContentProp = 11041
    pptiC6_22DMBMassProp = 11042
    pptiC6_22DMBVolProp = 11043
    pptiC6_23DMBMassProp = 11044
    pptiC6_23DMBVolProp = 11045
    pptiC6_2MPMassProp = 11046
    pptiC6_2MPVolProp = 11047
    pptiC6_3MPMassProp = 11048
    pptiC6_3MPVolProp = 11049
    pptiC7_22mPentaneMassProp = 11050
    pptiC7_22mPentaneVolProp = 11051
    pptiC7_24mPentaneMassProp = 11052
    pptiC7_24mPentaneVolProp = 11053
    pptiC7_223mButaneMassProp = 11054
    pptiC7_223mButaneVolProp = 11055
    pptiC7_33mPentaneMassProp = 11056
    pptiC7_33mPentaneVolProp = 11057
    pptiC7_23mPentaneMassProp = 11058
    pptiC7_23mPentaneVolProp = 11059
    pptiC7_2mHexaneMassProp = 11060
    pptiC7_2mHexaneVolProp = 11061
    pptiC7_3mHexaneMassProp = 11062
    pptiC7_3mHexaneVolProp = 11063
    pptiC7_3ePentaneMassProp = 11064
    pptiC7_3ePentaneVolProp = 11065
    pptC6iParaffinMassProp = 11066
    pptC6iParaffinVolProp = 11067
    pptC7iParaffinMassProp = 11068
    pptC7iParaffinVolProp = 11069
    pptC8iParaffinMassProp = 11070
    pptC8iParaffinVolProp = 11071
    pptC9iParaffinMassProp = 11072
    pptC9iParaffinVolProp = 11073
    pptC10iParaffinMassProp = 11074
    pptC10iParaffinVolProp = 11075
    pptC11iParaffinMassProp = 11076
    pptC11iParaffinVolProp = 11077
    pptC6nParaffinMassProp = 11078
    pptC6nParaffinVolProp = 11079
    pptC7nParaffinMassProp = 11080
    pptC7nParaffinVolProp = 11081
    pptC8nParaffinMassProp = 11082
    pptC8nParaffinVolProp = 11083
    pptC9nParaffinMassProp = 11084
    pptC9nParaffinVolProp = 11085
    pptC10nParaffinMassProp = 11086
    pptC10nParaffinVolProp = 11087
    pptC11nParaffinMassProp = 11088
    pptC11nParaffinVolProp = 11089
    pptC6OlefinMassProp = 11090
    pptC6OlefinVolProp = 11091
    pptC7OleffinMassProp = 11092
    pptC7OleffinVolProp = 11093
    pptC8OlefinMassProp = 11094
    pptC8OlefinVolProp = 11095
    pptC9OleffinMassProp = 11096
    pptC9OleffinVolProp = 11097
    pptC10OlefinMassProp = 11098
    pptC10OlefinVolProp = 11099
    pptC11OleffinMassProp = 11100
    pptC11OleffinVolProp = 11101
    pptBezeneContentMassProp = 11102
    pptBezeneContentVolProp = 11103
    pptTolueneContentMassProp = 11104
    pptTolueneContentVolProp = 11105
    pptmetaXyleneContentMassProp = 11106
    pptmetaXyleneContentVolProp = 11107
    pptorthoXyleneContentMassProp = 11108
    pptorthoXyleneContentVolProp = 11109
    pptparaXyleneContentMassProp = 11110
    pptparaXyleneContentVolProp = 11111
    pptEthylBenzenContentMassProp = 11112
    pptEthylBenzenContentVolProp = 11113
    pptC6NAlkylcyclopentaneMassProp = 11114
    pptC6NAlkylcyclopentaneVolProp = 11115
    pptC6NAlkylcyclohexaneMassProp = 11116
    pptC6NAlkylcyclohexaneVolProp = 11117
    pptC7NAlkylcyclopentaneMassProp = 11118
    pptC7NAlkylcyclopentaneVolProp = 11119
    pptC7NAlkylcyclohexaneMassProp = 11120
    pptC7NAlkylcyclohexaneVolProp = 11121
    pptC8NAlkylcyclopentaneMassProp = 11122
    pptC8NAlkylcyclopentaneVolProp = 11123
    pptC8NAlkylcyclohexaneMassProp = 11124
    pptC8NAlkylcyclohexaneVolProp = 11125
    pptC9NAlkylcyclopentaneMassProp = 11126
    pptC9NAlkylcyclopentaneVolProp = 11127
    pptC9NAlkylcyclohexaneMassProp = 11128
    pptC9NAlkylcyclohexaneVolProp = 11129
    pptC10NAlkylcyclopentaneMassProp = 11130
    pptC10NAlkylcyclopentaneVolProp = 11131
    pptC10NAlkylcyclohexaneMassProp = 11132
    pptC10NAlkylcyclohexaneVolProp = 11133
    pptC11NAlkylcyclopentaneMassProp = 11134
    pptC11NAlkylcyclopentaneVolProp = 11135
    pptC11NAlkylcyclohexaneMassProp = 11136
    pptC11NAlkylcyclohexaneVolProp = 11137
    pptC8AromaticMassProp = 11138
    pptC8AromaticVolProp = 11139
    pptC9AromaticMassProp = 11140
    pptC9AromaticVolProp = 11141
    pptC10AromaticMassProp = 11142
    pptC10AromaticVolProp = 11143
    pptC11AromaticMassProp = 11144
    pptC11AromaticVolProp = 11145
    pptC6NaphtheneMassProp = 11146
    pptC6NaphtheneVolProp = 11147
    pptC7NaphtheneMassProp = 11148
    pptC7NaphtheneVolProp = 11149
    pptC8NaphtheneMassProp = 11150
    pptC8NaphtheneVolProp = 11151
    pptC9NaphtheneMassProp = 11152
    pptC9NaphtheneVolProp = 11153
    pptC10NaphtheneMassProp = 11154
    pptC10NaphtheneVolProp = 11155
    pptC11NaphtheneMassProp = 11156
    pptC11NaphtheneVolProp = 11157
    pptIsoparaffinMassProp = 11158
    pptIsoparaffinVolProp = 11159
    pptONMassProp = 11160
    pptONVolProp = 11161
    pptNaphtheneGCMassProp = 11162
    pptNaphtheneGCVolProp = 11163
    pptiOlefinMassProp = 11164
    pptiOlefinVolProp = 11165
    pptnOlefinMassProp = 11166
    pptnOlefinVolProp = 11167
    pptnParaffinMassProp = 11168
    pptnParaffinVolProp = 11169
    pptOiC6MassProp = 11170
    pptOiC6VolProp = 11171
    pptOiC7MassProp = 11172
    pptOiC7VolProp = 11173
    pptOiC8MassProp = 11174
    pptOiC8VolProp = 11175
    pptOiC9MassProp = 11176
    pptOiC9VolProp = 11177
    pptOiC10MassProp = 11178
    pptOiC10VolProp = 11179
    pptOiC11MassProp = 11180
    pptOiC11VolProp = 11181
    pptPnC12PlusMassProp = 11182
    pptPnC12PlusVolProp = 11183
    pptPiC12PlusMassProp = 11184
    pptPiC12PlusVolProp = 11185
    pptOiC12PlusMassProp = 11186
    pptOiC12PlusVolProp = 11187
    pptOnC12PlusMassProp = 11188
    pptOnC12PlusVolProp = 11189
    pptNC12PlusMassProp = 11190
    pptNC12PlusVolProp = 11191
    pptAC12PlusMassProp = 11192
    pptAC12PlusVolProp = 11193
    pptAromaticGCMassProp = 11194
    pptAromaticGCVolProp = 11195
    pptCentroidBoilTempProp = 11196
    pptOtherPetroleumProp = 11197


class CSTRHeaterType:
    cstr_LiquidHeater = 0
    cstr_VesselHeater = 1


class PFRPressureDropType:
    pfr_UserSpecified = 0
    pfr_ErgunEquation = 1


class PFRHeatTransfer:
    pfr_DirectQ = 0
    pfr_Formula = 1


class PFRTubeSideHeatTransInfo:
    pfr_StandardType = 0
    pfr_EmpiricalType = 1
    pfr_UserSpecifiedType = 2


class PFREmpiricalFlowBasis:
    pfr_MolarFlow = 3
    pfr_MassFlow = 4
    pfr_VolumeFlow = 5


class PFRSegmentInitializationType:
    pfr_InitFromCurrentSeg = 0
    pfr_InitFromPreviousSeg = 1
    pfr_ReInitSeg = 2


class PFRPhaseType:
    pfr_VapourOnly = 0
    pfr_LiquidOnly = 1
    pfr_Overall = 5


class GibbsReactorType:
    gr_NoReactions = 0
    gr_SpecdRxnsOnly = 2
    gr_GibbsRxnsOnly = 3


class SSCellType:
    ssctUnknown = 0
    ssctNumber = 1
    ssctLabel = 2
    ssctFormula = 3


class SSCellAttachmentType:
    sscaNoAttachment = 0
    sscaImport = 1
    sscaExport = 2


class StreamType:
    Feedst = 0
    Productst = 1


class FractionBasis:
    frbMolarFlow = 9
    frbMassFlow = 10
    frbLiqVolFlow = 11


class FractionType:
    ftSplitFractions = 0
    ftStreamFractions = 1


class GCycConfiguration:
    gccHighEfficiency = 0
    gccHighOutput = 1
    gccUserDefined = 2


class HCycConfiguration:
    hccMode1 = 0
    hccMode2 = 1
    hccUserDefined = 2


class EffMethod:
    emLapple = 0
    emLeithLicht = 1


class BHFConfiguration:
    bhcDefault = 0
    bhcUserDefined = 1


class ColumnPhase:
    cpVapour = 0
    cpLiquid = 1


class ColumnDrawPhase:
    cdpLiquid = 0
    cdpVapour = 1


class ColumnFlowBasis:
    cfbMoleFlow = 3
    cfbMassFlow = 4
    cfbVolumeFlow = 5
    cfbStdVolumeFlow = 1023


class ColumnCutPointType:
    ccptTBP = 50
    ccptD86 = 51
    ccptD1160VAC = 52
    ccptD1160ATM = 54
    ccptD2887 = 55


class ColumnD86Conversion:
    cd86API1980 = 0
    cd86API1987 = 1
    cd86API1994 = 2
    cd86EdmisterOkamato = 3


class ColumnD2887Conversion:
    cd2887API1987 = 0
    cd2887API1994Indirect = 1
    cd2887API1994Direct = 2


class ColumnRefluxType:
    crlight = 1
    crheavy = 2


class ColumnTransportPropety:
    ctpSurfaceTension = 20
    ctpThermalConductivity = 21
    ctpViscosity = 22


class ColumnVapourPressureType:
    cvpGeneralVapourPressure = 10
    cvpReidVapourPressure = 11


class ColumnPhysicalProperty:
    cppAvgMassLiquidDensity = 30
    cppMoleDensity = 31
    cppMoleWeight = 32
    cppActualMassDensity = 33


class ColumnColdProperty:
    ccpFlashPoint = 40
    ccpPourPoint = 41
    ccpRON = 42


class ColumnPumpAroundSpecType:
    cpaFlowRate = 0
    cpaTemperatureDrop = 1
    cpaReturnTemperature = 2
    cpaDuty = 3
    cpaReturnVapourFraction = 4


class COverCalculationType:
    covrFull = 1
    covrInlet = 2
    covrGasLiq = 4
    covrLiqLiq = 8
    covrVapExit = 16
    covrInletDP = 32
    covrExitDP = 64


class COverDispensionCode:
    cocodeLgtInGasFeed = 0
    cocodeHvyInGasFeed = 1
    cocodeGasInLgtFeed = 2
    cocodeHvyInLgtFeed = 3
    cocodeGasInHvyFeed = 4
    cocodeLgtInHvyFeed = 5
    cocodeLgtInGasToExit = 6
    cocodeHvyInGasToExit = 7
    cocodeLgtInGasProd = 8
    cocodeHvyInGasProd = 9
    cocodeGasInLgtProd = 10
    cocodeHvyInLgtProd = 11
    cocodeGasInHvyProd = 12
    cocodeLgtInHvyProd = 13


class COverDispersionBasis:
    cobaseMass = 0
    cobaseMole = 1
    cobaseLiqVol = 2
    cobaseActVol = 3
    cobasePct = 4
    cobaseNumber = 5
    cobaseCumMass = 6
    cobaseCumMole = 7
    cobaseCumLiqVol = 8
    cobaseCumActVol = 9
    cobaseCumPct = 10
    cobaseUnknown = 127


class psSchedule:
    psActual = 0
    psSchedule_40 = 1
    psSchedule_80 = 2
    psSchedule_160 = 3
    psSchedule_10 = 10
    psSchedule_20 = 11
    psSchedule_30 = 12
    psSchedule_STD = 13
    psSchedule_60 = 14
    psSchedule_100 = 15
    psSchedule_120 = 16
    psSchedule_140 = 17
    psSchedule_XS = 18
    psSchedule_XXS = 19
    psSchedule_5S = 100
    psSchedule_10S = 101
    psSchedule_40S = 102
    psSchedule_80S = 103


class psNominalDiam:
    psNDNone = -32767
    psND0_125Inch = 0
    psND0_25Inch = 1
    psND0_375Inch = 2
    psND0_5Inch = 3
    psND0_75Inch = 4
    psND1Inch = 5
    psND1_25Inch = 6
    psND1_5Inch = 7
    psND2Inch = 8
    psND2_5Inch = 9
    psND3Inch = 10
    psND3_5Inch = 11
    psND4Inch = 12
    psND5Inch = 13
    psND6Inch = 14
    psND8Inch = 15
    psND10Inch = 16
    psND12Inch = 17
    psND14Inch = 18
    psND16Inch = 19
    psND18Inch = 20
    psND20Inch = 21
    psND22Inch = 22
    psND24Inch = 23
    psND26Inch = 24
    psND28Inch = 25
    psND30Inch = 26
    psND32Inch = 27
    psND34Inch = 28
    psND36Inch = 29
    psND42Inch = 30
    psND46Inch = 31
    psND48Inch = 32
    psND54Inch = 33
    psND60Inch = 34


class psMaterial:
    psMEUser_Specified = -32767
    psMESmooth = 0
    psDrawn_Tube = 1
    psMild_Steel = 2
    psAsphalted_Iron = 3
    psGalvanized_Iron = 4
    psCast_Iron = 5
    psSmooth_Concrete = 6
    psRough_Concrete = 7
    psSmooth_Riveted_Steel = 8
    psRough_Riveted_Steel = 9
    psSmooth_Wood_Stave = 10
    psRough_Wood_Stave = 11
    psPlasticTubing = 12
    psRubberHose = 13


class PipeSegSegmentType:
    pssPipe = 0
    pssSwage_Abrupt = 1
    pssSwage_45degree = 2
    pssElbow_45Std = 3
    pssElbow_45Long = 4
    pssElbow_90Std = 5
    pssElbow_90Long = 6
    pssBend_90_r_d1 = 7
    pssBend_90_r_d1_5 = 8
    pssBend_90_r_d2 = 9
    pssBend_90_r_d3 = 10
    pssBend_90_r_d4 = 11
    pssBend_90_r_d6 = 12
    pssBend_90_r_d8 = 13
    pssBend_90_r_d10 = 14
    pssBend_90_r_d12 = 15
    pssBend_90_r_d14 = 16
    pssBend_90_r_d16 = 17
    pssBend_90_r_d20 = 18
    pssElbow_45Mitre = 19
    pssElbow_90Mitre = 20
    pss180DegreeCloseReturn = 21
    pssTee_BranchBlanked = 22
    pssTee_AsElbow = 23
    pssCoupling_Union = 24
    pssGateValve_Open = 25
    pssGateValve_ThreeQuarter = 26
    pssGateValve_Half = 27
    pssGateValve_OneQuarter = 28
    pssGateValve_Crane_Open = 29
    pssDiaphramValve_Open = 30
    pssDiaphramValve_ThreeQuarter = 31
    pssDiaphramValve_Half = 32
    pssDiaphramValve_OneQuarter = 33
    pssGlobeValve_Open = 34
    pssGlobeValve_Half = 35
    pssGlobeValve_Crane_Open = 36
    pssAngleValve_Open = 37
    pssAngleValve_45deg_Open = 38
    pssAngleValve_90deg_Open = 39
    pssBlowoffValve_Open = 40
    pssPlugCock_Angle5 = 41
    pssPlugCock_Angle10 = 42
    pssPlugCock_Angle20 = 43
    pssPlugCock_Angle40 = 44
    pssPlugCock_Angle60 = 45
    pssPlugCock_Open = 46
    pssButterflyValve_Angle5 = 47
    pssButterflyValve_Angle10 = 48
    pssButterflyValve_Angle20 = 49
    pssButterflyValve_Angle40 = 50
    pssButterflyValve_Angle60 = 51
    pssButterflyValve_2_8in_Open = 52
    pssButterflyValve_10_14in_Open = 53
    pssButterflyValve_16_24in_Open = 54
    pssBallValve_Open = 55
    pssCheckValve_Swing = 56
    pssCheckValve_Disk = 57
    pssCheckValve_Ball = 58
    pssCheckValve_Lift = 59
    pssCheckValve_45degLift = 60
    pssFootValve = 61
    pssFootValve_Poppetdisk = 62
    pssFootValve_Hingeddisk = 63
    pssWaterMeter_Disk = 64
    pssWaterMeter_Piston = 65
    pssWaterMeter_Rotary = 66
    pssWaterMeter_Turbine = 67
    pssUserDefined = 68


class sbMode:
    sbOff = 0
    sbMin = 1
    sbMax = 2
    sbMedian = 3
    sbAvg = 4
    sbSum = 5
    sbProduct = 6
    sbQuotient = 7
    sbManual = 8
    sbHand_Sel = 9


class srcAction:
    srcReverse = 0
    srcDirect = 1


class srcExecution:
    srcInternal = 0
    srcExternal = 1


class srcCtrlMode:
    srcOff1 = 0
    srcManual1 = 1
    srcAutomatic = 2


class srcSPMode:
    srcLocal = 0
    srcRemote = 1


class srcSPLocal:
    srcNo_Tracking1 = 0
    srcRemote_Tracking = 1


class srcRemoteSP:
    srcUse_Percent = 0
    srcUse_PV = 1


class srcSPManual:
    srcNo_Tracking2 = 0
    srcTracking_PV = 1


class srcAlgoSelection:
    srcVelForm = 0
    srcPosFormARW = 1
    srcPosForNoARW = 2


class srcDesignType:
    srcPID = 0
    srcPI = 1


class srcScheduleBasis:
    srcSP = 0
    srcPV1 = 1


class srcSelectedRange:
    srcLowRange = 0
    srcMedRange = 1
    srcHighRange = 2


class srcSignal:
    srcPV = 0
    srcOP = 1
    srcSP1 = 2
    srcDV = 3
    srcRS = 4


class srcSignalAlarm:
    srcNormal = 0
    srcLowLow = 1
    srcLow1 = 2
    srcHigh1 = 3
    srcHighHigh = 4


class srcBackInit:
    srcOutput2 = 0
    srcOutput1 = 1


class rcAction:
    rcReverse = 0
    rcDirect = 1


class rcExecution:
    rcInternal = 0
    rcExternal = 1


class rcCtrlMode:
    rcOff = 0
    rcManual = 1
    rcAutomatic = 2


class rcSPMode:
    rcLocal = 0
    rcRemote = 1


class rcSPLocal:
    rcNo_Tracking = 0
    rcRemote_Tracking = 1


class rcRemoteSP:
    rcUse_Percent = 0
    rcUse_PV = 1


class rcSPManual:
    rcNo_Tracking1 = 0
    rcTracking_PV = 1


class rcAlgoSelection:
    rcVelForm = 0
    rcPosFormARW = 1
    rcPosForNoARW = 2


class rcDesignType:
    rcPID = 0
    rcPI = 1


class rcScheduleBasis:
    rcSP = 0
    rcPV = 1


class rcSelectedRange:
    rcLowRange = 0
    rcMedRange = 1
    rcHighRange = 2


class rcSignal:
    rcPV1 = 0
    rcOP = 1
    rcSP1 = 2
    rcDV = 3
    rcRS = 4


class rcSignalAlarm:
    rcNormal = 0
    rcLowLow = 1
    rcLow = 2
    rcHigh = 3
    rcHighHigh = 4


class scAction:
    scReverse = 0
    scDirect = 1


class scExcution:
    scInternal = 0
    scExternal = 1


class scCtrlMode:
    scOff = 0
    scManual = 1
    scAutomatic = 2


class scDataFormat:
    scActual = 0
    scNormalized = 1


class scLeftAxis:
    scPV_and_SP = 0
    scErrorFormat = 1


class cryHeaterOrCooler:
    cryCooling = 0
    cryHeating = 1


class cryMoleOrMass:
    cryMole = 3
    cryMass = 4


class cryCompOrTotal:
    cryComponent = 0
    cryTotal = 1


class neuHeaterOrCooler:
    neuCooling = 0
    neuHeating = 1


class preHeaterOrCooler:
    preCooling = 0
    preHeating = 1


class co2FormationFlag:
    co2Undetermined = 0
    co2SolidCO2 = 1
    co2NoForm = 2
    co2NoCO2 = 3


class phaseForCO2Calc:
    phaseAutoSelect = 0
    phaseVapor = 1
    phaseLiquid = 2
    phaseAqueous = 3


class co2FreezeFromPhase:
    specifiedPhaseNotPresent = 0
    freezeFromVapor = 1
    freezeFromLiquid = 2
    freezeFromAqueous = 3
    notApplicable = 4


class envTableType:
    envBubble = 0
    envDewPt = 1
    envQuality1 = 2
    envQuality2 = 3
    envHydrate = 4
    envIsotherm1 = 5
    envIsotherm2 = 6
    envIsotherm3 = 7
    envIsobar1 = 8
    envIsobar2 = 9
    envIsobar3 = 10


class pbuBalvalType:
    pbuTemp = 1
    pbuPressure = 2
    pbuMoleFlow = 3
    pbuMassFlow = 4
    pbuVolFlow = 5
    pbuHeatFlow = 6
    pbuEnthalpy = 7
    pbuEntropy = 8
    pbuUnitLess = 999


class LPPropertyPackage:
    lpPengRobinson = 2
    lpPRSV = 4
    lpSourPR = 6
    lpSRK = 8
    lpKabadiDanner = 10
    lpSourSRK = 12


class LPFlashType:
    lpTPFlash = 0
    lpPHFlash = 1


class LPProperty:
    lpEOSSqrt = 0
    lpEOSb = 1
    lpEOSM = 2
    lpEOSMW = 3


class LumperMethod:
    lmeMontelGouel = 0
    lmeCustom = 1
    lmeHysysOilChar = 2


class DelumperMethod:
    dmeCompRecovery = 0
    dmeHysysOilChar = 1


class PSVFluidPhase:
    fpVapour = 0
    fpLiq1 = 1
    fpLiq2 = 2
    fpFeed = 3
    fpMixedLiquid = 4
    fpSolid = 5


class TargetVarType:
    AirDemand = 0
    H2SRatio = 1
    H2SWetMole = 2
    H2SDryMole = 3
    SO2WetMole = 4
    SO2DryMole = 5


class srurfEmpMode:
    rfRichFeedAG = 0
    rfLeanFeedAG = 1
    rfNH3SWSFeed = 2
    rfOxygenEnrich = 3
    rfStraightThroughAmineAG = 4
    rfSWSAcidGas = 5
    rfSplitFlowLeanAG = 8
    rfOxygenEnrichAllAG = 6
    rfCoFiringAmineAG = 7
    rfCoFiringSWSAG = 9


class srurfFurnmodel:
    rfEmpiricalKinetic = 0
    rfThermodynamic = 1
    rfOutletKnown = 2


class srurfCompSpecType:
    rfMole = 0
    rfMass = 1


class SRURFType:
    rfSingleChamber = 0
    rfTwoChamber = 1


class SRUWasteHeatExchangerType:
    stSinglePass = 0
    stDoublePass = 1


class SRUCatConvCatalystType:
    srucatAlumina = 0
    srucatTitania = 1


class sruBurnType:
    Equilibrium = 0
    AcidGasOrder = 1
    FuelGasOrder = 2


class saturatorOpWVUnit:
    wvMgPerM3Wet = 0
    wvLbPerMMft3Wet = 1
    wvMgPerM3Dry = 2
    wvLbPerMMft3Dry = 3
    wvKgPerKgDry = 4


class BlowdownUpdateLevel:
    bulNone = 0
    bulLow = 2
    bulMedium = 4
    bulHigh = 10


class BlowdownRunEndedStatus:
    bresNotRun = -32767
    bresRunning = 0
    bresCompleted = 1
    bresUserStop = 2
    bresException = 3
    bresSolverHold = 4
    bresNotReadyToRun = 5
    bresConfigurationInvalid = 6


class BlowndownStreamType:
    bstPressureBoundary = 1
    bstZeroMassFlowBoundary = 2
    bstConnectivityStream = 3


class BlowdownWallMaterial:
    bwmUserDefined = 0
    bwmCarbonSteel = 1
    bwmStainlessSteel = 2
    bwmInconel625 = 3
    bwmIncoloy825 = 4


class BlowdownInternalMaterial:
    bimUserDefined = 0
    bimStainlessSteel = 2
    bimInconel625 = 3
    bimIncoloy825 = 4

    
class BlowdownExternalMaterial:
    bemUserDefined = 0
    bemCellularGlass = 1


class BlowdownVesselHeadGeometry:
    bvhgFlat = 0
    bvhg21SemiEllipsoidal = 1
    bvhgHemispherical = 2


class BlowdownFireType:
    bftNone = 0
    bftPoolFire = 1


class BlowdownFireHeatFlux:
    bfhfAPI521 = 0
    bfhfUserDefined = 1


class BlowdownCompositionPhaseSpecification:
    bcpsOverall = 0
    bcpsIndividual = 1


class BlowdownInternalSlabType:
    bistNone = 2
    bistUniformSlab = 1
    bistZoneSpecifiedSlab = 0


class BlowdownInternalSlabMaterial:
    bismUserDefined = 0
    bismCarbonSteel = 1
    bismStainlessSteel = 2
    bismInconel625 = 3
    bismIncoloy825 = 4


class BlowdownOrificeType:
    botFixedDiameterPlate = 1
    botConstantMassVelocityChoke = 2


class BlowdowninsulatingLayer:
    biltWall = 0
    biltInsulation = 1
    biltCladding = 2


class LineSizingCalculationType:
    lsctDesign = 0
    lsctRating = 1


class LineSizingPipeMaterial:
    lspmCarbonSteel = 0
    lspmStainlessSteel = 1


class LineSizingFlowType:
    lsftUnknown = -32767
    lsftLiquidOnly = 0
    lsftVapourOnly = 1
    lsftTwoPhase = 2
    lsftElongatedBubble = 3
    lsftStratified = 4
    lsftSlug = 5
    lsftWave = 6
    lsftAnnularMist = 7
    lsftDispersedBubble = 8
    lsftSegregated = 9
    lsftTransition = 10
    lsftIntermittent = 11
    lsftDistributed = 12
    lsftThreePhase = 13
    lsftUnrecognised = 14
    lsftBubble = 15
    lsftMist = 16
    lsftBubbly = 17
    lsftAnnular = 18
    lsftStratifiedSmooth = 19
    lsftStratifiedWavy = 20
    lsftSlugFlow = 21
    lsftBubbleFlow = 22
    lsftSinglePhaseGas = 23
    lsftSinglePhaseLiquid = 24
    lsftTwoPhaseOilWater = 25
    lsftSinglePhaseOil = 26
    lsftSinglePhaseWater = 27


class LineSizingCriteriaMet:
    lscmMet = 0
    lscmFailed = 1
    lscmUndetermined = 2


class LineSizingFlowCorrelation:
    lscfcGregoryAzizMandhane = 0
    lscfcBeggsAndBrill1973 = 1
    lscfcBeggsAndBrill1979 = 2
    lscfcHTFSLiquidSlip = 3
    lscfcHTFSHomogeneousFlow = 4
    lscfcTulsaUnifiedModel2Phase = 5
