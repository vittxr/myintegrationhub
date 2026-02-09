# Guide

GitHub Actions allows you set up a cron job based on a YAML file.

1. Create the file `.github/workflows/cronjob.yml`
2. Use the same file as this repository.
3. Configure the following secrets (Path: Settings > Secrets and Variables > Actions)
   * Create the `ENV_FILE` secret (use the same content as the `.env.example` file, but you need to set up the credential keys based on your Habitica account and Google Sheet ID)
   * Create the `GSHEETS_CREDS` secret
     * Download `gsheets_creds.json` from Google Cloud. See: `_docs/gsheets_auth.md`
     * Before creating the secret, convert the JSON to Base64
