# Git

## Useful Tricks
### Get the commit hash of the first commit
```bash
git rev-list HEAD | tail -n 1
```

### Get the commit hash of the latest commit
```bash
git rev-list HEAD | head -n 1
```

### Check, which branches contain a given commit hash
This is very useful, if you obtain the hash (e.g. from a status log), but you are not sure which branch(es) this commit belongs to.

```bash
git branch --contains COMMIT_HASH
```

## Clients
### macOS
- [GitUp](https://gitup.co/)
- [Fork](https://git-fork.com/)
![](https://git-fork.com/images/ImageWithNotes1.png)
