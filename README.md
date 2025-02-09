<p align="center">
  <a href="https://nextjs-fastapi-starter.vercel.app/">
    <img src="https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png" height="96">
    <h3 align="center">Smart Emoji AI</h3>
  </a>
</p>

<p align="center">A Next.js 14 project utilizing <a href="https://fastapi.tiangolo.com/">FastAPI</a> as the API backend.</p>

---

## 🚀 Introduction

**Smart Emoji AI** helps users pick emojis by predicting the best match based on their input text. The frontend is built using **Next.js 14**, while the backend API is powered by **FastAPI**. The NLP model used for emoji prediction is maintained in a separate [repository](https://github.com/arnon3339/emoji-model).

## 🌍 Live Demo

Check out the live deployment: [Smart Emoji AI](https://nextjs-fastapi-emojiiai.vercel.app/)

## 📦 Deploy Your Own

Deploy this project to **Vercel** with one click:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Farnon3339%2Fnextjs-fastapi-emojiiai%2Ftree%2Fmain)

## 📦 Deploy Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/arnon3339/nextjs-fastapi-emojiiai.git
cd nextjs-fastapi-emojiiai
```

### 2️⃣ Set Up a Virtual Environment (Backend)

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scriptsctivate  # Windows
```

### 3️⃣ Install Dependencies

```bash
npm install  # or yarn or pnpm install
```

### 4️⃣ Start the Development Server

```bash
npm run dev  # or yarn dev or pnpm dev
```

The **Next.js** frontend runs on [http://localhost:3000](http://localhost:3000).
The **FastAPI** backend runs on [http://127.0.0.1:8000](http://127.0.0.1:8000).

If needed, modify the backend port in `package.json` and update `next.config.js` accordingly.

## 📂 Project Repositories

- **Frontend & API:** [Smart Emoji AI](https://github.com/arnon3339/nextjs-fastapi-emojiiai)
- **NLP Model:** [Emoji Prediction Model](https://github.com/arnon3339/emoji-model)
- **Docker Deployment:** *(Coming soon!)*

## 📚 Learn More

Explore the technologies used in this project:

- 📖 [Next.js Documentation](https://nextjs.org/docs) – Learn about Next.js features and API.
- 🎓 [Next.js Interactive Tutorial](https://nextjs.org/learn)
- ⚡ [FastAPI Documentation](https://fastapi.tiangolo.com/)

For contributions and feedback, check out the [Next.js GitHub repository](https://github.com/vercel/next.js/). Happy coding! 🚀
