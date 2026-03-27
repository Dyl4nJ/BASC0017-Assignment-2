# BASC0017 Assignment 2 – Bayesian Decision Model of a Gap Year

## Overview

This project models the decision of whether to take a gap year between the second and third year of university as a problem of decision-making under uncertainty.

The key uncertainty is whether a future self will behave in a disciplined or undisciplined manner. This is formalised as a Bayesian decision problem in which the present self updates beliefs based on a signal and chooses whether to take a gap year.

The model is calculated using empirical data on internships and graduate outcomes, allowing for a numerical solution and comparative statics analysis.

---

## Model Structure

### Players
- Present Self (decision-maker)
- Nature (determines future discipline and labour market conditions)

### Actions
- **G**: Take a gap year  
- **N**: Continue directly to third year  

### States of the World
- Discipline: \( D \) (disciplined), \( U \) (undisciplined)  
- Labour market: \( G \) (good), \( B \) (bad)  

### Information
- The present self observes a **private signal** about future discipline
- Beliefs are updated using **Bayes’ Rule**

---

## Bayesian Updating

Posterior beliefs after observing signal \( s \):

\[
\mu(s) = P(D \mid s)
\]

The model distinguishes between:
- Good signal \( g \)
- Bad signal \( b \)

---

## Payoff Structure

Gap year payoffs are modelled over three periods:

\[
u(G, \theta, m) = \delta S + \delta^2 I(\theta, m) + \delta^3 F - K(\theta)
\]

No gap year yields a safe payoff:

\[
u(N) = n
\]

---

## Empirical Calibration

The model uses a dataset of ~10,000 students to estimate the effect of internships on outcomes.

### Key findings:
- Placement probability increases from **49.1% → 85.2%** with internship experience
- At least one internship increases placement to **65.0%**
- Salaries remain approximately constant (~$90,000)

### Interpretation:
Internships increase the **probability of employment**, not wages.

---

## Numerical Results

Using empirical calibration:

- \( W = 90{,}000 \)
- \( C = 10{,}000 \)

Payoffs:

- Disciplined:  
  \( u(G, D) = 55{,}520 \)

- Undisciplined:  
  \( u(G, U) = 34{,}190 \)

- No gap year:  
  \( u(N) = 44{,}190 \)

---

## Decision Rule

Taking a gap year is optimal when:

\[
\mu(s) > \mu^*
\]

where:

\[
\mu^* \approx 0.43
\]

### Interpretation:
A gap year is optimal if there is at least a **43% belief** that the future self will behave in a disciplined manner.

---

## Comparative Statics

Key results:

- Increased patience (\( \delta \)) → lowers threshold  
- Better labour market conditions (\( r \)) → lowers threshold  
- Higher safe payoff (\( n \)) → raises threshold  
- Greater discipline advantage → lowers threshold  

---

## Methods & Tools

- Python (pandas, matplotlib)
- Descriptive statistics
- Expected utility theory
- Bayesian updating

---

## Key Insight

The value of a gap year is driven primarily by **reducing employment risk**, rather than increasing wages.

---

## Limitations

- Discipline is treated as exogenous  
- Behavioural biases (e.g. overconfidence, time inconsistency) are not modelled  
- Signal accuracy is assumed rather than estimated  

---

## Author

Dylan Jagiwala  
UCL – Economics & Philosophy  
BASC0017: Interdisciplinary Game Theory
## Key Result

> A gap year is optimal if and only if  
> \( \mu(s) \geq 0.43 \)
