module.exports = {
  apps: [
    {
      name: "fastserver",
      script: "uvicorn",
      args: "main:app --host 0.0.0.0 --port 8000",
      interpreter: "bash",
      env: {
        PYTHONPATH: ".",
      },
    },
  ],
};
