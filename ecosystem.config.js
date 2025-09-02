module.exports = {
  apps: [
    {
      name: "fastserver",
      script: "./.venv/bin/uvicorn",
      args: "main:app --host 0.0.0.0 --port 8000",
      interpreter: null, // let the shebang inside uvicorn pick python
      env: {
        PYTHONPATH: ".",
      },
    },
  ],
};
