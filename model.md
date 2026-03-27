Oringal Word Document (LaTex Below):

Derivation of the Gap-Year Decision Rule

Timing structure of the gap-year payoff
The gap-year payoff is modelled over a finite horizon T=3:
	Period 1: savings from working, S
	Period 2: internship payoff, I(θ,m), which depends on both discipline type θand market state m
	Period 3: long-run graduate/career benefit, F
The discount factor is δ∈(0,1), so future payoffs are discounted.
Hence, if I take a gap year and state (θⓜ,m)occurs, the payoff is
u(G,θ,m)=δS+δ^2 I(θ,m)+δ^3 F-K(θ)

If I do not take a gap year, the safe payoff is
u(N)=n
Definitions of terms
Where:
	S: savings benefit from working during the gap year 
	I(θ,m): internship payoff, depending on discipline type and internship-market conditions 
	F: longer-run graduate/career benefit 
	K(θ): behavioural cost associated with type θ
	n: safe payoff from continuing directly into third year 
Assumptions on ordering of payoffs
Assume internship outcomes satisfy
I(D,G)>I(D,B)>I(U,G)>I(U,B)

so disciplined behaviour and a good market each increase the value of the gap year.
Also assume
K(U)>K(D)

so the undisciplined type faces a greater behavioural cost.
Expected internship payoffs conditional on type
Let r=P(G)denote the probability of a good internship market, and 1-r=P(B)the probability of a bad market.
Then expected internship payoffs conditional on type are
I ˉ_D=rI(D,G)+(1-r)I(D,B),
I ˉ_U=rI(U,G)+(1-r)I(U,B)
Derivation of expected utility from taking a gap year
After observing signal s, let
μ(s)=P(D∣s)

be the posterior probability that I am disciplined.
Then the expected utility of taking a gap year is
EU(G∣s)=μ(s)[δS+δ^2 I ˉ_D+δ^3 F-K(D)]+(1-μ(s))[δS+δ^2 I ˉ_U+δ^3 F-K(U)]

Expanding this gives
EU(G∣s)=μ(s)δS+μ(s)δ^2 I ˉ_D+μ(s)δ^3 F-μ(s)K(D)
+(1-μ(s))δS+(1-μ(s))δ^2 I ˉ_U+(1-μ(s))δ^3 F-(1-μ(s))K(U)

Now collect like terms.
Savings term
μ(s)δS+(1-μ(s))δS=δS[μ(s)+(1-μ(s))]=δS

Final-career-benefit term
μ(s)δ^3 F+(1-μ(s))δ^3 F=δ^3 F[μ(s)+(1-μ(s))]=δ^3 F

Internship term
μ(s)δ^2 I ˉ_D+(1-μ(s))δ^2 I ˉ_U=δ^2 [μ(s)I ˉ_D+(1-μ(s))I ˉ_U]

Behavioural-cost term
-μ(s)K(D)-(1-μ(s))K(U)

So the collected form is
EU(G∣s)=δS+δ^2 [μ(s)I ˉ_D+(1-μ(s))I ˉ_U]+δ^3 F-[μ(s)K(D)+(1-μ(s))K(U)]
Derivation of the threshold condition
The expected utility of not taking the gap year is
EU(N∣s)=n

Taking the gap year is optimal if and only if
EU(G∣s)>n

Substitute in the collected form:
δS+δ^2 [μ(s)I ˉ_D+(1-μ(s))I ˉ_U]+δ^3 F-[μ(s)K(D)+(1-μ(s))K(U)]>n

Expand the internship and cost terms:
δS+δ^2 [μ(s)I ˉ_D+I ˉ_U-μ(s)I ˉ_U]+δ^3 F-[μ(s)K(D)+K(U)-μ(s)K(U)]>n

Group the terms in μ(s):
δS+δ^2 I ˉ_U+δ^3 F-K(U)+μ(s)[δ^2 (I ˉ_D-I ˉ_U)+K(U)-K(D)]>n

Rearranging:
μ(s)[δ^2 (I ˉ_D-I ˉ_U)+K(U)-K(D)]>n-δS-δ^2 I ˉ_U-δ^3 F+K(U)

Hence
μ(s)>(n-δS-δ^2 I ˉ_U-δ^3 F+K(U))/(δ^2 (I ˉ_D-I ˉ_U)+K(U)-K(D))

Define the threshold
μ^*=(n-δS-δ^2 I ˉ_U-δ^3 F+K(U))/(δ^2 (I ˉ_D-I ˉ_U)+K(U)-K(D))

Therefore, the decision rule is:
"Choose " G"  "⟺"  " μ(s)>μ^*

# Derivation of the Gap-Year Decision Rule

## Timing structure of the gap-year payoff

The gap-year payoff is modelled over a finite horizon \(T=3\):

- **Period 1:** savings from working, \(S\)
- **Period 2:** internship payoff, \(I(\theta, m)\), which depends on discipline type \(\theta\) and market state \(m\)
- **Period 3:** long-run graduate/career benefit, \(F\)

The discount factor is \(\delta \in (0,1)\), so future payoffs are discounted.

Hence, if I take a gap year and state \((\theta,m)\) occurs, the payoff is:

\[
u(G,\theta,m)=\delta S+\delta^2 I(\theta,m)+\delta^3 F-K(\theta)
\]

If I do not take a gap year, the safe payoff is:

\[
u(N)=n
\]

## Definitions of terms

Where:

- \(S\): savings benefit from working during the gap year
- \(I(\theta,m)\): internship payoff, depending on discipline type and internship-market conditions
- \(F\): longer-run graduate/career benefit
- \(K(\theta)\): behavioural cost associated with type
- \(n\): safe payoff from continuing directly into third year

## Assumptions on ordering of payoffs

Assume internship outcomes satisfy:

\[
I(D,G) > I(D,B), \quad I(U,G) > I(U,B), \quad I(D,m) > I(U,m)
\]

So disciplined behaviour and a good market each increase the value of the gap year.

Also assume:

\[
K(U) > K(D)
\]

So the undisciplined type faces a greater behavioural cost.

## Expected internship payoffs conditional on type

Let \(r=P(G)\) denote the probability of a good internship market, and \(1-r=P(B)\) the probability of a bad market.

Then expected internship payoffs conditional on type are:

\[
\bar I_D = rI(D,G) + (1-r)I(D,B)
\]

\[
\bar I_U = rI(U,G) + (1-r)I(U,B)
\]

## Derivation of expected utility from taking a gap year

After observing signal \(s\), let

\[
\mu(s)=P(D \mid s)
\]

be the posterior probability that I am disciplined.

Then the expected utility of taking a gap year is:

\[
EU(G \mid s)=\mu(s)\big[\delta S+\delta^2 \bar I_D+\delta^3 F-K(D)\big] + (1-\mu(s))\big[\delta S+\delta^2 \bar I_U+\delta^3 F-K(U)\big]
\]

Expanding this gives:

\[
EU(G \mid s)=\mu(s)\delta S+\mu(s)\delta^2 \bar I_D+\mu(s)\delta^3 F-\mu(s)K(D)
\]
\[
\qquad +(1-\mu(s))\delta S+(1-\mu(s))\delta^2 \bar I_U+(1-\mu(s))\delta^3 F-(1-\mu(s))K(U)
\]

Now collect like terms.

### Savings term

\[
\mu(s)\delta S+(1-\mu(s))\delta S=\delta S
\]

### Final-career-benefit term

\[
\mu(s)\delta^3 F+(1-\mu(s))\delta^3 F=\delta^3 F
\]

### Internship term

\[
\mu(s)\delta^2 \bar I_D+(1-\mu(s))\delta^2 \bar I_U
= \delta^2\big[\mu(s)\bar I_D+(1-\mu(s))\bar I_U\big]
\]

### Behavioural-cost term

\[
\mu(s)K(D)+(1-\mu(s))K(U)
\]

So the collected form is:

\[
EU(G \mid s)=\delta S+\delta^2\big[\mu(s)\bar I_D+(1-\mu(s))\bar I_U\big]+\delta^3 F-\big[\mu(s)K(D)+(1-\mu(s))K(U)\big]
\]

## Derivation of the threshold condition

The expected utility of not taking the gap year is:

\[
EU(N)=n
\]

Taking the gap year is optimal if and only if:

\[
EU(G \mid s)>n
\]

Substitute in the collected form:

\[
\delta S+\delta^2\big[\mu(s)\bar I_D+(1-\mu(s))\bar I_U\big]+\delta^3 F-\big[\mu(s)K(D)+(1-\mu(s))K(U)\big]>n
\]

Expand the internship and cost terms:

\[
\delta S+\delta^2\big[\mu(s)\bar I_D+\bar I_U-\mu(s)\bar I_U\big]+\delta^3 F-\big[\mu(s)K(D)+K(U)-\mu(s)K(U)\big]>n
\]

Group the terms in \(\mu(s)\):

\[
\delta S+\delta^2 \bar I_U+\delta^3 F-K(U)+\mu(s)\big[\delta^2(\bar I_D-\bar I_U)+K(U)-K(D)\big]>n
\]

Rearranging:

\[
\mu(s)\big[\delta^2(\bar I_D-\bar I_U)+K(U)-K(D)\big] > n-\delta S-\delta^2 \bar I_U-\delta^3 F+K(U)
\]

Hence,

\[
\mu(s) > \frac{n-\delta S-\delta^2 \bar I_U-\delta^3 F+K(U)}{\delta^2(\bar I_D-\bar I_U)+K(U)-K(D)}
\]

Define the threshold:

\[
\mu^* = \frac{n-\delta S-\delta^2 \bar I_U-\delta^3 F+K(U)}{\delta^2(\bar I_D-\bar I_U)+K(U)-K(D)}
\]

Therefore, the decision rule is:

\[
\text{Choose } G \iff \mu(s) ≥ \mu^*
\]
