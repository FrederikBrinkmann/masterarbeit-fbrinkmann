# Architektur

Kurze Architekturbeschreibung der LLM-Pipeline

- FastAPI Backend nimmt Ingest-Requests entgegen (/ingest)
- Worker verarbeitet Jobs asynchron und ruft LLM-Services auf
- Dummy Ticket API dient als Zielsystem für erstellte Tickets
- Evaluation vergleicht Vorhersagen mit Gold-Labels
