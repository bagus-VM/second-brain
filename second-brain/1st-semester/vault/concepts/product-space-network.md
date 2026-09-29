---
title: "Product Space Network"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The product space network connects exported products that require similar capabilities — revealing how countries diversify by moving to nearby products in capability space.

## Core Intuition
Products that are exported by the same set of countries share capabilities (knowledge, institutions, inputs, infrastructure). The product space network captures this similarity: nodes are products, edges connect products that require similar capabilities. Sophisticated products sit in a dense core; less sophisticated products lie in sparse peripheral regions.

## Formal Definition / Statement
**Network formation:**
- Nodes: SITC-4 product classes
- Edges: products are similar if countries that export one competitively also tend to export the other competitively

**Proximity measure:**
φ_ij = min{P(RCA_i > 1 | RCA_j > 1), P(RCA_j > 1 | RCA_i > 1)}

where RCA (Revealed Comparative Advantage) > 1 means a country exports a product more than expected relative to the world average.

**Key insight:** edges do not mean product-to-product trade. They reveal shared capabilities.

**Finding:** sophisticated products sit in a dense core; less sophisticated products often lie in sparse peripheral regions. Countries diversify by moving to nearby products, so peripheral position limits feasible development paths.

## Key Properties / Complexity
1. **Capability-based**: edges reflect shared capabilities, not direct trade
2. **Core-periphery structure**: sophisticated products in the dense core
3. **Development constraints**: countries can only diversify to nearby products
4. **Policy implications**: peripheral countries have limited development paths
5. **Multi-scale structure**: communities at different resolution levels

## Worked Example
Product space of 775 SITC-4 products (Hidalgo et al. 2007):

**Core:** machinery, chemicals, capital-intensive goods — densely connected
**Periphery:** agriculture, raw products — sparsely connected
**Development path:** a country exporting coffee can diversify to other agricultural products (nearby in the product space), but jumping to machinery (far away) is difficult

## Common Pitfalls
1. **Confusing proximity with trade**: edges mean shared capabilities, not product-to-product trade
2. **Ignoring the core-periphery structure**: not all products are equally accessible
3. **Assuming all countries can diversify equally**: peripheral position limits development paths
4. **Over-generalizing**: the product space is specific to export data, not all economic activity

## Connections
- [[community-detection]] — communities in the product space reveal capability clusters
- [[modularity]] — can detect communities in the product space
- [[network-science-l04]] — lecture overview

## Open Questions
- How does the product space evolve over time?
- Can we predict which countries will diversify successfully?
- How do policy interventions affect a country's position in the product space?
