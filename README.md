# SauceDemo E2E Purchase Test (Playwright + Python)

## Источник задания
Тестовое задание QA для стажёра/junior.  
**Компания:** Effective Mobile 
**Год:** 2026 
**Ссылка:** https://github.com/Hexlet/ru-test-assignments/blob/main/qa/effective-mobile/README.md

## Что сделано
- E2E UI сценарий: авторизация → добавление «Sauce Labs Backpack» → корзина → checkout → подтверждение успеха.
- Негативные кейсы: неверный пароль, пустые поля checkout.
- Page Object Model (POM): локаторы вынесены в `pages/`.

## Что НЕ сделано и почему
- **API GitHub (create/check/delete repo)** — это независимое задание, не входящее в основной сценарий покупки. В рамках КТ2 выбран только UI-сценарий целиком.
- CI (GitHub Actions), кросс-браузерность — не входят в минимальный объём.

## Как запустить

### 1. Клонировать репозиторий
```bash
git clone <repo-url>
cd saucedemo-e2e-qa