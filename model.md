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
