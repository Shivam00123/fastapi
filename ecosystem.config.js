// ecosystem.config.js
module.exports = {
  apps: [
    {
      name: "fastserver",
      script: "python3",
      args: "-m uvicorn main:app --host 0.0.0.0 --port 8000",
      env: {
        PYTHONPATH: ".",
      },
    },
  ],
};
