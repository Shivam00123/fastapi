module.exports = {
  apps: [
    {
      name: "fastserver",
      script: "-m",
      args: "uvicorn main:app --host 0.0.0.0 --port 8000",
      interpreter: "./.venv/bin/python3",
      env: {
        PYTHONPATH: ".",
      },
    },
  ],
};
