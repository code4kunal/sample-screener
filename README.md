# Stocksift - Professional Stock Screener

Stocksift is a full-stack professional stock screening application that helps investors and traders identify potential investment opportunities through customizable screeners, backtesting, and case studies.

## Features

- 🔍 Customizable stock screeners
- 📊 Real-time and historical data analysis
- 📈 Backtesting capabilities
- 📚 Educational case studies
- 🔐 Secure authentication
- 💳 Subscription-based access
- 📱 Responsive design

## Tech Stack

### Frontend
- React with Next.js
- Tailwind CSS
- shadcn/ui components
- Recharts for data visualization
- JWT-based authentication

### Backend
- Python with FastAPI
- PostgreSQL database
- Redis for caching
- OpenSearch for search functionality
- yfinance and Alpha Vantage for stock data

### DevOps
- Docker and Docker Compose
- GitHub Actions for CI/CD
- Vercel for frontend deployment
- Render/Railway for backend deployment
- Prometheus + Grafana for monitoring

## Getting Started

### Prerequisites
- Node.js (v18 or higher)
- Python (v3.9 or higher)
- Docker and Docker Compose
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stocksift.git
cd stocksift
```

2. Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

4. Start the development environment:
```bash
docker-compose up -d
npm run dev  # Frontend
uvicorn main:app --reload  # Backend
```

## Project Structure

```
stocksift/
├── frontend/           # Next.js frontend application
├── backend/            # FastAPI backend application
├── docker/             # Docker configuration files
└── docs/              # Documentation
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any queries or support, please reach out to [your-email@example.com](mailto:your-email@example.com)
