# Kubernetes
## Kubectl

### Troubleshooting
#### Manually replacing a pod
##### Replacing a pod without a deployment manifest
There might be situations, in which you might not have the needed `deployment.yaml` manifest file. In this case, you can still replace the pod by asking `kubectl` to return the YAML deployment manufest that the pod has last been deployed with:[^replace]

```bash
kubectl get pod PODNAME -n NAMESPACE -o yaml | kubectl replace --force -f -
```

- [ ] ==check, this can be added as an alias to the `kubectl` command==

[^replace]: [How to retry image pull in a kubernetes Pods? | StackOverflow](https://stackoverflow.com/questions/40259178/how-to-retry-image-pull-in-a-kubernetes-pods)
