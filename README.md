# SpendSence

SpendSense is an AI Personal Finance Coach Agent MVP.

It uses multiple agents to analyze sample transaction data and give basic financial advice.

## Agents

- Categorization Agent: categorizes transactions
- Pattern Agent: analyzes spending patterns
- Alert Agent: warns when budget usage is high
- Weekly Coach Agent: gives financial advice

## How to Run

```bash
python main.py

## Future Improvements

In the current MVP, SpendSense uses sample CSV transaction data to demonstrate the agent logic.

In the future, the system can be expanded with:

- Real bank API connection to automatically import user transactions
- Claude API integration for smarter personalized financial advice
- Web dashboard for visualizing spending, budgets, and alerts
- Email or SMS alerts using services like SendGrid or Twilio
- User login and personal budget settings
- Savings goal tracking with weekly progress updates
