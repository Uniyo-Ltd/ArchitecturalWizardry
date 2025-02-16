GoMark System Design Document
Background
Welcome to GoMark, where sales soar and portfolios thrive! Picture this: Balco, a company that loves to collect and nurture software businesses, has crafted a magical suite to make business operations as smooth as butter. Within this suite lies GoMark, the go-to-market wizard, offering:

Pipeline Tracking - See your sales funnels in real-time, like watching a live performance!
Upsell Outreach - Automatically emails those high-priority customers, making upgrades feel like a gift.

Problem Statement
Oh no! An intern with too much curiosity and not enough caution has accidentally deleted all of GoMark's code and infrastructure. The challenge? Rebuild this magical platform from scratch, but this time, make it even better for 20+ portfolio companies!

Tasks
1. System Design
Requirements
High-Level Architecture Diagram:

<img width="1630" alt="Screenshot 2025-02-16 at 00 08 46" src="https://github.com/user-attachments/assets/3e1a8dcc-694d-42cb-b523-96eb5e83b172" />


Infrastructure Diagram:

<img width="1565" alt="Screenshot 2025-02-16 at 00 05 56" src="https://github.com/user-attachments/assets/c9ec0759-6085-49db-bc35-0795dc1cca42" />



Monitoring and Observability:
Tools: Prometheus (metrics), Grafana (visuals), ELK Stack (logs), New Relic (app performance), Sentry (error tracking).
Practices: Real-time metrics, automated alerts, log analysis, health checks for a healthy system heartbeat.
Programming Languages:
Web Server: C (Nginx/Apache) - because performance should be as swift as a ninja.
Application Server: Go - for when you need speed and concurrency like a pro gamer.
Database: SQL (PostgreSQL) - ensuring data integrity with the precision of a Swiss watch.
Configuration Management (Orchestra): Python - for its versatility and rich ecosystem, like a Swiss Army knife.
External API (HubSpot, Upso): TypeScript - for clean, typed code that's as reliable as a trusty companion.

Additional Questions
Simplification for Low Scale (<10 companies): 
One server to rule them all, SQLite for simplicity, local assets, and basic monitoring.
Preventing Inconsistent Configurations:
Lock down with IAM, use webhooks as spies, and sync regularly like a well-oiled machine.

Deliverables
This document, now in your Git repository, showcasing our architectural magic and infrastructural wizardry. Enjoy the show!

This document is set up with Mermaid diagrams for visualization. To see these diagrams rendered, ensure your Git platform supports Mermaid or use a tool that does. Now, go forth and rebuild GoMark with flair!
