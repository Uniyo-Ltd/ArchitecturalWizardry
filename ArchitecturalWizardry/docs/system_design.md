markdown
# ArchitecturalWizardry

## GoMark System Design Document

### Background
Welcome to **GoMark**, where sales soar and portfolios thrive! Picture this: Balco, a company that loves to collect and nurture software businesses, has crafted a magical suite to make business operations as smooth as butter. Within this suite lies **GoMark**, the go-to-market wizard, offering:

- **Pipeline Tracking** - See your sales funnels in real-time, like watching a live performance!
- **Upsell Outreach** - Automatically emails those high-priority customers, making upgrades feel like a gift.

### Problem Statement
Oh no! An intern with too much curiosity and not enough caution has accidentally deleted all of GoMark's code and infrastructure. The challenge? Rebuild this magical platform from scratch, but this time, make it even better for 20+ portfolio companies!

### Tasks
#### 1. System Design
##### Requirements

**High-Level Architecture Diagram:**
<img width="1565" alt="Screenshot 2025-02-16 at 00 05 56" src="https://github.com/user-attachments/assets/0f238c2b-4976-46f5-aeda-3c7b28035e81" />

Infrastructure Diagram:
<img width="1630" alt="Screenshot 2025-02-16 at 00 08 46" src="https://github.com/user-attachments/assets/f802d62c-01c3-413a-8fa1-b169fec0191f" />


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

**Note:** 
- Ensure your repository uses GitHub, as other platforms might not natively support Mermaid rendering in READMEs. 
- GitHub will render Mermaid diagrams if they are correctly wrapped in ```mermaid code blocks. However, for some complex diagrams or custom themes, you might need to check if GitHub's Mermaid support includes all the features you're using.
- If the diagrams don't render, GitHub might still be updating its Mermaid support, or there might be a syntax issue. Always test in GitHub's markdown preview or live view to ensure it works.
