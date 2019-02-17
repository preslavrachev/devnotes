# Travis CI Server

## Environment Variables
Travis comes with a few preset environment libraries[^envvars] that can be access from within the build file:

- `TRAVIS_REPO_SLUG` - The slug (in form: owner_name/repo_name) of the repository currently being built.

## Travis CLI
### Changing the repository URL once you have configured it
Often, you might change the address of the remote URL (e.g, when changing the name of the repo on GitHub). This will probably reuslt in Travis CLI throwing the followign message at you:

```
fatal: Authentication failed for [my-repo-url]
```

This is because Travis CLI caches the information locally as part of the `.git/config` file. Resolving the upper issue is just a matter of fixing the URL in the config file[^1].

[^envvars]: [https://docs.travis-ci.com/user/environment-variables/#convenience-variables](https://docs.travis-ci.com/user/environment-variables/#convenience-variables)
[^1]: [https://github.com/travis-ci/travis-ci/issues/2334#issuecomment-72932432](https://github.com/travis-ci/travis-ci/issues/2334#issuecomment-72932432)
