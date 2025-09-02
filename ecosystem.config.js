module.exports = {
  apps: [
    {
      name: "fastserver",
      script: "python3",
      args: "-m uvicorn main:app --host 0.0.0.0 --port 8000",
      interpreter: null, // make sure PM2 doesn’t try to override
      env: {
        PYTHONPATH: ".",
      },
    },
  ],
};
