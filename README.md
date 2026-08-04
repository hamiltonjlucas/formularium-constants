# formularium-constants

**Formularium** physical constants as [Axiom](https://dev.axiomide.com) nodes — one
`Get*` node per constant (71 total) returning the full
`formularium-types.ConstantSpec` (value, uncertainty, unit, natural-units mass
dimension, tier, source), plus `GetCatalog` returning every constant at once.

The shared protobuf contracts (`ConstantSpec`, `FormulaSpec`, `Catalog`,
`FormulaResult`, the engine report messages) live in the proto-only
[`formularium-types`](https://github.com/hamiltonjlucas/formularium-types) package,
which this package — like every other in the fleet — `axiom import`s.

| Node | Symbol | Name | Value | Source |
|---|---|---|---|---|
| `GetAWolf` | A_wolf | Wolfenstein A parameter | 0.826 dimensionless | derived |
| `GetDeltaABit` | Delta_A_bit | horizon area quantum (dyadic) | 7.2428e-70 m^2 | derived |
| `GetDeltaM21Sq` | Delta_m21_sq | solar mass-squared splitting | 7.41e-05 eV^2 | NuFIT |
| `GetDeltaM31Sq` | Delta_m31_sq | atmospheric mass-squared splitting | 0.002507 eV^2 | NuFIT |
| `GetDeltaM32Sq` | Delta_m32_sq | Delta m^2_32 neutrino splitting | 0.0024329 eV^2 | derived |
| `GetES` | E_S | Schwinger critical field | 1.32328e+18 V/m | derived |
| `GetFFaraday` | F_faraday | Faraday constant | 96485.3 C/mol | derived |
| `GetGF` | G_F | Fermi constant | 1.16638e-05 GeV^-2 | CODATA |
| `GetGN` | G_N | Newtonian gravitational constant | 6.6743e-11 m^3/(kg*s^2) | CODATA |
| `GetH0` | H_0 | Hubble constant | 67.4 km/s/Mpc | Planck |
| `GetLambdaQcd` | Lambda_QCD | QCD scale (1-loop nf=3 estimate) | 0.2445 GeV | derived |
| `GetLambdaCc` | Lambda_cc | cosmological constant | 1.0904e-52 m^-2 | derived |
| `GetMPl` | M_Pl | Planck mass | 1.22089e+19 GeV | derived |
| `GetMW` | M_W | W boson mass | 80.377 GeV | PDG |
| `GetMZ` | M_Z | Z boson mass | 91.1876 GeV | PDG |
| `GetNA` | N_A | Avogadro constant | 6.02214e+23 mol^-1 | definition |
| `GetNDs` | N_dS | de Sitter horizon capacity | 3.309e+122 dimensionless | derived |
| `GetOmegaLambda` | Omega_Lambda | dark-energy density parameter | 0.6847 dimensionless | Planck |
| `GetRGas` | R_gas | molar gas constant | 8.31446 J/(mol*K) | derived |
| `GetRInf` | R_inf | Rydberg constant | 1.09737e+07 m^-1 | CODATA |
| `GetRy` | Ry | Rydberg energy | 13.6057 eV | CODATA |
| `GetSChshCl` | S_CHSH_cl | CHSH classical bound | 2 dimensionless | derived |
| `GetSIcTriv` | S_IC_triv | communication-trivialization threshold | 3.26599 dimensionless | derived |
| `GetSNsMax` | S_NS_max | no-signaling CHSH maximum (PR box) | 4 dimensionless | derived |
| `GetSTsirelson` | S_Tsirelson | Tsirelson bound | 2.82843 dimensionless | derived |
| `GetVCb` | V_cb | CKM |V_cb| | 0.041 dimensionless | PDG |
| `GetVUb` | V_ub | CKM |V_ub| | 0.00382 dimensionless | PDG |
| `GetVUs` | V_us | CKM |V_us| | 0.2243 dimensionless | PDG |
| `GetZ0` | Z_0 | impedance of free space | 376.73 ohm | derived |
| `GetA0` | a_0 | Bohr radius | 5.29177e-11 m | CODATA |
| `GetAE` | a_e | electron anomalous magnetic moment | 0.00115965 dimensionless | derived |
| `GetAlpha` | alpha | fine-structure constant | 0.00729735 dimensionless | CODATA |
| `GetAlphaS` | alpha_s | strong coupling at M_Z | 0.1179 dimensionless | PDG |
| `GetBWien` | b_wien | Wien displacement-law constant | 0.00289777 m*K | derived |
| `GetBeta0Qcd` | beta0_QCD | QCD one-loop beta coefficient (nf=3) | 9 dimensionless | definition |
| `GetC` | c | speed of light | 2.99792e+08 m/s | definition |
| `GetEC` | e_C | elementary charge (SI) | 1.60218e-19 C | definition |
| `GetEEm` | e_em | EM coupling (natural units) | 0.302822 dimensionless | derived |
| `GetEpsilon0` | epsilon_0 | vacuum electric permittivity | 8.85419e-12 F/m | convention |
| `GetHbar` | hbar | reduced Planck constant | 1.05457e-34 J*s | definition |
| `GetKB` | k_B | Boltzmann constant | 1.38065e-23 J/K | definition |
| `GetKN` | k_N | nucleon mass in units of Lambda_QCD | 3.842 dimensionless | derived |
| `GetKappaCap` | kappa_cap | holographic capacity density | 9.5702e+68 m^-2 | derived |
| `GetLP` | l_P | Planck length | 1.61626e-35 m | derived |
| `GetLambdaC` | lambda_C | electron Compton wavelength | 2.42631e-12 m | CODATA |
| `GetMH` | m_H | Higgs boson mass | 125.25 GeV | PDG |
| `GetMB` | m_b | bottom-quark mass | 4.18 GeV | PDG |
| `GetMC` | m_c | charm-quark mass | 1.27 GeV | PDG |
| `GetMD` | m_d | down-quark mass | 0.00467 GeV | PDG |
| `GetME` | m_e | electron mass | 0.000510999 GeV | CODATA |
| `GetMMu` | m_mu | muon mass | 0.105658 GeV | PDG |
| `GetMN` | m_n | neutron mass | 0.939565 GeV | CODATA |
| `GetMP` | m_p | proton mass | 0.938272 GeV | CODATA |
| `GetMS` | m_s | strange-quark mass | 0.0934 GeV | PDG |
| `GetMT` | m_t | top-quark mass | 172.57 GeV | PDG |
| `GetMTau` | m_tau | tau mass | 1.77686 GeV | PDG |
| `GetMU` | m_u | up-quark mass | 0.00216 GeV | PDG |
| `GetMmuMe` | mmu_me | muon-to-electron mass ratio | 206.768 dimensionless | derived |
| `GetMpMe` | mp_me | proton-to-electron mass ratio | 1836.15 dimensionless | derived |
| `GetMu0` | mu_0 | vacuum magnetic permeability | 1.25664e-06 N/A^2 | convention |
| `GetMuB` | mu_B | Bohr magneton | 9.27401e-24 J/T | CODATA |
| `GetRE` | r_e | classical electron radius | 2.81794e-15 m | CODATA |
| `GetRhoCrit` | rho_crit | critical density of the universe | 8.53e-27 kg/m^3 | derived |
| `GetS12sq` | s12sq | neutrino sin^2(theta12) | 0.303 dimensionless | NuFIT |
| `GetS13sq` | s13sq | neutrino sin^2(theta13) | 0.02225 dimensionless | NuFIT |
| `GetS23sq` | s23sq | neutrino sin^2(theta23) | 0.451 dimensionless | NuFIT |
| `GetSigmaSb` | sigma_SB | Stefan-Boltzmann constant | 5.67037e-08 W/(m^2*K^4) | derived |
| `GetSigmaT` | sigma_T | Thomson cross section | 6.65246e-29 m^2 | CODATA |
| `GetSin2Thetaw` | sin2_thetaW | weak mixing angle | 0.23122 dimensionless | PDG |
| `GetTP` | t_P | Planck time | 5.39125e-44 s | derived |
| `GetV` | v | Higgs vacuum expectation value | 246.22 GeV | derived |

The machine-readable source of truth is [`nodes/specs.py`](nodes/specs.py).
Part of the [Formularium](https://github.com/hamiltonjlucas/formularium) project.

License: Apache-2.0.
