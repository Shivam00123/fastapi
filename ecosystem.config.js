module.exports = {
  apps: [
    {
      name: "fastserver",
      script: "./.venv/bin/python3", // use python inside your venv
      args: "-m uvicorn main:app --host 0.0.0.0 --port 8000",
      env: {
        PYTHONPATH: ".",
      },
    },
  ],
};
