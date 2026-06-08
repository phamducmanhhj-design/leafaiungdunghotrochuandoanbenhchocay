---
title: LeafAI CNN API
emoji: 🌿
colorFrom: green
colorTo: blue
sdk: docker
pinned: false
---

# LeafAI CNN API

FastAPI service for LeafAI leaf disease CNN inference.

Endpoints:

- `GET /health`
- `POST /predict`

`/predict` accepts either multipart field `image` or JSON field `image_data_url`.
