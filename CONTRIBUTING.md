### 🐾 Steps to follow

#### 📋 Fork the repository

First, you need to fork the repository to your GitHub account. Click on the "Fork" button on the top right corner of the repository page.

#### 🌿 Create a branch

Create a new branch based on the `develop` branch with a objective name for your contribution:

```bash title="Terminal"
git checkout -b feature/your-feature-name develop
```

#### ⌨️ Develop your changes

If you need help to quickstart the local environment, check the [Getting Started](/getting-started) guide.

#### 📦 Preparing the commit

After all changes done, check for lint errors and format the code:

- For the chatbot:

```console
pipenv run isort . && pipenv run black .
```

- For the documentation:

```console
npm run lint && npm run format
```

> [!TIP]  
> If you use `pnpm`, `yarn`, or `bun`, simply replace `npm` with the respective package manager.

&nbsp;

#### ✍️ Opening a pull request

All done? Now you can push your changes to your forked repository and open a pull request to wait for a review.

> [!IMPORTANT]  
> Don't forget to correctly describe your changes within the commits and the pull request.

&nbsp;

### 📜 Code of Conduct

Be sure to read and follow all of the rules on our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).