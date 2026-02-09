---
author: @christian-mk
status: draft
---

# Demo data for custom feeds

Orcfax seeks to expand service options to include publication of custom data.
The aim is for this process to be largely driven by integrators who will be
expected to understand the desired payload (i.e. on-chain data), the sources
necessary to derive it, and how their specific solutions will engage with it.

However, it's prudent that Orcfax choose what kind(s) of data to include in its
demo/PoC so that stakeholders can conceptualize the value of this solution.

## Weather

**Use case:** Parametric Insurance

**Problem:** traditional indemnity-based insurance models require significant
operational overhead and can result in protracted claims processes.

**Solution:** parametric insurance reduces operational overhead and improves
stakeholder experience by automating the payout process by setting payout
triggers based on the policy
(e.g. rainfall totals, wind gust, heat index, snowfall, drought index, etc).

**Advantage of a web3 solution:**

- history of payouts publicly accessible
- enables new use cases (prediction markets, GameFi, modeling)

**Risk(s):** Insurance solutions relying on external data providers to trigger
policy payouts must trust data accuracy and authenticity.

**Scope:** As stated, the payload is determined by policy type. For the purpose
of the demo, a decision should be made whether a single policy type
(flooding, fire, drought)) should be selected or whether multiple datapoints can
be surfaced in the payload for multiple policy types.

### Weather sources (global)

| Provider | Limits |
| [Visual Crossing][ws-1] | 1000/day |
| [Weatherbit][ws-2] | 50/day & 1/sec |
| [OpenWeather][ws-3] | 1000/day |
| [Tomorrow.io][ws-4] | 500/day, 25/hr, 3/sec |
| [Open-Mateo][ws-5] | 10,000/day, 5,000/hour, 600/min |

Additional sources of note:

- MateoStat
- WeatherStack
- WeatherAPI.com
- NOAA Climate Data Online (CDO) (US)

[ws-1]: https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/
[ws-2]: https://www.weatherbit.io/api
[ws-3]: https://openweathermap.org/api/one-call-3?collection=one_call_api_3.0
[ws-4]: https://docs.tomorrow.io/reference/welcome
[ws-5]: https://open-meteo.com/en/docs

## AI

**Use case:** Proof-of-Verifiable-Inference (PoVI) -- [FluxPoint Studios][int-1]

**Problem:**

**Solution:** A plutus validator that consumes an Orcfax statement as a
reference input, checks its the right feed and its recent, then uses the score
to parameterize/gate contract actions. Flux would use it to power risk-aware
DeFi UX (collateral rules, vault weights, liquidation thresholds), with PoI
receipts archived for anyone to audit the inference step.

**Advantage of a web3 solution:**

**Risk(s):**

**Scope:**

1.  Orcfax collector/validator nodes query a PoI inference endpoint determined
    by Flux that returns {output + signed receipt}.

        Long-term goal: Nodes query primary sources directly
        (HTTP + ledger queries), then run a deterministic inference locally.
        Produces (a) the feed output and (b) a signed PoI receipt. Raw source
        responses can be included in the Orcfax audit package.

2.  for smart contract use, the on-chain body can be minimal
    (e.g. {risk_score, confidence}). PoI “proof” details don’t need to live in
    the datum. We can put the compact PoI fingerprint
    (jobId/resultHash/receiptHash + modelId) in tx metadata and store the full
    receipt + canonicalized inputs + raw source captures in the Orcfax audit
    package for verify/audit.

3.  heartbeat and on-demand publication models are supported and a hybrid is
    ideal; heartbeat (e.g. hourly/daily) + deviation thresholds for big moves.
    On-demand for integrator-triggered actions
    (liquidations, rebalances, mint/burn events) where they need a fresh score
    right now.

[int-1]: https://fluxpointstudios.com/
