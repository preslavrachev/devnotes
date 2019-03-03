# Blockchains

## Hard vs. Soft Forks
Consensus rule changes broadly fall into two categories: **hard forks** and **soft forks**. By definition, **hard forks loosen or eliminate existing rules whereas soft forks only tighten or add new rules.**[^forks] A **hard fork** does away with presently existing validation checks, which automatically calls for the creation of a separate chain, independent of the original one. **Soft forks**, on the other hand, add new rules and validation checks, but make sure that  new blocks will be backwards-compatible and accepted by clients, which haven't upgraded. In general, soft forks do not result in chains splitting from one another. Do keep in mind, however, that at a certain point of time, clients having the soft fork update might stop accepting pre-soft-fork blocks, essentially forcing old clients to upgrade.

[^forks]: [Forks, Signaling, and Activation | Medium](https://medium.com/@elombrozo/forks-signaling-and-activation-d60b6abda49a)