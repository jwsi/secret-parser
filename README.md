# Submodule Checkout Action

This action checks out a private or public submodule hosted within GitHub.

## Inputs

### `ssh-key`

An optional SSH key used when checking out private submodules.

## Example usage

#### Public Submodules:

```
uses: jwsi/submodule-checkout@v1
```

#### Private Submodules:

```
uses: jwsi/submodule-checkout@v1
with:
  ssh-key: '${{ secrets.DEPLOY_KEY }}'
```